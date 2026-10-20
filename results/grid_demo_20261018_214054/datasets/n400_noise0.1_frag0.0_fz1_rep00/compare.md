# n400_noise0.1_frag0.0_fz1_rep00

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=30000
- true model: `E*C*d+A*f<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 1.000 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 0.995 | False | 0.000 | 0.000 | 0 | 0.027 | 0.982 | 0.012 | 0.529 |
| kde | 0.995 | False | 0.000 | 0.000 | 0 | 0.040 | 0.971 | 0.031 | 0.545 |
| expert | 1.000 | False | 0.000 | 0.000 | 0 | 0.029 | 0.982 | 0.018 | 0.546 |
| opt | 0.718 | True | 0.875 | 0.501 | 12 | 0.129 | 0.948 | 0.050 | 0.767 |
| opt_c6c7 | 0.521 | False | 0.902 | 0.395 | 7 | 0.071 | 0.897 | 0.102 | 0.563 |
| opt_expert | 0.428 | False | 0.894 | 0.389 | 6 | 0.086 | 0.869 | 0.127 | 0.565 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.545 | 0 |
| opt_c6c7 | 1.000 | 0.333 | 0 |
| opt_expert | 1.000 | 0.316 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*f+A*C*d*e*f+A*b*D*E*f+A*B*e*f+A*B*c*f+A*B*C*d*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | A*c*D*E*f+A*C*d*E*f+A*B*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | A*D*E*f+A*B*c*D*f+A*B*C*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 2 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | C*d*E+A*d*f+A*c*E*f+A*b*E+A*B*e*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*d*E*f+A*c*E*f+A*B*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | A*f<->G |

