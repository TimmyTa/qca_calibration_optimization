# n400_noise0.2_frag0.0_fz0_rep01

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=33001
- true model: `B*A+A*c*d<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.209 | False | 0.878 | 0.160 | 1 | 0.000 | 1.000 | 0.000 | 0.798 |
| quantile | 0.850 | False | 0.000 | 0.000 | 0 | 0.112 | 0.971 | 0.039 | 0.585 |
| kde | 0.980 | False | 0.000 | 0.000 | 0 | 0.062 | 1.000 | 0.000 | 0.674 |
| expert | 0.519 | False | 0.878 | 0.349 | 7 | 0.047 | 1.000 | 0.000 | 0.772 |
| opt | 0.586 | False | 0.841 | 0.473 | 10 | 0.110 | 0.957 | 0.060 | 0.844 |
| opt_c6c7 | 0.530 | False | 0.861 | 0.402 | 9 | 0.120 | 0.911 | 0.091 | 0.637 |
| opt_expert | 0.501 | False | 0.848 | 0.376 | 9 | 0.105 | 0.946 | 0.048 | 0.658 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.050 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.350 | 0 |
| opt | 1.000 | 0.500 | 0 |
| opt_c6c7 | 1.000 | 0.474 | 0 |
| opt_expert | 1.000 | 0.450 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | A*B*C*d*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | A*c*d*e*F+A*B*d*e+A*B*c*e*F+A*B*c*d*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | A*c*d*e*F+A*B*e*F+A*B*c*e+A*B*c*d*F+A*B*C*d*f<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | A*b*c*d*e*F+A*B*c*E*F+A*B*c*D*F+A*B*C*e+A*B*C*D*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | A*B*e*F+A*B*d*e+A*B*c*e+A*B*c*D*F+A*B*C*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*e*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*d*e*F+A*B*d*e+A*B*c*F<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*d*F+A*B*f+A*B*e<->G |
| opt_c6c7 | 3 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | B*f+B*c*D+A*c*d+A*B*e<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*B*e+A*B*D*F+A*B*C*D<->G |

