# n200_noise0.1_frag0.0_fz1_rep02

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=18002
- true model: `C*F+a*e*c<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.631 | True | 0.870 | 0.720 | 21 | 0.000 | 1.000 | 0.000 | 0.558 |
| quantile | 0.583 | True | 0.832 | 0.711 | 22 | 0.033 | 0.973 | 0.026 | 0.535 |
| kde | 0.628 | True | 0.837 | 0.739 | 20 | 0.041 | 0.966 | 0.034 | 0.548 |
| expert | 0.586 | False | 0.791 | 0.708 | 26 | 0.097 | 0.865 | 0.135 | 0.547 |
| opt | 0.815 | True | 0.855 | 0.611 | 19 | 0.099 | 0.927 | 0.060 | 0.677 |
| opt_c6c7 | 0.666 | True | 0.830 | 0.732 | 24 | 0.056 | 0.917 | 0.070 | 0.531 |
| opt_expert | 0.654 | True | 0.852 | 0.703 | 18 | 0.057 | 0.907 | 0.086 | 0.537 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.875 | 0 |
| quantile | 0.864 | 0.792 | 3 |
| kde | 1.000 | 0.870 | 0 |
| expert | 0.462 | 0.706 | 14 |
| opt | 1.000 | 0.950 | 0 |
| opt_c6c7 | 0.833 | 0.952 | 4 |
| opt_expert | 0.889 | 0.889 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.750 | 1.000 | C*E*F+C*D*F+a*c*e*f+a*c*D*e+a*B*e*F+A*b*C*F<->G |
| quantile | 1 | 0.000 | 0.625 | 1.000 | C*E*F+C*D*F+B*C*F+a*D*e*f+a*B*D*e+a*B*c*e*f+a*B*C*D+A*C*F<->G |
| kde | 8 | 0.250 | 0.857 | 1.000 | C*d*E*F+C*D*e*F+b*C*d*F+a*c*e*f+a*c*D*e+a*C*F+a*B*c*e<->G |
| expert | 14 | 0.000 | 0.286 | 1.000 | b*C*d*E+B*C*D*E*f+a*c*e*f+a*c*D*F+a*b*c*F+a*b*C*E+a*b*C*D*f+a*B*E*f+A*c*d*e*F+A*C*d*E*F+A*b*C*D*e*F<->G |
| opt | 4 | 0.000 | 0.833 | 1.000 | C*d*E*F+B*C*F+a*D*e*F+a*C*D*F+a*B*c*e+A*C*e*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.625 | 1.000 | C*E*F+C*D*F+B*C*F+a*D*e*f+a*b*C*e*f+a*B*c*e+a*B*C*D+A*C*F<->G |
| opt_expert | 1 | 0.000 | 0.714 | 1.000 | b*C*E*F+a*c*D*e+a*C*E*F+a*B*D*F+a*B*c*e+A*C*D*F+A*b*c*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*F+a*c*e<->G |
| quantile | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | C*F+a*c*e+a*C*D<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*F+a*c*e<->G |
| expert | 40 | 0.000 | 0.197 | 0.787 | 0.000 | 1.000 | d*e*F+C*F+b*C*d+B*C*D+a*F+a*C*E+a*b*e+a*B*c<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*F+a*c*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | C*F+a*c*e+a*b*e+a*B*C*D<->G |
| opt_expert | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | C*F+b*d*e*F+a*c*e+a*B*D*F<->G |

