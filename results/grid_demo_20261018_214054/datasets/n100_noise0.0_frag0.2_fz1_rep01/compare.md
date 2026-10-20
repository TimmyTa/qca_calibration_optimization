# n100_noise0.0_frag0.2_fz1_rep01

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=4001
- true model: `d*f*e+B*e*f<->G`  (irrelevant: A, C)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.975 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.526 |
| quantile | 0.895 | False | 0.000 | 0.000 | 0 | 0.044 | 0.962 | 0.045 | 0.543 |
| kde | 0.905 | False | 0.000 | 0.000 | 0 | 0.053 | 0.950 | 0.057 | 0.544 |
| expert | 0.995 | False | 0.000 | 0.000 | 0 | 0.065 | 0.922 | 0.078 | 0.538 |
| opt | 0.671 | True | 0.950 | 0.511 | 8 | 0.125 | 0.900 | 0.102 | 0.721 |
| opt_c6c7 | 0.425 | False | 0.942 | 0.444 | 6 | 0.091 | 0.852 | 0.137 | 0.575 |
| opt_expert | 0.387 | False | 0.930 | 0.390 | 3 | 0.077 | 0.888 | 0.105 | 0.574 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 1.000 | 0 |
| opt_c6c7 | 1.000 | 0.750 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*D*e*f+a*B*c*e*f+A*d*e*f<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | a*B*D*e*f+A*C*d*e*f+A*B*d*e*f+A*B*C*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*B*C*D*e*f+A*B*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*e*f+B*e*f<->G |
| opt_c6c7 | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*e*f+B*D*e*f+A*B*e*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*D*e*f+A*d*e*f<->G |

