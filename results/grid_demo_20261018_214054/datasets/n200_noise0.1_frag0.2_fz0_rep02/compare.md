# n200_noise0.1_frag0.2_fz0_rep02

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=19002
- true model: `f*b*D+F*e*b<->G`  (irrelevant: A, C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.306 | False | 0.875 | 0.359 | 3 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.860 | False | 0.000 | 0.000 | 0 | 0.104 | 0.955 | 0.042 | 0.609 |
| kde | 0.845 | False | 0.000 | 0.000 | 0 | 0.053 | 1.000 | 0.000 | 0.697 |
| expert | 0.423 | False | 0.871 | 0.278 | 3 | 0.052 | 1.000 | 0.000 | 0.791 |
| opt | 0.719 | True | 0.889 | 0.540 | 9 | 0.104 | 0.927 | 0.070 | 0.850 |
| opt_c6c7 | 0.524 | False | 0.872 | 0.485 | 9 | 0.108 | 0.927 | 0.073 | 0.663 |
| opt_expert | 0.561 | False | 0.862 | 0.499 | 8 | 0.080 | 0.948 | 0.058 | 0.690 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.214 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.214 | 0 |
| opt | 1.000 | 0.600 | 0 |
| opt_c6c7 | 1.000 | 0.818 | 0 |
| opt_expert | 1.000 | 0.615 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*e*F+A*b*c*D*E*f+A*b*C*D*e*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | b*c*d*e*F+A*b*C*D*e*F<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+b*C*D*e*F+a*b*D*f+a*b*C*e*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.833 | 1.000 | b*c*d*e*F+b*c*D*E*f+a*b*d*e*F+a*b*D*E*f+a*b*c*D*f+A*b*C*D*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*c*D*E*f+b*C*D*e*F+a*b*D*f+a*b*c*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*e*F+a*b*d*e+A*b*c*E*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*e*F+b*C*e*F<->G |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*e*F+a*b*D*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*e*F+b*D*f<->G |
| opt_expert | 6 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*e*F+b*c*D*f+a*b*D*f<->G |

