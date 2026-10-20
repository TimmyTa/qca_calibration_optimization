# n200_noise0.2_frag0.2_fz1_rep00

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=24000
- true model: `B*a+E*f<->G`  (irrelevant: C, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.845 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.553 |
| quantile | 0.870 | False | 0.000 | 0.000 | 0 | 0.039 | 0.983 | 0.025 | 0.541 |
| kde | 0.875 | False | 0.000 | 0.000 | 0 | 0.044 | 0.968 | 0.033 | 0.543 |
| expert | 0.500 | False | 0.000 | 0.000 | 0 | 0.044 | 0.974 | 0.026 | 0.572 |
| opt | 0.544 | True | 0.914 | 0.520 | 9 | 0.139 | 0.942 | 0.055 | 0.759 |
| opt_c6c7 | 0.357 | False | 0.892 | 0.366 | 6 | 0.065 | 0.954 | 0.048 | 0.597 |
| opt_expert | 0.358 | False | 0.930 | 0.427 | 5 | 0.111 | 0.867 | 0.138 | 0.598 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.375 | 0 |
| opt_c6c7 | 1.000 | 0.240 | 0 |
| opt_expert | 1.000 | 0.227 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*f+a*B*d*e*F+a*B*c*d*F+a*B*c*d*e+a*B*C*D*f+A*b*c*D*E*f+A*B*c*d*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*f+a*B*c*d*e+a*B*c*D*E*f+a*B*C*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*f+a*B*c*d*e+a*B*C*D*e*F+A*b*c*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*f+c*E*f+a*b*E*f+a*B*d*F+a*B*c<->G |
| opt_c6c7 | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*E*f+a*C*e+a*C*d+a*B*d<->G |
| opt_expert | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E*f+C*D*e*F+a*B*c+A*D*E*f<->G |

