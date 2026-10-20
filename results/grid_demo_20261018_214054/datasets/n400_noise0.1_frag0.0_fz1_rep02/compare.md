# n400_noise0.1_frag0.0_fz1_rep02

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=30002
- true model: `d*b*a+c*f+A*C*F<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.890 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.554 |
| quantile | 0.935 | False | 0.000 | 0.000 | 0 | 0.031 | 0.986 | 0.022 | 0.539 |
| kde | 0.900 | False | 0.000 | 0.000 | 0 | 0.031 | 0.970 | 0.030 | 0.552 |
| expert | 0.590 | False | 0.000 | 0.000 | 0 | 0.104 | 0.880 | 0.120 | 0.560 |
| opt | 0.731 | True | 0.893 | 0.518 | 15 | 0.150 | 0.912 | 0.088 | 0.792 |
| opt_c6c7 | 0.404 | False | 0.915 | 0.331 | 5 | 0.075 | 0.913 | 0.089 | 0.570 |
| opt_expert | 0.417 | False | 0.920 | 0.319 | 6 | 0.055 | 0.924 | 0.082 | 0.574 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.517 | 0 |
| opt_c6c7 | 1.000 | 0.167 | 0 |
| opt_expert | 1.000 | 0.200 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*e*f+B*c*D*f+a*c*e*f+a*b*C*d*e*F+A*c*D*f+A*C*D*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.667 | B*c*D*e*f+a*b*c*d*e*f+A*c*D*e*f+A*B*c*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.333 | B*c*e*f+a*c*d*e*f+a*B*c*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | c*D*f+B*c*e*f+a*b*d+A*C*F<->G |
| opt_c6c7 | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*e*f+a*b*d*f+A*c*D*e*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*e*f+a*B*c*d*f<->G |

