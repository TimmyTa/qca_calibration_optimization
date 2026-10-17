# n100_noise0.2_frag0.0_fz1_rep01

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=10001
- true model: `e*d+A*c*E<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.295 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.557 |
| quantile | 0.420 | False | 0.000 | 0.000 | 0 | 0.058 | 0.960 | 0.043 | 0.512 |
| kde | 0.390 | False | 0.000 | 0.000 | 0 | 0.078 | 0.925 | 0.078 | 0.528 |
| expert | 0.117 | False | 0.848 | 0.240 | 1 | 0.069 | 0.912 | 0.088 | 0.545 |
| opt | 0.512 | True | 0.856 | 0.524 | 9 | 0.166 | 0.913 | 0.078 | 0.765 |
| opt_c6c7 | 0.242 | False | 0.848 | 0.417 | 3 | 0.075 | 0.882 | 0.115 | 0.539 |
| opt_expert | 0.237 | False | 0.840 | 0.437 | 3 | 0.078 | 0.862 | 0.118 | 0.512 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.056 | 0 |
| opt | 1.000 | 0.450 | 0 |
| opt_c6c7 | 0.667 | 0.118 | 1 |
| opt_expert | 0.667 | 0.118 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | a*b*C*d*e*f<->G |
| opt | 2 | 0.500 | 0.900 | 1.000 | b*C*d*e*F+A*c*d*E*F+A*c*D*E*f+A*b*d*e*F+A*B*C*d*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 0.500 | a*b*c*d*E*F+a*b*C*d*e*F+A*B*C*d*e*f<->G |
| opt_expert | 1 | 0.000 | 0.667 | 0.500 | a*b*c*d*E*F+a*b*C*d*e*F+A*B*C*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*C*d*e<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*f+C*d*e+A*c*d*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e+b*c*d*F<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e+a*b*c*d*F<->G |

