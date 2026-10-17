# n200_noise0.0_frag0.2_fz1_rep01

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=16001
- true model: `C*e*d+c*a*D<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.347 | True | 0.852 | 0.514 | 3 | 0.000 | 1.000 | 0.000 | 0.548 |
| quantile | 0.463 | True | 0.859 | 0.549 | 5 | 0.039 | 0.970 | 0.023 | 0.541 |
| kde | 0.490 | True | 0.850 | 0.608 | 6 | 0.033 | 0.980 | 0.017 | 0.543 |
| expert | 0.334 | False | 0.876 | 0.446 | 2 | 0.071 | 0.901 | 0.099 | 0.537 |
| opt | 0.873 | True | 0.871 | 0.585 | 9 | 0.117 | 0.958 | 0.057 | 0.728 |
| opt_c6c7 | 0.529 | True | 0.845 | 0.512 | 4 | 0.064 | 0.883 | 0.115 | 0.533 |
| opt_expert | 0.563 | True | 0.848 | 0.594 | 6 | 0.047 | 0.927 | 0.063 | 0.538 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.250 | 0 |
| quantile | 1.000 | 0.385 | 0 |
| kde | 1.000 | 0.500 | 0 |
| expert | 1.000 | 0.182 | 0 |
| opt | 1.000 | 0.750 | 0 |
| opt_c6c7 | 1.000 | 0.333 | 0 |
| opt_expert | 1.000 | 0.462 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*f+a*b*C*d*e*f+a*B*c*D*e*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*c*D*e*f+a*b*C*d*e*f+a*B*c*D*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*c*D*e*f+a*b*C*d*e*f+a*B*c*D*F+a*B*C*d*e*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*f+a*b*C*d*e*f<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+a*c*D*e*f+a*c*D*E*F+a*C*d*e*F+a*b*C*d*e+a*B*c*D*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*f+a*b*c*D*E*F+a*b*C*d*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*c*D*E*F+a*b*c*D*e*f+a*b*C*d*e+a*B*c*D*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 27 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*e*f+B*c*e*F+a*b*c*D*e<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*e*f+a*B*c*D<->G |
| kde | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*e*f+a*c*D*e+a*B*d*e+a*B*c*D<->G |
| expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e*f+a*b*c*D*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*d*e+a*c*D<->G |
| opt_c6c7 | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 0.500 | a*d*e+a*c*D<->G |
| opt_expert | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 0.500 | a*c*D+a*b*C*e<->G |

