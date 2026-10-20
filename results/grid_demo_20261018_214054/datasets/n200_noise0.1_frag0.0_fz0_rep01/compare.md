# n200_noise0.1_frag0.0_fz0_rep01

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=17001
- true model: `A*f+B*e+B*D*f<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.557 | True | 0.925 | 0.587 | 13 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.431 | False | 0.864 | 0.455 | 10 | 0.112 | 0.973 | 0.044 | 0.586 |
| kde | 0.450 | False | 0.886 | 0.472 | 8 | 0.050 | 1.000 | 0.000 | 0.703 |
| expert | 0.572 | True | 0.919 | 0.557 | 13 | 0.050 | 0.995 | 0.005 | 0.773 |
| opt | 0.708 | True | 0.886 | 0.505 | 17 | 0.111 | 0.912 | 0.100 | 0.704 |
| opt_c6c7 | 0.665 | True | 0.872 | 0.511 | 13 | 0.113 | 0.913 | 0.078 | 0.662 |
| opt_expert | 0.663 | True | 0.892 | 0.522 | 13 | 0.100 | 0.932 | 0.065 | 0.651 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.433 | 0 |
| quantile | 1.000 | 0.333 | 0 |
| kde | 1.000 | 0.267 | 0 |
| expert | 1.000 | 0.433 | 0 |
| opt | 1.000 | 0.630 | 0 |
| opt_c6c7 | 1.000 | 0.433 | 0 |
| opt_expert | 1.000 | 0.448 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*c*D*f+B*C*d*e*F+a*B*c*D*e+A*c*D*f+A*B*c*e*f+A*B*C*e*F+A*B*C*E*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | B*C*d*e*F+a*B*c*D*f+a*B*c*D*e+A*c*D*e*f+A*B*c*e*f+A*B*C*e*F+A*B*C*D*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*B*c*D*e+a*B*C*d*e*F+A*B*D*E*f+A*B*c*e*f+A*B*C*D*e*F<->G |
| expert | 1 | 1.000 | 1.000 | 0.667 | B*C*d*e*F+a*B*c*D*e+A*c*D*f+A*b*C*d*e*f+A*B*c*e*f+A*B*C*e*F+A*B*C*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e+a*B*d*e*F+a*B*D*e*f+a*B*c*e+a*B*c*D*f+A*d*e*f+A*c*e*f+A*B*C*E*f+A*B*C*D*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*D*e*f+B*C*e*F+a*B*C*D*f+A*C*e*f+A*b*c*D*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*D*e*F+B*c*D*e+a*B*D*e+a*B*c*D*f+a*B*C*e*F+A*b*c*D*f+A*B*c*e*F+A*B*C*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*e+a*B*c*D+A*c*D*f+A*B*f<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*e+a*B*c*D+A*c*e*f+A*B*D*f<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*e*f+B*D*e+a*B*C*F+A*B*D*f<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*e+B*C*e+A*e*f+A*c*D*f+A*B*f<->G |
| opt | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 0.000 | B*e+B*D*f+A*e*f+A*B<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | B*D*f+B*C*e*F+A*f<->G |
| opt_expert | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | B*e+B*D*f+A*c*f<->G |

