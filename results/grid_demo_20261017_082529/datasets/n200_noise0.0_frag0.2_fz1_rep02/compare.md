# n200_noise0.0_frag0.2_fz1_rep02

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=16002
- true model: `C*d+E*F+E*D<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.651 | True | 0.888 | 0.740 | 18 | 0.000 | 1.000 | 0.000 | 0.552 |
| quantile | 0.596 | True | 0.857 | 0.716 | 22 | 0.051 | 0.942 | 0.063 | 0.523 |
| kde | 0.616 | False | 0.863 | 0.715 | 17 | 0.060 | 0.947 | 0.053 | 0.554 |
| expert | 0.651 | True | 0.885 | 0.716 | 16 | 0.089 | 0.923 | 0.077 | 0.578 |
| opt | 0.813 | True | 0.875 | 0.732 | 19 | 0.144 | 0.885 | 0.113 | 0.761 |
| opt_c6c7 | 0.767 | True | 0.877 | 0.732 | 20 | 0.049 | 0.925 | 0.080 | 0.542 |
| opt_expert | 0.765 | True | 0.853 | 0.750 | 22 | 0.044 | 0.907 | 0.090 | 0.523 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.944 | 0.630 | 1 |
| quantile | 0.864 | 0.559 | 3 |
| kde | 0.882 | 0.536 | 2 |
| expert | 1.000 | 0.500 | 0 |
| opt | 1.000 | 0.613 | 0 |
| opt_c6c7 | 1.000 | 0.667 | 0 |
| opt_expert | 1.000 | 0.667 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.889 | 1.000 | b*c*D*E*F+B*C*E*F+a*b*c*d*F+a*b*C*d*f+a*B*c*D*E+A*C*d*E*F+A*C*D*E*f+A*B*d*E*F+A*B*C*d*e<->G |
| quantile | 2 | 0.000 | 0.591 | 1.000 | b*D*E*F+B*C*E*F+a*b*c*d*F+a*b*C*d*f+a*b*C*D*E+a*B*c*D*E*f+A*C*d*F+A*b*C*D*e*f+A*B*C*F+A*B*C*E+A*B*C*d<->G |
| kde | 2 | 0.000 | 0.800 | 1.000 | B*c*D*E+a*c*E*F+a*b*c*d*E+a*b*C*d*e*f+a*b*C*D*E*f+a*B*d*E*F+A*c*D*E+A*B*D*E*F+A*B*c*d*F+A*B*C*d*e*f<->G |
| expert | 2 | 0.000 | 0.857 | 1.000 | C*d*E*F+B*D*E*F+B*C*d*e*f+a*b*c*E*F+a*b*C*E*f+A*B*C*d*F+A*B*C*D*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | C*E*F+b*E*F+a*b*C*d*f+A*C*d*e+A*b*C*D*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.875 | 1.000 | b*c*E*F+b*C*d*E*f+B*C*d*E*F+a*B*c*D*E*f+A*E*F+A*C*E+A*C*d*f+A*b*D*E<->G |
| opt_expert | 1 | 0.000 | 0.857 | 1.000 | C*E*F+b*D*E*F+b*C*d*f+a*b*E*F+a*B*c*D*E*f+A*C*E+A*C*d<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | E*F+D*E+C+a*b*d<->G |
| quantile | 6 | 0.000 | 0.375 | 0.500 | 0.000 | 1.000 | D*E+C*f+b*d*F+B*C<->G |
| kde | 2 | 0.000 | 0.600 | 1.000 | 0.000 | 1.000 | E*F+D*E+C+a*b*E+A*B*d*F<->G |
| expert | 3 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | D*E*F+C*f+C*d+a*b*E<->G |
| opt | 6 | 0.000 | 0.375 | 0.500 | 0.000 | 1.000 | E*F+D*f+C*d*e+a*C*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | E*F+D*E+C<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | E*F+D*E+b*C*d+A*C*d<->G |

