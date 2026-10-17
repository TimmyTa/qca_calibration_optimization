# n100_noise0.2_frag0.0_fz0_rep01

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=9001
- true model: `B*d+e*f+f*a*B<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.463 | True | 0.877 | 0.596 | 12 | 0.000 | 1.000 | 0.000 | 0.801 |
| quantile | 0.415 | False | 0.820 | 0.438 | 9 | 0.095 | 0.965 | 0.052 | 0.614 |
| kde | 0.460 | True | 0.858 | 0.586 | 12 | 0.052 | 1.000 | 0.000 | 0.697 |
| expert | 0.457 | True | 0.863 | 0.546 | 11 | 0.044 | 1.000 | 0.000 | 0.773 |
| opt | 0.593 | True | 0.888 | 0.537 | 13 | 0.112 | 0.890 | 0.105 | 0.766 |
| opt_c6c7 | 0.570 | True | 0.838 | 0.541 | 13 | 0.102 | 0.898 | 0.085 | 0.661 |
| opt_expert | 0.548 | True | 0.860 | 0.536 | 11 | 0.067 | 0.958 | 0.042 | 0.679 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.833 | 0.400 | 2 |
| quantile | 0.889 | 0.320 | 1 |
| kde | 0.917 | 0.440 | 1 |
| expert | 0.727 | 0.320 | 3 |
| opt | 0.923 | 0.522 | 1 |
| opt_c6c7 | 1.000 | 0.650 | 0 |
| opt_expert | 0.909 | 0.455 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.750 | 0.667 | b*C*d*e*f+a*c*D*E*f+a*b*D*e*f+a*B*c*d*E*F+a*B*c*D*e*F+A*B*D*e*f+A*B*c*e*f+A*B*C*d*e*F<->G |
| quantile | 3 | 0.000 | 0.750 | 0.333 | a*b*c*D*f+a*b*C*e*f+A*C*d*e*f+A*B*e*f<->G |
| kde | 3 | 0.000 | 0.875 | 0.667 | b*C*d*e*f+a*c*D*E*f+a*b*D*e*f+a*B*c*d*E*F+A*c*D*e*f+A*B*D*e*f+A*B*c*e*f+A*B*C*d*e*F<->G |
| expert | 2 | 0.000 | 0.625 | 0.667 | b*C*d*e*f+a*b*c*D*f+a*b*C*e*f+a*B*c*d*E*F+a*B*c*D*e*F+A*b*c*d*e*F+A*B*D*e*f+A*B*c*e*f<->G |
| opt | 1 | 0.000 | 0.875 | 0.667 | C*d*e*f+B*C*e*f+a*b*c*D*e*f+a*b*C*D*E*f+a*B*C*d*E+A*b*d*e*f+A*B*D*e*f+A*B*c*d*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | C*d*e*f+B*C*e*f+a*b*c*D*e*f+a*B*c*d*e*F+a*B*c*D*E*f+a*B*C*d*E*F+A*d*e*f+A*B*e*f<->G |
| opt_expert | 6 | 0.000 | 0.857 | 0.667 | b*C*d*e*f+B*C*D*e*f+a*b*D*e*f+a*b*C*D*f+a*B*C*d*E+A*B*D*e*f+A*B*C*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | C*e*f+B*d+B*c*e+a*D*f<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*f+a*b*D*f+A*B*e*f<->G |
| kde | 4 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | D*e*f+C*e*f+B*d+a*E*f<->G |
| expert | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*f+B*d*E+B*c*e+a*b*D*f+A*c*d*e<->G |
| opt | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | e*f+c*f+a*E<->G |
| opt_c6c7 | 4 | 0.000 | 0.333 | 0.667 | 0.000 | 1.000 | f+B*c*d+a*d*E<->G |
| opt_expert | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*f+B*D*f+a*D*f+a*B*d<->G |

