# n100_noise0.1_frag0.2_fz1_rep01

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=8001
- true model: `C*b*A+e*F*B<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.326 | False | 0.921 | 0.396 | 2 | 0.000 | 1.000 | 0.000 | 0.556 |
| quantile | 0.398 | False | 0.906 | 0.406 | 3 | 0.056 | 0.950 | 0.047 | 0.554 |
| kde | 0.398 | False | 0.906 | 0.406 | 3 | 0.056 | 0.950 | 0.047 | 0.554 |
| expert | 0.760 | False | 0.000 | 0.000 | 0 | 0.084 | 0.867 | 0.133 | 0.487 |
| opt | 0.741 | True | 0.956 | 0.512 | 10 | 0.130 | 0.938 | 0.060 | 0.788 |
| opt_c6c7 | 0.380 | False | 0.904 | 0.498 | 5 | 0.083 | 0.872 | 0.123 | 0.554 |
| opt_expert | 0.366 | True | 0.897 | 0.500 | 5 | 0.071 | 0.895 | 0.098 | 0.547 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.167 | 0 |
| quantile | 1.000 | 0.200 | 0 |
| kde | 1.000 | 0.200 | 0 |
| expert |  | 0.000 | 0 |
| opt | 0.900 | 0.818 | 1 |
| opt_c6c7 | 1.000 | 0.385 | 0 |
| opt_expert | 1.000 | 0.385 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | A*b*C*d*e*f+A*b*C*D*e*F<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | A*b*C*e*f+A*b*C*D*e<->G |
| kde | 1 | 1.000 | 1.000 | 0.500 | A*b*C*e*f+A*b*C*D*e<->G |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 0.000 | 0.800 | 1.000 | a*B*d*e*F+a*B*c*e*F+A*b*C*e+A*b*C*d+A*B*c*d*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | A*b*C*e*f+A*b*C*D*f+A*b*C*D*e+A*B*C*d*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | A*b*C*e*f+A*b*C*D*f+A*b*C*D*e+A*B*C*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*e*F+A*C*d*f<->G |
| quantile | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*e*F+A*C*e*f<->G |
| kde | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*e*F+A*C*e*f<->G |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*e*F+A*d*E*f+A*C*e+A*b*d*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*D*e+A*C*e*f+A*b*C*D*f+A*B*C*e<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*e+A*C*e*f+A*b*C*D*f+A*B*C*e<->G |

