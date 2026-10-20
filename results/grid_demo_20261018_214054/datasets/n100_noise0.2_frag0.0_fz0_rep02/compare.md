# n100_noise0.2_frag0.0_fz0_rep02

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=9002
- true model: `a*c*b+d*b<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.334 | False | 0.902 | 0.334 | 4 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.855 | False | 0.000 | 0.000 | 0 | 0.101 | 0.982 | 0.030 | 0.615 |
| kde | 0.665 | False | 0.000 | 0.000 | 0 | 0.060 | 1.000 | 0.000 | 0.683 |
| expert | 0.216 | False | 0.892 | 0.149 | 1 | 0.031 | 1.000 | 0.000 | 0.797 |
| opt | 0.708 | True | 0.957 | 0.502 | 12 | 0.114 | 0.933 | 0.085 | 0.860 |
| opt_c6c7 | 0.414 | False | 0.880 | 0.427 | 10 | 0.108 | 0.915 | 0.075 | 0.663 |
| opt_expert | 0.524 | False | 0.879 | 0.474 | 9 | 0.062 | 0.992 | 0.008 | 0.719 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.750 | 0.188 | 1 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.062 | 0 |
| opt | 0.667 | 0.667 | 4 |
| opt_c6c7 | 0.700 | 0.700 | 3 |
| opt_expert | 0.889 | 0.533 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 1.000 | a*b*c*E*f+a*b*C*d*E*F+a*B*c*d*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | a*b*c*D*E*f<->G |
| opt | 1 | 0.000 | 0.625 | 1.000 | a*c*d*e*f+a*b*c*D*e*F+a*b*c*D*E*f+a*b*C*d*F+a*B*d*E*f+A*b*d*e*f+A*b*c*d*e+A*B*c*d*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 1.000 | b*C*d*e*f+a*b*D*e*F+a*b*c*D*f+a*B*c*d*e*f+a*B*C*d*E*f+A*b*c*d*e<->G |
| opt_expert | 1 | 0.000 | 0.800 | 1.000 | a*c*d*e*f+a*b*c*E*f+a*b*c*D*F+a*b*C*d*F+A*b*c*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*E*F+a*b*c*E*f+a*B*c*d*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*c*D*f<->G |
| opt | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*E*f+b*C*d+a*c*d*e*f+a*b*c*D*F+a*B*d*E*f+A*d*E*F+A*b*d*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*e+a*c*d*e*f+a*b*e*F+a*b*c*f+a*B*C*E*f<->G |
| opt_expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*F+a*c*d*f+a*c*D*e*F+a*b*c*E+A*b*d*e*F<->G |

