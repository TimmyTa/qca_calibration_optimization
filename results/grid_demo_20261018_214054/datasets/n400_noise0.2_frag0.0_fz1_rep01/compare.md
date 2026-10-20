# n400_noise0.2_frag0.0_fz1_rep01

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=34001
- true model: `d*e*f+F*b+e*f*C<->G`  (irrelevant: A)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.410 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.345 | False | 0.000 | 0.000 | 0 | 0.027 | 0.990 | 0.005 | 0.542 |
| kde | 0.340 | False | 0.000 | 0.000 | 0 | 0.018 | 0.995 | 0.000 | 0.542 |
| expert | 0.325 | False | 0.000 | 0.000 | 0 | 0.071 | 0.908 | 0.092 | 0.537 |
| opt | 0.716 | True | 0.868 | 0.502 | 16 | 0.116 | 0.958 | 0.037 | 0.744 |
| opt_c6c7 | 0.463 | False | 0.894 | 0.386 | 5 | 0.075 | 0.863 | 0.124 | 0.539 |
| opt_expert | 0.500 | False | 0.884 | 0.414 | 7 | 0.059 | 0.896 | 0.098 | 0.542 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.571 | 0 |
| opt_c6c7 | 1.000 | 0.200 | 0 |
| opt_expert | 1.000 | 0.259 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 2 | 0.500 | 0.917 | 1.000 | b*C*e*f+b*C*E*F+b*C*D*e+A*b*e*F+A*b*D*F+A*B*d*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.333 | b*C*D*e*F+A*b*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.333 | b*D*e*F+b*C*e*F+A*b*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*F+b*C*e+A*d*e*f+A*b*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | b*e*F<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | b*e*F<->G |

