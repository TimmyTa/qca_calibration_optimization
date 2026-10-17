# n100_noise0.1_frag0.0_fz0_rep00

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=5000
- true model: `C*E*b+A*D<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.647 | True | 0.862 | 0.766 | 17 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.380 | False | 0.000 | 0.000 | 0 | 0.102 | 0.973 | 0.023 | 0.634 |
| kde | 0.159 | False | 0.808 | 0.309 | 2 | 0.052 | 1.000 | 0.000 | 0.705 |
| expert | 0.651 | False | 0.818 | 0.667 | 14 | 0.071 | 0.945 | 0.055 | 0.770 |
| opt | 0.796 | True | 0.903 | 0.558 | 11 | 0.112 | 0.925 | 0.087 | 0.835 |
| opt_c6c7 | 0.675 | True | 0.894 | 0.529 | 13 | 0.103 | 0.927 | 0.097 | 0.666 |
| opt_expert | 0.669 | True | 0.856 | 0.578 | 13 | 0.073 | 0.957 | 0.043 | 0.691 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.941 | 0.941 | 1 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.118 | 0 |
| expert | 1.000 | 0.875 | 0 |
| opt | 1.000 | 0.733 | 0 |
| opt_c6c7 | 1.000 | 1.000 | 0 |
| opt_expert | 1.000 | 0.929 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.875 | 1.000 | b*C*d*E*f+B*c*D*e*f+a*b*C*E*f+A*D*e*f+A*D*E*F+A*b*c*D+A*B*D*F+A*B*C*D<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*b*C*D*e*f+A*b*C*D*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*C*E*f+A*C*D+A*b*D*e*F+A*B*D*e*f+A*B*D*E*F<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | b*C*D*E*F+a*b*C*E*f+A*c*D*e*F+A*C*D*E*F+A*b*D*F+A*b*D*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*E*f+A*D*e*F+A*b*c*D+A*b*C*d*E*f+A*B*D*f<->G |
| opt_expert | 3 | 1.000 | 1.000 | 1.000 | b*C*d*E*f+a*b*C*E*f+A*c*D*e+A*b*c*D*f+A*b*C*D*F+A*B*D*e+A*B*C*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*C*E*f+B*c*e*f+A*D<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | A*b*C*D<->G |
| expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*C*E*f+A*D<->G |
| opt | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*E+a*b*C*d*f+A*D*F+A*D*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*C*E+A*D<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*C*E*f+A*D<->G |

