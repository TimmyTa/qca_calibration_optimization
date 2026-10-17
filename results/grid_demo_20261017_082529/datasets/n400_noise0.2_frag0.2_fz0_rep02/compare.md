# n400_noise0.2_frag0.2_fz0_rep02

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=35002
- true model: `e*D+f*A*e<->G`  (irrelevant: B, C)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.739 | True | 0.863 | 0.592 | 12 | 0.000 | 1.000 | 0.000 | 0.796 |
| quantile | 0.556 | False | 0.779 | 0.497 | 11 | 0.090 | 0.985 | 0.018 | 0.623 |
| kde | 0.648 | True | 0.810 | 0.585 | 11 | 0.048 | 1.000 | 0.000 | 0.702 |
| expert | 0.732 | True | 0.857 | 0.541 | 13 | 0.041 | 1.000 | 0.000 | 0.768 |
| opt | 0.792 | True | 0.816 | 0.504 | 14 | 0.086 | 0.949 | 0.045 | 0.731 |
| opt_c6c7 | 0.720 | True | 0.846 | 0.501 | 12 | 0.088 | 0.956 | 0.051 | 0.658 |
| opt_expert | 0.729 | True | 0.829 | 0.524 | 12 | 0.070 | 0.970 | 0.033 | 0.674 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.667 | 0 |
| quantile | 1.000 | 0.611 | 0 |
| kde | 1.000 | 0.611 | 0 |
| expert | 1.000 | 0.722 | 0 |
| opt | 1.000 | 0.737 | 0 |
| opt_c6c7 | 1.000 | 0.632 | 0 |
| opt_expert | 1.000 | 0.600 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e+a*c*D*e*f+a*b*D*e+A*c*d*e*f+A*b*d*e*f+A*B*D*e*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e+a*c*D*e*f+a*b*D*e+A*c*d*e*f+A*B*D*e*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e+a*c*D*e*f+a*b*D*e+A*c*d*e*f+A*B*D*e*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e+a*c*D*e*f+a*b*D*e+A*d*e*f+A*B*D*e*F<->G |
| opt | 3 | 1.000 | 1.000 | 1.000 | B*C*D*e*F+a*D*e*f+a*b*D*e+A*c*e*f+A*c*D*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e+a*c*D*e*f+a*b*D*e+A*c*d*e*f+A*b*d*e*f+A*B*D*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e*F+a*b*C*D*e+a*B*D*e*f+A*b*d*e*f+A*B*D*e*F+A*B*c*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | D*e+A*c*d*f+A*b*e*f<->G |
| quantile | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | D*e+A*c*e*f<->G |
| kde | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | D*e+A*c*d*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*e+A*e*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | D*e+A*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*e+A*e*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*e*f+b*D*e+A*D*e+A*c*e*f+A*b*e*f<->G |

