# n200_noise0.0_frag0.2_fz0_rep00

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=15000
- true model: `F*E+e*b*a+E*c*B<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.605 | True | 0.936 | 0.765 | 16 | 0.000 | 1.000 | 0.000 | 0.794 |
| quantile | 0.390 | False | 0.000 | 0.000 | 0 | 0.102 | 0.963 | 0.028 | 0.606 |
| kde | 0.299 | False | 0.876 | 0.291 | 2 | 0.046 | 1.000 | 0.000 | 0.702 |
| expert | 0.664 | True | 0.955 | 0.697 | 16 | 0.037 | 1.000 | 0.000 | 0.764 |
| opt | 0.834 | True | 0.959 | 0.511 | 12 | 0.116 | 0.956 | 0.082 | 0.773 |
| opt_c6c7 | 0.741 | True | 0.919 | 0.539 | 14 | 0.108 | 0.949 | 0.070 | 0.666 |
| opt_expert | 0.698 | True | 0.908 | 0.549 | 11 | 0.115 | 0.907 | 0.080 | 0.656 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.762 | 0 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.095 | 0 |
| expert | 1.000 | 0.762 | 0 |
| opt | 1.000 | 0.500 | 0 |
| opt_c6c7 | 1.000 | 0.583 | 0 |
| opt_expert | 1.000 | 0.478 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 0.667 | b*D*E*F+B*C*E*F+a*E*F+a*b*c*d*F+a*b*C*D*F+A*B*c*d*E<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 0.333 | a*b*C*E*F<->G |
| expert | 2 | 0.000 | 0.714 | 0.667 | C*D*E*F+b*D*E*F+B*d*E*F+a*E*F+a*b*c*d*F+a*b*c*D*e*f+a*b*C*D*F<->G |
| opt | 1 | 0.000 | 0.800 | 0.667 | b*C*D*E*F+B*c*d*E+a*d*E*F+a*c*E*F+a*b*c*d*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.833 | 0.667 | b*D*E*F+B*c*d*E+a*d*E*F+a*c*E*F+a*b*c*d*F+A*C*D*E*F<->G |
| opt_expert | 1 | 0.000 | 0.857 | 1.000 | C*D*E*F+a*C*E*F+a*b*d*E*F+a*b*c*D*e*f+a*b*C*D*F+a*B*D*E*F+A*B*c*d*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 0.000 | E*F+a*b*F+A*B*c*E<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | a*b*C*E<->G |
| expert | 3 | 0.000 | 0.333 | 0.333 | 0.000 | 0.667 | E*F+a*b*F+a*b*c*e<->G |
| opt | 2 | 0.000 | 0.667 | 0.667 | 0.000 | 0.500 | E*F+B*c*E+a*b*c*F<->G |
| opt_c6c7 | 3 | 0.000 | 0.667 | 0.667 | 0.000 | 0.667 | E*F+B*c*E+a*b*c*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | E*F+a*b*e<->G |

