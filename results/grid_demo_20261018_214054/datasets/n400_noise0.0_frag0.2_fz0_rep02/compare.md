# n400_noise0.0_frag0.2_fz0_rep02

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=27002
- true model: `A*f+B*D<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 7, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.607 | True | 0.930 | 0.681 | 12 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.589 | False | 0.922 | 0.387 | 5 | 0.106 | 0.983 | 0.036 | 0.607 |
| kde | 0.260 | False | 0.878 | 0.224 | 1 | 0.056 | 1.000 | 0.000 | 0.691 |
| expert | 0.661 | True | 0.959 | 0.585 | 11 | 0.070 | 0.982 | 0.018 | 0.741 |
| opt | 0.801 | True | 0.898 | 0.524 | 10 | 0.115 | 0.896 | 0.110 | 0.803 |
| opt_c6c7 | 0.790 | True | 0.949 | 0.515 | 8 | 0.121 | 0.904 | 0.110 | 0.642 |
| opt_expert | 0.727 | True | 0.944 | 0.529 | 10 | 0.099 | 0.945 | 0.057 | 0.670 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.545 | 0 |
| quantile | 1.000 | 0.192 | 0 |
| kde | 1.000 | 0.045 | 0 |
| expert | 1.000 | 0.458 | 0 |
| opt | 1.000 | 0.370 | 0 |
| opt_c6c7 | 1.000 | 0.320 | 0 |
| opt_expert | 1.000 | 0.400 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 3 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+B*C*D*e*F+B*C*D*E*f+a*B*c*D*e+A*c*d*e*f+A*b*d*e*f+A*B*C*D*e<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+a*B*c*D*F+A*B*C*D*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*B*C*D*e*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+a*B*D*e*F+a*B*c*D*e+A*b*d*e*f+A*B*c*d*f+A*B*C*D*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*D*E+a*B*D*e*f+a*B*D*E*F+a*B*C*D+A*B*C*e*f<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | B*C*D*e+a*B*D*e*F+A*b*d*e*f+A*B*C*e*f<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+a*B*D*e*F+a*B*c*D*e+A*c*d*e*f+A*B*D*E*f+A*B*c*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*F+B*D*E+B*c*D+A*e*f<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*D+A*D*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*D*e*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*D+A*f<->G |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | B*D+A*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*D+A*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*D+A*f<->G |

