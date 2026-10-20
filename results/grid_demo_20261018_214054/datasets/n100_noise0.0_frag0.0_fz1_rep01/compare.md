# n100_noise0.0_frag0.0_fz1_rep01

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=2001
- true model: `E*c*A+a*f*E+e*C*F<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.685 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.800 | False | 0.000 | 0.000 | 0 | 0.039 | 0.970 | 0.030 | 0.537 |
| kde | 0.800 | False | 0.000 | 0.000 | 0 | 0.036 | 0.975 | 0.028 | 0.538 |
| expert | 0.565 | False | 0.000 | 0.000 | 0 | 0.075 | 0.915 | 0.085 | 0.560 |
| opt | 0.855 | True | 0.948 | 0.553 | 12 | 0.148 | 0.922 | 0.073 | 0.779 |
| opt_c6c7 | 0.460 | False | 0.928 | 0.312 | 3 | 0.097 | 0.843 | 0.160 | 0.542 |
| opt_expert | 0.411 | False | 0.909 | 0.332 | 4 | 0.073 | 0.907 | 0.100 | 0.559 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.750 | 0 |
| opt_c6c7 | 1.000 | 0.200 | 0 |
| opt_expert | 1.000 | 0.200 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 2 | 0.000 | 0.667 | 0.667 | c*d*E*f+B*c*E*f+a*C*d*e*F+a*b*C*e*F+a*B*d*E*f+A*B*C*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.333 | A*c*d*E*f+A*b*c*d*E<->G |
| opt_expert | 1 | 0.000 | 0.667 | 0.333 | b*c*d*E*f+A*c*d*E*f+A*b*c*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 2 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | c*d*E*f+C*e*F+B*c*E*f+a*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*d*E<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*E*f+A*c*d*E*f+A*b*c*d*E<->G |

