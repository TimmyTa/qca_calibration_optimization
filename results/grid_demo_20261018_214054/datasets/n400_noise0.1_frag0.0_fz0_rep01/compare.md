# n400_noise0.1_frag0.0_fz0_rep01

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=29001
- true model: `b*f*E+F*C*b<->G`  (irrelevant: A, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.311 | False | 0.891 | 0.257 | 2 | 0.000 | 1.000 | 0.000 | 0.798 |
| quantile | 1.000 | False | 0.000 | 0.000 | 0 | 0.105 | 0.981 | 0.018 | 0.597 |
| kde | 0.995 | False | 0.000 | 0.000 | 0 | 0.057 | 1.000 | 0.000 | 0.683 |
| expert | 0.715 | False | 0.000 | 0.000 | 0 | 0.053 | 1.000 | 0.000 | 0.755 |
| opt | 0.752 | True | 0.900 | 0.521 | 10 | 0.095 | 0.939 | 0.065 | 0.826 |
| opt_c6c7 | 0.539 | False | 0.877 | 0.470 | 11 | 0.127 | 0.926 | 0.090 | 0.658 |
| opt_expert | 0.551 | True | 0.873 | 0.503 | 11 | 0.096 | 0.958 | 0.046 | 0.675 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.125 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.625 | 0 |
| opt_c6c7 | 1.000 | 0.688 | 0 |
| opt_expert | 1.000 | 0.688 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | a*b*C*D*E*f+A*b*C*d*E*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 0.000 | 0.500 | 1.000 | b*C*d*F+b*C*d*E+A*b*E*f+A*b*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*d*E*f+b*C*E*F+b*C*d*F+A*b*c*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*d*E*f+b*C*E*F+b*C*d*F+A*b*c*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*E*f+a*b*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*E+b*C*d*F+A*b*E*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*E*f+b*D*E+b*C*d*F<->G |
| opt_expert | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*E*f+b*D*E+b*C*d*F<->G |

