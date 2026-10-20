# n100_noise0.2_frag0.0_fz0_rep00

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=9000
- true model: `b*a*F+D*F*b<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.418 | False | 0.942 | 0.448 | 8 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.470 | False | 0.883 | 0.278 | 1 | 0.112 | 0.962 | 0.062 | 0.605 |
| kde | 0.404 | False | 0.900 | 0.328 | 2 | 0.051 | 1.000 | 0.000 | 0.704 |
| expert | 0.518 | False | 0.909 | 0.402 | 8 | 0.060 | 1.000 | 0.000 | 0.770 |
| opt | 0.677 | True | 0.951 | 0.513 | 10 | 0.118 | 0.903 | 0.100 | 0.884 |
| opt_c6c7 | 0.606 | True | 0.831 | 0.517 | 14 | 0.114 | 0.913 | 0.085 | 0.642 |
| opt_expert | 0.407 | False | 0.855 | 0.443 | 3 | 0.102 | 0.902 | 0.100 | 0.675 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.750 | 0.600 | 2 |
| quantile | 1.000 | 0.083 | 0 |
| kde | 1.000 | 0.200 | 0 |
| expert | 0.875 | 0.700 | 1 |
| opt | 0.600 | 0.857 | 4 |
| opt_c6c7 | 0.571 | 0.889 | 6 |
| opt_expert | 0.667 | 0.250 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.600 | 1.000 | b*c*D*F+a*c*D*e*F+a*b*D*E*F+A*b*D*e*F+A*B*C*D*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*F<->G |
| kde | 1 | 1.000 | 1.000 | 0.500 | b*c*D*e*F<->G |
| expert | 2 | 0.000 | 0.750 | 1.000 | b*C*d*E*F+a*b*E*F+a*b*c*D*F+A*b*D*e*F<->G |
| opt | 1 | 0.000 | 0.333 | 1.000 | b*C*d*E*F+a*c*D*e*F+a*b*D*E*F+a*B*c*d*E*F+a*B*C*D*e*f+A*b*D*e*F<->G |
| opt_c6c7 | 2 | 0.000 | 0.375 | 1.000 | b*C*d*E*F+a*c*d*E*F+a*c*D*e*F+a*b*E*F+a*b*c*F+a*b*c*D*e+a*B*C*D*e+A*b*D*e*F<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | b*c*D*e*F+A*b*C*d*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*D*F+a*c*D*e*F+A*B*C*D*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*D*e*F<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*e*F<->G |
| expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*e*F+a*b*E*F+A*b*C*F<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*F+b*E*F+B*C*D*e*f+a*c*e*F+A*b*F<->G |
| opt_c6c7 | 2 | 0.000 | 0.100 | 0.250 | 0.000 | 1.000 | b*E*F+b*D*F+b*c*D*e+a*c*F+a*B*C*D*e<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*e*F+A*b*C*d*E<->G |

