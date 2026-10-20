# n100_noise0.1_frag0.0_fz0_rep01

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=5001
- true model: `C*F*e+A*C*b<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.343 | False | 0.881 | 0.312 | 2 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.840 | False | 0.000 | 0.000 | 0 | 0.113 | 0.952 | 0.035 | 0.614 |
| kde | 0.730 | False | 0.000 | 0.000 | 0 | 0.060 | 1.000 | 0.000 | 0.695 |
| expert | 0.190 | False | 0.868 | 0.210 | 1 | 0.038 | 1.000 | 0.000 | 0.764 |
| opt | 0.710 | True | 0.918 | 0.500 | 6 | 0.082 | 0.965 | 0.032 | 0.845 |
| opt_c6c7 | 0.531 | False | 0.864 | 0.495 | 6 | 0.116 | 0.915 | 0.098 | 0.656 |
| opt_expert | 0.465 | True | 0.842 | 0.504 | 6 | 0.090 | 0.958 | 0.045 | 0.688 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.222 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.111 | 0 |
| opt | 0.833 | 0.500 | 1 |
| opt_c6c7 | 1.000 | 0.667 | 0 |
| opt_expert | 1.000 | 0.750 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | A*b*C*d*e*f+A*b*C*D*E*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | A*b*C*D*E*f<->G |
| opt | 1 | 0.000 | 0.833 | 1.000 | a*b*C*d*e*F+a*B*C*D*e*F+A*b*C*d*e*f+A*b*C*D*e*F+A*b*C*D*E*f+A*B*c*D*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*D*e*F+a*C*D*e*F+a*b*C*e*F+A*b*C*d*e*f+A*b*C*D*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*C*d*e*F+a*B*C*e*F+A*b*C*d*e*f+A*b*C*D*e*F+A*b*C*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | A*b*C*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.667 | A*b*C*D*f<->G |
| opt | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*e*F+B*c*D*e*f+B*C*D*e*F+A*C*D*E+A*b*C*e<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*e*F+B*C*D*F+A*C*d*e+A*C*D*E<->G |
| opt_expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e*F+B*C*e*F+A*C*D*E+A*b*C*e<->G |

