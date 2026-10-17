# n100_noise0.1_frag0.2_fz1_rep01

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=8001
- true model: `C*b*A+e*F*B<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.523 | True | 0.879 | 0.606 | 9 | 0.000 | 1.000 | 0.000 | 0.556 |
| quantile | 0.505 | True | 0.876 | 0.589 | 9 | 0.056 | 0.950 | 0.047 | 0.554 |
| kde | 0.505 | True | 0.876 | 0.589 | 9 | 0.056 | 0.950 | 0.047 | 0.554 |
| expert | 0.426 | False | 0.847 | 0.523 | 4 | 0.084 | 0.867 | 0.133 | 0.487 |
| opt | 0.737 | True | 0.915 | 0.521 | 11 | 0.149 | 0.935 | 0.070 | 0.823 |
| opt_c6c7 | 0.580 | True | 0.846 | 0.526 | 8 | 0.080 | 0.855 | 0.135 | 0.533 |
| opt_expert | 0.584 | True | 0.860 | 0.537 | 8 | 0.077 | 0.855 | 0.137 | 0.530 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.750 | 0 |
| quantile | 1.000 | 0.600 | 0 |
| kde | 1.000 | 0.600 | 0 |
| expert | 1.000 | 0.444 | 0 |
| opt | 0.909 | 0.909 | 1 |
| opt_c6c7 | 1.000 | 0.889 | 0 |
| opt_expert | 1.000 | 0.889 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.800 | 1.000 | B*C*d*e*F+A*C*e*F+A*b*C*e+A*b*C*d*F+A*b*C*D*f<->G |
| quantile | 1 | 0.000 | 0.667 | 1.000 | B*C*d*e*F+A*C*e*F+A*b*C*f<->G |
| kde | 1 | 0.000 | 0.667 | 1.000 | B*C*d*e*F+A*C*e*F+A*b*C*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | A*b*C*e*f+A*b*C*D*e+A*B*C*d*e*F<->G |
| opt | 1 | 0.000 | 0.667 | 1.000 | B*c*D*e*F+a*B*c*e*F+A*C*d*e*F+A*b*C*e+A*b*C*d+A*B*c*d*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.750 | 0.500 | A*C*d*e*F+A*b*C*f+A*b*C*e+A*b*C*d<->G |
| opt_expert | 1 | 0.000 | 0.750 | 0.500 | A*C*d*e*F+A*b*C*f+A*b*C*e+A*b*C*d<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*e*F+A*C*e+A*C*d+A*b*C*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | B*C*e*F+A*C*e+A*b*C*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | B*C*e*F+A*C*e+A*b*C*f<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | C*e*F+A*b*C*e<->G |
| opt | 2 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | B*e*F+A*c*d*E*f+A*C*e+A*b*C*d<->G |
| opt_c6c7 | 4 | 0.000 | 0.500 | 0.500 | 0.000 | 0.250 | B*d*e*F+A*b*C<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | C*e*F+A*b*C<->G |

