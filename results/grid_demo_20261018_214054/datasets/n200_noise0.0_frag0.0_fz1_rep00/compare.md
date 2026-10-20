# n200_noise0.0_frag0.0_fz1_rep00

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=14000
- true model: `a*D*c+E*D<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.375 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.546 |
| quantile | 0.425 | False | 0.000 | 0.000 | 0 | 0.034 | 0.977 | 0.025 | 0.530 |
| kde | 0.425 | False | 0.000 | 0.000 | 0 | 0.049 | 0.956 | 0.043 | 0.538 |
| expert | 0.486 | False | 0.955 | 0.432 | 6 | 0.101 | 0.877 | 0.123 | 0.567 |
| opt | 0.815 | True | 0.919 | 0.501 | 10 | 0.134 | 0.931 | 0.057 | 0.743 |
| opt_c6c7 | 0.528 | True | 0.923 | 0.523 | 5 | 0.060 | 0.897 | 0.110 | 0.537 |
| opt_expert | 0.388 | True | 0.912 | 0.509 | 5 | 0.064 | 0.886 | 0.125 | 0.532 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.429 | 0 |
| opt | 1.000 | 0.588 | 0 |
| opt_c6c7 | 1.000 | 0.333 | 0 |
| opt_expert | 1.000 | 0.263 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | b*C*D*E+a*C*D*E*F+A*C*D*E*f<->G |
| opt | 2 | 1.000 | 1.000 | 0.500 | C*D*E*F+b*C*D*E+a*B*D*E*F+A*b*D*E*F+A*B*D*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | b*C*D*E*f+A*C*D*E*F+A*b*D*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | b*C*D*E*f+A*B*D*E*f+A*B*C*D*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*E<->G |
| opt | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*E+A*D*E*F<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*E+A*B*D*E<->G |

