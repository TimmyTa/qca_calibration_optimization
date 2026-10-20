# n400_noise0.0_frag0.0_fz1_rep00

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=26000
- true model: `d*C*b+B*A<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.915 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.548 |
| quantile | 0.920 | False | 0.000 | 0.000 | 0 | 0.032 | 0.982 | 0.021 | 0.542 |
| kde | 0.925 | False | 0.000 | 0.000 | 0 | 0.019 | 0.990 | 0.010 | 0.547 |
| expert | 0.715 | False | 0.000 | 0.000 | 0 | 0.074 | 0.912 | 0.087 | 0.542 |
| opt | 0.845 | True | 0.923 | 0.549 | 14 | 0.151 | 0.931 | 0.068 | 0.789 |
| opt_c6c7 | 0.461 | False | 0.937 | 0.364 | 3 | 0.077 | 0.886 | 0.122 | 0.553 |
| opt_expert | 0.432 | False | 0.923 | 0.399 | 4 | 0.076 | 0.870 | 0.137 | 0.545 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.583 | 0 |
| opt_c6c7 | 1.000 | 0.143 | 0 |
| opt_expert | 1.000 | 0.190 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e+A*B*e*F+A*B*d*f+A*B*C*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | A*B*d*E*f+A*B*C*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | A*B*d*e*F+A*B*c*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*C*d+A*B<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*B*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | A*B*d<->G |

