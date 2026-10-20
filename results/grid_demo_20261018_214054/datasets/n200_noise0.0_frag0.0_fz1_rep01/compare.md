# n200_noise0.0_frag0.0_fz1_rep01

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=14001
- true model: `B*C+d*a<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.456 | False | 0.912 | 0.490 | 7 | 0.000 | 1.000 | 0.000 | 0.562 |
| quantile | 0.435 | False | 0.905 | 0.476 | 5 | 0.040 | 0.976 | 0.033 | 0.533 |
| kde | 0.500 | True | 0.923 | 0.506 | 11 | 0.053 | 0.970 | 0.033 | 0.550 |
| expert | 0.404 | False | 0.910 | 0.476 | 6 | 0.091 | 0.880 | 0.120 | 0.554 |
| opt | 0.839 | True | 0.905 | 0.638 | 18 | 0.138 | 0.910 | 0.094 | 0.749 |
| opt_c6c7 | 0.542 | True | 0.910 | 0.533 | 7 | 0.076 | 0.839 | 0.170 | 0.534 |
| opt_expert | 0.524 | True | 0.900 | 0.545 | 7 | 0.073 | 0.842 | 0.161 | 0.530 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.269 | 0 |
| quantile | 1.000 | 0.185 | 0 |
| kde | 1.000 | 0.423 | 0 |
| expert | 1.000 | 0.273 | 0 |
| opt | 1.000 | 0.750 | 0 |
| opt_c6c7 | 1.000 | 0.333 | 0 |
| opt_expert | 1.000 | 0.333 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 1.000 | 1.000 | 1.000 | a*C*d*e*f+a*b*c*d*e+a*B*d*e*F+a*B*C*d*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*e+a*B*C*d*F+a*B*C*d*e<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*d*e+a*b*c*d*F+a*b*C*d*f+a*B*C*d*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*f+a*C*d*e*f+a*B*c*d*e*F+a*B*C*E*f<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | B*C*E*F+B*C*d*e+a*b*d*F+a*b*d*e+a*b*C*d+A*B*C*e+A*B*C*d<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*d*e*f+a*b*c*d*e+a*B*C*d*E*f+a*B*C*D*e+A*B*C*d*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*C*D*e*f+a*b*d*e*f+a*b*c*d*e+a*B*C*d*e*F+A*B*C*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*d*e*F+a*b*d*e*f+a*B*C*d<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*e+a*B*C*d<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*d*f+a*d*e+a*b*c*d+a*B*C*d<->G |
| expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e*f+B*e*F+B*C*d+a*B*C<->G |
| opt | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*F+a*d*f+a*b*d+A*B*C<->G |
| opt_c6c7 | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*E+B*C*e+a*d*e<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*e+a*d*e<->G |

