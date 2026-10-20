# n200_noise0.1_frag0.0_fz1_rep01

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=18001
- true model: `e*F*c+B*F*C<->G`  (irrelevant: A, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.880 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.559 |
| quantile | 0.640 | False | 0.000 | 0.000 | 0 | 0.055 | 0.974 | 0.030 | 0.548 |
| kde | 0.645 | False | 0.000 | 0.000 | 0 | 0.051 | 0.978 | 0.023 | 0.549 |
| expert | 0.845 | False | 0.000 | 0.000 | 0 | 0.086 | 0.863 | 0.137 | 0.537 |
| opt | 0.683 | True | 0.936 | 0.504 | 11 | 0.135 | 0.939 | 0.066 | 0.763 |
| opt_c6c7 | 0.453 | False | 0.930 | 0.472 | 6 | 0.081 | 0.902 | 0.105 | 0.553 |
| opt_expert | 0.506 | False | 0.920 | 0.499 | 8 | 0.074 | 0.920 | 0.085 | 0.546 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.733 | 0 |
| opt_c6c7 | 1.000 | 0.500 | 0 |
| opt_expert | 1.000 | 0.667 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e*F+B*c*d*e*F+B*C*D*E*F+a*c*e*F+a*B*C*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*F+a*b*c*d*e*F+A*b*c*D*e*F+A*B*C*E*F+A*B*C*d*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*C*E*F+a*c*d*e*F+A*B*c*D*e*F+A*B*C*d*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 3 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | D*e*F+B*C*F+a*c*e*F+A*B*d<->G |
| opt_c6c7 | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*F+a*c*e+a*B*d*E+A*B*C*F<->G |
| opt_expert | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*D*e*F+B*C*F+a*c*e*F<->G |

