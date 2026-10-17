# n100_noise0.0_frag0.0_fz1_rep02

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=2002
- true model: `d*a+D*B<->G`  (irrelevant: C, E, F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.569 | True | 0.857 | 0.772 | 27 | 0.000 | 1.000 | 0.000 | 0.541 |
| quantile | 0.546 | True | 0.841 | 0.746 | 26 | 0.034 | 0.977 | 0.033 | 0.529 |
| kde | 0.538 | True | 0.835 | 0.756 | 27 | 0.040 | 0.968 | 0.035 | 0.531 |
| expert | 0.605 | True | 0.829 | 0.740 | 19 | 0.091 | 0.903 | 0.097 | 0.564 |
| opt | 0.845 | True | 0.946 | 0.725 | 23 | 0.151 | 0.930 | 0.070 | 0.781 |
| opt_c6c7 | 0.632 | True | 0.818 | 0.735 | 23 | 0.064 | 0.858 | 0.132 | 0.523 |
| opt_expert | 0.623 | True | 0.807 | 0.748 | 24 | 0.069 | 0.843 | 0.155 | 0.514 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.963 | 0.897 | 1 |
| quantile | 1.000 | 0.963 | 0 |
| kde | 0.963 | 0.963 | 1 |
| expert | 1.000 | 0.704 | 0 |
| opt | 1.000 | 0.958 | 0 |
| opt_c6c7 | 1.000 | 0.958 | 0 |
| opt_expert | 0.958 | 1.000 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.571 | 1.000 | B*C*D*E*f+a*d*f+a*c*D*e*F+a*C*d+a*B*F+a*B*e+A*B*c*D<->G |
| quantile | 1 | 0.000 | 0.714 | 1.000 | a*d*f+a*d*E+a*C*d+a*B*e+a*B*C*F+A*B*D*f+A*B*c*D<->G |
| kde | 1 | 0.000 | 0.625 | 1.000 | a*d*f+a*d*E+a*c*D*e*F+a*C*d+a*B*e+a*B*C*F+A*B*D*f+A*B*c*D<->G |
| expert | 4 | 0.250 | 0.857 | 1.000 | B*D*E*f+B*c*D*E+a*C*d*f+a*b*d*f+a*b*C*d*E+a*B*E*f+a*B*D<->G |
| opt | 10 | 0.300 | 0.910 | 1.000 | B*C*D*e+a*C*d*E+a*b*d*e*f+a*b*c*d*e+a*B*E*F+a*B*d*F+a*B*d*E+a*B*D*e*f+A*B*D*F+A*B*D*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.786 | 1.000 | B*c*D*E*F+B*C*D*E*f+a*d*F+a*b*d+a*B*E+a*B*D*f+a*B*c*F<->G |
| opt_expert | 4 | 0.000 | 0.750 | 1.000 | B*c*D*E*F+B*C*D*E*f+a*d*F+a*d*E+a*c*E*F+a*b*d+a*B*D*f+a*B*C*D<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | B*D*E*f+B*c*D+a*d+a*c*e*F+a*B<->G |
| quantile | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | B*D*f+B*c*D+a*d+a*B<->G |
| kde | 1 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | B*D*f+B*c*D+a*d+a*c*e*F+a*B<->G |
| expert | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*E+a*b*d*f+a*b*C*d*E+a*B*E*f+a*B*D+a*B*C*f<->G |
| opt | 1 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | B*D+a*d*f+a*d*E+a*c*d+a*B<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | B*D*E+a*d+a*B<->G |
| opt_expert | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | B*D+a*d+a*c*F<->G |

