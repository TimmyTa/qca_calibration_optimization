# n400_noise0.2_frag0.2_fz1_rep01

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=36001
- true model: `b*A+d*b*F+a*D*f<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.579 | True | 0.804 | 0.652 | 15 | 0.000 | 1.000 | 0.000 | 0.556 |
| quantile | 0.511 | True | 0.810 | 0.559 | 10 | 0.041 | 0.968 | 0.030 | 0.530 |
| kde | 0.545 | True | 0.807 | 0.609 | 12 | 0.022 | 1.000 | 0.007 | 0.538 |
| expert | 0.553 | False | 0.827 | 0.520 | 8 | 0.056 | 0.938 | 0.062 | 0.548 |
| opt | 0.707 | True | 0.832 | 0.518 | 10 | 0.116 | 0.935 | 0.071 | 0.717 |
| opt_c6c7 | 0.608 | True | 0.803 | 0.595 | 11 | 0.052 | 0.920 | 0.074 | 0.521 |
| opt_expert | 0.621 | True | 0.800 | 0.598 | 12 | 0.061 | 0.906 | 0.094 | 0.528 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.933 | 0.538 | 1 |
| quantile | 1.000 | 0.357 | 0 |
| kde | 1.000 | 0.462 | 0 |
| expert | 1.000 | 0.348 | 0 |
| opt | 1.000 | 0.370 | 0 |
| opt_c6c7 | 0.909 | 0.357 | 1 |
| opt_expert | 0.833 | 0.385 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 0.667 | c*D*e*f+b*D*e*f+a*B*c*D*f+A*b*c*e+A*b*C*f+A*b*C*d<->G |
| quantile | 1 | 0.000 | 0.800 | 0.667 | b*C*D*e*f+a*B*c*D*e*f+A*b*d*e+A*b*c*e+A*b*C*D*f<->G |
| kde | 1 | 0.000 | 0.800 | 0.667 | b*D*e*f+a*B*c*D*f+A*b*d*e+A*b*c*e+A*b*C*d*f<->G |
| expert | 1 | 0.000 | 0.667 | 0.333 | b*C*D*e*f+A*b*e*f+A*b*C*d<->G |
| opt | 1 | 1.000 | 1.000 | 0.667 | a*D*e*f+a*B*c*D*f+A*b*e*f+A*b*c*d*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.600 | 0.667 | b*c*d*e*F+b*C*D*e*f+B*c*D*e*f+A*b*d*e+A*b*c*e<->G |
| opt_expert | 1 | 0.000 | 0.667 | 1.000 | b*c*d*e*F+b*C*D*e*f+a*B*D*e*f+A*b*c*D*e+A*b*C*d*e+A*B*c*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | c*D*f+b*D*f+A*b<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*f+b*D*f+A*b*e<->G |
| kde | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*D*f+a*b*D*f+A*b*e+A*b*d*f<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*e*f+A*b*d<->G |
| opt | 4 | 0.000 | 0.417 | 0.417 | 0.000 | 0.000 | b*D*f+a*D*f+A*b*d<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*f+b*d*e*F+b*C*f+A*b*c<->G |
| opt_expert | 3 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | b*d*e*F+b*c+a*D*f+A*c*f+A*b*f<->G |

