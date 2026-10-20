# n400_noise0.2_frag0.2_fz1_rep01

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=36001
- true model: `b*A+d*b*F+a*D*f<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.730 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.556 |
| quantile | 0.850 | False | 0.000 | 0.000 | 0 | 0.041 | 0.968 | 0.030 | 0.530 |
| kde | 0.870 | False | 0.000 | 0.000 | 0 | 0.022 | 1.000 | 0.007 | 0.538 |
| expert | 0.790 | False | 0.000 | 0.000 | 0 | 0.056 | 0.938 | 0.062 | 0.548 |
| opt | 0.501 | True | 0.871 | 0.506 | 11 | 0.112 | 0.967 | 0.030 | 0.743 |
| opt_c6c7 | 0.350 | False | 0.903 | 0.246 | 2 | 0.085 | 0.880 | 0.111 | 0.562 |
| opt_expert | 0.379 | False | 0.904 | 0.267 | 2 | 0.067 | 0.905 | 0.083 | 0.544 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.393 | 0 |
| opt_c6c7 | 1.000 | 0.074 | 0 |
| opt_expert | 1.000 | 0.080 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*c*D*f+a*b*D*e*f+A*b*d*e*F+A*b*c*e*f+A*b*C*d*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.667 | A*b*c*d*e*F+A*b*c*D*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | A*b*c*d*e*F+A*b*c*D*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e*F+a*c*D*f+a*b*D*e*f+A*b*d*E+A*b*c*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e*F+b*c*D*f<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e*F+b*c*D*f<->G |

