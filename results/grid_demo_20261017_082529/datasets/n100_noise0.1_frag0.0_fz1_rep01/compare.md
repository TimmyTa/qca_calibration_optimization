# n100_noise0.1_frag0.0_fz1_rep01

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=6001
- true model: `c*A+C*E+f*B<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.545 | True | 0.845 | 0.727 | 22 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.449 | True | 0.831 | 0.688 | 23 | 0.049 | 0.928 | 0.067 | 0.535 |
| kde | 0.550 | False | 0.805 | 0.655 | 13 | 0.121 | 0.795 | 0.200 | 0.589 |
| expert | 0.448 | True | 0.832 | 0.647 | 19 | 0.040 | 0.960 | 0.040 | 0.560 |
| opt | 0.728 | True | 0.878 | 0.673 | 15 | 0.151 | 0.908 | 0.093 | 0.793 |
| opt_c6c7 | 0.579 | True | 0.822 | 0.682 | 17 | 0.100 | 0.810 | 0.188 | 0.571 |
| opt_expert | 0.587 | True | 0.822 | 0.705 | 19 | 0.077 | 0.848 | 0.157 | 0.556 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.909 | 0.690 | 2 |
| quantile | 0.826 | 0.594 | 4 |
| kde | 0.692 | 0.562 | 4 |
| expert | 0.842 | 0.516 | 3 |
| opt | 1.000 | 0.600 | 0 |
| opt_c6c7 | 0.941 | 0.667 | 1 |
| opt_expert | 0.895 | 0.708 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 6 | 0.000 | 0.818 | 1.000 | b*C*d*E*f+B*D*E*F+B*c*d*f+a*c*d*E*f+a*b*C*E*f+a*B*D*e*f+a*B*c*f+a*B*C*E*F+A*c*d*E*F+A*B*c*D*e+A*B*C*E*f<->G |
| quantile | 4 | 0.000 | 0.571 | 1.000 | B*C*D*e*f+a*c*D*E*f+a*b*D*E*f+a*b*c*D*f+a*b*C*d*e*f+a*B*c*d*e*f+a*B*C*E*F+A*c*d*E*F+A*b*d*E+A*b*c*e*F+A*b*C*E*F+A*B*D*e*f+A*B*C*E*f+A*B*C*D<->G |
| kde | 2 | 0.000 | 0.250 | 0.333 | c*D*e*f+B*C*D*e+A*b*c*D*F+A*b*C*d*e*f+A*B*D*e+A*B*C*D*F<->G |
| expert | 3 | 0.000 | 0.667 | 1.000 | b*C*d*E*f+B*c*f+a*c*d*f+a*B*D*E*F+A*c*d*E*F+A*C*d*E*f+A*B*c*D<->G |
| opt | 7 | 0.429 | 0.929 | 1.000 | B*c*d*e*f+a*B*C*d*E*F+A*C*d*E*f+A*b*d*E*F+A*B*d*f+A*B*c*E*F+A*B*c*D*e+A*B*C*D*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.714 | 0.667 | b*C*E*F+a*C*E*F+a*B*D*E*f+a*B*C*D*F+A*D*E*F+A*C*E*f+A*B*C*D*f<->G |
| opt_expert | 2 | 0.000 | 0.500 | 1.000 | a*c*d*e*f+a*C*d*E*F+a*B*c*D*E*f+a*B*C*D*e*F+A*d*E*f+A*c*E*F+A*b*d*E+A*b*c*d*f+A*b*C*E*f+A*B*D*E*F+A*B*c*d*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.600 | 1.000 | 0.000 | 1.000 | E*f+D*E+C*E+B*f+A*c<->G |
| quantile | 1 | 0.000 | 0.400 | 0.667 | 0.000 | 1.000 | d*f+c*f+C*E+B*C*D+A*c<->G |
| kde | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | d+c*f+B*C+A*c<->G |
| expert | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | d*f+D*E+B*f+A*c*F<->G |
| opt | 5 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | c*D*F+C*E+B*e*f+A*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.500 | 0.667 | 0.000 | 0.000 | C*E+B*f+a*B*e+A*E<->G |
| opt_expert | 8 | 0.000 | 0.200 | 0.333 | 0.000 | 0.500 | c*f+C*E+B*C*D+A*E+A*B*c<->G |

