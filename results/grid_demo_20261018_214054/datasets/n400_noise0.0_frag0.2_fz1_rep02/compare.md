# n400_noise0.0_frag0.2_fz1_rep02

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=28002
- true model: `C*b+A*f*d<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.935 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.550 |
| quantile | 0.980 | False | 0.000 | 0.000 | 0 | 0.030 | 0.977 | 0.015 | 0.531 |
| kde | 0.980 | False | 0.000 | 0.000 | 0 | 0.042 | 0.958 | 0.035 | 0.552 |
| expert | 0.990 | False | 0.000 | 0.000 | 0 | 0.086 | 0.895 | 0.105 | 0.554 |
| opt | 0.871 | True | 0.955 | 0.520 | 14 | 0.134 | 0.972 | 0.029 | 0.791 |
| opt_c6c7 | 0.505 | False | 0.911 | 0.445 | 8 | 0.059 | 0.926 | 0.072 | 0.575 |
| opt_expert | 0.436 | False | 0.913 | 0.404 | 6 | 0.059 | 0.928 | 0.076 | 0.559 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.700 | 0 |
| opt_c6c7 | 1.000 | 0.381 | 0 |
| opt_expert | 1.000 | 0.286 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*e*F+b*C*D*e+A*b*c*d*f+A*b*C*E+A*B*d*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+A*b*C*F+A*b*C*d*E+A*b*C*D*e+A*B*C*d*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | a*b*C*d*e+A*b*C*E*F+A*b*C*d*E+A*b*C*D*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*C+A*d*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d+A*C*e*f+A*b*C<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*F+b*C*e+b*C*d<->G |

