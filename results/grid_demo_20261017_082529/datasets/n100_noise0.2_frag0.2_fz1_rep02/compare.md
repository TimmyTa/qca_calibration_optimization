# n100_noise0.2_frag0.2_fz1_rep02

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=12002
- true model: `D*a*B+f*D<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.155 | False | 0.885 | 0.333 | 2 | 0.000 | 1.000 | 0.000 | 0.542 |
| quantile | 0.227 | False | 0.887 | 0.414 | 5 | 0.045 | 0.950 | 0.063 | 0.546 |
| kde | 0.267 | False | 0.887 | 0.411 | 5 | 0.058 | 0.945 | 0.063 | 0.556 |
| expert | 0.194 | False | 0.861 | 0.244 | 1 | 0.108 | 0.860 | 0.140 | 0.558 |
| opt | 0.720 | True | 0.911 | 0.527 | 17 | 0.146 | 0.945 | 0.055 | 0.808 |
| opt_c6c7 | 0.465 | True | 0.836 | 0.506 | 8 | 0.073 | 0.850 | 0.163 | 0.544 |
| opt_expert | 0.298 | True | 0.847 | 0.547 | 7 | 0.047 | 0.918 | 0.082 | 0.547 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.118 | 0 |
| quantile | 1.000 | 0.294 | 0 |
| kde | 0.800 | 0.235 | 1 |
| expert | 1.000 | 0.077 | 0 |
| opt | 0.706 | 0.750 | 5 |
| opt_c6c7 | 0.750 | 0.462 | 2 |
| opt_expert | 0.857 | 0.400 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | A*b*D*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*f+a*B*C*D*e*f+A*b*D*e*f<->G |
| kde | 1 | 0.000 | 0.667 | 0.500 | b*c*D*E*f+a*b*c*D*e*F+A*b*D*e*f<->G |
| expert | 1 | 1.000 | 1.000 | 0.500 | A*b*c*D*e*f<->G |
| opt | 2 | 0.000 | 0.375 | 1.000 | b*D*e*f+a*c*D*e+a*C*D*f+a*B*D*e+a*B*C*E*F+A*b*c*E*f+A*b*C*e*f+A*B*c*D*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | a*b*D*f+A*b*e*f<->G |
| opt_expert | 1 | 0.000 | 0.800 | 1.000 | a*c*D*e*f+a*b*C*D*E*f+a*B*C*D*e*F+A*b*D*e*f+A*b*c*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*b*e*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*c*D*f+a*B*C*D*e*f+A*b*e*f<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*f+b*c*D*e+A*b*D*f<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*b*c*D*f<->G |
| opt | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*D*e+a*C*E*f+a*B*F+A*C*e*f+A*b*c*f+A*B*c*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*D*f+A*b*e*f<->G |
| opt_expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*e*f+b*C*D*E*f+a*B*D*e+A*b*c*e*f+A*b*C*D*f<->G |

