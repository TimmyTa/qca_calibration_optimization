# n200_noise0.2_frag0.0_fz0_rep00

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=21000
- true model: `D*A+A*f*E<->G`  (irrelevant: B, C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.537 | True | 0.843 | 0.612 | 13 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.538 | False | 0.813 | 0.465 | 10 | 0.091 | 0.973 | 0.032 | 0.622 |
| kde | 0.457 | True | 0.813 | 0.516 | 9 | 0.053 | 1.000 | 0.000 | 0.694 |
| expert | 0.515 | True | 0.813 | 0.625 | 14 | 0.046 | 1.000 | 0.000 | 0.805 |
| opt | 0.674 | True | 0.830 | 0.501 | 13 | 0.077 | 0.943 | 0.067 | 0.727 |
| opt_c6c7 | 0.630 | True | 0.811 | 0.509 | 15 | 0.101 | 0.943 | 0.073 | 0.662 |
| opt_expert | 0.587 | True | 0.803 | 0.501 | 11 | 0.079 | 0.963 | 0.029 | 0.669 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.846 | 0.550 | 2 |
| quantile | 1.000 | 0.500 | 0 |
| kde | 1.000 | 0.450 | 0 |
| expert | 0.786 | 0.550 | 3 |
| opt | 0.923 | 0.706 | 1 |
| opt_c6c7 | 0.867 | 0.722 | 2 |
| opt_expert | 1.000 | 0.611 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 1.000 | a*B*c*d*e*F+A*d*E*f+A*c*D*f+A*c*D*E+A*B*D*e*f+A*B*c*E<->G |
| quantile | 3 | 1.000 | 1.000 | 1.000 | A*c*D*E*F+A*C*d*E*f+A*b*c*D*f+A*B*d*E*f+A*B*D*e*f+A*B*D*E*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*c*E*f+A*c*D*f+A*b*c*D*E+A*B*d*E*f+A*B*D*e*f<->G |
| expert | 1 | 0.000 | 0.571 | 1.000 | B*c*D*E*F+a*B*c*d*e*F+A*d*E*f+A*c*D*f+A*c*D*E+A*B*D*e*f+A*B*c*E<->G |
| opt | 1 | 0.000 | 0.800 | 1.000 | A*d*E*f+A*c*D*f+A*c*D*E+A*b*D*f+A*B*C*d*e*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 1.000 | A*d*E*f+A*D*e*F+A*c*D*e+A*b*c*D+A*B*c*E*F+A*B*C*d*f<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | A*c*D*E*F+A*C*d*E*f+A*b*c*D*f+A*B*d*E*f+A*B*D*e*f+A*B*C*D*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | a*B*c*d*e+A*E*f+A*D+A*c*E<->G |
| quantile | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 0.500 | A*E*f+A*D*f+A*D*E<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*D*e+A*b*c*E+A*B*E*f<->G |
| expert | 6 | 0.000 | 0.400 | 1.000 | 0.000 | 1.000 | B*D*E*F+a*B*c*d*e+A*E*f+A*D+A*c*E<->G |
| opt | 5 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | B*e*F+A*f+A*c*D<->G |
| opt_c6c7 | 2 | 0.000 | 0.375 | 0.750 | 0.000 | 1.000 | C*f+A*D+A*b*f+A*B*E<->G |
| opt_expert | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 0.667 | A*E*f+A*D*f+A*D*E<->G |

