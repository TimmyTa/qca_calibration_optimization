# n200_noise0.2_frag0.2_fz0_rep00

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=23000
- true model: `C*a*b+B*A*F<->G`  (irrelevant: D, E)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.520 | False | 0.890 | 0.481 | 6 | 0.000 | 1.000 | 0.000 | 0.805 |
| quantile | 0.319 | False | 0.892 | 0.213 | 1 | 0.101 | 0.975 | 0.033 | 0.611 |
| kde | 0.365 | False | 0.000 | 0.000 | 0 | 0.059 | 1.000 | 0.000 | 0.688 |
| expert | 0.527 | False | 0.890 | 0.429 | 5 | 0.044 | 1.000 | 0.000 | 0.769 |
| opt | 0.699 | True | 0.879 | 0.511 | 11 | 0.088 | 0.945 | 0.059 | 0.811 |
| opt_c6c7 | 0.402 | False | 0.835 | 0.420 | 6 | 0.099 | 0.924 | 0.093 | 0.665 |
| opt_expert | 0.499 | False | 0.862 | 0.418 | 5 | 0.080 | 0.986 | 0.018 | 0.685 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.375 | 0 |
| quantile | 1.000 | 0.067 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.312 | 0 |
| opt | 0.818 | 0.600 | 2 |
| opt_c6c7 | 1.000 | 0.429 | 0 |
| opt_expert | 1.000 | 0.312 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*e*F+a*b*C*D*E*F+A*B*d*E*F+A*B*c*D*e*F+A*B*C*E*F<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | A*B*c*d*E*F<->G |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*e*F+a*b*C*D*E*F+A*B*d*E*F+A*B*C*E*F<->G |
| opt | 1 | 0.000 | 0.667 | 1.000 | B*c*d*E*F+a*b*C*d*e*F+a*b*C*D*E*F+A*B*e*F+A*B*C*F+A*B*C*d*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*e*F+a*b*C*D*E*F+A*B*D*e*F+A*B*c*d*E*F+A*B*C*D*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*e*F+a*b*C*d*E*f+a*b*C*D*E*F+A*B*d*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*F+a*b*d*e*F+a*b*D*E*F+A*B*E*F<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d*E<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*d*e*F+a*b*D*E*F+A*B*E*F<->G |
| opt | 45 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | B*c*d*F+B*C*d*e*f+a*C*D*E+a*b*d*F+A*B*F<->G |
| opt_c6c7 | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*E*F+a*E*F+a*C*d*F+A*B*D*F<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*d*F+a*b*C*E+A*B*d*F<->G |

