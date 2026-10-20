# n200_noise0.2_frag0.0_fz0_rep02

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=21002
- true model: `A*b*d+E*d*b<->G`  (irrelevant: C, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.155 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.796 |
| quantile | 0.885 | False | 0.000 | 0.000 | 0 | 0.096 | 0.978 | 0.011 | 0.609 |
| kde | 0.920 | False | 0.000 | 0.000 | 0 | 0.047 | 1.000 | 0.000 | 0.705 |
| expert | 0.357 | False | 0.870 | 0.280 | 3 | 0.086 | 0.984 | 0.016 | 0.701 |
| opt | 0.479 | False | 0.811 | 0.437 | 7 | 0.113 | 0.886 | 0.124 | 0.753 |
| opt_c6c7 | 0.453 | False | 0.820 | 0.338 | 6 | 0.127 | 0.904 | 0.093 | 0.663 |
| opt_expert | 0.416 | False | 0.810 | 0.377 | 7 | 0.125 | 0.897 | 0.104 | 0.653 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.273 | 0 |
| opt | 0.857 | 0.600 | 1 |
| opt_c6c7 | 0.833 | 0.500 | 1 |
| opt_expert | 0.714 | 0.455 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*d*E*F+A*b*C*d*e*f<->G |
| opt | 1 | 0.000 | 0.833 | 1.000 | b*c*d*e*f+a*b*c*d*E*F+a*b*C*d*E*f+A*b*d*e*f+A*b*c*d*f+A*b*c*d*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.833 | 1.000 | a*b*c*d*e*f+a*b*c*d*E*F+a*b*C*d*E*f+A*b*c*d*e*F+A*b*c*d*E*f+A*b*C*d*e*f<->G |
| opt_expert | 2 | 0.000 | 0.500 | 1.000 | b*C*d*e*f+a*b*d*e*f+a*b*d*E*F+a*b*C*d*E+A*b*c*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*d*F+A*b*C*d*e<->G |
| opt | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | b*c*F+b*c*d*e+b*C*E*f+A*b*d<->G |
| opt_c6c7 | 4 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | c*d*e+b*c*d*F+b*C*d*f+A*d<->G |
| opt_expert | 3 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | b*d*E+b*c*F+b*C*d*f+a*b*d*f<->G |

