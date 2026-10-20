"""
run_experiment -- simulation study for calibration-anchor optimization, scored with QCA.

  step 1  generate datasets            simulation.mode = "meaningful": simulate_meaningful.simulate (pure Python)
                                       otherwise: simulate_qca_cna.simulate (R package cna, main process)
  step 2  for every dataset, in parallel worker processes (pure Python):
            OUT rule (data-driven from the raw data, or fixed) -- same for every mode
            every anchor mode in the config: oracle / quantile / kde / expert / optimize
            calibrate -> truth table -> OUT rows -> conservative + parsimonious solutions
            score against the truth: anchors, memberships, OUT rows, solutions
  step 3  aggregate (grid): grid_all.csv, grid_summary*.csv, summary.md

Output
  results/<name>_<timestamp>/
    config.json
    datasets/<dataset>/
      data/raw.csv, data/true_memberships.csv, data/truth.json
      modes/<mode>/anchors.json, truth_table.csv, calibrated.csv, solutions.json, seeds.csv
      compare.csv, compare.md, anchors_compare.csv
    grid_all.csv, grid_summary_by_mode.csv, grid_summary.csv, summary.md, failures.csv

Usage
  python run_experiment.py --config configs/experiment.json             # one dataset ("simulation")
  python run_experiment.py --config configs/experiment.json --grid      # the "grid" section
  python run_experiment.py --config configs/experiment.json --grid --workers 8
  python run_experiment.py --resume results/grid_demo_<timestamp>       # continue an interrupted grid
"""
import argparse
import copy
import json
import multiprocessing as mp
import os
import sys
import time
import traceback
from datetime import datetime

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import anchor_optimization as ao  # noqa: E402
import qca_core as q  # noqa: E402


def save_json(obj, path):
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=2,
                  default=lambda o: o.tolist() if hasattr(o, "tolist") else (bool(o) if isinstance(o, np.bool_) else str(o)))


# =============================================================== step 1 ====
def dataset_list(cfg, grid):
    """[(name, simulation settings)]; seeds depend only on setting index + rep."""
    base = cfg["simulation"]
    if not grid:
        s = base
        return [(f"n{s['n']}_noise{s['noise']}_frag{s['frag']}_seed{s['seed']}", dict(s))]
    g = cfg["grid"]
    fuzz = g.get("fuzzvalues", [base.get("fuzzvalues", "seq(0, 0.4, 0.01)")])
    if base.get("mode") == "meaningful":            # no makeFuzzy: a fuzz dimension would only add reps
        fuzz = [None]
    settings = [(n, nz, fr, fz) for n in g.get("n", [base["n"]]) for nz in g.get("noise", [base["noise"]])
                for fr in g.get("frag", [base["frag"]]) for fz in range(len(fuzz))]
    out = []
    for si, (n, nz, fr, fz) in enumerate(settings):
        for rep in range(g.get("reps", 1)):
            s = {**base, "n": n, "noise": nz, "frag": fr, "fuzzvalues": fuzz[fz],
                 "seed": g.get("seed_base", 1000) + 1000 * si + rep, "fuzz_id": fz, "rep": rep}
            out.append((f"n{n}_noise{nz}_frag{fr}_fz{fz}_rep{rep:02d}", s))
    return out


def generate(datasets, root, L):
    """Write data/ for every dataset that does not have it yet
    (mode "meaningful": pure Python; other modes need R + cna)."""
    todo = [(n, s) for n, s in datasets if not os.path.exists(os.path.join(root, n, "data", "truth.json"))]
    if not todo:
        return
    for j, (name, s) in enumerate(todo, 1):
        if s.get("mode") == "meaningful":
            import simulate_meaningful as sim
            kw = {k: s[k] for k in ("n", "k", "mode", "noise", "frag", "shape", "seed") if k in s}
            kw["L"] = L                                 # data generated with the L used for scoring
        else:
            import simulate_qca_cna as sim
            sim.FUZZVALUES = s.get("fuzzvalues", sim.FUZZVALUES)
            kw = {k: s[k] for k in ("n", "k", "mode", "noise", "frag", "seed") if k in s}
            if s.get("mode") == "concov":
                kw.update(con=s.get("con", 0.85), cov=s.get("cov", 0.85))
        raw, mem, truth = sim.simulate(**kw)
        d = os.path.join(root, name, "data")
        os.makedirs(d, exist_ok=True)
        raw.round(6).to_csv(os.path.join(d, "raw.csv"), index=False)
        mem.to_csv(os.path.join(d, "true_memberships.csv"), index=False)
        save_json({**truth, "simulation": s}, os.path.join(d, "truth.json"))
        print(f"[data {j}/{len(todo)}] {name}: asf {truth['asf']} | fit {truth['actual_con_cov']}", flush=True)


# =============================================================== step 2 ====
def expert_noisy(true, conds, error, seed):
    """Imperfect expert: crossover moved by N(0, error)*(i - e); each side width
    scaled by exp(N(0, error))."""
    rng = np.random.default_rng(seed)
    out = {}
    for f in conds:
        e, c, i = true[f]
        c2 = c + rng.normal(0, error) * (i - e)
        out[f] = (c2 - (c - e) * np.exp(rng.normal(0, error)), c2, c2 + (i - c) * np.exp(rng.normal(0, error)))
    return out


def mode_anchors(m, P, X, conds, true, expert, cfg, out_dir):
    """Anchors for one mode. Returns (anchors, extra info)."""
    kind, info = m["mode"], {}
    if kind == "oracle":
        return {f: tuple(true[f]) for f in conds}, info
    if kind == "quantile":
        qs = m.get("quantiles", cfg["params"].get("quantile_anchors", [0.05, 0.5, 0.95]))
        return {f: ao.quantile_anchors(X[:, k], qs) for k, f in enumerate(conds)}, info
    if kind == "kde":
        return dict(P.reference), info
    if kind == "expert":
        return dict(expert), info
    if kind != "optimize":
        raise ValueError(f"unknown mode {kind!r}")

    params = ao.merge_params({**cfg["params"], **m.get("params", {}),
                              "de": {**cfg["params"].get("de", {}), **m.get("params", {}).get("de", {})}})
    box, theory = None, None
    use = m.get("expert")                       # None | "noisy" | "truth_box"
    w = m.get("expert_box", 0.1)
    if use == "noisy":                          # box around the imperfect expert's crossover
        box = {f: (expert[f][1] - w * (expert[f][2] - expert[f][0]),
                   expert[f][1] + w * (expert[f][2] - expert[f][0])) for f in conds}
        theory = expert
        params["init"] = params.get("init", []) + ["theory"]
    elif use == "truth_box":                    # optimistic: box around the TRUE crossover
        box = {f: (true[f][1] - w * (true[f][1] - true[f][0]), true[f][1] + w * (true[f][2] - true[f][1]))
               for f in conds}
    Popt = ao.AnchorProblem(X, P.y_raw, conds, P.outcome, P.outcome_anchor, P.rule, params,
                            expert=box, theory=theory)
    best, runs = Popt.solve(n_seeds=m.get("n_seeds", cfg.get("optimize_seeds", 3)))
    pd.DataFrame([{"seed": r["seed"], "seconds": round(r["seconds"], 1),
                   **{k: r["eval"][k] for k in ("S", "objective", "feasible", "violation", "cons", "cov",
                                                "n_positive_rows")},
                   **{f"{f}_{s}": round(v, 4) for f in conds for s, v in zip("eci", r["anchors"][f])},
                   **{f"{f}_c_pct": round(float(r["percentiles"][k, 1]), 4) for k, f in enumerate(conds)}}
                  for r in runs]).to_csv(os.path.join(out_dir, "seeds.csv"), index=False)
    feas = [r for r in runs if r["eval"]["feasible"]] or runs
    cpct = np.array([r["percentiles"][:, 1] for r in feas])
    info = {"opt_feasible": best["eval"]["feasible"], "opt_n_feasible_seeds": sum(r["eval"]["feasible"] for r in runs),
            "opt_crossover_pct_sd": float(cpct.std(axis=0).mean()),
            "opt_seconds": round(sum(r["seconds"] for r in runs), 1)}
    if m.get("profile"):
        prof = [row for f in conds for row in Popt.profile(f, m["profile"])]
        pd.DataFrame(prof).to_csv(os.path.join(out_dir, "profile.csv"), index=False)
    return best["anchors"], info


def score_mode(name, anchors, P, true, true_mu, truth, truth_rows):
    """All metrics for one anchor set (QCA only)."""
    conds = P.conds
    ev, sols = ao.qca_result(P, anchors)
    mu = ev["mu"]
    observed = ev["n_full"] >= 1
    row = {"mode": name, "S": ev["S"], "feasible": ev["feasible"], "cons": ev["cons"], "cov": ev["cov"],
           "n_positive_rows": ev["n_positive_rows"],
           "membership_mae": float(np.abs(mu - true_mu).mean()),
           "same_side_0.5": float(((mu > 0.5) == (true_mu > 0.5)).mean()),
           "crossover_err_pct": float(np.mean([abs(P.pct(k, anchors[f][1]) - P.pct(k, true[f][1]))
                                               for k, f in enumerate(conds)])),
           "crossover_err_scaled": float(np.mean([abs(anchors[f][1] - true[f][1]) / (true[f][2] - true[f][0])
                                                  for f in conds])),
           "crisp": float(ev["crisp"].mean()),
           **q.row_scores(ev["positive"], observed, truth_rows),
           "n_cs": len(sols["conservative"]), "n_ps": len(sols["parsimonious"]),
           "qmc_truncated": sols["truncated"]}
    irr = truth.get("irrelevant", [])
    for kind, key in (("cs", "conservative"), ("ps", "parsimonious")):
        cmps = [q.compare_with_truth(s, truth["asf"], irr) for s in sols[key]]
        if cmps:
            row[f"{kind}_solution"] = sols[key][0]
            for metric in ("correct", "sub_correct", "exact", "complete_sup", "complete_sub",
                           "term_precision", "term_precision_sub", "paths_found_sup", "paths_found_sub",
                           "irrelevant_in"):
                row[f"{kind}_{metric}"] = float(np.mean([c[metric] for c in cmps]))   # mean over tied solutions
            row[f"{kind}_spurious"] = ",".join(sorted({f for c in cmps for f in c["spurious"]}))
        else:
            row[f"{kind}_solution"] = "(none)"
    return row, ev, sols


def run_dataset(args):
    """Worker: all modes for one dataset folder. Returns the compare table rows."""
    ds_dir, cfg = args
    t_start = time.time()
    truth = json.load(open(os.path.join(ds_dir, "data", "truth.json")))
    raw = pd.read_csv(os.path.join(ds_dir, "data", "raw.csv"))
    conds, outcome = truth["conditions"], truth["outcome"]
    true = {f: tuple(v) for f, v in truth["anchors_exclusion_crossover_inclusion"].items()}
    X, y_raw = raw[conds].to_numpy(float), raw[outcome].to_numpy(float)
    params = ao.merge_params(cfg["params"])
    L = params["L"]

    a_y = true[outcome]                                         # outcome anchor fixed at the truth
    rule = ao.rule_from_reference(X, y_raw, a_y, L, params["quantile_anchors"], params["delta"],
                                  cfg.get("qca_rule", "conventional"))
    P = ao.AnchorProblem(X, y_raw, conds, outcome, a_y, rule, params)
    true_mu = np.column_stack([q.calibrate(X[:, k], true[f], L) for k, f in enumerate(conds)])
    truth_rows = q.row_truth(truth["asf"], conds, P.bits)
    seed = int(truth.get("seed", truth.get("simulation", {}).get("seed", 0)))
    expert = expert_noisy(true, conds, cfg.get("expert", {}).get("error", 0.1), seed + 7)

    rows, anc_rows = [], []
    for m in cfg["modes"]:
        out_dir = os.path.join(ds_dir, "modes", m["name"])
        os.makedirs(out_dir, exist_ok=True)
        t0 = time.time()
        anchors, info = mode_anchors(m, P, X, conds, true, expert, cfg, out_dir)
        row, ev, sols = score_mode(m["name"], anchors, P, true, true_mu, truth, truth_rows)
        row.update(info)
        row["seconds"] = round(time.time() - t0, 1)
        rows.append(row)
        save_json({f: list(anchors[f]) for f in conds}, os.path.join(out_dir, "anchors.json"))
        save_json(sols, os.path.join(out_dir, "solutions.json"))
        labels = ["".join(c if b else c.lower() for c, b in zip(conds, P.bits[r])) for r in range(len(P.bits))]
        pd.DataFrame({"row": labels, "n": ev["n_full"], "incl": ev["incl_full"].round(4),
                      "PRI": ev["pri_full"].round(4), "OUT": ev["positive"].astype(int),
                      "truth": truth_rows.astype(int), "bootstrap_freq_OUT": ev["boot_freq_out"].round(4)}
                     ).to_csv(os.path.join(out_dir, "truth_table.csv"), index=False)
        cal = pd.DataFrame(ev["mu"].round(4), columns=conds)
        cal[outcome] = P.y.round(4)
        cal.to_csv(os.path.join(out_dir, "calibrated.csv"), index=False)
        for k, f in enumerate(conds):
            anc_rows.append({"mode": m["name"], "condition": f, "relevant": f in truth.get("relevant", []),
                             "e": anchors[f][0], "c": anchors[f][1], "i": anchors[f][2],
                             "true_e": true[f][0], "true_c": true[f][1], "true_i": true[f][2],
                             "c_pct": P.pct(k, anchors[f][1]), "true_c_pct": P.pct(k, true[f][1])})
    table = pd.DataFrame(rows)
    table.insert(1, "rule", f"nu={rule['nu']} tau={rule['tau']:.3f} pi={rule['pi']:.3f}")
    table.to_csv(os.path.join(ds_dir, "compare.csv"), index=False)
    pd.DataFrame(anc_rows).to_csv(os.path.join(ds_dir, "anchors_compare.csv"), index=False)
    write_compare_md(ds_dir, truth, rule, table)
    return os.path.basename(ds_dir), time.time() - t_start


def _md(df, cols, fmt="{:.3f}"):
    d = df[[c for c in cols if c in df.columns]]
    cell = lambda v: fmt.format(v) if isinstance(v, (float, np.floating)) and not pd.isna(v) else ("" if pd.isna(v) else str(v))
    return "\n".join(["| " + " | ".join(d.columns) + " |", "|" + "---|" * len(d.columns)] +
                     ["| " + " | ".join(cell(v) for v in r) + " |" for r in d.itertuples(index=False)])


def write_compare_md(ds_dir, truth, rule, t):
    s = truth.get("simulation", {})
    md = [f"# {os.path.basename(ds_dir)}", "",
          f"- data: n={truth['n']}, noise={s.get('noise')}, frag={s.get('frag')}, fuzzvalues=`{s.get('fuzzvalues')}`, seed={s.get('seed')}",
          f"- true model: `{truth['asf']}`  (irrelevant: {', '.join(truth.get('irrelevant', [])) or '-'})",
          f"- OUT rule (same for every mode): n >= {rule['nu']}, incl >= {rule['tau']:.3f}, PRI >= {rule['pi']:.3f}", "",
          "## Calibration", "",
          _md(t, ["mode", "S", "feasible", "cons", "cov", "n_positive_rows", "membership_mae", "same_side_0.5",
                  "crossover_err_pct", "crisp"]), "",
          "## Truth-table rows vs truth", "",
          _md(t, ["mode", "row_precision", "row_recall", "false_positive_rows"]), "",
          "## Conservative solution vs truth", "",
          _md(t, ["mode", "n_cs", "cs_correct", "cs_term_precision", "cs_paths_found_sup",
                  "cs_solution"]), "",
          "## Parsimonious solution vs truth", "",
          _md(t, ["mode", "n_ps", "ps_sub_correct", "ps_term_precision_sub", "ps_paths_found_sub", "ps_exact",
                  "ps_irrelevant_in", "ps_solution"]), ""]
    open(os.path.join(ds_dir, "compare.md"), "w").write("\n".join(md) + "\n")


# =============================================================== step 3 ====
KEY_METRICS = ["S", "feasible", "membership_mae", "same_side_0.5", "crossover_err_pct", "crisp",
               "row_precision", "row_recall", "n_cs", "cs_correct", "cs_term_precision", "cs_paths_found_sup",
               "n_ps", "ps_sub_correct", "ps_term_precision_sub", "ps_paths_found_sub",
               "ps_exact", "ps_irrelevant_in"]


def aggregate(root, datasets, cfg):
    tables = []
    for name, s in datasets:
        f = os.path.join(root, "datasets", name, "compare.csv")
        if os.path.exists(f):
            t = pd.read_csv(f)
            for key in ("n", "noise", "frag", "fuzz_id", "rep", "seed"):
                t.insert(0, key, s.get(key))
            t.insert(0, "dataset", name)
            tables.append(t)
    if not tables:
        return None
    df = pd.concat(tables, ignore_index=True)
    df.to_csv(os.path.join(root, "grid_all.csv"), index=False)
    metrics = [m for m in KEY_METRICS if m in df.columns]
    df[metrics] = df[metrics].apply(pd.to_numeric, errors="coerce")
    order = [m["name"] for m in cfg["modes"]]
    overall = df.groupby("mode")[metrics].mean().reindex(order).round(4)
    overall.insert(0, "datasets", df.groupby("mode").size().reindex(order))
    overall.to_csv(os.path.join(root, "grid_summary_by_mode.csv"))
    keys = ["n", "noise", "frag", "fuzz_id", "mode"]
    by = df.groupby(keys)[metrics].mean().round(4)
    by.to_csv(os.path.join(root, "grid_summary.csv"))
    md = [f"# {os.path.basename(root)}", "", f"datasets finished: {df['dataset'].nunique()}", "",
          "Rates (feasible, *_correct, *_irrelevant_in, ps_exact) are shares of datasets; the rest are means.", "",
          "## Overall by mode", "", _md(overall.reset_index(), ["mode", "datasets"] + metrics), ""]
    for m in ("row_precision", "row_recall", "cs_term_precision", "ps_term_precision_sub", "membership_mae"):
        if m in df.columns:
            piv = df.pivot_table(index="mode", columns=["noise", "n"], values=m, aggfunc="mean").reindex(order).round(3)
            piv.columns = [f"noise {a} / n {b}" for a, b in piv.columns]
            md += [f"## {m} by noise x n", "", _md(piv.reset_index(), ["mode"] + list(piv.columns)), ""]
    open(os.path.join(root, "summary.md"), "w").write("\n".join(md) + "\n")
    return overall


# ================================================================ main =====
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=os.path.join(HERE, "configs", "experiment.json"))
    ap.add_argument("--name")
    ap.add_argument("--grid", action="store_true")
    ap.add_argument("--resume", metavar="DIR")
    ap.add_argument("--workers", type=int, default=None)
    a = ap.parse_args()

    if a.resume:
        root = a.resume
        cfg = json.load(open(os.path.join(root, "config.json")))
        grid = cfg.get("_grid_run", True)
    else:
        cfg = {k: v for k, v in json.load(open(a.config)).items() if not k.startswith("_")}
        grid = a.grid
        name = a.name or cfg.get("experiment_name", "exp")
        root = os.path.join(HERE, "results", f"{'grid_' if grid else ''}{name}_{datetime.now():%Y%m%d_%H%M%S}")
        os.makedirs(root, exist_ok=True)
        cfg["_grid_run"] = grid
        cfg["params"] = ao.merge_params(cfg.get("params", {}))
        save_json(cfg, os.path.join(root, "config.json"))
    workers = a.workers or cfg.get("workers") or max(1, (os.cpu_count() or 2) - 0)
    workers = 8
    print("output:", root, flush=True)

    datasets = dataset_list(cfg, grid)
    generate(datasets, os.path.join(root, "datasets"), cfg["params"]["L"])
    todo = [(os.path.join(root, "datasets", n), cfg) for n, _ in datasets
            if not os.path.exists(os.path.join(root, "datasets", n, "compare.csv"))]
    print(f"{len(datasets)} datasets, {len(todo)} to run, {len(cfg['modes'])} modes, {workers} workers", flush=True)

    failures, t0 = [], time.time()
    if todo:
        ctx = mp.get_context("spawn")
        with ctx.Pool(min(workers, len(todo))) as pool:
            for j, res in enumerate(pool.imap_unordered(_safe_run, todo), 1):
                if res[0] == "error":
                    failures.append({"dataset": res[1], "error": res[2]})
                    pd.DataFrame(failures).to_csv(os.path.join(root, "failures.csv"), index=False)
                    print(f"  [{j}/{len(todo)}] {res[1]} FAILED: {res[2].splitlines()[-1]}", flush=True)
                else:
                    eta = (time.time() - t0) / j * (len(todo) - j)
                    print(f"  [{j}/{len(todo)}] {res[1]} done in {res[2]:.0f}s, ETA {eta / 60:.1f} min", flush=True)

    overall = aggregate(root, datasets, cfg)
    if not grid:
        print(open(os.path.join(root, "datasets", datasets[0][0], "compare.md")).read())
    elif overall is not None:
        with pd.option_context("display.width", 250, "display.max_columns", 40):
            print(overall.to_string())
    if failures:
        print(f"{len(failures)} dataset(s) failed, see failures.csv")
    print("saved:", root)


def _safe_run(args):
    try:
        name, secs = run_dataset(args)
        return ("ok", name, secs)
    except Exception:
        return ("error", os.path.basename(args[0]), traceback.format_exc())


if __name__ == "__main__":
    main()
