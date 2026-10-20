# n200_noise0.1_frag0.0_fz1_rep02

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=18002
- true model: `C*F+a*e*c<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.265 | False | 0.920 | 0.383 | 4 | 0.000 | 1.000 | 0.000 | 0.558 |
| quantile | 0.287 | False | 0.909 | 0.410 | 4 | 0.033 | 0.973 | 0.026 | 0.535 |
| kde | 0.285 | False | 0.000 | 0.000 | 0 | 0.041 | 0.966 | 0.034 | 0.548 |
| expert | 0.460 | False | 0.924 | 0.452 | 8 | 0.097 | 0.865 | 0.135 | 0.547 |
| opt | 0.773 | True | 0.911 | 0.515 | 14 | 0.137 | 0.922 | 0.071 | 0.782 |
| opt_c6c7 | 0.529 | True | 0.906 | 0.563 | 10 | 0.084 | 0.859 | 0.139 | 0.533 |
| opt_expert | 0.519 | True | 0.908 | 0.531 | 11 | 0.079 | 0.871 | 0.124 | 0.541 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.167 | 0 |
| quantile | 1.000 | 0.167 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.471 | 0 |
| opt | 1.000 | 0.667 | 0 |
| opt_c6c7 | 1.000 | 0.625 | 0 |
| opt_expert | 1.000 | 0.647 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | a*C*d*E*F+a*C*D*e*F<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | a*C*D*e*F+a*b*C*d*E*F+A*b*C*d*e*F<->G |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*c*D*e*F+a*b*c*e*F+a*b*C*E*F+A*C*d*E*F+A*b*C*D*e*F<->G |
| opt | 2 | 0.500 | 0.929 | 1.000 | C*D*E*F+a*D*e*F+a*c*D*e+a*b*c*e*F+a*b*C*E*F+a*B*c*e*f+A*b*C*d*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*C*E*F+B*C*D*F+a*C*D*E*F+a*B*c*D*e+A*b*C*d*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | C*D*E*F+B*C*D*F+a*c*D*e*F+a*B*c*D*e+A*C*D*F+A*b*C*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*C*d*E*F+a*C*D*e*F<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*e*F+a*C*D*e*F+a*b*C*d*F<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | C*F+a*e*F<->G |
| opt | 4 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | C*E*F+a*c*e+a*C*D*F+A*C*d*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | C*F+a*D*e<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | C*F+a*D*e<->G |

