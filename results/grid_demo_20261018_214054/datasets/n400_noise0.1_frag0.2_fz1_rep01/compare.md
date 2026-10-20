# n400_noise0.1_frag0.2_fz1_rep01

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=32001
- true model: `a*b+b*e<->G`  (irrelevant: C, D, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.945 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.544 |
| quantile | 0.900 | False | 0.000 | 0.000 | 0 | 0.036 | 0.973 | 0.026 | 0.529 |
| kde | 0.850 | False | 0.000 | 0.000 | 0 | 0.045 | 0.958 | 0.041 | 0.545 |
| expert | 0.455 | False | 0.000 | 0.000 | 0 | 0.065 | 0.946 | 0.054 | 0.561 |
| opt | 0.820 | True | 0.913 | 0.509 | 13 | 0.119 | 0.935 | 0.060 | 0.711 |
| opt_c6c7 | 0.530 | False | 0.882 | 0.431 | 7 | 0.089 | 0.842 | 0.152 | 0.547 |
| opt_expert | 0.456 | False | 0.906 | 0.417 | 6 | 0.076 | 0.885 | 0.114 | 0.553 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.565 | 0 |
| opt_c6c7 | 1.000 | 0.304 | 0 |
| opt_expert | 1.000 | 0.261 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*e*F+b*C*D*e+a*b*d*F+a*b*c*d*e+a*b*C*F+A*b*D*e<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | b*C*e*F+a*b*c*e*f+a*b*c*d*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+a*b*e*F+a*b*c*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*e*F+b*D*e+a*b<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*e*F+a*b*c<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*e*F+a*b*D*e<->G |

