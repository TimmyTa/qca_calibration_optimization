# n200_noise0.1_frag0.0_fz1_rep01

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=18001
- true model: `e*F*c+B*F*C<->G`  (irrelevant: A, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.407 | True | 0.851 | 0.517 | 6 | 0.000 | 1.000 | 0.000 | 0.559 |
| quantile | 0.512 | True | 0.880 | 0.559 | 9 | 0.055 | 0.974 | 0.030 | 0.548 |
| kde | 0.521 | True | 0.883 | 0.574 | 10 | 0.051 | 0.978 | 0.023 | 0.549 |
| expert | 0.455 | False | 0.835 | 0.491 | 5 | 0.086 | 0.863 | 0.137 | 0.537 |
| opt | 0.814 | True | 0.866 | 0.515 | 11 | 0.090 | 0.943 | 0.061 | 0.645 |
| opt_c6c7 | 0.676 | True | 0.862 | 0.539 | 7 | 0.060 | 0.913 | 0.087 | 0.526 |
| opt_expert | 0.708 | True | 0.849 | 0.585 | 9 | 0.063 | 0.926 | 0.087 | 0.527 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.375 | 0 |
| quantile | 1.000 | 0.562 | 0 |
| kde | 1.000 | 0.625 | 0 |
| expert | 1.000 | 0.556 | 0 |
| opt | 1.000 | 0.733 | 0 |
| opt_c6c7 | 1.000 | 0.500 | 0 |
| opt_expert | 1.000 | 0.600 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | B*c*D*e*F+a*c*d*e*F+A*c*D*e*F+A*B*C*D*E*F<->G |
| quantile | 2 | 0.000 | 0.700 | 1.000 | B*c*e*F+B*C*D*E*F+a*c*d*e*F+a*B*C*D*F+A*B*d*e*F<->G |
| kde | 2 | 0.000 | 0.750 | 1.000 | B*c*e*F+B*C*D*E*F+a*c*d*e*F+a*B*C*E*F+a*B*C*D*F+A*B*d*e*F<->G |
| expert | 1 | 0.000 | 0.667 | 0.500 | b*c*d*e*F+A*b*c*e*F+A*B*d*e*F<->G |
| opt | 1 | 0.000 | 0.833 | 1.000 | c*d*e*F+B*d*e*F+a*B*C*e*F+a*B*C*d*F+A*c*e*F+A*B*C*D*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.750 | 1.000 | B*C*D*e*F+A*c*D*e*F+A*B*e*F+A*B*C*D*F<->G |
| opt_expert | 1 | 0.000 | 0.800 | 1.000 | c*d*e*F+a*B*C*D*e*F+A*c*e*F+A*B*d*e*F+A*B*C*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*F+a*c*e*F+A*B*E*F<->G |
| quantile | 66 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*e*F+a*B*C*D*F+A*C*E*F+A*B*d*F+A*B*c*F<->G |
| kde | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | B*e*F+B*C*F+a*b*c*e<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | c*e*F+B<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | c*e*F+B*F<->G |
| opt_c6c7 | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*e*F+B*e*F+A*B*F<->G |
| opt_expert | 4 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*e*F+B*e*F+B*D*E<->G |

