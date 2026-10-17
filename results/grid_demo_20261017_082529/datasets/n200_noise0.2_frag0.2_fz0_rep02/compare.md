# n200_noise0.2_frag0.2_fz0_rep02

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=23002
- true model: `A*c*e+b*C*d+d*a<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.583 | True | 0.898 | 0.649 | 15 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.515 | False | 0.826 | 0.453 | 9 | 0.112 | 0.975 | 0.033 | 0.592 |
| kde | 0.570 | True | 0.842 | 0.631 | 14 | 0.064 | 1.000 | 0.000 | 0.677 |
| expert | 0.605 | True | 0.858 | 0.632 | 16 | 0.045 | 1.000 | 0.000 | 0.772 |
| opt | 0.708 | True | 0.907 | 0.517 | 12 | 0.085 | 0.946 | 0.060 | 0.836 |
| opt_c6c7 | 0.655 | True | 0.815 | 0.562 | 16 | 0.121 | 0.924 | 0.072 | 0.626 |
| opt_expert | 0.662 | True | 0.805 | 0.550 | 16 | 0.114 | 0.923 | 0.074 | 0.630 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.933 | 0.519 | 1 |
| quantile | 1.000 | 0.346 | 0 |
| kde | 1.000 | 0.519 | 0 |
| expert | 0.938 | 0.556 | 1 |
| opt | 0.917 | 0.458 | 1 |
| opt_c6c7 | 0.875 | 0.583 | 2 |
| opt_expert | 0.938 | 0.577 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.900 | 1.000 | b*C*d*E*f+B*C*d*e*f+a*c*d*e*F+a*C*d*E*f+a*b*d*E*f+a*b*C*d*E+a*B*c*d*F+A*b*c*e*f+A*b*C*d*e*F+A*B*c*D*e<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*f+a*b*d*E*f+a*b*C*d*F+a*B*c*d*e*F+a*B*C*d*f+A*b*c*d*e*f<->G |
| kde | 4 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+b*C*d*E*f+a*c*d*e*F+a*b*d*E*f+a*b*C*d*F+a*B*c*d*F+a*B*C*d*f+A*b*c*d*e*f+A*B*c*D*e<->G |
| expert | 8 | 0.000 | 0.900 | 1.000 | b*C*d*e*F+b*C*d*E*f+B*C*d*e*f+a*c*d*e*F+a*C*d*E*f+a*b*d*E*f+a*b*C*d*F+a*B*c*d*F+A*b*c*e*f+A*B*c*D*e<->G |
| opt | 1 | 0.000 | 0.857 | 1.000 | b*C*d*E*f+B*c*d*E*f+a*b*C*d*E+a*B*c*d*e*F+a*B*C*d*f+A*c*d*e*f+A*B*c*D*e<->G |
| opt_c6c7 | 2 | 0.000 | 0.688 | 1.000 | b*C*d*E*f+B*c*d*f+a*b*C*d*e*F+a*B*d*f+a*B*c*d*e+a*B*C*d*E+A*d*e*f+A*B*c*D*e<->G |
| opt_expert | 1 | 0.000 | 0.714 | 1.000 | b*c*d*f+b*C*d*e*F+a*b*d*E+a*B*c*d*e*F+a*B*C*d*f+A*b*d*f+A*b*c*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | b*d*E*f+B*C*e*f+a*d*E+a*c*d*F+A*c*e+A*b*e*F<->G |
| quantile | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*f+a*d*e*F+a*C*d+A*c*d*e<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*f+b*C*d*F+a*d*F+a*d*E+a*C*d+a*b*d+A*c*d*e+A*B*c*e<->G |
| expert | 1 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | b*d*E*f+b*C*d*F+B*C*e*f+a*d*F+a*d*E+a*b*d+A*c*e<->G |
| opt | 2 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | c*d*E*f+b*d*E+B*c*e*F+a*C*f+A*c*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | d*e*f+c*d*f+b*d+B*c*e+a*C*d<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | b*d*f+b*d*e+a*d+A*c*e<->G |

