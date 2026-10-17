"""
anchor_optimization -- calibration-anchor optimization for fsQCA
(docs/calibration_optimization_problem_en.md, plus constraints C6 and C7).

    max_theta  S(a(theta)) - lambda * R(theta)
    s.t.  C2  Cons >= cons_floor            C3  Cov >= cov_floor
          C4  share_min <= share(mu_k > .5) <= share_max          for every condition
          C5  |P| >= min_positive_rows
          C6  q_c - q_e >= min_side and q_i - q_c >= min_side     (optional, against crisp sets)
          C7  crisp_k <= cap_k                                     (optional, crispness cap)
    C1 (ordering + minimum percentile gap delta) holds by construction:
          theta_k = (c_k, t_e, t_i),  q_e = d + (c - 2d) t_e,  q_c = c,  q_i = c + d + (1 - c - 2d) t_i

  S   bootstrap stability: mean Jaccard between the OUT=1 row set on B bootstrap
      samples and on the full sample (weights drawn once from bootstrap_seed).
  OUT rule (nu, tau, pi) is fixed for the whole optimization (rule_from_reference:
      "conventional" = n.cut from the data, incl .80, PRI .50; "data_driven"; or fixed).
  Solver: differential evolution DE/rand/1/bin with a feasibility rule
      (feasible > infeasible; among feasible higher objective; among infeasible
      smaller violation). A trial replaces its parent when it is at least as
      good, so the population can drift across the plateaus of S.
      Repeated over solver seeds; the best run is the point estimate, the
      spread across seeds is reported (solution set, spec section 8).

Library
    from anchor_optimization import AnchorProblem, DEFAULTS, kde_anchors
    P = AnchorProblem(X, y_raw, conds, outcome, outcome_anchor, rule, params)
    best, runs = P.solve(n_seeds=5)

CLI (real data)
    python anchor_optimization.py configs/template.json
"""
import copy
import json
import os
import sys
import time

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")      # tiny matrices: threaded BLAS is ~10x slower

import numpy as np
import pandas as pd

import qca_core as q

DEFAULTS = {
    "L": 3.0,                          # log-odds at e / i (3.0 = simulator; ln 19 = 2.944)
    "B": 200, "bootstrap_seed": 12345,
    "delta": 0.05,                     # C1 minimum percentile gap
    "cons_floor": 0.80, "cov_floor": 0.50,          # C2, C3
    "share_min": 0.30, "share_max": 0.70,           # C4
    "min_positive_rows": 2,                          # C5
    "min_side": 0.0,                   # C6 (0 = off)
    "crisp_tol": -1.0,                 # C7 relative: cap = crispness(KDE reference) + tol (< 0 = off)
    "max_crisp": 0.0,                  # C7 absolute cap (0 = off)
    "lambda": 0.0, "omega": 1.0,       # regularization of the crossover
    "reference": "kde",                # reference crossover for R: kde | median | expert
    "init": ["kde", "center"],         # starting points put into the DE population
    "de": {"pop": 60, "generations": 150, "F": 0.7, "CR": 0.9},
    "profile_generations": 40,
    "quantile_anchors": [0.05, 0.50, 0.95],
    "max_qmc_checks": 200000,
}


def merge_params(user=None):
    p = copy.deepcopy(DEFAULTS)
    user = copy.deepcopy(user or {})
    de = {**p["de"], **user.pop("de", {})}
    p.update(user)
    p["de"] = de
    return p


# ================================================== reference anchors ======
def kde_crossover_pct(x, lo=0.10, hi=0.90):
    """Percentile of the KDE antimode nearest the median; troughs outside the
    [lo, hi] percentiles are tail bumps and ignored; 0.5 if none."""
    x = np.asarray(x, float)
    sd, iqr = x.std(ddof=1), np.subtract(*np.percentile(x, [75, 25]))
    h = 0.9 * min(sd, iqr / 1.34 if iqr > 0 else sd) * len(x) ** -0.2
    if not h > 0:
        return 0.5
    grid = np.linspace(x.min(), x.max(), 512)
    dens = np.exp(-0.5 * ((grid[:, None] - x[None, :]) / h) ** 2).sum(1)
    mins = [j for j in range(1, len(grid) - 1) if dens[j] < dens[j - 1] and dens[j] < dens[j + 1]
            and lo <= q.ecdf(x, grid[j]) <= hi]
    if not mins:
        return 0.5
    return q.ecdf(x, grid[min(mins, key=lambda j: abs(grid[j] - np.median(x)))])


def kde_anchors(x, quantiles=(0.05, 0.50, 0.95), delta=0.05):
    """Data-only reference anchors: KDE-antimode crossover, outer quantiles."""
    c = float(np.clip(kde_crossover_pct(x), 2 * delta, 1 - 2 * delta))
    pct = [min(quantiles[0], c - delta), c, max(quantiles[2], c + delta)]
    return tuple(float(v) for v in np.quantile(x, pct))


def quantile_anchors(x, quantiles=(0.05, 0.50, 0.95)):
    return tuple(float(v) for v in np.quantile(x, quantiles))


def rule_from_reference(X, y_raw, outcome_anchor, L, quantiles=(0.05, 0.50, 0.95), delta=0.05,
                        spec="conventional"):
    """OUT rule (nu, tau, pi) from the raw data alone (truth table built with
    the KDE reference anchors). spec:
      "conventional"  n.cut from the data (keeps >= 80% of cases), incl >= .80, PRI >= .50
      "data_driven"   n.cut, incl and PRI all from the data (largest gaps)
      {"nu": int | "auto", "tau": float, "pi": float}  fixed values ("auto" = n.cut from the data)"""
    K = X.shape[1]
    mu = np.column_stack([q.calibrate(X[:, k], kde_anchors(X[:, k], quantiles, delta), L) for k in range(K)])
    dd = q.rule_from_data(mu, q.calibrate(y_raw, outcome_anchor, L), q.row_bits(K))
    if spec == "data_driven":
        return dd
    if spec == "conventional":
        return {"nu": dd["nu"], "tau": 0.80, "pi": 0.50}
    return {"nu": dd["nu"] if spec.get("nu", "auto") == "auto" else int(spec["nu"]),
            "tau": float(spec["tau"]), "pi": float(spec["pi"])}


# ============================================================= problem =====
class AnchorProblem:
    def __init__(self, X, y_raw, conds, outcome, outcome_anchor, rule, params=None,
                 expert=None, theory=None):
        """
        X (N, K) raw conditions; y_raw raw outcome; outcome_anchor fixed (e, c, i)
        rule      {"nu", "tau", "pi"}: the OUT rule (fixed during optimization)
        params    see DEFAULTS
        expert    optional {condition: (lo, hi)} crossover interval in raw units
        theory    optional {condition: (e, c, i)}: start point / reference
        """
        self.p = merge_params(params)
        p = self.p
        self.X, self.conds, self.outcome = np.asarray(X, float), list(conds), outcome
        self.N, self.K = self.X.shape
        self.L, d = p["L"], p["delta"]
        self.rule = rule
        self.y_raw, self.outcome_anchor = np.asarray(y_raw, float), tuple(outcome_anchor)
        self.y = q.calibrate(y_raw, outcome_anchor, self.L)
        self.bits = q.row_bits(self.K)
        rng = np.random.default_rng(p["bootstrap_seed"])
        Wb = rng.multinomial(self.N, np.full(self.N, 1 / self.N), size=p["B"]).astype(float)
        self.W = np.vstack([np.ones(self.N), Wb])                    # row 0 = full sample
        self.sorted = [np.sort(self.X[:, k]) for k in range(self.K)]

        # crossover box C_k
        lo, hi = np.full(self.K, 2 * d), np.full(self.K, 1 - 2 * d)
        self.expert = dict(expert or {})
        for f, (a, b) in self.expert.items():
            k = self.conds.index(f)
            lo[k] = min(max(self.pct(k, a), 2 * d), 1 - 2 * d)
            hi[k] = max(min(self.pct(k, b), 1 - 2 * d), lo[k])
        self.lo = np.concatenate([lo, np.zeros(2 * self.K)])
        self.hi = np.concatenate([hi, np.ones(2 * self.K)])

        self.theory = {f: tuple(v) for f, v in (theory or {}).items()}
        self.reference = {f: kde_anchors(self.X[:, k], p["quantile_anchors"], d)
                          for k, f in enumerate(self.conds)}
        # regularization reference crossover (percentile)
        if p["reference"] == "median":
            self.q0 = np.full(self.K, 0.5)
        elif p["reference"] == "expert" and self.expert:
            self.q0 = (lo + hi) / 2
        elif p["reference"] == "theory" and self.theory:
            self.q0 = np.array([self.pct(k, self.theory[f][1]) for k, f in enumerate(self.conds)])
        else:
            self.q0 = np.array([self.pct(k, self.reference[f][1]) for k, f in enumerate(self.conds)])
        # C7 caps
        if p["max_crisp"] > 0:
            self.crisp_cap = np.full(self.K, p["max_crisp"])
        elif p["crisp_tol"] >= 0:
            self.crisp_cap = np.array([q.crispness(q.calibrate(self.X[:, k], self.reference[f], self.L))
                                       for k, f in enumerate(self.conds)]) + p["crisp_tol"]
        else:
            self.crisp_cap = None

    # ---- percentile space
    def pct(self, k, v):
        return float(np.searchsorted(self.sorted[k], v, side="right") / self.N)

    def percentiles(self, theta):
        d, K = self.p["delta"], self.K
        c, te, ti = theta[:K], theta[K:2 * K], theta[2 * K:]
        return np.stack([d + (c - 2 * d) * te, c, c + d + (1 - c - 2 * d) * ti], 1)

    def theta_of(self, anchors):
        d, K = self.p["delta"], self.K
        qs = np.array([[self.pct(k, v) for v in anchors[f]] for k, f in enumerate(self.conds)])
        c = np.clip(qs[:, 1], self.lo[:K], self.hi[:K])
        te = np.clip((qs[:, 0] - d) / np.maximum(c - 2 * d, 1e-9), 0, 1)
        ti = np.clip((qs[:, 2] - c - d) / np.maximum(1 - c - 2 * d, 1e-9), 0, 1)
        return np.concatenate([c, te, ti])

    def anchors_of(self, theta):
        qs = self.percentiles(theta)
        return {f: tuple(float(v) for v in np.quantile(self.X[:, k], qs[k])) for k, f in enumerate(self.conds)}

    # ---- objective and constraints
    def evaluate(self, anchors, theta=None):
        p, r = self.p, self.rule
        mu = np.column_stack([q.calibrate(self.X[:, k], anchors[f], self.L) for k, f in enumerate(self.conds)])
        m, n, incl, pri = q.truth_table(mu, self.y, self.bits, self.W)
        out = q.out_rule(n, incl, pri, r["nu"], r["tau"], r["pi"])
        P0, Pb = out[0], out[1:]
        inter, union = (Pb & P0).sum(1), (Pb | P0).sum(1)
        S = float(np.where(union == 0, 1.0, inter / np.maximum(union, 1)).mean())
        cons, cov = q.solution_fit(m, self.y, P0)
        share = (mu > 0.5).mean(0)
        crisp = np.array([q.crispness(mu[:, k]) for k in range(self.K)])
        qs = (self.percentiles(theta) if theta is not None else
              np.array([[self.pct(k, v) for v in anchors[f]] for k, f in enumerate(self.conds)]))
        sides = np.concatenate([qs[:, 1] - qs[:, 0], qs[:, 2] - qs[:, 1]])
        reg = float(p["omega"] * np.mean((qs[:, 1] - self.q0) ** 2)) if p["lambda"] > 0 else 0.0
        n_pos = int(P0.sum())
        viol = (max(0.0, p["cons_floor"] - cons) + max(0.0, p["cov_floor"] - cov)
                + np.maximum(0.0, p["share_min"] - share).sum() + np.maximum(0.0, share - p["share_max"]).sum()
                + max(0, p["min_positive_rows"] - n_pos) / max(p["min_positive_rows"], 1))
        if p["min_side"] > 0:
            viol += np.maximum(0.0, p["min_side"] - sides).sum()
        if self.crisp_cap is not None:
            viol += np.maximum(0.0, crisp - self.crisp_cap).sum()
        return {"S": S, "objective": S - p["lambda"] * reg, "reg": reg,
                "feasible": bool(viol <= 1e-12), "violation": float(viol),
                "cons": cons, "cov": cov, "n_positive_rows": n_pos,
                "share_in": share, "crisp": crisp, "min_side": float(sides.min()),
                "positive": P0, "n_full": n[0], "incl_full": incl[0], "pri_full": pri[0],
                "boot_freq_out": out[1:].mean(0), "mu": mu, "m": m}

    def fun(self, theta):
        r = self.evaluate(self.anchors_of(theta), theta)
        return r["feasible"], r["objective"], r["violation"]

    # ---- solver
    def start_points(self):
        pts = []
        for kind in self.p["init"]:
            if kind == "kde":
                pts.append(self.theta_of(self.reference))
            elif kind == "center":
                K = self.K
                pts.append(np.concatenate([np.clip(0.5, self.lo[:K], self.hi[:K]), np.full(2 * K, 0.5)]))
            elif kind in ("theory", "expert_anchors") and self.theory:
                pts.append(self.theta_of(self.theory))
        return [np.clip(x, self.lo, self.hi) for x in pts]

    def solve(self, n_seeds=5, seeds=None, verbose=False):
        """Returns (best run, all runs). A run: seed, theta, anchors, percentiles,
        evaluation (without the big arrays) and seconds."""
        runs = []
        for s in (seeds or range(n_seeds)):
            t0 = time.time()
            theta, fit = differential_evolution(self.fun, self.lo, self.hi, s, **self.p["de"],
                                                init=self.start_points())
            ev = self.evaluate(self.anchors_of(theta), theta)
            runs.append({"seed": int(s), "theta": theta, "anchors": self.anchors_of(theta),
                         "percentiles": self.percentiles(theta), "fit": fit,
                         "eval": {k: v for k, v in ev.items() if k not in ("mu", "m", "positive", "n_full",
                                                                           "incl_full", "pri_full", "boot_freq_out")},
                         "seconds": time.time() - t0})
            if verbose:
                e = runs[-1]["eval"]
                print(f"  seed {s}: S={e['S']:.4f} feasible={e['feasible']} cons={e['cons']:.3f} "
                      f"cov={e['cov']:.3f} |P|={e['n_positive_rows']} ({runs[-1]['seconds']:.1f}s)")
        best = runs[0]
        for r in runs[1:]:
            if better(r["fit"], best["fit"]) and not better(best["fit"], r["fit"]):
                best = r
        return best, runs

    def profile(self, f, npts=9, seed=0):
        """S_k*(c): re-optimize with the crossover of f fixed on a grid over C_k."""
        k = self.conds.index(f)
        de = {**self.p["de"], "generations": self.p["profile_generations"]}
        out = []
        for c in np.linspace(self.lo[k], self.hi[k], npts):
            lo, hi = self.lo.copy(), self.hi.copy()
            lo[k] = hi[k] = c
            theta, (feas, obj, _) = differential_evolution(
                self.fun, lo, hi, seed, **de, init=[np.clip(x, lo, hi) for x in self.start_points()])
            out.append({"condition": f, "c_pct": float(c), "c_raw": float(np.quantile(self.X[:, k], c)),
                        "S_star": float(obj) if feas else None, "feasible": bool(feas)})
        return out


def better(a, b):
    """Feasibility rule on (feasible, objective, violation)."""
    if a[0] and b[0]:
        return a[1] >= b[1]
    if a[0] != b[0]:
        return a[0]
    return a[2] <= b[2]


def differential_evolution(fun, lo, hi, seed, pop=60, generations=150, F=0.7, CR=0.9, init=()):
    rng = np.random.default_rng(seed)
    D = len(lo)
    X = lo + rng.random((pop, D)) * (hi - lo)
    for j, x0 in enumerate(list(init)[:pop]):
        X[j] = np.clip(x0, lo, hi)
    fit = [fun(x) for x in X]
    idx = np.arange(pop)
    for _ in range(generations):
        for j in range(pop):
            r1, r2, r3 = rng.choice(idx[idx != j], 3, replace=False)
            v = np.clip(X[r1] + F * (X[r2] - X[r3]), lo, hi)
            mask = rng.random(D) < CR
            mask[rng.integers(D)] = True
            trial = np.where(mask, v, X[j])
            ft = fun(trial)
            if better(ft, fit[j]):
                X[j], fit[j] = trial, ft
    best = 0
    for j in range(1, pop):
        if better(fit[j], fit[best]) and not better(fit[best], fit[j]):
            best = j
    return X[best], fit[best]


# ===================================================== QCA result model ====
def qca_result(P, anchors):
    """Truth table + conservative / parsimonious solutions for an anchor set,
    using the problem's outcome calibration and OUT rule."""
    ev = P.evaluate(anchors)
    sols = q.solutions(ev["positive"], ev["n_full"], P.K, P.conds, P.outcome,
                       P.rule["nu"], P.p["max_qmc_checks"])
    return ev, sols


# ================================================================== CLI ====
def _load(cfg):
    path = cfg["data"]
    d = pd.read_excel(path) if path.endswith((".xlsx", ".xls")) else pd.read_csv(path)
    cols = cfg.get("columns", {})
    raw = pd.DataFrame({k: pd.to_numeric(d[cols.get(k, k)].astype(str).str.replace(",", "."))
                        for k in cfg["conditions"] + [cfg["outcome"]]})
    if cfg.get("id_column"):
        raw.index = d[cfg["id_column"]]
    return raw


def main(cfg_path):
    cfg = {k: v for k, v in json.load(open(cfg_path)).items() if not k.startswith("_")}
    raw = _load(cfg)
    conds, out = cfg["conditions"], cfg["outcome"]
    X, y_raw = raw[conds].to_numpy(float), raw[out].to_numpy(float)
    params = merge_params(cfg.get("params", {}))
    a_y = tuple(cfg["outcome_anchor"])
    rule = rule_from_reference(X, y_raw, a_y, params["L"], params["quantile_anchors"], params["delta"],
                               cfg.get("qca_rule", "conventional"))
    theory = {k: tuple(v) for k, v in cfg.get("theory_anchors", {}).items()}
    expert = {k: tuple(v) for k, v in cfg.get("expert_intervals", {}).items()}
    P = AnchorProblem(X, y_raw, conds, out, a_y, rule, params, expert=expert, theory=theory)
    print("OUT rule:", rule)

    compare = {"reference_kde": P.reference}
    if all(k in theory for k in conds):
        compare["theory"] = theory
    best, runs = P.solve(n_seeds=cfg.get("n_seeds", 5), verbose=True)
    compare["optimized"] = best["anchors"]

    out_dir = cfg.get("out_dir", "output")
    os.makedirs(out_dir, exist_ok=True)
    rows = []
    for name, a in compare.items():
        ev, sols = qca_result(P, a)
        rows.append({"anchors": name, "S": round(ev["S"], 4), "feasible": ev["feasible"],
                     "cons": round(ev["cons"], 3), "cov": round(ev["cov"], 3),
                     "n_positive_rows": ev["n_positive_rows"],
                     "crisp": round(float(ev["crisp"].mean()), 3),
                     "conservative": " | ".join(sols["conservative"]) or "(none)",
                     "parsimonious": " | ".join(sols["parsimonious"][:5]) or "(none)",
                     "n_parsimonious": len(sols["parsimonious"])})
    table = pd.DataFrame(rows)
    with pd.option_context("display.width", 220, "display.max_colwidth", 80):
        print(table.to_string(index=False))
    table.to_csv(os.path.join(out_dir, "comparison.csv"), index=False)
    pd.DataFrame([(f, *best["anchors"][f]) for f in conds] + [(out, *a_y)],
                 columns=["set", "e", "c", "i"]).to_csv(os.path.join(out_dir, "anchors_optimized.csv"), index=False)
    pd.DataFrame([{"seed": r["seed"], **{k: r["eval"][k] for k in ("S", "feasible", "cons", "cov", "n_positive_rows")},
                   **{f"{f}_c": r["anchors"][f][1] for f in conds}} for r in runs]
                 ).to_csv(os.path.join(out_dir, "seeds.csv"), index=False)
    print("saved to", out_dir)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1])
