# n100_noise0.0_frag0.2_fz1_rep02

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=4002
- true model: `F*B+e*F*D+B*a<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.489 | True | 0.878 | 0.712 | 13 | 0.000 | 1.000 | 0.000 | 0.543 |
| quantile | 0.478 | True | 0.896 | 0.649 | 9 | 0.049 | 0.952 | 0.048 | 0.526 |
| kde | 0.378 | False | 0.879 | 0.622 | 9 | 0.072 | 0.908 | 0.092 | 0.540 |
| expert | 0.437 | True | 0.864 | 0.638 | 7 | 0.058 | 0.922 | 0.078 | 0.519 |
| opt | 0.761 | True | 0.934 | 0.574 | 12 | 0.137 | 0.927 | 0.080 | 0.751 |
| opt_c6c7 | 0.586 | True | 0.870 | 0.670 | 10 | 0.050 | 0.920 | 0.070 | 0.533 |
| opt_expert | 0.609 | True | 0.892 | 0.656 | 10 | 0.056 | 0.932 | 0.067 | 0.534 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.684 | 0 |
| quantile | 1.000 | 0.429 | 0 |
| kde | 0.889 | 0.500 | 1 |
| expert | 1.000 | 0.318 | 0 |
| opt | 1.000 | 0.667 | 0 |
| opt_c6c7 | 1.000 | 0.625 | 0 |
| opt_expert | 1.000 | 0.588 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | B*c*d*E*F+a*B*e*F+a*B*d*e+a*B*C*E*f+a*B*C*d+A*b*C*D*e*F+A*B*C*D*E*F<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | B*C*d*E*F+a*B*D*e*F+a*B*C*E*f+a*B*C*d*f+A*b*C*D*e*F+A*B*C*E*F<->G |
| kde | 1 | 0.000 | 0.833 | 1.000 | B*c*D*e*F+a*B*C*d*E*f+A*C*D*e*F+A*B*D*F+A*B*C*E*F+A*B*C*D*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*B*c*D*e*F+a*B*C*e*f+a*B*C*d*E*F+a*B*C*D*f+A*b*C*D*e*F+A*B*c*d*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*F+a*B*e*F+a*B*d*F+a*B*d*e+a*B*C*d+A*b*D*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*F+a*B*d*e*f+a*B*D*e*F+a*B*C*E*f+A*b*C*D*e*F+A*B*c*d*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*F+a*B*d*e*f+a*B*D*e*F+a*B*C*E*f+A*b*C*D*e*F+A*B*c*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | C*D*e*F+B*E*F+a*B<->G |
| quantile | 4 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | C*D*e*F+B*C*F+a*B<->G |
| kde | 4 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | C*D*e*F+B*D*F+B*C*F+B*C*D+a*B<->G |
| expert | 3 | 0.000 | 0.222 | 0.222 | 0.000 | 1.000 | B*D*F+a*B*C+A*e*F<->G |
| opt | 6 | 0.000 | 0.333 | 0.333 | 0.000 | 0.667 | b*D*e+B*C*F+a*B<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 0.000 | D*e*F+B*d*F+a*B*f<->G |
| opt_expert | 3 | 0.333 | 0.778 | 0.778 | 0.333 | 0.333 | C*D*e+B*F+a*B<->G |

