# n400_noise0.0_frag0.2_fz1_rep02

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=28002
- true model: `C*b+A*f*d<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.647 | True | 0.850 | 0.646 | 11 | 0.000 | 1.000 | 0.000 | 0.550 |
| quantile | 0.557 | True | 0.848 | 0.604 | 8 | 0.030 | 0.977 | 0.015 | 0.531 |
| kde | 0.442 | True | 0.832 | 0.589 | 7 | 0.042 | 0.958 | 0.035 | 0.552 |
| expert | 0.637 | False | 0.830 | 0.567 | 5 | 0.086 | 0.895 | 0.105 | 0.554 |
| opt | 0.888 | True | 0.872 | 0.616 | 16 | 0.107 | 0.966 | 0.040 | 0.739 |
| opt_c6c7 | 0.705 | True | 0.857 | 0.600 | 9 | 0.047 | 0.926 | 0.072 | 0.535 |
| opt_expert | 0.703 | True | 0.855 | 0.611 | 10 | 0.045 | 0.940 | 0.060 | 0.543 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.647 | 0 |
| quantile | 1.000 | 0.364 | 0 |
| kde | 1.000 | 0.333 | 0 |
| expert | 1.000 | 0.250 | 0 |
| opt | 1.000 | 0.762 | 0 |
| opt_c6c7 | 1.000 | 0.429 | 0 |
| opt_expert | 1.000 | 0.455 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+b*C*D*e*f+A*b*C*F+A*b*C*E+A*B*C*d*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+A*b*C*F+A*b*C*d*E+A*b*C*D*e+A*B*C*d*e*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+A*b*C*F+A*b*C*D*e+A*B*C*d*e*f<->G |
| expert | 1 | 1.000 | 1.000 | 0.500 | A*b*C*e*f+A*b*C*d<->G |
| opt | 4 | 1.000 | 1.000 | 1.000 | b*C*e*F+b*C*d*E*f+b*C*D*e+A*C*d*E*f+A*b*c*d*f+A*b*C*E+A*B*d*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+A*b*C*E+A*b*C*D+A*B*C*d*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*C*D*e*f+a*b*C*d*e*F+A*b*C*E+A*b*C*D+A*B*C*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | b*C*f+b*C*d+A*C*d*f+A*b*C<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d+A*C*e*f+A*b*C*F<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E*F+b*C*d+A*C*d*e*f+A*b*C*e<->G |
| expert | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | b*C*d*F+A*b*C*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*C+A*d*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*C+A*C*e*f<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | b*C+A*C*d*f<->G |

