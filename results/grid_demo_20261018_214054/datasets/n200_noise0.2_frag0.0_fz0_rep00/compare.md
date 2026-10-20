# n200_noise0.2_frag0.0_fz0_rep00

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=21000
- true model: `D*A+A*f*E<->G`  (irrelevant: B, C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.494 | False | 0.909 | 0.410 | 6 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.365 | False | 0.000 | 0.000 | 0 | 0.091 | 0.973 | 0.032 | 0.622 |
| kde | 0.490 | False | 0.000 | 0.000 | 0 | 0.053 | 1.000 | 0.000 | 0.694 |
| expert | 0.374 | False | 0.879 | 0.327 | 4 | 0.046 | 1.000 | 0.000 | 0.805 |
| opt | 0.635 | True | 0.879 | 0.501 | 10 | 0.104 | 0.924 | 0.082 | 0.839 |
| opt_c6c7 | 0.587 | False | 0.853 | 0.446 | 10 | 0.105 | 0.927 | 0.087 | 0.654 |
| opt_expert | 0.429 | False | 0.847 | 0.422 | 8 | 0.075 | 0.954 | 0.037 | 0.695 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.300 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.200 | 0 |
| opt | 0.900 | 0.529 | 1 |
| opt_c6c7 | 1.000 | 0.588 | 0 |
| opt_expert | 1.000 | 0.421 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | A*c*d*E*f+A*b*c*D*f+A*b*c*D*E+A*B*d*E*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | A*b*c*D*f+A*b*c*D*E+A*B*C*d*E*f<->G |
| opt | 2 | 0.000 | 0.833 | 1.000 | a*B*c*d*e*F+A*c*d*E*f+A*c*D*e*f+A*c*D*E*F+A*b*D*E*f+A*B*d*E*f<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | A*D*e*f+A*c*d*E*f+A*b*D*f+A*B*d*E*f+A*B*C*D*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | A*c*D*e*f+A*C*D*E*f+A*b*c*D*E+A*B*d*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*b*D+A*b*c*E+A*B*d*E*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*b*D+A*B*C*E*f<->G |
| opt | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d*e+B*C*E+A*D*F+A*c*d*E*f+A*c*D*e+A*b*D*E<->G |
| opt_c6c7 | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*D*e+A*c*d*E+A*b*D+A*B*d*E<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*D*f+A*b*D*E+A*B*E*f<->G |

