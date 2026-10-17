# TODO

## Next runs
- [ ] Pilot: `configs/experiment.json --grid` with `reps = 3` (108 datasets); check opt vs opt_c6c7 vs opt_expert vs baselines on the QCA metrics.
- [ ] Full study: `reps = 20`, `optimize_seeds = 5` on a multi-core machine.
- [ ] `concov` design (Baumgartner & Ambühl 2020 noise mechanism) next to `template`.

## Optimizer
- [ ] Add C6 and C7 to the formal problem statement; sweep `min_side` (0, 0.1, 0.2) and `crisp_tol` (0, 0.05, 0.1). Check whether C6 is still needed with C7, and how often the true anchors violate C6 = 0.2.
- [ ] Constraint or penalty on solution ambiguity (`n_cs`, `n_ps`) as an alternative to C7.
- [ ] Stability at the solution level: minimize on each bootstrap sample and compare solutions instead of positive-row sets.
- [ ] Expert experiments: `expert.error` (0.05, 0.1, 0.2, 0.3) × `expert_box` (0.05, 0.1, 0.2), plus a deliberately biased expert.
- [ ] Sensitivity to `lambda` / `reference`, `share_min` / `share_max`, `B`, `delta`, and the DE settings.
- [ ] Profile plots S_k*(c) for a few datasets.

## Scoring
- [ ] Re-add `cna` inverse search as a secondary benchmark (comparability with Baumgartner & Ambühl 2020).
- [ ] Intermediate solution (directional expectations) next to conservative / parsimonious.
- [ ] Correlation between S and the QCA correctness metrics across datasets and modes.
- [ ] Plots: metrics by noise × n × fuzzvalues per mode.

## Simulation
- [ ] Jitter raw values (makeFuzzy steps of 0.01 → many ties in raw data).
- [ ] Vary the number of conditions (4, 6, 8), model complexity, anchor asymmetry, skewness of raw distributions.
- [ ] Outcome-anchor misspecification.
- [ ] Write up the `psrm2020` validation of the generator.

## Real data
- [ ] Run the Meurer et al. (2025) case study (`configs/meurer2025.json`) and compare with the earlier v3 results.
- [ ] Nested cross-validation for the real-data CLI.

## Engineering
- [ ] Unit tests (`qca_core.minimize` vs reference cases, calibration round trip, parametrization gaps, rule uses no ground truth).
- [ ] Pin versions; save `pip freeze` / R `sessionInfo()` into each results folder.
