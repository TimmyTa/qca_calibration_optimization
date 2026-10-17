# n100_noise0.2_frag0.0_fz0_rep00

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=9000
- true model: `b*a*F+D*F*b<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.594 | True | 0.863 | 0.687 | 17 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.312 | False | 0.812 | 0.403 | 4 | 0.112 | 0.962 | 0.062 | 0.605 |
| kde | 0.535 | True | 0.816 | 0.676 | 16 | 0.051 | 1.000 | 0.000 | 0.704 |
| expert | 0.528 | True | 0.851 | 0.537 | 11 | 0.060 | 1.000 | 0.000 | 0.770 |
| opt | 0.703 | True | 0.919 | 0.511 | 11 | 0.125 | 0.888 | 0.105 | 0.799 |
| opt_c6c7 | 0.583 | True | 0.815 | 0.514 | 9 | 0.109 | 0.853 | 0.127 | 0.638 |
| opt_expert | 0.649 | True | 0.810 | 0.501 | 8 | 0.112 | 0.892 | 0.105 | 0.676 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.529 | 0.900 | 8 |
| quantile | 1.000 | 0.333 | 0 |
| kde | 0.562 | 0.900 | 7 |
| expert | 0.727 | 0.800 | 3 |
| opt | 0.545 | 1.000 | 5 |
| opt_c6c7 | 0.556 | 0.714 | 4 |
| opt_expert | 0.625 | 0.714 | 3 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.364 | 1.000 | c*D*e*F+b*c*D*F+b*C*d*E*F+a*b*E*F+a*b*c*F+a*b*c*D*e+a*B*D*e*F+a*B*c*d*e*f+A*b*D*e*F+A*B*c*d*E*F+A*B*C*D*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e*F+a*b*D*e*F+a*b*c*d*E*F<->G |
| kde | 1 | 0.000 | 0.400 | 1.000 | b*c*D*F+b*C*d*E*F+a*b*E*F+a*b*c*F+a*b*c*D*e+a*B*D*e*F+a*B*c*d*e*f+A*b*D*e*F+A*B*c*d*E*F+A*B*C*D*e*f<->G |
| expert | 1 | 0.000 | 0.500 | 1.000 | b*c*D*F+b*C*d*E*F+a*c*D*e*F+a*b*E*F+A*b*D*e*F+A*B*c*d*E*F<->G |
| opt | 2 | 0.000 | 0.286 | 1.000 | b*c*D*e*F+b*C*E*F+a*c*D*e*F+a*b*c*D*F+a*B*c*d*E*F+A*b*C*d*E+A*B*C*d*e*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.200 | 0.500 | b*c*D*F+a*c*D*e*F+a*b*c*D*e+A*b*C*E*F+A*B*C*D*e*f<->G |
| opt_expert | 1 | 0.000 | 0.400 | 1.000 | b*c*D*e*F+a*c*D*e*F+a*b*c*E*F+A*b*C*E*F+A*b*C*d*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 14 | 0.000 | 0.111 | 0.500 | 0.000 | 1.000 | c*e*F+b*D*F+b*C*E*F+B*c*d*F+B*c*d*e+a*D*e*F+a*b*c*F+a*b*c*D*e+A*B*C*D*f<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*D*e*F+a*b*c*d*E*F+A*b*c*e*F<->G |
| kde | 8 | 0.000 | 0.125 | 0.500 | 0.000 | 1.000 | b*D*F+b*C*E*F+B*c*d*F+B*c*d*e+a*D*e*F+a*b*c*F+a*b*c*D*e+A*B*C*D*f<->G |
| expert | 6 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | b*D*F+B*c*d*F+a*c*D*e*F+a*b*E*F+A*b*C*F<->G |
| opt | 4 | 0.000 | 0.200 | 1.000 | 0.000 | 1.000 | b*F+a*c*e*F+a*c*d*F+A*b*d*E+A*B*d*e*f<->G |
| opt_c6c7 | 4 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | b*D*F+b*C*E*F+a*c*D*e+A*C*D*e<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*F+a*c*D*e*F+A*b*F<->G |

