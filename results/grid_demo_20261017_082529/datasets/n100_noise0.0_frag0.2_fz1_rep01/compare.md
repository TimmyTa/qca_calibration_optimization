# n100_noise0.0_frag0.2_fz1_rep01

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=4001
- true model: `d*f*e+B*e*f<->G`  (irrelevant: A, C)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.480 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.526 |
| quantile | 0.429 | False | 0.871 | 0.372 | 1 | 0.044 | 0.962 | 0.045 | 0.543 |
| kde | 0.429 | False | 0.869 | 0.376 | 1 | 0.053 | 0.950 | 0.057 | 0.544 |
| expert | 0.665 | False | 0.000 | 0.000 | 0 | 0.065 | 0.922 | 0.078 | 0.538 |
| opt | 0.825 | True | 0.923 | 0.511 | 6 | 0.131 | 0.938 | 0.058 | 0.760 |
| opt_c6c7 | 0.350 | True | 0.868 | 0.532 | 4 | 0.064 | 0.883 | 0.115 | 0.540 |
| opt_expert | 0.301 | True | 0.867 | 0.501 | 3 | 0.054 | 0.907 | 0.092 | 0.537 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile | 1.000 | 0.125 | 0 |
| kde | 1.000 | 0.111 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 1.000 | 0 |
| opt_c6c7 | 1.000 | 0.364 | 0 |
| opt_expert | 1.000 | 0.333 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 1 | 1.000 | 1.000 | 0.500 | a*B*c*D*e*f<->G |
| kde | 1 | 1.000 | 1.000 | 0.500 | a*B*c*D*e*f<->G |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*e*f+a*B*D*e*f+a*B*c*e*f+A*b*c*d*e*f+A*B*C*d*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*B*c*D*e*f+A*c*d*e*f+A*B*d*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*B*c*D*e*f+A*B*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*D*e*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*D*e*f<->G |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*e*f+B*e*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*c*e*f+A*b*c*d*e+A*B*d*e*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*D*e*f+A*d*e*f<->G |

