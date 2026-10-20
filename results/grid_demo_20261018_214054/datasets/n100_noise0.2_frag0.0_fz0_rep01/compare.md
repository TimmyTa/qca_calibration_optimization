# n100_noise0.2_frag0.0_fz0_rep01

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=9001
- true model: `B*d+e*f+f*a*B<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.459 | False | 0.935 | 0.491 | 8 | 0.000 | 1.000 | 0.000 | 0.801 |
| quantile | 0.286 | False | 0.871 | 0.277 | 3 | 0.095 | 0.965 | 0.052 | 0.614 |
| kde | 0.436 | False | 0.918 | 0.431 | 6 | 0.052 | 1.000 | 0.000 | 0.697 |
| expert | 0.386 | False | 0.901 | 0.449 | 7 | 0.044 | 1.000 | 0.000 | 0.773 |
| opt | 0.573 | True | 0.939 | 0.522 | 12 | 0.111 | 0.922 | 0.068 | 0.862 |
| opt_c6c7 | 0.540 | True | 0.871 | 0.504 | 9 | 0.117 | 0.863 | 0.132 | 0.630 |
| opt_expert | 0.500 | True | 0.881 | 0.501 | 8 | 0.068 | 0.940 | 0.060 | 0.682 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.875 | 0.280 | 1 |
| quantile | 1.000 | 0.120 | 0 |
| kde | 1.000 | 0.240 | 0 |
| expert | 0.857 | 0.240 | 1 |
| opt | 0.917 | 0.524 | 1 |
| opt_c6c7 | 1.000 | 0.643 | 0 |
| opt_expert | 0.875 | 0.292 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.800 | 0.667 | b*C*d*e*f+a*b*c*D*f+a*b*C*e*f+a*B*c*d*E*F+A*B*D*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.333 | b*C*d*e*f+A*C*d*e*f<->G |
| kde | 1 | 1.000 | 1.000 | 0.333 | b*C*d*e*f+a*b*D*e*f+A*B*D*e*f<->G |
| expert | 1 | 0.000 | 0.800 | 0.667 | a*b*D*e*f+a*b*c*D*f+a*B*c*d*E*F+A*b*C*d*e*f+A*B*D*e*f<->G |
| opt | 2 | 0.000 | 0.889 | 1.000 | b*C*d*e*f+B*C*D*e*f+a*b*c*D*e*f+a*b*C*D*E*f+a*B*c*D*E*f+a*B*C*d*E+A*b*d*e*f+A*B*D*e*f+A*B*C*e*f<->G |
| opt_c6c7 | 3 | 1.000 | 1.000 | 0.667 | b*c*D*e*f+b*C*d*e*f+B*C*D*e*f+a*B*C*d*E*F+A*b*C*e*f+A*B*C*d*e*F<->G |
| opt_expert | 1 | 0.000 | 0.800 | 1.000 | b*C*d*e*f+a*b*D*e*f+a*b*C*D*f+a*B*C*d*E*f+A*B*D*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*f+B*d*E+B*D*e*f+a*b*D*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e*f<->G |
| kde | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*f+B*D*e*f+a*D*e*f<->G |
| expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*E+B*D*e*f+a*b*D*f+A*C*e*f<->G |
| opt | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | e*f+D*f+a*d*E<->G |
| opt_c6c7 | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 0.833 | b*e*f+B*D*f+B*C*d*e+a*B*d<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*e*f+B*d*E+a*b*D*f+A*B*D*f<->G |

