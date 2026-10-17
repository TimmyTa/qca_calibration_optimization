# n100_noise0.1_frag0.0_fz1_rep02

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=6002
- true model: `B*d+a*E+A*f*B<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.542 | True | 0.823 | 0.741 | 18 | 0.000 | 1.000 | 0.000 | 0.544 |
| quantile | 0.554 | True | 0.823 | 0.726 | 21 | 0.036 | 0.962 | 0.038 | 0.529 |
| kde | 0.546 | True | 0.824 | 0.720 | 19 | 0.031 | 0.963 | 0.037 | 0.534 |
| expert | 0.498 | False | 0.790 | 0.726 | 22 | 0.046 | 0.960 | 0.040 | 0.531 |
| opt | 0.712 | True | 0.863 | 0.622 | 11 | 0.141 | 0.873 | 0.127 | 0.713 |
| opt_c6c7 | 0.605 | True | 0.810 | 0.697 | 17 | 0.106 | 0.792 | 0.212 | 0.516 |
| opt_expert | 0.628 | True | 0.821 | 0.696 | 18 | 0.066 | 0.900 | 0.103 | 0.521 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.833 | 0.682 | 3 |
| quantile | 0.857 | 0.720 | 3 |
| kde | 0.842 | 0.667 | 3 |
| expert | 0.727 | 0.727 | 6 |
| opt | 0.909 | 0.435 | 1 |
| opt_c6c7 | 0.706 | 0.600 | 5 |
| opt_expert | 0.833 | 0.652 | 3 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 1.000 | B*c*D*f+a*c*d*E*F+a*b*c*d*E+a*b*C*E*F+a*B*C*E*f+A*C*d*E*F+A*B*c*f+A*B*c*D*e+A*B*C*d*e<->G |
| quantile | 1 | 0.000 | 0.667 | 1.000 | c*D*E*f+C*d*E*F+B*c*D*f+a*b*c*d*E+a*b*C*E*F+a*B*c*E*F+a*B*C*E*f+A*B*c*f+A*B*C*d*e<->G |
| kde | 1 | 0.000 | 0.667 | 1.000 | c*D*E*f+b*C*d*E*F+B*c*D*f+a*b*c*d*E+a*b*C*E*F+a*B*c*E*F+a*B*C*E*f+A*B*c*f+A*B*C*d*e<->G |
| expert | 2 | 0.000 | 0.444 | 0.667 | C*d*E*F+B*D*E*f+a*b*c*d*E+a*b*C*D*E+a*B*C*d*E+A*c*E*f+A*C*d*F+A*B*c*D+A*B*C*d*e<->G |
| opt | 1 | 0.000 | 0.667 | 1.000 | c*d*E*f+B*c*E*f+B*c*d*f+a*b*c*d*E+A*B*d*e*f+A*B*c*d*e<->G |
| opt_c6c7 | 2 | 0.000 | 0.429 | 0.667 | c*d*E*f+b*C*d*E*F+a*b*E*f+a*B*d*e*f+a*B*c*f+A*b*d*e*f+A*B*c*d*e<->G |
| opt_expert | 2 | 0.000 | 0.667 | 1.000 | c*d*E*f+B*C*d*e*f+a*b*d*E*F+a*B*E*f+a*B*d*f+A*c*E*f+A*b*d*E*f+A*B*c*D*f+A*B*C*d*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | B*f+B*c*e+a*E+A*C*d<->G |
| quantile | 4 | 0.000 | 0.438 | 0.583 | 0.000 | 1.000 | E*f+B*c+a*E+A*C*d<->G |
| kde | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | c*f+a*E+A*C*d<->G |
| expert | 2 | 0.000 | 0.600 | 1.000 | 0.000 | 1.000 | d+B*f+B*c+a*E+A*c*f<->G |
| opt | 12 | 0.000 | 0.125 | 0.167 | 0.000 | 1.000 | B*f+B*c+a*c*d*E+A*d*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | E*f+C*E+B*f+A*d*e<->G |
| opt_expert | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 0.000 | E*f+B+a*E<->G |

