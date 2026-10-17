# n100_noise0.2_frag0.2_fz0_rep01

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=11001
- true model: `c*B+E*A<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.456 | True | 0.866 | 0.543 | 8 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.289 | False | 0.796 | 0.254 | 2 | 0.117 | 0.942 | 0.030 | 0.581 |
| kde | 0.325 | False | 0.821 | 0.351 | 4 | 0.059 | 1.000 | 0.000 | 0.685 |
| expert | 0.500 | True | 0.806 | 0.585 | 11 | 0.058 | 1.000 | 0.000 | 0.757 |
| opt | 0.599 | True | 0.847 | 0.554 | 10 | 0.070 | 0.932 | 0.070 | 0.780 |
| opt_c6c7 | 0.454 | True | 0.808 | 0.500 | 9 | 0.100 | 0.923 | 0.092 | 0.649 |
| opt_expert | 0.466 | True | 0.805 | 0.500 | 10 | 0.090 | 0.958 | 0.037 | 0.665 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.421 | 0 |
| quantile | 1.000 | 0.100 | 0 |
| kde | 1.000 | 0.211 | 0 |
| expert | 0.909 | 0.526 | 1 |
| opt | 1.000 | 0.476 | 0 |
| opt_c6c7 | 1.000 | 0.600 | 0 |
| opt_expert | 1.000 | 0.526 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*B*c*d*e*F+A*b*C*E*f+A*B*c*d*f+A*B*c*d*E+A*B*c*D*e*F+A*B*C*D*E*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | A*B*c*d*e*f+A*B*c*d*E*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*B*c*d*e*F+A*B*c*d*e*f+A*B*c*d*E*F+A*B*c*D*e*F<->G |
| expert | 1 | 0.000 | 0.875 | 1.000 | a*B*c*E*f+a*B*c*d*e*F+A*b*c*d*e*F+A*b*C*E*f+A*B*c*d*f+A*B*c*d*E+A*B*c*D*e*F+A*B*C*D*E*F<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+B*c*d*E*f+A*C*d*E*F+A*b*C*d*E+A*B*c*e*F+A*B*c*d<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+a*B*c*E*f+A*b*C*d*E+A*B*c*d*E+A*B*C*D*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+a*B*c*E*f+A*b*C*d*E*f+A*B*c*e*F+A*B*c*d+A*B*C*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*e+B*C*D*E+A*f+A*d*E<->G |
| quantile | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*e+B*c*d*F<->G |
| kde | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*e+A*d*E*F<->G |
| expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*e+B*C*D*E+a*B*c+A*f+A*c*d<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*f+B*c*e+A*d*E<->G |
| opt_c6c7 | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*f+B*c*e+B*C*D*F+A*d*E<->G |
| opt_expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*E*f+B*c*e*F+B*C*D*E+A*E*f+A*B*c*d<->G |

