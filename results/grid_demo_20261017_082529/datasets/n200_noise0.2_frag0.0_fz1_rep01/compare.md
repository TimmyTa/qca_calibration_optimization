# n200_noise0.2_frag0.0_fz1_rep01

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=22001
- true model: `a*d+a*e+b*E*A<->G`  (irrelevant: C, F)
- OUT rule (same for every mode): n >= 4, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.474 | True | 0.835 | 0.612 | 11 | 0.000 | 1.000 | 0.000 | 0.552 |
| quantile | 0.452 | True | 0.868 | 0.514 | 7 | 0.034 | 0.977 | 0.016 | 0.528 |
| kde | 0.463 | False | 0.787 | 0.605 | 10 | 0.078 | 0.903 | 0.094 | 0.561 |
| expert | 0.492 | False | 0.849 | 0.526 | 6 | 0.100 | 0.902 | 0.098 | 0.589 |
| opt | 0.675 | True | 0.820 | 0.504 | 10 | 0.101 | 0.885 | 0.112 | 0.634 |
| opt_c6c7 | 0.581 | True | 0.821 | 0.574 | 9 | 0.064 | 0.879 | 0.121 | 0.530 |
| opt_expert | 0.590 | True | 0.825 | 0.561 | 9 | 0.050 | 0.895 | 0.104 | 0.521 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.355 | 0 |
| quantile | 1.000 | 0.233 | 0 |
| kde | 0.600 | 0.240 | 4 |
| expert | 1.000 | 0.207 | 0 |
| opt | 1.000 | 0.400 | 0 |
| opt_c6c7 | 1.000 | 0.321 | 0 |
| opt_expert | 1.000 | 0.300 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 3 | 1.000 | 1.000 | 1.000 | a*c*d*e*F+a*b*d*E*f+a*b*c*D*e+a*b*C*d*f+a*B*C*e*F+a*B*C*D*e+A*b*C*D*E*F<->G |
| quantile | 1 | 1.000 | 1.000 | 0.667 | a*c*d*e*F+a*b*d*E*f+a*b*c*e*F+a*B*C*D*e<->G |
| kde | 1 | 0.000 | 0.250 | 0.333 | b*c*d*E*f+a*C*E*f+a*b*c*E+a*B*C*D*e*F<->G |
| expert | 2 | 1.000 | 1.000 | 0.667 | a*b*D*e*F+a*b*c*e*F+a*b*C*d*E*f+a*B*C*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 0.667 | a*c*d*e*F+a*C*d*f+a*B*e*F+a*B*d*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.667 | a*c*d*f+a*c*d*e+a*B*d*e+a*B*c*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | a*c*d*f+a*c*d*e+a*B*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | a*e+a*d+A*E*F<->G |
| quantile | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | a*e+a*d<->G |
| kde | 2 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | e+c*d*f+a*C*f+a*b*c<->G |
| expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*f+a*C*e+a*b*e<->G |
| opt | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | a*f+a*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | a*f+a*e<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*e*F+a*d*f<->G |

