# n100_noise0.2_frag0.2_fz1_rep01

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=12001
- true model: `E*C*A+C*b<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.510 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.740 | False | 0.000 | 0.000 | 0 | 0.039 | 0.977 | 0.023 | 0.538 |
| kde | 0.790 | False | 0.000 | 0.000 | 0 | 0.046 | 0.965 | 0.035 | 0.540 |
| expert | 0.525 | False | 0.000 | 0.000 | 0 | 0.068 | 0.928 | 0.072 | 0.555 |
| opt | 0.442 | False | 0.888 | 0.484 | 6 | 0.136 | 0.878 | 0.117 | 0.708 |
| opt_c6c7 | 0.411 | False | 0.931 | 0.318 | 2 | 0.055 | 0.925 | 0.072 | 0.557 |
| opt_expert | 0.358 | False | 0.908 | 0.356 | 3 | 0.061 | 0.930 | 0.083 | 0.561 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 0.833 | 0.385 | 1 |
| opt_c6c7 | 1.000 | 0.143 | 0 |
| opt_expert | 1.000 | 0.214 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 0.000 | 0.800 | 1.000 | a*b*C*E*F+A*b*c*d*E*f+A*b*C*d*e*f+A*b*C*D*E*f+A*B*C*d*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*E*F+A*b*C*D*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*E*F+A*b*C*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*C+A*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*E<->G |
| opt_expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | E*F+A*D*E<->G |

