# n200_noise0.1_frag0.2_fz1_rep00

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=20000
- true model: `B*d+C*f*D<->G`  (irrelevant: A, E)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.330 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.550 |
| quantile | 0.345 | False | 0.000 | 0.000 | 0 | 0.038 | 0.962 | 0.042 | 0.521 |
| kde | 0.435 | False | 0.000 | 0.000 | 0 | 0.074 | 0.903 | 0.100 | 0.550 |
| expert | 0.335 | False | 0.000 | 0.000 | 0 | 0.085 | 0.892 | 0.108 | 0.556 |
| opt | 0.726 | True | 0.932 | 0.554 | 15 | 0.106 | 0.987 | 0.019 | 0.720 |
| opt_c6c7 | 0.451 | False | 0.907 | 0.348 | 3 | 0.060 | 0.881 | 0.117 | 0.528 |
| opt_expert | 0.425 | False | 0.911 | 0.357 | 3 | 0.077 | 0.870 | 0.132 | 0.541 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.750 | 0 |
| opt_c6c7 | 1.000 | 0.143 | 0 |
| opt_expert | 1.000 | 0.143 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*C*D*E*f+a*B*d*F+a*B*c*d*e+A*C*D*e*f+A*B*d*E+A*B*C*d<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | A*B*d*E*f+A*B*c*d*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | A*B*d*E*f+A*B*c*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*D*f+B*d<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*E*F+A*B*d*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*F+B*d*E*f<->G |

