# n200_noise0.2_frag0.2_fz0_rep02

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=23002
- true model: `A*c*e+b*C*d+d*a<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.611 | True | 0.940 | 0.557 | 11 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.291 | False | 0.883 | 0.213 | 2 | 0.112 | 0.975 | 0.033 | 0.592 |
| kde | 0.144 | False | 0.892 | 0.187 | 1 | 0.064 | 1.000 | 0.000 | 0.677 |
| expert | 0.577 | True | 0.928 | 0.502 | 10 | 0.045 | 1.000 | 0.000 | 0.772 |
| opt | 0.716 | True | 0.919 | 0.508 | 11 | 0.084 | 0.939 | 0.062 | 0.824 |
| opt_c6c7 | 0.582 | True | 0.877 | 0.508 | 12 | 0.117 | 0.931 | 0.072 | 0.642 |
| opt_expert | 0.567 | True | 0.885 | 0.501 | 12 | 0.103 | 0.912 | 0.084 | 0.645 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.407 | 0 |
| quantile | 1.000 | 0.077 | 0 |
| kde | 1.000 | 0.037 | 0 |
| expert | 1.000 | 0.370 | 0 |
| opt | 0.909 | 0.417 | 1 |
| opt_c6c7 | 1.000 | 0.480 | 0 |
| opt_expert | 0.917 | 0.458 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*f+a*b*d*E*f+a*b*C*d*E+a*B*c*d*e*F+a*B*C*d*f+A*b*c*d*e*f+A*b*C*d*e*F+A*B*c*D*e<->G |
| quantile | 1 | 1.000 | 1.000 | 0.333 | a*b*d*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 0.667 | a*b*C*d*E*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*f+a*b*d*E*f+a*b*C*d*E+a*B*c*d*e*F+a*B*C*d*f+A*b*c*d*e*f+A*B*c*D*e<->G |
| opt | 1 | 0.000 | 0.857 | 1.000 | b*C*d*E*f+a*b*C*d*E+a*B*c*d*e*F+a*B*C*d*f+A*c*d*e*f+A*B*c*d*f+A*B*c*D*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 1.000 | b*c*d*e*f+b*C*d*E*f+B*c*d*e*F+a*b*C*d*F+a*B*C*d*f+A*B*c*D*e<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | b*C*d*E+a*B*d*e*F+a*B*C*d+A*b*C*d*F+A*B*c*d*E*f+A*B*c*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*f+b*C*E*F+a*C*f+a*B*e*F+A*c*d*e+A*b*e*F+A*B*c*e<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*d*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*C*f<->G |
| expert | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*f+b*C*d*E+B*D*e*f+B*c*e*F+a*C*f<->G |
| opt | 3 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | b*d*E+a*C*f+a*B*e*F+A*c*e+A*c*d*f<->G |
| opt_c6c7 | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*e*F+b*d*E+b*c*d+a*b*d+a*B*C*f+A*B*c<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*f+b*C*d*E+B*c*e+a*B*C*d+A*b*d*e*F<->G |

