# fsQCA Calibration-Anchor Optimization — Simulation Study (QCA scoring)

Does optimizing fsQCA calibration anchors (maximizing bootstrap stability of the
truth-table conclusion under fit constraints) lead to **correct QCA results**? This
repository simulates data with a known causal structure and known calibration anchors.
It then compares the optimizer with simple baselines, a simulated imperfect expert and
an oracle that knows the true anchors, all scored with **QCA**: truth table →
OUT rows → conservative / parsimonious solutions → comparison with the true model.

## Files

| File | Purpose |
|---|---|
| `qca_core.py` | fsQCA building blocks: calibration, truth table, OUT rule, Quine–McCluskey minimization, comparison of solutions with the true model. Pure Python. |
| `anchor_optimization.py` | The optimizer (problem statement + C6/C7), reference anchors, OUT rule from data. Library and CLI for real data. |
| `run_experiment.py` | Simulation study: generate → all modes → QCA scoring → summaries. Single dataset or grid, parallel, resumable. |
| `simulate_qca_cna.py` | Data generator (R package `cna` via rpy2): random causal model, fuzzy memberships, raw layer with known anchors. |
| `configs/experiment.json` | Simulation-study configuration. |
| `configs/template.json` | Template for real data. |
| `configs/meurer2025.json` | Meurer et al. (2025) case study. |
| `docs/optimization.md` | Method, design decisions, scoring, findings. |
| `docs/calibration_optimization_problem_en.md` | Formal problem statement. |
| `HOW_TO_RUN.md` | Setup and run guide. |
| `TODO.md` | Open work. |

R is needed **only to generate data**; optimization and scoring are pure Python.

## Pipeline

```
run_experiment.py
 step 1  simulate (main process, R/cna)
         random asf, fragmentation, noise, makeFuzzy  -> true memberships
         known asymmetric anchors, inverse calibration -> raw data
 step 2  per dataset (parallel workers, Python only)
         OUT rule from the raw data (same for every mode)
         modes: oracle | quantile | kde | expert | optimize (+ variants)
         anchors -> calibrate -> truth table -> OUT rows -> conservative / parsimonious solutions
         score vs truth: anchors, memberships, OUT rows, solution terms
 step 3  grid_all.csv, grid_summary_by_mode.csv, grid_summary.csv, summary.md
```

## Modes

| Mode | Anchors |
|---|---|
| `oracle` | True anchors (upper bound). |
| `quantile` | 5th / 50th / 95th percentiles. |
| `kde` | KDE-antimode crossover, 5 / 95 percentiles (data-only reference). |
| `expert` | Simulated imperfect expert: true anchors + error (`expert.error`). |
| `optimize` | The optimizer; per-mode `params` (e.g. C6 `min_side`, C7 `crisp_tol`), and optionally the expert: `"expert": "noisy"` (box around the expert's crossover) or `"truth_box"` (optimistic: box around the true crossover). |

## Main metrics (per dataset × mode; averaged in the summaries)

| Metric | Meaning |
|---|---|
| `row_precision` | Share of OUT = 1 rows where the true model says the outcome is present. |
| `row_recall` | Share of observed true rows that are coded OUT = 1. |
| `cs_correct`, `cs_term_precision` | Conservative solution: all terms / share of terms that contain a true path (no false sufficiency claim). |
| `cs_paths_found_sup` | Share of true paths contained in some conservative term. |
| `ps_sub_correct`, `ps_term_precision_sub` | Parsimonious solution: all terms / share of terms that are sub-conjunctions of a true path (only true causal literals). |
| `ps_paths_found_sub`, `ps_exact` | Parsimonious completeness / exact recovery. |
| `ps_irrelevant_in` | The parsimonious solution mentions an irrelevant condition. |
| `n_cs`, `n_ps` | Number of tied minimal solutions (model ambiguity). |
| `membership_mae`, `same_side_0.5`, `crossover_err_pct`, `crisp` | Calibration quality against the true anchors. |
| `S`, `feasible`, `cons`, `cov` | Objective and constraints under the dataset's OUT rule. |

## Quick start

```bash
python3 run_experiment.py --config configs/experiment.json                 # one dataset
python3 run_experiment.py --config configs/experiment.json --grid          # grid
python3 run_experiment.py --resume results/grid_demo_<timestamp>           # continue
python3 anchor_optimization.py configs/template.json                       # real data
streamlit run streamlit_app.py                       # view demo result
```

See [HOW_TO_RUN.md](HOW_TO_RUN.md).

## References

- Ragin, C. C. (2008). *Redesigning Social Inquiry: Fuzzy Sets and Beyond*. University of Chicago Press.
- Baumgartner, M., & Ambühl, M. (2020). Causal modeling with multi-value and fuzzy-set Coincidence Analysis. *Political Science Research and Methods*, 8(3), 526–542.
- Ambühl, M., & Baumgartner, M. *cna* R package (vignette, section "Benchmarking").
- Krogslund, C., Choi, D. D., & Poertner, M. (2015). Fuzzy sets on shaky ground. *Political Analysis*, 23(1), 21–41.
- Oana, I.-E., & Schneider, C. Q. (2024). A robustness test protocol for applied QCA. *Sociological Methods & Research*, 53(1), 57–88.
