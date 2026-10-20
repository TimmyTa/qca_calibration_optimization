# Calibration-Anchor Optimization — Method, Design, Scoring

The formal problem is in [`calibration_optimization_problem_en.md`](calibration_optimization_problem_en.md).
This document describes the implementation (`anchor_optimization.py`, `qca_core.py`),
the simulation study (`run_experiment.py`) and the design decisions behind them.

## 1. Problem

```
max_θ  S(a(θ)) − λ R(θ)
s.t.   C2  Cons ≥ 0.80          C3  Cov ≥ 0.50
       C4  0.30 ≤ share(μ_k > .5) ≤ 0.70        every condition k
       C5  |P| ≥ 2
       C6  q_c − q_e ≥ m, q_i − q_c ≥ m          optional (min_side)
       C7  crisp_k ≤ crisp_k(reference) + tol     optional (crisp_tol; or max_crisp)
```

**Variables.** θ_k = (c_k, t_e, t_i) in percentile space:

- q_e = δ + (c − 2δ) t_e
- q_c = c
- q_i = c + δ + (1 − c − 2δ) t_i

This gives C1 (ordering, minimum gap δ = 0.05) by construction. The crossover is
boxed in 𝒞_k = [2δ, 1 − 2δ], or the percentile image of an expert interval.

**S, bootstrap stability.**

- The positive-row set P is the set of truth-table rows coded OUT = 1.
- S is the mean Jaccard similarity between P on B = 200 bootstrap samples and P on
  the full sample.
- The multinomial weights are drawn once, from `bootstrap_seed`.

**OUT rule.** (ν, τ, π) is fixed for the whole optimization and computed **once per
dataset from the raw data** (§3).

**Outcome anchor.** Fixed. Optimizing it would redefine the outcome to make the result
look stable.

**R, regularization (optional).** Squared distance of the crossover percentile to a
reference: KDE antimode, median, expert midpoint or theory.

**Solver.** Differential evolution DE/rand/1/bin, with pop 60, 150 generations,
F = 0.7, CR = 0.9.

- Feasibility rule: a feasible solution beats an infeasible one. Among feasible
  solutions the higher objective wins; among infeasible ones the smaller total
  violation wins.
- A trial replaces its parent when it is **at least as good**. This lets the
  population drift across the plateaus of the piecewise-constant S.
- The population is seeded with the KDE reference anchors and a centre point (and with
  the theory or expert anchors if given).

**Solution set.** The solver is repeated over seeds with the bootstrap weights fixed.
The best run is the point estimate, and the spread of crossovers across seeds is
reported (spec §8). `profile()` computes S_k\*(c).

### C6 and C7: why they exist

Earlier experiments (with `cna` scoring) showed that maximizing S without further
constraints buys stability by making sets **nearly crisp**: e and i get squeezed
toward c. Every case then falls clearly into one truth-table row, so P barely changes
under resampling. But the calibration is distorted and the solution space becomes
ambiguous. On one test dataset this produced 291 `cna` models, 0.7% of them correct.

- **C6** keeps a minimum percentile distance on **each side** of the crossover. A
  minimum total width alone was not enough: the optimizer kept one side wide and
  squeezed the other.
- **C7** caps each condition's crispness, the mean of 2|μ − .5|, at its crispness under
  the KDE reference anchors plus a tolerance. The cap is computed from the raw data
  only.

## 2. Scoring with QCA

Every mode is scored with **the same OUT rule**, so differences come from the anchors.
For each mode:

1. Calibrate (direct method, L = 3.0, which matches the generator).
2. Build the truth table with the shared OUT rule.
3. **Row level**, independent of minimization. Compare the OUT = 1 rows with the rows
   where the true model says the outcome is present: `row_precision`, `row_recall`,
   `false_positive_rows`.
4. **Conservative solution.** Quine–McCluskey on the OUT rows, no remainders. Its terms
   are supersets of true paths when correct:
   - `cs_correct`: every term contains a true path, i.e. no false sufficiency claim.
   - `cs_term_precision`: the share of such terms.
   - `cs_paths_found_sup`: true paths covered.
5. **Parsimonious solution.** Rows with n < ν are used as logical remainders. Correct
   terms are sub-conjunctions of true paths:
   - `ps_sub_correct` / `ps_term_precision_sub`: only true causal literals.
   - `ps_paths_found_sub`, `ps_exact`.
   - `ps_irrelevant_in`: an irrelevant condition appears.
6. `n_cs`, `n_ps` count tied minimal solutions (model ambiguity). Solution metrics are
   averaged over the tied solutions.
7. **Calibration quality:**
   - `membership_mae`, `same_side_0.5`;
   - `crossover_err_pct` (crossover error in percentile points), `crossover_err_scaled`;
   - `crisp`.

`qca_core.minimize` reproduces `qmc_qca.py` exactly on the Meurer et al. example (2
conservative and 19 parsimonious solutions). It caps the exhaustive cover search at
`max_qmc_checks` and falls back to a greedy cover, which sets `qmc_truncated = True`.

`cna`-based scoring is deliberately not part of this version (see TODO).

## 3. The OUT rule and the PRI problem of simulated data

The OUT rule is an analyst's choice, and it must never be tuned with the ground truth.
`rule_from_reference` computes it from the raw data, using the KDE reference anchors:

- `"conventional"` (default): n.cut = the largest frequency threshold that keeps ≥ 80%
  of cases; incl ≥ 0.80; PRI ≥ 0.70.
- `"data_driven"`: n.cut as above; incl and PRI at the middle of the largest gap in the
  row values within [.75, .90] and [.50, .75].
- Fixed values, e.g. `{"nu": 2, "tau": 0.85, "pi": 0.60}` (Meurer et al.).

**Finding.** `makeFuzzy` adds uniform noise up to `fuzzvalues` to crisp
configurations. This pushes memberships toward 0.5 and gives every case partial
membership in many rows, which **lowers the PRI of the truly sufficient rows**. Oracle
check over 6 datasets per cell (N = 150, true anchors):

| fuzzvalues max | noise | median PRI, true rows | median PRI, other rows | row recall, conventional rule | row recall, data-driven rule |
|---|---|---|---|---|---|
| 0.2 | 0 | 0.75 | 0.17 | 1.00 | 0.92 |
| 0.2 | 0.1 | 0.72 | 0.21 | 0.93 | 0.86 |
| 0.4 | 0 | 0.63 | 0.26 | 0.89 | 0.77 |
| 0.4 | 0.1 | 0.61 | 0.30 | 0.86 | 0.49 |

Row precision is ≈ 0.96–1.00 in every cell. Consequences:

- **The conventional rule is the default**, because the gap-based rule is too strict on
  noisy, very fuzzy data.
- **`fuzzvalues` is a design factor** (0.2 = clean, 0.4 = hard). Values ≥ 0.5 create
  memberships of exactly 0.5 and should be avoided.
- **With fixed τ = 0.85 / π = 0.60** (the original specification), even the true
  anchors often yield no or very few OUT rows. The optimizer can then only become
  feasible by distorting the anchors.

## 4. The simulated expert

On real data, the alternative to optimization is the anchors an expert or the original
authors chose. `expert_noisy` simulates an **imperfect** expert:

- crossover moved by N(0, error)·(i − e);
- each side width scaled by exp(N(0, error)).

The default is error = 0.1. Modes:

- **`expert`** uses those anchors directly.
- **`optimize` with `"expert": "noisy"`** limits the crossover to the expert crossover
  ± `expert_box`·(i − e) and starts from the expert anchors.
- **`"expert": "truth_box"`** (box around the **true** crossover) is available, but it
  is **optimistic**: the box always contains the answer.

## 5. Status

- **Pipeline.** Verified end to end: single run, parallel grid, `--resume`, real-data CLI.
- **Earlier pilot (v3 implementation, `cna` scoring).** The optimizer was "stable but
  wrong". It reached higher S than the true anchors and recovered the truth less often
  than simple baselines. Crispification and too-strict truth-table thresholds were the
  main causes.
- **Next.** The pilot of this version, with QCA scoring. See TODO.
