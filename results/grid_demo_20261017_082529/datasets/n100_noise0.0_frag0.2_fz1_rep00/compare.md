# n100_noise0.0_frag0.2_fz1_rep00

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=4000
- true model: `c*E+D*e+C*B<->G`  (irrelevant: A, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.628 | True | 0.892 | 0.759 | 27 | 0.000 | 1.000 | 0.000 | 0.551 |
| quantile | 0.603 | True | 0.879 | 0.726 | 29 | 0.065 | 0.935 | 0.057 | 0.520 |
| kde | 0.616 | False | 0.906 | 0.709 | 17 | 0.129 | 0.845 | 0.155 | 0.601 |
| expert | 0.601 | True | 0.862 | 0.748 | 30 | 0.083 | 0.932 | 0.068 | 0.579 |
| opt | 0.723 | True | 0.902 | 0.748 | 25 | 0.136 | 0.842 | 0.152 | 0.679 |
| opt_c6c7 | 0.686 | True | 0.897 | 0.706 | 22 | 0.100 | 0.840 | 0.160 | 0.531 |
| opt_expert | 0.704 | True | 0.895 | 0.705 | 22 | 0.100 | 0.838 | 0.167 | 0.537 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.889 | 0.686 | 3 |
| quantile | 0.793 | 0.657 | 6 |
| kde | 0.824 | 0.500 | 3 |
| expert | 0.767 | 0.767 | 7 |
| opt | 0.840 | 0.750 | 4 |
| opt_c6c7 | 0.773 | 0.607 | 5 |
| opt_expert | 0.773 | 0.630 | 5 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 16 | 0.000 | 0.625 | 1.000 | b*c*D*E*f+b*C*D*e*f+B*c*D*e+B*C*d*e+a*d*E*F+a*D*e*F+a*b*C*d*E+a*B*c*E*F+A*B*d*e*F+A*B*d*E*f+A*B*D*e*f+A*B*C*E*F<->G |
| quantile | 1 | 0.000 | 0.538 | 1.000 | c*D*E*F+b*c*D*E+b*C*D*e+B*c*D*e*f+a*d*E*F+a*b*C*E*f+a*B*D*e*F+a*B*C*d*e*f+A*b*D*F+A*b*C*e*f+A*B*d*E*f+A*B*c*d*e*F+A*B*C*E*F<->G |
| kde | 1 | 0.000 | 0.200 | 0.333 | c*D*f+B*d*E*f+a*c*f+a*b*D*e*f+A*B*c*d*e*F<->G |
| expert | 4 | 0.000 | 0.458 | 1.000 | b*D*e*F+B*c*D*e*f+a*d*E*F+a*b*d*e*f+a*b*C*e+a*b*C*d+a*B*c*E*F+A*c*d*E*f+A*C*e*f+A*b*c*D+A*B*c*e*F+A*B*C*d<->G |
| opt | 1 | 0.000 | 0.300 | 0.667 | D*E*F+B*c*D+a*c*E*F+a*b*C*D*F+a*b*C*D*E+a*B*E*F+A*c*D*E+A*B*D*F+A*B*c*F+A*B*C*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.375 | 1.000 | b*D*F+B*c*E*F+a*b*E*F+a*b*D*E+a*B*c*D*e+A*B*c*d*F+A*B*c*D*f+A*B*C*d*E*f<->G |
| opt_expert | 1 | 0.000 | 0.375 | 1.000 | b*D*F+B*c*E*F+a*b*E*F+a*b*D*E+a*B*c*D*e+A*B*c*d*F+A*B*c*D*f+A*B*C*d*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | F+E+D+B*C<->G |
| quantile | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | F+E+D+C<->G |
| kde | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | F+E+D+a<->G |
| expert | 1 | 0.000 | 0.600 | 1.000 | 0.000 | 1.000 | F+E+D+C+a<->G |
| opt | 4 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | F+C+a*B+A*D<->G |
| opt_c6c7 | 2 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | F+E+D<->G |
| opt_expert | 7 | 0.143 | 0.667 | 0.667 | 0.000 | 0.857 | E+D+B<->G |

