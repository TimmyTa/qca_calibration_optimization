# n200_noise0.1_frag0.0_fz0_rep02

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=17002
- true model: `A*b+b*F*d<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.373 | False | 0.890 | 0.361 | 4 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.600 | False | 0.000 | 0.000 | 0 | 0.110 | 0.962 | 0.028 | 0.602 |
| kde | 0.860 | False | 0.000 | 0.000 | 0 | 0.056 | 1.000 | 0.000 | 0.690 |
| expert | 0.602 | False | 0.917 | 0.454 | 8 | 0.054 | 1.000 | 0.000 | 0.747 |
| opt | 0.791 | True | 0.915 | 0.561 | 9 | 0.090 | 0.932 | 0.077 | 0.796 |
| opt_c6c7 | 0.573 | True | 0.892 | 0.510 | 9 | 0.111 | 0.902 | 0.106 | 0.640 |
| opt_expert | 0.522 | True | 0.892 | 0.512 | 10 | 0.110 | 0.927 | 0.061 | 0.649 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.211 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.421 | 0 |
| opt | 1.000 | 0.474 | 0 |
| opt_c6c7 | 1.000 | 0.500 | 0 |
| opt_expert | 1.000 | 0.526 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*E*F+A*b*c*E*f+A*b*c*D*e*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | A*b*d*f+A*b*D*e*F+A*b*c*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*F+A*b*d*E*f+A*b*c*f+A*b*c*D<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*E*F+A*b*E*f+A*b*c*D+A*b*C*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*d*E*F+A*b*E*f+A*b*c*D+A*b*C*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*d*E*F+A*c*E*f+A*b*c*D*F<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | A*d*f+A*b*D<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*d*F+A*d*f+A*b*c*D<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | a*d*F+A*b*f+A*b*D<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*d*F+A*b<->G |

