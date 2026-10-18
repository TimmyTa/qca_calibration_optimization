# How to Run

## 1. Setup (once)

```bash
# R (only for data generation)
sudo apt install -y r-base r-base-dev
Rscript -e 'install.packages("cna", repos="https://cloud.r-project.org")'

# Python
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install numpy pandas scipy
python3 -m pip install rpy2              # R >= 4.4
# python3 -m pip install rpy2==3.5.16    # R 4.1 - 4.3

python3 -c "import numpy, pandas; from rpy2.robjects.packages import importr; importr('cna'); print('OK')"
```

Activate the environment (`source .venv/bin/activate`) in every new terminal.

## 2. One dataset

```bash
python3 run_experiment.py --config configs/experiment.json
```

- Uses the `"simulation"` section of the config.
- Prints `compare.md`: calibration, OUT rows, and solutions for every mode.
- About 1–3 minutes, depending on `optimize_seeds` and `de.generations`.

Output: `results/<name>_<timestamp>/datasets/<dataset>/`

| File | Content |
|---|---|
| `data/raw.csv` | Raw data: the only input the modes see. |
| `data/true_memberships.csv`, `data/truth.json` | Answer key: true model, anchors, design. |
| `modes/<mode>/anchors.json` | Anchors of the mode. |
| `modes/<mode>/truth_table.csv` | n, incl, PRI, OUT, truth, bootstrap frequency of OUT per row. |
| `modes/<mode>/calibrated.csv` | Calibrated memberships. |
| `modes/<mode>/solutions.json` | Conservative and parsimonious solutions. |
| `modes/<mode>/seeds.csv` | Optimize modes only: one row per solver seed. |
| `compare.csv`, `compare.md` | One row per mode. |
| `anchors_compare.csv` | Estimated vs true anchors per condition. |

## 3. Grid

```bash
python3 run_experiment.py --config configs/experiment.json --grid --workers 8
# long runs: in the background
nohup python3 run_experiment.py --config configs/experiment.json --grid --workers 8 > run.log 2>&1 &
tail -f run.log
```

- **Data first.** All datasets are generated first, in the main process with R.
- **Then in parallel.** Modes run in parallel worker processes, Python only.
- **Saved as you go.** Every finished dataset is written immediately.

**Interrupted?** Continue with:

```bash
python3 run_experiment.py --resume results/grid_demo_<timestamp> --workers 8
```

Finished datasets are skipped; failed ones are listed in `failures.csv`.

Results in the run folder:

- `grid_all.csv`: every dataset × mode row.
- `grid_summary_by_mode.csv`: mean per mode.
- `grid_summary.csv`: mean per setting × mode.
- `summary.md`: readable tables, including metrics by noise × n.

Runtime scales with datasets × optimize modes × `optimize_seeds` × `de.generations`.
With the default config, one dataset takes about 2–4 CPU-minutes.

## 4. Config (`configs/experiment.json`)

| Key | Meaning |
|---|---|
| `simulation` | One dataset: `n`, `k`, `mode` (template / concov), `noise`, `frag`, `seed`, `fuzzvalues`. |
| `grid` | Lists for `n`, `noise`, `frag`, `fuzzvalues`; `reps`; `seed_base`. |
| `qca_rule` | OUT rule used by the optimizer **and** for scoring every mode: `"conventional"` (n.cut from the data, incl ≥ .80, PRI ≥ .50), `"data_driven"`, or `{"nu": "auto"/int, "tau": .., "pi": ..}`. |
| `expert.error` | Error of the simulated expert. |
| `optimize_seeds` | Solver seeds per optimize mode (overridable per mode with `n_seeds`). |
| `workers` | Parallel processes (default: all cores). |
| `modes` | List of `{"name", "mode", …}`; see README. |
| `params` | Optimizer defaults (`anchor_optimization.DEFAULTS`); overridable per mode. |

Useful mode variants:

```json
{"name": "opt",          "mode": "optimize"},
{"name": "opt_c6c7",     "mode": "optimize", "params": {"min_side": 0.2, "crisp_tol": 0.0}},
{"name": "opt_expert",   "mode": "optimize", "params": {"min_side": 0.2, "crisp_tol": 0.0}, "expert": "noisy", "expert_box": 0.1},
{"name": "opt_truthbox", "mode": "optimize", "expert": "truth_box", "expert_box": 0.5},
{"name": "opt_profile",  "mode": "optimize", "profile": 9}
```

`fuzzvalues` sets how far memberships are pushed toward 0.5 by `makeFuzzy`. With 0.4,
the true rows have low PRI (median ≈ 0.6, some below 0.5). Keep values ≤ 0.45 to avoid
memberships of exactly 0.5.

## 5. Real data

```bash
cp configs/template.json configs/my_study.json      # fill in data, conditions, outcome, outcome_anchor
python3 anchor_optimization.py configs/my_study.json
```

This prints the OUT rule, the solver seeds, and, for the KDE reference / theory /
optimized anchors, S, Cons, Cov, the OUT rows and the conservative and parsimonious
solutions. It writes `comparison.csv`, `anchors_optimized.csv` and `seeds.csv` to
`out_dir`.

Case study: `python3 anchor_optimization.py configs/meurer2025.json` (set `"data"` to the
path of their `data.xlsx`).


## 5.2  CNA Test
```bash
  python cna_test.py results/grid_demo_<timestamp>
  python cna_test.py results/grid_demo_<timestamp> --mode opt --con 0.75 --cov 0.70 --max-secs 30
  python cna_test.py results/grid_demo_<timestamp> --fit-only      # only true_con / true_cov (fast)

```

## 6. View results (Streamlit GUI)

Visualise grid results interactively — no need to open CSV files by hand.

### Install

```bash
source .venv/bin/activate
python3 -m pip install streamlit plotly
```

### Run

```bash
streamlit run streamlit_app.py
```

Open `http://localhost:8501`.

Or point directly at one result folder:

```bash
streamlit run streamlit_app.py -- --root results/grid_demo_20261017_082529
```

Run in the background (server):

```bash
nohup streamlit run streamlit_app.py --server.port 8501 --server.headless true > streamlit.log 2>&1 &
tail -f streamlit.log
```

### Sidebar

| Item | Meaning |
|---|---|
| **Root folder** | Enter `results/` (or any folder containing `grid_all.csv`); the app finds every sub-folder with `grid_all.csv`. |
| **Result folder** | Dropdown of the folders found. |
| **Filters** | `mode`, `n`, `noise`, `frag`, `fuzz_id`. |
| **Metrics** | Select the metrics to display (default: `S`, `crisp`, `row_recall`, `membership_mae`, `ps_exact`, `cs_correct`). |

### Tabs

| Tab | Content |
|---|---|
| **Summary** | Mean per mode + bar chart + `summary.md`. |
| **Compare modes** | Pivot table (mode × setting) + box plot of the metric distribution. |
| **Trend** | Line plot over `noise` / `frag` / `n`, optional facet. |
| **Heatmap** | 2-D heatmap (e.g. `noise` × `frag`), selectable metric and mode. |
| **Scatter** | Scatter of any two metrics, coloured by mode / n / noise / frag. |
| **Dataset** | One dataset in detail: `compare.csv`, `compare.md`, `anchors_compare.csv`, `truth.json`, and under `modes/<mode>/`: `anchors.json`, `solutions.json`, `truth_table.csv`, `calibrated.csv`, `seeds.csv`. |
| **Raw** | Filtered `grid_all.csv` + **download CSV** button + `config.json` + `failures.csv` (if present). |

### Notes

- The app **caches** data (`st.cache_data`) → fast after the first load.
- The filtered table can be **downloaded** as CSV.
- If the folder contains `failures.csv`, it is shown on the **Raw** tab.
- If `grid_all.csv` lacks a column (`n`, `noise`, ...), the app still runs — only the
  corresponding filter is hidden.


## 7. Troubleshooting

| Problem | Fix |
|---|---|
| `undefined symbol: R_getVar` | R < 4.4: `pip install rpy2==3.5.16` |
| `No module named 'scipy'` etc. | activate the venv; `python3 -m pip install numpy pandas scipy` |
| rpy2 cannot find R | `export R_HOME=$(R RHOME)` |
| slow | lower `de.generations` / `optimize_seeds`, raise `--workers`; BLAS is limited to 1 thread on purpose |
| `qmc_truncated = True` | minimization hit `max_qmc_checks`; a greedy cover was used for that solution |
| Streamlit does not start | `python3 -m pip install streamlit plotly` inside the venv; check `streamlit run --help` |
| Streamlit finds no `grid_all.csv` | enter the folder that contains `results/`, or the run folder itself; the app searches recursively |