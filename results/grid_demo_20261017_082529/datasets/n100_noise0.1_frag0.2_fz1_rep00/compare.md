# n100_noise0.1_frag0.2_fz1_rep00

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=8000
- true model: `D*C+f*C*b+a*C<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.608 | True | 0.883 | 0.738 | 13 | 0.000 | 1.000 | 0.000 | 0.563 |
| quantile | 0.529 | True | 0.874 | 0.679 | 15 | 0.066 | 0.925 | 0.070 | 0.525 |
| kde | 0.557 | True | 0.864 | 0.690 | 14 | 0.050 | 0.948 | 0.043 | 0.530 |
| expert | 0.598 | False | 0.872 | 0.762 | 14 | 0.046 | 0.958 | 0.042 | 0.564 |
| opt | 0.810 | True | 0.893 | 0.654 | 11 | 0.114 | 0.938 | 0.065 | 0.727 |
| opt_c6c7 | 0.602 | True | 0.870 | 0.679 | 15 | 0.088 | 0.845 | 0.163 | 0.524 |
| opt_expert | 0.617 | True | 0.881 | 0.682 | 13 | 0.065 | 0.900 | 0.107 | 0.516 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.923 | 0.571 | 1 |
| quantile | 0.800 | 0.571 | 3 |
| kde | 0.786 | 0.478 | 3 |
| expert | 0.929 | 0.650 | 1 |
| opt | 1.000 | 0.611 | 0 |
| opt_c6c7 | 0.667 | 0.588 | 5 |
| opt_expert | 0.923 | 0.600 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.875 | 1.000 | C*D*e*f+b*C*D*e+a*C*d*e*F+a*b*D*e*f+a*b*C*d*E*f+A*C*D*e+A*b*C*e*f+A*b*C*D*f<->G |
| quantile | 1 | 0.000 | 0.571 | 0.667 | b*C*d*E+a*C*d*e*F+a*C*D*e*f+a*b*D*e*f+A*C*D*e*F+A*b*C*e+A*B*C*D*E*f<->G |
| kde | 1 | 0.000 | 0.714 | 1.000 | b*C*d*E*f+b*C*D*e+a*C*d*e*F+a*C*D*e*f+a*b*D*e*f+A*C*D*e*F+A*b*C*d<->G |
| expert | 2 | 0.000 | 0.875 | 1.000 | b*C*e*f+a*C*d*e*F+a*C*D*e*f+a*b*D*e*f+a*b*C*e+a*b*C*d*f+A*C*D*e*F+A*b*C*D<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | b*C*e*f+a*C*d*e*F+a*C*D*e*f+a*b*C*e+a*b*C*d*f+A*C*D*e*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.556 | 1.000 | b*c*d*e*f+b*C*d*e*F+b*C*d*E*f+b*C*D*e*f+a*B*C*d*e*f+a*B*C*d*E*F+A*C*d*e*F+A*C*D*E*f+A*b*C*d<->G |
| opt_expert | 1 | 0.000 | 0.857 | 1.000 | b*C*d*f+b*C*d*e+a*C*d*e*F+a*C*D*e*f+a*b*C*e+A*b*C*f+A*B*C*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | C*f+C*D*e+b*e*f+a*C*e<->G |
| quantile | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | C+b*e*f<->G |
| kde | 8 | 0.000 | 0.094 | 0.125 | 0.000 | 1.000 | C*e+C*d*f+b*e*f+A*C*d<->G |
| expert | 2 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | C*f+a*D*e*f+a*C*e+A*C*D<->G |
| opt | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | C*f+C*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | C+b*d*e*f<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | C*e+b*C<->G |

