# n400_noise0.1_frag0.2_fz1_rep02

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=32002
- true model: `a*e*F+d*C+e*c<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.385 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.537 |
| quantile | 0.640 | False | 0.000 | 0.000 | 0 | 0.048 | 0.964 | 0.036 | 0.531 |
| kde | 0.640 | False | 0.000 | 0.000 | 0 | 0.045 | 0.971 | 0.033 | 0.537 |
| expert | 0.362 | False | 0.913 | 0.338 | 2 | 0.138 | 0.850 | 0.150 | 0.621 |
| opt | 0.819 | True | 0.919 | 0.535 | 15 | 0.146 | 0.987 | 0.014 | 0.822 |
| opt_c6c7 | 0.483 | False | 0.910 | 0.424 | 6 | 0.066 | 0.873 | 0.121 | 0.550 |
| opt_expert | 0.470 | False | 0.906 | 0.424 | 5 | 0.085 | 0.860 | 0.144 | 0.560 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.071 | 0 |
| opt | 1.000 | 0.517 | 0 |
| opt_c6c7 | 1.000 | 0.207 | 0 |
| opt_expert | 1.000 | 0.185 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.333 | a*b*c*d*e*f+A*b*c*d*e*F<->G |
| opt | 4 | 0.250 | 0.875 | 1.000 | a*c*d*e*f+a*b*d*e*F+a*B*C*D*e*F+A*c*e*F+A*b*d*e*f+A*b*c*e+A*B*C*d*f+A*B*C*d*e<->G |
| opt_c6c7 | 2 | 0.500 | 0.875 | 0.667 | a*b*c*d*e*f+A*C*d*e*f+A*b*d*e*F+A*b*c*e*F<->G |
| opt_expert | 1 | 0.000 | 0.750 | 0.667 | b*c*d*e*f+A*b*d*e*f+A*b*c*d*e+A*B*C*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | c*e*F+a*c*e<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e+B*C*d+a*B*e*F+A*c*e<->G |
| opt_c6c7 | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | c*e*F+c*d*f+A*d*e<->G |
| opt_expert | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | c*e+B*d*e*F+A*b*d*e*f<->G |

