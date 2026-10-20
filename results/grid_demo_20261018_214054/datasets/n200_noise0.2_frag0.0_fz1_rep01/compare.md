# n200_noise0.2_frag0.0_fz1_rep01

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=22001
- true model: `a*d+a*e+b*E*A<->G`  (irrelevant: C, F)
- OUT rule (same for every mode): n >= 4, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.350 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.552 |
| quantile | 0.269 | False | 0.940 | 0.250 | 1 | 0.034 | 0.977 | 0.016 | 0.528 |
| kde | 0.320 | False | 0.000 | 0.000 | 0 | 0.078 | 0.903 | 0.094 | 0.561 |
| expert | 0.430 | False | 0.000 | 0.000 | 0 | 0.100 | 0.902 | 0.098 | 0.589 |
| opt | 0.500 | True | 0.899 | 0.500 | 7 | 0.108 | 0.916 | 0.081 | 0.678 |
| opt_c6c7 | 0.338 | False | 0.876 | 0.398 | 7 | 0.052 | 0.912 | 0.081 | 0.533 |
| opt_expert | 0.474 | False | 0.912 | 0.427 | 5 | 0.076 | 0.884 | 0.124 | 0.559 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile | 1.000 | 0.033 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.233 | 0 |
| opt_c6c7 | 1.000 | 0.226 | 0 |
| opt_expert | 1.000 | 0.185 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 1 | 1.000 | 1.000 | 0.333 | a*b*c*D*e*F<->G |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 0.667 | a*b*d*E*f+a*b*c*e*F+a*b*C*D*e*f+a*B*C*e*F<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 0.667 | a*b*c*e*F+a*b*C*d*e*f+a*B*D*e*F+a*B*c*d*e*f+a*B*C*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | a*b*c*e*F+a*b*c*d*E*f+a*b*C*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.750 | a*c*D*F<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | a*e+a*d*f<->G |
| opt_c6c7 | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*D+a*C*e+a*b*F+a*B*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*d*f+a*b*e<->G |

