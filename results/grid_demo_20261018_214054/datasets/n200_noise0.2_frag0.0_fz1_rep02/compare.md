# n200_noise0.2_frag0.0_fz1_rep02

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=22002
- true model: `e*A+B*A+e*C<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.315 | False | 0.904 | 0.326 | 2 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 0.285 | False | 0.915 | 0.316 | 2 | 0.041 | 0.982 | 0.025 | 0.541 |
| kde | 0.308 | False | 0.895 | 0.290 | 1 | 0.068 | 0.937 | 0.065 | 0.577 |
| expert | 0.338 | False | 0.916 | 0.263 | 1 | 0.048 | 0.973 | 0.027 | 0.568 |
| opt | 0.692 | True | 0.889 | 0.502 | 10 | 0.158 | 0.912 | 0.088 | 0.785 |
| opt_c6c7 | 0.386 | False | 0.876 | 0.499 | 9 | 0.066 | 0.902 | 0.105 | 0.559 |
| opt_expert | 0.549 | True | 0.889 | 0.502 | 8 | 0.077 | 0.858 | 0.137 | 0.557 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.065 | 0 |
| quantile | 1.000 | 0.065 | 0 |
| kde | 1.000 | 0.037 | 0 |
| expert | 1.000 | 0.031 | 0 |
| opt | 1.000 | 0.333 | 0 |
| opt_c6c7 | 0.889 | 0.333 | 1 |
| opt_expert | 1.000 | 0.308 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*e*F+A*B*C*d*e*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | A*b*c*d*e*F+A*B*C*d*e*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*B*C*d*e*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | A*B*C*d*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | C*d*e*F+b*C*e*F+A*b*c*d*e+A*B*c*d*E*F+A*B*c*D*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.750 | 1.000 | C*D*e*F+b*c*d*e*F+A*b*c*D*e+A*B*C*e*F<->G |
| opt_expert | 2 | 1.000 | 1.000 | 0.833 | b*C*D*e*F+a*C*d*e*F+A*b*c*d*e*F+A*b*c*D*e*f+A*B*C*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e*F<->G |
| quantile | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*b*d*e+A*B*C*d*F<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*e*F<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*B*C*d*F<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*F+A*b*d*e+A*B*c*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*D*e+B*C*e+a*d*e+A*b*c*e<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*F+A*b*e<->G |

