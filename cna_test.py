"""
cna_test.py -- secondary benchmark: cna inverse search on the anchors of a
run_experiment.py results folder (Baumgartner & Ambuehl style scoring).

For every dataset x mode in the folder:
  raw data + mode anchors (modes/<mode>/anchors.json) -> calibrate (same L as the run)
  outcome calibrated with its true anchor (as in run_experiment.py)
  -> cna(con, cov, maxstep) with a time limit -> score against the true asf

Scores
  n_models        models returned
  timeout         cna hit the time limit (counted separately, NOT as "no model")
  error_free      no model, or at least one model is a submodel of the truth
  correct         at least one model is a submodel of the truth (lenient when many models)
  correct_share   share of returned models that are submodels of the truth
  unique_correct  exactly one model, and it is correct
  exact           the true asf is among the models
  irrelevant_in   share of returned models containing an irrelevant condition
  true_con, true_cov  consistency / coverage of the TRUE asf on the mode's memberships
  true_passes     the true asf itself meets con and cov (if not, cna cannot return it)

Usage
  python cna_test.py results/grid_demo_<timestamp>
  python cna_test.py results/grid_demo_<timestamp> --mode opt --con 0.75 --cov 0.70 --max-secs 30
  python cna_test.py results/grid_demo_<timestamp> --fit-only      # only true_con / true_cov (fast)
"""
import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

import qca_core as q
import simulate_qca_cna as sq          # loads R + cna (rpy2)

r_ = sq._r


def run_cna(mem, outcome, true_asf, irrelevant, con, cov, maxstep, max_secs):
    sq._to_r(mem.round(4), "dd")
    sq.ro.globalenv["asf_t"] = true_asf
    ok = bool(r_(f'''tryCatch({{ setTimeLimit(elapsed={max_secs}, transient=TRUE)
        res <- asf(cna(dd, outcome="{outcome}", con={con}, cov={cov}, maxstep=c({",".join(map(str, maxstep))})))
        setTimeLimit(); TRUE }}, error=function(err) {{ setTimeLimit(); res <<- NULL; FALSE }})''')[0])
    if not ok:
        return {"timeout": True, "n_models": np.nan, "error_free": np.nan, "correct": np.nan,
                "correct_share": np.nan, "unique_correct": np.nan, "exact": np.nan,
                "irrelevant_in": np.nan, "models": ""}
    n = int(r_("if (is.null(res)) 0L else nrow(res)")[0])
    if n == 0:
        return {"timeout": False, "n_models": 0, "error_free": True, "correct": False, "correct_share": 0.0,
                "unique_correct": False, "exact": False, "irrelevant_in": 0.0, "models": ""}
    models = list(r_("as.character(res$condition)"))
    sub = np.array(list(r_("as.logical(unname(is.submodel(res$condition, asf_t)))")), bool)
    exact = bool(r_("any(sapply(res$condition, function(m) isTRUE(unname(identical.model(m, asf_t)))))")[0])
    irr = {f.upper() for f in irrelevant}
    irr_in = np.mean([bool(irr & set(re.findall(r"[A-Za-z]", m.split("<->")[0].upper()))) for m in models])
    return {"timeout": False, "n_models": n, "error_free": bool(sub.any()), "correct": bool(sub.any()),
            "correct_share": float(sub.mean()), "unique_correct": n == 1 and bool(sub.any()),
            "exact": exact, "irrelevant_in": float(irr_in), "models": " | ".join(models[:50])}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("results_dir")
    ap.add_argument("--mode", default=None, help="only this mode")
    ap.add_argument("--con", type=float, default=0.75)
    ap.add_argument("--cov", type=float, default=0.70)
    ap.add_argument("--maxstep", type=int, nargs=3, default=[3, 3, 9])
    ap.add_argument("--max-secs", type=int, default=20, help="time limit per cna call")
    ap.add_argument("--fit-only", action="store_true",
                    help="only compute the fit of the true asf (no cna search)")
    a = ap.parse_args()

    root = Path(a.results_dir)
    cfg_path = root / "config.json"
    L = json.load(open(cfg_path)).get("params", {}).get("L", 3.0) if cfg_path.exists() else 3.0
    mode_order = ([m["name"] for m in json.load(open(cfg_path)).get("modes", [])] if cfg_path.exists() else [])

    rows = []
    for ds in sorted(p for p in root.glob("datasets/*") if (p / "data" / "truth.json").exists()):
        truth = json.load(open(ds / "data" / "truth.json"))
        raw = pd.read_csv(ds / "data" / "raw.csv")
        conds, outcome = truth["conditions"], truth["outcome"]
        true = truth["anchors_exclusion_crossover_inclusion"]
        y = q.calibrate(raw[outcome].to_numpy(float), true[outcome], L)        # same as run_experiment
        for md in sorted(p for p in (ds / "modes").glob("*") if (p / "anchors.json").exists()):
            if a.mode and md.name != a.mode:
                continue
            anchors = json.load(open(md / "anchors.json"))
            mem = pd.DataFrame({f: q.calibrate(raw[f].to_numpy(float), anchors[f], L) for f in conds})
            mem[outcome] = y
            t_con, t_cov = sq.fit_of(truth["asf"], mem.round(4))                   # fit of the true asf
            fit = {"true_con": t_con, "true_cov": t_cov,
                   "true_passes": bool(t_con >= a.con and t_cov >= a.cov)}
            if a.fit_only:
                res = {}
            else:
                try:
                    res = run_cna(mem, outcome, truth["asf"], truth.get("irrelevant", []),
                                  a.con, a.cov, a.maxstep, a.max_secs)
                except Exception as e:                                            # keep going
                    res = {"timeout": False, "n_models": np.nan, "models": f"ERROR: {e}"}
            rows.append({"dataset": ds.name, "mode": md.name, "asf": truth["asf"], **fit, **res})
        print(f"  {ds.name}: done", flush=True)

    if not rows:
        raise SystemExit("no dataset/mode with anchors.json found")
    df = pd.DataFrame(rows)
    order = [m for m in mode_order if m in set(df["mode"])] + sorted(set(df["mode"]) - set(mode_order))
    num = ["n_models", "error_free", "correct", "correct_share", "unique_correct", "exact", "irrelevant_in",
           "true_con", "true_cov", "true_passes"]
    num = [c for c in num if c in df]
    df[num] = df[num].apply(pd.to_numeric, errors="coerce")
    agg = {"datasets": ("dataset", "nunique"), "true_con": ("true_con", "mean"),
           "true_cov": ("true_cov", "mean"), "true_passes": ("true_passes", "mean")}
    if not a.fit_only:
        agg.update(timeouts=("timeout", "mean"), no_model=("n_models", lambda s: (s == 0).mean()),
                   models_median=("n_models", "median"), correct=("correct", "mean"),
                   correct_share=("correct_share", "mean"), unique_correct=("unique_correct", "mean"),
                   exact=("exact", "mean"), error_free=("error_free", "mean"),
                   irrelevant_in=("irrelevant_in", "mean"))
    summary = df.groupby("mode").agg(**agg).reindex(order).round(3)
    print(f"\ncna benchmark (con={a.con}, cov={a.cov}, maxstep={a.maxstep}, L={L}); "
          f"rates exclude time-outs\n")
    print(summary.to_string())
    if not a.fit_only:
        # when the true asf passes the thresholds, how often does cna actually find it?
        ok = df[df["true_passes"] == 1]
        if len(ok):
            print("\nonly datasets where the true asf meets con/cov under the mode's anchors:")
            print(ok.groupby("mode").agg(datasets=("dataset", "nunique"), correct=("correct", "mean"),
                                         exact=("exact", "mean"), correct_share=("correct_share", "mean"))
                  .reindex(order).round(3).to_string())
    tag = f"con{a.con}_cov{a.cov}" + ("_fit" if a.fit_only else "")
    df.to_csv(root / f"cna_benchmark_all_{tag}.csv", index=False)
    summary.to_csv(root / f"cna_benchmark_summary_{tag}.csv")
    print(f"\nsaved: {root / f'cna_benchmark_all_{tag}.csv'}\n       {root / f'cna_benchmark_summary_{tag}.csv'}")


if __name__ == "__main__":
    main()