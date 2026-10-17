# n400_noise0.0_frag0.0_fz1_rep02

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=26002
- true model: `C*f+C*A+e*f<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.681 | True | 0.867 | 0.744 | 24 | 0.000 | 1.000 | 0.000 | 0.549 |
| quantile | 0.696 | True | 0.827 | 0.765 | 25 | 0.036 | 0.978 | 0.023 | 0.540 |
| kde | 0.691 | True | 0.864 | 0.729 | 23 | 0.017 | 0.997 | 0.003 | 0.548 |
| expert | 0.705 | True | 0.828 | 0.727 | 17 | 0.056 | 0.943 | 0.057 | 0.556 |
| opt | 0.855 | True | 0.866 | 0.656 | 18 | 0.112 | 0.897 | 0.105 | 0.691 |
| opt_c6c7 | 0.787 | True | 0.834 | 0.656 | 16 | 0.062 | 0.898 | 0.108 | 0.536 |
| opt_expert | 0.792 | True | 0.837 | 0.708 | 19 | 0.057 | 0.910 | 0.089 | 0.535 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.750 | 0 |
| quantile | 1.000 | 0.806 | 0 |
| kde | 1.000 | 0.719 | 0 |
| expert | 1.000 | 0.531 | 0 |
| opt | 1.000 | 0.600 | 0 |
| opt_c6c7 | 1.000 | 0.516 | 0 |
| opt_expert | 1.000 | 0.613 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 18 | 1.000 | 1.000 | 1.000 | c*e*f+a*C*D*f+a*b*C*E*f+A*d*e*f+A*C*D*E+A*b*C*D+A*B*C*e*F+A*B*C*E*f<->G |
| quantile | 6 | 1.000 | 1.000 | 1.000 | c*d*e*f+C*D*E*f+b*D*e*f+B*d*e*f+a*b*C*E*f+A*c*e*f+A*C*d*e+A*C*D*F+A*b*C*F+A*B*C*E*f<->G |
| kde | 4 | 1.000 | 1.000 | 1.000 | c*e*f+a*C*D*f+a*b*C*E*f+A*d*e*f+A*C*D*E+A*b*C*D+A*B*C*E*f+A*B*C*d*e<->G |
| expert | 14 | 1.000 | 1.000 | 1.000 | B*d*e*f+a*C*D*f+A*C*D*e*F+A*b*C*e*f+A*B*c*e*f+A*B*C*e*F+A*B*C*E*f+A*B*C*D*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | C*D*f+B*D*e*f+B*C*e*f+A*C*D+A*B*C*f+A*B*C*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | C*D*E*f+b*C*f+A*C*d*e*f+A*C*D*e*F+A*b*C<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | C*D*f+B*D*e*f+B*C*e*f+A*C*e*F+A*C*D+A*B*C*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | e*f+C*f+A*C<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | e*f+C*f+A*C<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | e*f+C*f+A*C<->G |
| expert | 1 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | d*e*f+C*f+A*e*f+A*C*e+A*C*D<->G |
| opt | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | e*f+C*f+A*C*e+A*C*D<->G |
| opt_c6c7 | 5 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | C*f+A*D*e+A*b*C<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | e*f+C*f+A*C*e+A*C*D<->G |

