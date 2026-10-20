# n100_noise0.0_frag0.0_fz1_rep02

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=2002
- true model: `d*a+D*B<->G`  (irrelevant: C, E, F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.145 | False | 0.903 | 0.254 | 1 | 0.000 | 1.000 | 0.000 | 0.541 |
| quantile | 0.180 | False | 0.000 | 0.000 | 0 | 0.034 | 0.977 | 0.033 | 0.529 |
| kde | 0.175 | False | 0.000 | 0.000 | 0 | 0.040 | 0.968 | 0.035 | 0.531 |
| expert | 0.275 | False | 0.000 | 0.000 | 0 | 0.091 | 0.903 | 0.097 | 0.564 |
| opt | 0.826 | True | 0.957 | 0.692 | 21 | 0.156 | 0.932 | 0.068 | 0.801 |
| opt_c6c7 | 0.323 | False | 0.905 | 0.491 | 4 | 0.060 | 0.918 | 0.087 | 0.537 |
| opt_expert | 0.307 | True | 0.892 | 0.508 | 5 | 0.048 | 0.903 | 0.092 | 0.535 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.034 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.875 | 0 |
| opt_c6c7 | 1.000 | 0.167 | 0 |
| opt_expert | 1.000 | 0.217 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | a*b*c*d*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 4 | 0.000 | 0.833 | 1.000 | B*C*D*F+a*C*d*E+a*b*d*e*f+a*B*E*F+a*B*d*E+a*B*D*e*f+a*B*C*F+A*B*D*E+A*B*c*D<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*e*f+a*B*c*D*e*F+a*B*C*d*e*F+a*B*C*D*E*F<->G |
| opt_expert | 1 | 0.000 | 0.750 | 1.000 | a*b*c*d*e*f+a*B*c*E*F+a*B*c*D*F+a*B*C*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*c*d*e<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 8 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | B*D+B*c*E+a*C*d*E+a*b*d*f+a*B*F<->G |
| opt_c6c7 | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*e*f+a*B*D*E+a*B*c*D*F+a*B*C*d*e<->G |
| opt_expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*e*f+a*B*D*e*F+a*B*c*E*F+a*B*C*d*e<->G |

