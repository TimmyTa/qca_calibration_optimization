# n400_noise0.1_frag0.2_fz1_rep01

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=32001
- true model: `a*b+b*e<->G`  (irrelevant: C, D, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.662 | True | 0.835 | 0.624 | 13 | 0.000 | 1.000 | 0.000 | 0.544 |
| quantile | 0.655 | True | 0.856 | 0.545 | 12 | 0.036 | 0.973 | 0.026 | 0.529 |
| kde | 0.588 | True | 0.854 | 0.562 | 11 | 0.045 | 0.958 | 0.041 | 0.545 |
| expert | 0.511 | True | 0.857 | 0.517 | 9 | 0.065 | 0.946 | 0.054 | 0.561 |
| opt | 0.897 | True | 0.818 | 0.536 | 16 | 0.093 | 0.933 | 0.070 | 0.671 |
| opt_c6c7 | 0.781 | True | 0.848 | 0.517 | 8 | 0.059 | 0.892 | 0.108 | 0.523 |
| opt_expert | 0.775 | True | 0.833 | 0.562 | 10 | 0.059 | 0.908 | 0.089 | 0.533 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.591 | 0 |
| quantile | 1.000 | 0.500 | 0 |
| kde | 1.000 | 0.478 | 0 |
| expert | 1.000 | 0.391 | 0 |
| opt | 1.000 | 0.696 | 0 |
| opt_c6c7 | 1.000 | 0.333 | 0 |
| opt_expert | 1.000 | 0.435 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*e*F+b*c*D*e+a*b*D*e+a*b*c*e+a*b*c*d*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*d*e*F+b*c*D*e+a*b*D*e*f+a*b*c*e+A*b*e*F+A*b*C*d*e<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | b*d*e*F+b*D*e*f+a*b*c*d*F+A*b*D*e<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e*f+a*b*c*d*F+a*b*C*D*E*F+A*b*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*e*F+b*D*e+a*b*d*F+a*b*C*F+A*b*C*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e*f+a*b*e*f+a*b*D*e+a*b*C*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e+b*C*e*F+a*b*e*F+a*b*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*e*F+b*c*e+a*b*e+a*b*c<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*e*F+b*d*e+b*c*e+a*b*e<->G |
| kde | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*e+a*b*c<->G |
| expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*e+a*b*D*F+a*b*c<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*e+a*b<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | b*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | b*e<->G |

