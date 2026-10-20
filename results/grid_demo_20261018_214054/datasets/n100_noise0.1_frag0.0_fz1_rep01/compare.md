# n100_noise0.1_frag0.0_fz1_rep01

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=6001
- true model: `c*A+C*E+f*B<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.360 | True | 0.903 | 0.536 | 10 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.355 | True | 0.901 | 0.527 | 10 | 0.049 | 0.928 | 0.067 | 0.535 |
| kde | 0.367 | False | 0.876 | 0.486 | 6 | 0.121 | 0.795 | 0.200 | 0.589 |
| expert | 0.319 | False | 0.918 | 0.459 | 8 | 0.040 | 0.960 | 0.040 | 0.560 |
| opt | 0.700 | True | 0.928 | 0.653 | 15 | 0.150 | 0.917 | 0.083 | 0.785 |
| opt_c6c7 | 0.537 | True | 0.925 | 0.539 | 10 | 0.109 | 0.823 | 0.183 | 0.574 |
| opt_expert | 0.569 | True | 0.918 | 0.580 | 11 | 0.095 | 0.852 | 0.152 | 0.573 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.345 | 0 |
| quantile | 1.000 | 0.312 | 0 |
| kde | 0.833 | 0.312 | 1 |
| expert | 1.000 | 0.258 | 0 |
| opt | 1.000 | 0.600 | 0 |
| opt_c6c7 | 1.000 | 0.455 | 0 |
| opt_expert | 0.909 | 0.455 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 0.833 | B*c*d*e*f+a*b*C*D*E*f+a*B*C*E*F+a*B*C*D*e*f+A*C*d*E*f+A*B*c*d*f+A*B*C*E*f<->G |
| quantile | 3 | 0.000 | 0.857 | 0.667 | B*C*D*E*F+a*b*C*D*E*f+a*B*c*d*e*f+a*B*C*E*F+a*B*C*D*e*f+A*b*d*E*f+A*B*C*E*f<->G |
| kde | 1 | 0.000 | 0.750 | 1.000 | a*B*C*D*e+A*b*c*D*E*F+A*B*D*e*f+A*B*C*D*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*f+B*c*d*e*f+a*B*C*D*E*F+A*b*c*d*E*F+A*B*d*E*f<->G |
| opt | 18 | 0.222 | 0.900 | 1.000 | a*B*c*d*e*f+a*B*C*d*E*F+a*B*C*D*e*f+A*b*d*E*F+A*b*C*d*E+A*B*c*d*E+A*B*c*D*F+A*B*c*D*e+A*B*C*d*f+A*B*C*D*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.833 | 1.000 | b*C*d*E*F+A*c*d*E*F+A*b*d*E+A*b*c*E*F+A*B*C*d*f+A*B*C*D*E*F<->G |
| opt_expert | 1 | 0.000 | 0.714 | 1.000 | b*C*d*E*F+a*B*C*D*e*F+A*c*d*E*F+A*b*d*E+A*b*c*E*F+A*B*C*d*f+A*B*C*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*E+B*d*e*f+a*B*C+A*E*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*f+C*E*f+B*C*E+a*B*C<->G |
| kde | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 0.000 | E+a*B*C+A*B*f<->G |
| expert | 3 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | C*E+B*d*e*f+A*d*f+A*b*E<->G |
| opt | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | C*E+B*e*f+A*E+A*c*D<->G |
| opt_c6c7 | 4 | 0.000 | 0.333 | 0.333 | 0.000 | 0.250 | C*E+A*E+A*B*f<->G |
| opt_expert | 4 | 0.000 | 0.250 | 0.333 | 0.000 | 0.250 | C*E+a*B*C+A*E+A*B*f<->G |

