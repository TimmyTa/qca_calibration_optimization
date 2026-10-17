"""
Simulated data for testing fsQCA calibration methods.
Python driver; the data-generating step calls the R package `cna`
(Ambuehl & Baumgartner) through rpy2.

Two tiers
---------
Tier 1 -- causal structure + fuzzy memberships (R package cna).
  mode="template" (default) follows the inverse-search benchmark template in
  the cna vignette ("Benchmarking" section, cna >= 4.0):
      randomAsf(full.ct(k+1))           ground-truth structure (asf)
      selectCases(asf, full)            ideal data: configurations compatible with asf
      drop `frag` share of them         fragmentation (limited diversity)
      sample n cases, `noise` share     noise = cases INcompatible with the asf
        drawn from the incompatible set
      makeFuzzy(fuzzvalues=seq(0,.4,.01))  fuzzification, as in the vignette
  mode="concov" uses selectCases1(asf, con, cov) instead, i.e. noise is
  controlled through target consistency/coverage.
  mode="psrm2020" reproduces the 2x2x2x2 fuzzy-set test design (tests 17-32)
  of the replication script of Baumgartner & Ambuehl (2020, PSRM 8:526-542;
  Harvard Dataverse doi:10.7910/DVN/YIEAF1): irrelevant factor included,
  relevant factor omitted, fragmentation (50% of rows), imperfect con=cov=.8.
  Differences from the script: the DGS is drawn with cna::randomAsf instead
  of the QCApro-style randomDGS helper, and the omitted factor is a random
  factor of the DGS instead of always "A".

Tier 2 -- calibration layer (this project's addition, not from cna):
  each membership is mapped back to a RAW value by inverting Ragin's (2008)
  direct calibration with KNOWN, asymmetric anchors (exclusion, crossover,
  inclusion). Recalibrating the raw data with the true anchors returns the
  Tier-1 memberships, so a calibration method can be scored on (a) anchor
  error and (b) whether the true asf is recovered.

Requirements: R >= 4.1 with package cna (>= 4.0); Python: rpy2, numpy, pandas.
(With R 4.3 use rpy2==3.5.16.)

Usage
-----
    python simulate_qca_cna.py --demo
    python simulate_qca_cna.py --grid --check --out sim_cna_grid
    python simulate_qca_cna.py --grid --mode concov --out sim_concov_grid
    python simulate_qca_cna.py --grid --check --mode psrm2020 --out sim_psrm2020_grid
"""
import argparse
import json
import os
import re

import numpy as np
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.packages import importr

cna = importr("cna")
LOGODDS_FULL = 3.0  # direct method: inclusion -> 0.95, exclusion -> 0.05
FUZZVALUES = "seq(0, 0.4, 0.01)"  # as in the cna vignette's fuzzy example


# ---------------------------------------------------------------- Tier 2 ----
def calibrate(x, anchors):
    """Ragin's direct method."""
    e, c, i = anchors
    x = np.asarray(x, float)
    lo = np.where(x >= c, LOGODDS_FULL * (x - c) / (i - c),
                  LOGODDS_FULL * (x - c) / (c - e))
    return 1.0 / (1.0 + np.exp(-lo))


def decalibrate(m, anchors, eps=0.005):
    """Inverse of calibrate(): membership -> raw value."""
    e, c, i = anchors
    m = np.clip(np.asarray(m, float), eps, 1 - eps)
    lo = np.log(m / (1 - m))
    return np.where(lo >= 0, c + lo * (i - c) / LOGODDS_FULL,
                    c + lo * (c - e) / LOGODDS_FULL)


def random_anchors(rng):
    """Asymmetric anchors on an arbitrary raw scale, so 'symmetric' or
    percentile defaults are not accidentally correct."""
    c = rng.uniform(20, 80)
    left = rng.uniform(5, 25)
    right = rng.uniform(5, 25)
    return (round(c - left, 3), round(c, 3), round(c + right, 3))


# ---------------------------------------------------------------- Tier 1 ----
def _r(code):
    return ro.r(code)


def _to_py(name):
    with localconverter(ro.default_converter + pandas2ri.converter):
        return ro.conversion.rpy2py(_r(name)).reset_index(drop=True)


def _to_r(df, name):
    with localconverter(ro.default_converter + pandas2ri.converter):
        ro.globalenv[name] = ro.conversion.py2rpy(df)


def draw_asf(k, outcome, compl="list(2:3, 2:3)", min_paths=2, min_irrelevant=1):
    """randomAsf, redrawn until the structure has >= min_paths disjuncts
    (equifinality), at least one conjunction, and >= min_irrelevant
    conditions that do not appear in it (decoys)."""
    for _ in range(500):
        _r(f'asf <- randomAsf(ct, outcome="{outcome}", compl={compl})')
        lhs = str(_r("asf")[0]).split("<->")[0]
        n_used = len(set(re.findall(r"[A-Za-z]", lhs.upper())))
        if (lhs.count("+") + 1 >= min_paths and "*" in lhs
                and k - n_used >= min_irrelevant):
            return
    raise RuntimeError("could not draw an asf meeting the constraints")


def membership_template(n, noise, frag):
    """cna vignette benchmark template: ideal data -> fragmentation ->
    noise from incompatible configurations -> makeFuzzy."""
    _r("full <- ct2df(ct)")
    _r("ideal <- ct2df(selectCases(asf, full))")
    _r(f"keep <- ideal[sample(nrow(ideal), max(1, nrow(ideal) - round(nrow(ideal) * {frag}))), , drop=FALSE]")
    _r("incomp <- full[!(do.call(paste, full) %in% do.call(paste, ideal)), , drop=FALSE]")
    n_noise = int(round(noise * n))
    _r(f"x <- keep[sample(nrow(keep), {n - n_noise}, replace=TRUE), , drop=FALSE]")
    if n_noise > 0:
        _r(f"x <- rbind(x, incomp[sample(nrow(incomp), {n_noise}, replace=TRUE), , drop=FALSE])")
    _r("x <- x[sample(nrow(x)), , drop=FALSE]; rownames(x) <- NULL")
    _r(f"d <- ct2df(makeFuzzy(x, fuzzvalues={FUZZVALUES}))")
    _r("d <- d[sample(nrow(d)), , drop=FALSE]; rownames(d) <- NULL")
    n_configs = int(_r("nrow(ideal)")[0])
    return {"ideal_configs": n_configs,
            "kept_configs": int(_r("nrow(keep)")[0]),
            "noise_cases": n_noise}


def membership_concov(n, con, cov, chunk=150, max_tries=200):
    """Alternative: selectCases1 keeps cases so that the asf reaches con/cov.
    Run in chunks (selectCases1 is slow on large pools); if every chunk meets
    con/cov >= target, the stacked data does too."""
    _r("d <- NULL")
    for _ in range(max_tries):
        _r(f"s <- some(ct, n={chunk}, replace=TRUE)")
        _r(f"fz <- makeFuzzy(s, fuzzvalues={FUZZVALUES})")
        _r(f"d <- rbind(d, ct2df(selectCases1(asf, con={con}, cov={cov}, fz)))")
        if int(_r("nrow(d)")[0]) >= n:
            break
    else:
        raise RuntimeError("selectCases1 could not return enough cases")
    _r(f"d <- d[sample(nrow(d), {n}), , drop=FALSE]; rownames(d) <- NULL")
    return {}


# Parameters of the fuzzy-set inverse-search tests 17-32 in the replication
# script of Baumgartner & Ambuehl (2020, PSRM; Dataverse doi:10.7910/DVN/YIEAF1).
# 2x2x2x2 design: irrelevant factor included / relevant factor omitted /
# fragmentation (50% of rows kept) / imperfect con=cov=.8 (selectCases1).
PSRM2020 = {
    "pool_perfect": 300,        # some(mydata, n=..., replace=TRUE); 150-500 in the script
    "pool_imperfect": 80,       # 30-80 in the script
    "fuzz_perfect": "seq(0, 0.3, 0.1)",
    "fuzz_imperfect": "seq(0, 0.3, 0.01)",
    "con_cov_imperfect": 0.8,
    "keep_share_frag": 0.5,     # "diversity index about 50%"
}


def membership_psrm2020(irrelevant, omit, frag, imperfect, rng):
    """Baumgartner & Ambuehl (2020) fs-test design:
    some(full, n, replace=TRUE) -> makeFuzzy -> selectCases(type="fs")
    [perfect] or selectCases1(con=.8, cov=.8) [imperfect] -> optional 50%
    row sampling [fragmentation] -> optional dropping of one relevant factor."""
    p = PSRM2020
    pool = p["pool_imperfect"] if imperfect else p["pool_perfect"]
    fuzz = p["fuzz_imperfect"] if imperfect else p["fuzz_perfect"]
    _r(f"x <- makeFuzzy(some(mydata, n={pool}, replace=TRUE), fuzzvalues={fuzz})")
    if imperfect:
        c = p["con_cov_imperfect"]
        _r(f"d <- ct2df(selectCases1(asf, con={c}, cov={c}, x))")
    else:
        _r('d <- ct2df(selectCases(asf, x, type="fs"))')
    if frag:
        _r(f"d <- d[sample(nrow(d), floor(nrow(d) * {p['keep_share_frag']})), , drop=FALSE]")
    _r("d_full <- d; rownames(d_full) <- NULL")   # before omission, for fit_of
    dropped = None
    if omit:
        lhs = str(_r("asf")[0]).split("<->")[0]
        used = sorted(set(re.findall(r"[A-Za-z]", lhs.upper())))
        dropped = str(rng.choice(used))
        _r(f'd <- d[, setdiff(names(d), "{dropped}"), drop=FALSE]')
    _r("rownames(d) <- NULL")
    return {"pool": pool, "fuzzvalues": fuzz, "omitted_factor": dropped}


def fit_of(asf, mem):
    """Consistency/coverage of the true asf in the generated data."""
    _to_r(mem, "dd")
    ro.globalenv["asf_t"] = asf
    info = _r('attr(condition(asf_t, dd), "info")')
    return float(info.rx2("con")[0]), float(info.rx2("cov")[0])


def recovered(asf, mem, outcome, con, cov):
    """Inverse search scoring (cna vignette, 'Benchmarking'):
    error_free - no model, or at least one model is a submodel of the truth
    correct    - at least one model is a submodel of the truth
    exact      - at least one model is identical to the truth."""
    _to_r(mem, "dd")
    ro.globalenv["asf_t"] = asf
    _r(f'res <- asf(cna(dd, outcome="{outcome}", con={con}, cov={cov}))')
    n_mod = int(_r("nrow(res)")[0])
    if n_mod == 0:
        return {"n_models": 0, "error_free": True, "correct": False, "exact": False}
    correct = bool(_r("any(unname(is.submodel(res$condition, asf_t)))")[0])
    exact = bool(_r("any(sapply(res$condition, function(m) isTRUE(unname(identical.model(m, asf_t)))))")[0])
    return {"n_models": n_mod, "error_free": correct, "correct": correct, "exact": exact}


# ------------------------------------------------------------- full pipeline
def simulate(n=150, k=6, mode="template", noise=0.1, frag=0.2,
             con=0.85, cov=0.85, seed=0, asf=None, cell=None, **asf_kw):
    """cell (mode="psrm2020" only): dict with boolean keys
    irrelevant, omit, frag, imperfect. n and k are then set by the design."""
    rng = np.random.default_rng(seed)
    _r(f"set.seed({int(seed)})")
    if mode == "psrm2020":
        cell = cell or {}
        n_exo = 4 if cell.get("omit") else 3          # as in the script
        letters = [chr(ord("A") + j) for j in range(n_exo + 1 + bool(cell.get("irrelevant")))]
        outcome = letters[n_exo]                       # irrelevant factor comes after the outcome
        _r(f"ct <- full.ct({n_exo + 1})")              # frame for the DGS
        _r(f"mydata <- full.ct({len(letters)})")       # data frame incl. irrelevant factor
        if asf is None:
            _r(f'asf <- randomAsf(ct, outcome="{outcome}")')
        else:
            ro.globalenv["asf"] = asf
    else:
        letters = [chr(ord("A") + j) for j in range(k + 1)]
        outcome = letters[-1]
        _r(f"ct <- full.ct({k + 1})")
        if asf is None:
            draw_asf(k, outcome, **asf_kw)
        else:
            ro.globalenv["asf"] = asf
    asf_str = str(_r("asf")[0])

    if mode == "psrm2020":
        meta = membership_psrm2020(rng=rng, **{key: bool(cell.get(key)) for key in
                                               ("irrelevant", "omit", "frag", "imperfect")})
        design = {"mode": mode, **{key: bool(cell.get(key)) for key in
                                   ("irrelevant", "omit", "frag", "imperfect")}, **meta}
    elif mode == "template":
        meta = membership_template(n, noise, frag)
        design = {"mode": mode, "noise": noise, "fragmentation": frag, **meta}
    elif mode == "concov":
        meta = membership_concov(n, con, cov)
        design = {"mode": mode, "target_con_cov": [con, cov]}
    else:
        raise ValueError(mode)
    mem = _to_py("d")
    mem_full = _to_py("d_full") if mode == "psrm2020" else mem
    n = len(mem)

    factors = list(mem.columns)
    used = set(re.findall(r"[A-Za-z]", asf_str.split("<->")[0].upper()))
    anchors = {f: random_anchors(rng) for f in factors}
    raw = pd.DataFrame({f: decalibrate(mem[f], anchors[f]) for f in factors})
    raw.insert(0, "case", [f"c{j:03d}" for j in range(1, n + 1)])
    con_a, cov_a = fit_of(asf_str, mem_full)
    truth = {
        "asf": asf_str,
        "outcome": outcome,
        "conditions": [f for f in factors if f != outcome],
        "relevant": sorted(used),
        "irrelevant": [f for f in factors if f != outcome and f not in used],
        "omitted_relevant": design.get("omitted_factor"),
        "anchors_exclusion_crossover_inclusion": anchors,
        "design": design,
        "actual_con_cov": [round(con_a, 4), round(cov_a, 4)],
        "fuzzvalues": design.get("fuzzvalues", FUZZVALUES),
        "n": n, "seed": seed,
    }
    return raw, mem, truth


def check_thresholds(truth, fixed=None):
    """Thresholds for the inverse-search check. Default: just below the
    realised fit of the true asf (an oracle setting, i.e. an upper bound)."""
    if fixed is not None:
        return fixed, fixed
    c, v = truth["actual_con_cov"]
    return (max(0.5, np.floor(c * 100) / 100 - 0.01),
            max(0.5, np.floor(v * 100) / 100 - 0.01))


def psrm2020_thresholds(design):
    """cna thresholds used for the fs tests in the 2020 replication script:
    perfect data con=cov=1 (cov lowered to .8 when a relevant factor is
    omitted); imperfect data con=cov=.8 (cov=.75 with omission)."""
    if design["imperfect"]:
        return 0.8, (0.75 if design["omit"] else 0.8)
    return 1.0, (0.8 if design["omit"] else 1.0)


PSRM_CELLS = [dict(irrelevant=i, omit=o, frag=f, imperfect=m)
              for m in (False, True) for f in (False, True)
              for o in (False, True) for i in (False, True)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--grid", action="store_true")
    ap.add_argument("--mode", choices=["template", "concov", "psrm2020"], default="template")
    ap.add_argument("--out", default="sim_cna_grid")
    ap.add_argument("--reps", type=int, default=None,
                    help="trials per cell (default 20; 50 for psrm2020, as in the paper)")
    ap.add_argument("--check", action="store_true",
                    help="run the cna inverse search on the true memberships")
    ap.add_argument("--check-con", type=float, default=None,
                    help="fixed con=cov for the check (default: just below realised fit)")
    a = ap.parse_args()
    if a.reps is None:
        a.reps = 50 if a.mode == "psrm2020" else 20

    def thresholds(truth):
        if a.mode == "psrm2020" and a.check_con is None:
            return psrm2020_thresholds(truth["design"])
        return check_thresholds(truth, a.check_con)

    if a.demo or not a.grid:
        cell = dict(irrelevant=True, omit=False, frag=False, imperfect=True)
        raw, mem, truth = simulate(n=150, mode=a.mode, seed=42,
                                   cell=cell if a.mode == "psrm2020" else None)
        out = raw.round(4).copy()
        for f in mem.columns:
            out[f"{f}_true_mem"] = mem[f].values
        out.to_csv("sim_cna_main.csv", index=False)
        with open("sim_cna_main_truth.json", "w") as fh:
            json.dump(truth, fh, indent=2)
        back = np.allclose(calibrate(raw["A"], truth["anchors_exclusion_crossover_inclusion"]["A"]),
                           np.clip(mem["A"], 0.005, 0.995), atol=1e-6)
        print("true asf:", truth["asf"], "| irrelevant:", truth["irrelevant"])
        print("design:", truth["design"], "| actual con/cov:", truth["actual_con_cov"])
        print("recalibration round-trip ok:", back)
        print("inverse search on true memberships:",
              recovered(truth["asf"], mem, truth["outcome"], *thresholds(truth)))

    if a.grid:
        os.makedirs(a.out, exist_ok=True)
        rows = []
        if a.mode == "psrm2020":
            for ci, cell in enumerate(PSRM_CELLS):
                tag = "".join(k[0].upper() if v else "-" for k, v in cell.items())
                for rep in range(a.reps):
                    name = f"cell{ci + 1:02d}_{tag}_rep{rep:02d}"
                    raw, mem, truth = simulate(mode="psrm2020", cell=cell,
                                               seed=2_000_000 + 1000 * ci + rep)
                    raw.round(4).to_csv(f"{a.out}/{name}.csv", index=False)
                    row = {"dataset": name, **{key: (json.dumps(v) if isinstance(v, (dict, list)) else v)
                                               for key, v in truth.items()}}
                    if a.check:
                        row.update({f"cna_{key}": v for key, v in recovered(
                            truth["asf"], mem, truth["outcome"], *thresholds(truth)).items()})
                    rows.append(row)
        if a.mode == "template":
            levels = [(nz, fr) for nz in (0.0, 0.1, 0.2) for fr in (0.0, 0.3)]
        elif a.mode == "concov":
            levels = [(lv, lv) for lv in (0.95, 0.85, 0.75)]
        else:
            levels = []
        for n in ((50, 150, 500) if levels else ()):
            for li, (p1, p2) in enumerate(levels):
                for rep in range(a.reps):
                    seed = 1_000_000 + 10_000 * li + 100 * n + rep
                    if a.mode == "template":
                        name = f"n{n}_noise{p1}_frag{p2}_rep{rep:02d}"
                        raw, mem, truth = simulate(n=n, mode="template", noise=p1, frag=p2, seed=seed)
                    else:
                        name = f"n{n}_fit{p1}_rep{rep:02d}"
                        raw, mem, truth = simulate(n=n, mode="concov", con=p1, cov=p2, seed=seed)
                    raw.round(4).to_csv(f"{a.out}/{name}.csv", index=False)
                    row = {"dataset": name, **{key: (json.dumps(v) if isinstance(v, (dict, list)) else v)
                                               for key, v in truth.items()}}
                    if a.check:
                        row.update({f"cna_{key}": v for key, v in recovered(
                            truth["asf"], mem, truth["outcome"],
                            *thresholds(truth)).items()})
                    rows.append(row)
        pd.DataFrame(rows).to_csv(f"{a.out}/ground_truth.csv", index=False)
        print(f"wrote {len(rows)} datasets + ground_truth.csv to {a.out}/")


if __name__ == "__main__":
    main()
