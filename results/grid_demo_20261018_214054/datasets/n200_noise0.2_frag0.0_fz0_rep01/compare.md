# n200_noise0.2_frag0.0_fz0_rep01

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=21001
- true model: `c*B+D*c+a*b*C<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.501 | True | 0.912 | 0.552 | 14 | 0.000 | 1.000 | 0.000 | 0.796 |
| quantile | 0.245 | False | 0.884 | 0.253 | 3 | 0.091 | 0.991 | 0.013 | 0.629 |
| kde | 0.377 | False | 0.880 | 0.387 | 6 | 0.046 | 1.000 | 0.000 | 0.704 |
| expert | 0.622 | True | 0.879 | 0.609 | 19 | 0.059 | 1.000 | 0.000 | 0.800 |
| opt | 0.743 | True | 0.903 | 0.530 | 17 | 0.114 | 0.937 | 0.058 | 0.816 |
| opt_c6c7 | 0.644 | True | 0.875 | 0.501 | 16 | 0.103 | 0.938 | 0.066 | 0.670 |
| opt_expert | 0.665 | True | 0.871 | 0.516 | 16 | 0.083 | 0.950 | 0.037 | 0.680 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.467 | 0 |
| quantile | 1.000 | 0.094 | 0 |
| kde | 1.000 | 0.200 | 0 |
| expert | 1.000 | 0.633 | 0 |
| opt | 1.000 | 0.586 | 0 |
| opt_c6c7 | 1.000 | 0.533 | 0 |
| opt_expert | 1.000 | 0.552 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.857 | 1.000 | B*c*e*F+a*c*D*e*f+a*b*D*E*F+a*b*C*d*e*f+a*B*c*D+A*b*c*D*F+A*B*c*d*F<->G |
| quantile | 1 | 0.000 | 0.500 | 0.667 | a*b*D*E*F+A*B*c*D*e*F<->G |
| kde | 1 | 1.000 | 1.000 | 0.667 | a*c*D*e*f+a*b*c*D*E*F+A*c*D*e*F+A*B*c*e*F<->G |
| expert | 1 | 0.000 | 0.857 | 1.000 | c*D*F+b*c*D*E+B*c*e*F+a*c*D+a*b*D*E*F+a*b*C*d*e*f+A*B*c*d*E<->G |
| opt | 1 | 0.000 | 0.833 | 1.000 | c*D*e*F+b*c*D*f+B*c*E*F+a*b*D*E*F+a*b*C*d*E+A*B*c*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.857 | 0.667 | b*c*D*e+B*c*e*F+B*c*D*F+a*c*D*e+a*b*D*F+a*b*c*D+a*B*c*F<->G |
| opt_expert | 1 | 0.000 | 0.857 | 0.667 | b*c*D*F+B*c*e*F+a*c*D*e+a*b*D*E*F+a*b*c*D+a*B*c*F+A*B*c*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*E*F+B*c*d*F+a*c*D*e*f+a*b*C*d*e*f+a*B*c*D+A*c*D*e*F<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*D*E*F+A*B*c*D*e<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*D*e*f+a*b*c*D*E*F+A*c*D*e*F+A*B*c*e<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*F+b*D*E+B*c*F+a*c*D+a*b*C*d*e*f+A*B*c<->G |
| opt | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | c*D+B*c*F+a*b*C*E<->G |
| opt_c6c7 | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e+b*D*F+b*D*E+B*c*F<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*F+b*D*E*F+B*c*F+a*c*D+A*B*c<->G |

