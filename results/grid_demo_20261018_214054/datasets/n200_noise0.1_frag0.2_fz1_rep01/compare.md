# n200_noise0.1_frag0.2_fz1_rep01

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=20001
- true model: `E*c+E*d+C*B<->G`  (irrelevant: A, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.211 | False | 0.910 | 0.286 | 2 | 0.000 | 1.000 | 0.000 | 0.552 |
| quantile | 0.460 | False | 0.000 | 0.000 | 0 | 0.044 | 0.940 | 0.054 | 0.510 |
| kde | 0.213 | False | 0.918 | 0.283 | 1 | 0.031 | 0.973 | 0.030 | 0.518 |
| expert | 0.285 | False | 0.000 | 0.000 | 0 | 0.089 | 0.922 | 0.077 | 0.555 |
| opt | 0.727 | True | 0.935 | 0.503 | 10 | 0.133 | 0.923 | 0.076 | 0.733 |
| opt_c6c7 | 0.385 | False | 0.901 | 0.487 | 7 | 0.068 | 0.892 | 0.112 | 0.526 |
| opt_expert | 0.403 | False | 0.885 | 0.487 | 5 | 0.068 | 0.873 | 0.124 | 0.527 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.074 | 0 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.033 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.357 | 0 |
| opt_c6c7 | 1.000 | 0.219 | 0 |
| opt_expert | 1.000 | 0.172 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.333 | A*C*d*E*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 0.667 | A*B*C*d*E*F<->G |
| expert | 0 |  |  |  | (none) |
| opt | 2 | 1.000 | 1.000 | 1.000 | c*D*E*f+a*B*C*D*e*f+A*c*D*E+A*C*d*E*F+A*B*c*E*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*F+A*c*D*E*f+A*b*d*E*F+A*B*c*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*F+A*b*c*D*E*F+A*B*d*E*F+A*B*c*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | C*d*E<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*E*F<->G |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 3 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | d*E+c*E+a*C*f<->G |
| opt_c6c7 | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*E+A*E*F+A*c*D*E+A*B*E<->G |
| opt_expert | 4 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | d*E+c*D*f+b*c*E<->G |

