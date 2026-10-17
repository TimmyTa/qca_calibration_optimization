# n200_noise0.2_frag0.0_fz0_rep02

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=21002
- true model: `A*b*d+E*d*b<->G`  (irrelevant: C, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.446 | False | 0.815 | 0.462 | 6 | 0.000 | 1.000 | 0.000 | 0.796 |
| quantile | 0.266 | False | 0.806 | 0.302 | 3 | 0.096 | 0.978 | 0.011 | 0.609 |
| kde | 0.335 | False | 0.000 | 0.000 | 0 | 0.047 | 1.000 | 0.000 | 0.705 |
| expert | 0.446 | False | 0.797 | 0.388 | 8 | 0.086 | 0.984 | 0.016 | 0.701 |
| opt | 0.500 | True | 0.804 | 0.502 | 9 | 0.080 | 0.965 | 0.039 | 0.765 |
| opt_c6c7 | 0.546 | False | 0.799 | 0.459 | 9 | 0.097 | 0.927 | 0.085 | 0.690 |
| opt_expert | 0.495 | False | 0.799 | 0.470 | 9 | 0.088 | 0.963 | 0.045 | 0.672 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.833 | 0.455 | 1 |
| quantile | 0.667 | 0.182 | 1 |
| kde |  | 0.000 | 0 |
| expert | 0.750 | 0.545 | 2 |
| opt | 0.667 | 0.600 | 3 |
| opt_c6c7 | 0.667 | 0.600 | 3 |
| opt_expert | 0.889 | 0.727 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.800 | 1.000 | b*C*d*E*F+a*b*d*E*F+a*b*c*d*e*f+A*b*c*d*e*F+A*b*C*d*e*f<->G |
| quantile | 1 | 0.000 | 0.500 | 0.500 | a*b*d*E*F+a*b*c*d*e*f<->G |
| kde | 0 |  |  |  | (none) |
| expert | 3 | 0.000 | 0.600 | 1.000 | b*C*d*e*f+b*C*d*E*F+a*b*c*d*f+a*b*c*d*E+A*b*c*d*e*F<->G |
| opt | 1 | 0.000 | 0.571 | 1.000 | b*C*d*e*f+b*C*d*E*F+a*b*d*e*f+a*b*d*E*F+A*b*c*d*e*F+A*b*c*d*E*f+A*b*c*D*e*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.600 | 1.000 | b*d*e*f+a*b*d*E*F+A*b*c*e*f+A*b*c*d*f+A*b*c*d*e<->G |
| opt_expert | 1 | 0.000 | 0.800 | 1.000 | b*C*d*E+a*b*d*E*F+a*b*c*d*e*f+A*b*d*e*F+A*b*C*d<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*E+a*b*c*d+A*b*d*F+A*b*C*d<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*d*E+a*b*c*d<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*F+b*C*d+a*b*d<->G |
| opt | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*F+b*C*d*f+a*b*c*d*e+A*b*e*F+A*b*d*E+A*b*D*e<->G |
| opt_c6c7 | 2 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | b*d*e*f+b*d*E*F+A*e*f+A*b*d<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*F+a*b*d*E+a*b*c*d+A*b*C*d<->G |

