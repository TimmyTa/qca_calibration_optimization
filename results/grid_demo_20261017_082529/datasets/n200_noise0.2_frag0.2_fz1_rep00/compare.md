# n200_noise0.2_frag0.2_fz1_rep00

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=24000
- true model: `B*a+E*f<->G`  (irrelevant: C, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.386 | True | 0.844 | 0.560 | 7 | 0.000 | 1.000 | 0.000 | 0.553 |
| quantile | 0.381 | True | 0.834 | 0.580 | 8 | 0.039 | 0.983 | 0.025 | 0.541 |
| kde | 0.365 | True | 0.831 | 0.570 | 7 | 0.044 | 0.968 | 0.033 | 0.543 |
| expert | 0.441 | True | 0.845 | 0.607 | 10 | 0.044 | 0.974 | 0.026 | 0.572 |
| opt | 0.743 | True | 0.844 | 0.561 | 13 | 0.127 | 0.892 | 0.112 | 0.698 |
| opt_c6c7 | 0.465 | True | 0.838 | 0.531 | 6 | 0.062 | 0.890 | 0.099 | 0.532 |
| opt_expert | 0.472 | True | 0.851 | 0.522 | 6 | 0.052 | 0.921 | 0.079 | 0.536 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.292 | 0 |
| quantile | 1.000 | 0.320 | 0 |
| kde | 1.000 | 0.280 | 0 |
| expert | 1.000 | 0.455 | 0 |
| opt | 1.000 | 0.481 | 0 |
| opt_c6c7 | 1.000 | 0.214 | 0 |
| opt_expert | 1.000 | 0.231 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*f+a*B*d*e*F+a*B*C*e*F+a*B*C*D*f+A*B*c*D*E*f<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*f+a*B*d*e*F+a*B*C*e*F+a*B*C*D*f+A*B*c*E*f<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*f+a*B*d*e*F+a*B*C*e*F+a*B*C*D*f+A*B*c*d*E*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*f+a*B*c*d*e+a*B*C*e*F+a*B*C*D*f+A*c*D*E*f+A*B*c*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*E*f+a*C*d*E*f+a*B*E*f+a*B*c*d+a*B*C*e*F+A*c*D*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+a*b*C*d*E*f+a*B*D*E*f+a*B*C*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+a*b*C*d*E*f+a*B*D*E*f+a*B*C*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*E*f+a*d*E*f+a*B*d*F+a*B*C<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*E*f+a*d*E*f+a*c*d*e*F+a*B*C<->G |
| kde | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*E*f+a*d*e*F+a*C*d*E+a*B*C*D<->G |
| expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | a*d*E*f+a*B+A*c*E*f<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*f+D*e+B*E*f+a*C*f+a*B*d<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*E*f+B*C*e*F+a*C*f<->G |
| opt_expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*E*f+B*C*e*F+a*C*d<->G |

