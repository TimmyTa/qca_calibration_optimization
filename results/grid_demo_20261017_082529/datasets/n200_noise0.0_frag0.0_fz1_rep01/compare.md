# n200_noise0.0_frag0.0_fz1_rep01

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=14001
- true model: `B*C+d*a<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.708 | True | 0.881 | 0.764 | 23 | 0.000 | 1.000 | 0.000 | 0.562 |
| quantile | 0.682 | True | 0.857 | 0.760 | 23 | 0.040 | 0.976 | 0.033 | 0.533 |
| kde | 0.606 | True | 0.834 | 0.764 | 29 | 0.053 | 0.970 | 0.033 | 0.550 |
| expert | 0.623 | False | 0.846 | 0.720 | 16 | 0.091 | 0.880 | 0.120 | 0.554 |
| opt | 0.858 | True | 0.867 | 0.700 | 20 | 0.120 | 0.926 | 0.078 | 0.714 |
| opt_c6c7 | 0.681 | True | 0.827 | 0.731 | 21 | 0.058 | 0.900 | 0.102 | 0.530 |
| opt_expert | 0.689 | True | 0.850 | 0.734 | 24 | 0.044 | 0.919 | 0.081 | 0.526 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.885 | 0 |
| quantile | 1.000 | 0.852 | 0 |
| kde | 0.793 | 0.885 | 6 |
| expert | 0.938 | 0.682 | 1 |
| opt | 1.000 | 0.800 | 0 |
| opt_c6c7 | 0.952 | 0.833 | 1 |
| opt_expert | 1.000 | 0.857 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | a*d*F+a*d*e+a*b*d+a*B*C*D*E+A*B*C*f+A*B*C*e+A*B*C*d<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | B*C*D*f+a*d*F+a*d*e+a*b*C*d+a*B*C*D*E+A*B*C*e+A*B*C*d<->G |
| kde | 2 | 0.000 | 0.556 | 1.000 | C*d*e*f+b*c*d*e+B*C*D*E+a*d*F+a*d*e+a*b*e*f+a*b*C*e+a*b*C*d+A*B*C<->G |
| expert | 1 | 0.000 | 0.833 | 1.000 | B*C*E*f+a*d*f+a*c*d*e+a*b*c*d+a*b*C*D*e*F+A*B*C*D*f<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | B*C*E*F+B*C*d*e+a*d*e*F+a*b*d*F+a*b*d*e+a*b*C*d+a*B*C*D*E+A*B*C*e+A*B*C*d<->G |
| opt_c6c7 | 1 | 0.000 | 0.857 | 1.000 | B*C*E*f+B*C*d*e*F+a*d*f+a*b*d+a*b*C*e*F+a*B*C*E+A*B*C*D*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*C*f+B*C*d*e+a*d*f+a*d*E+a*b*d+a*B*C<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*C+a*d<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*C+a*d<->G |
| kde | 3 | 0.000 | 0.333 | 1.000 | 0.000 | 1.000 | C*d*e*f+b*c*d*e+B*C+a*e*f+a*d+a*C*e<->G |
| expert | 2 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | C*D*e*F+B*C+a*d<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*E+a*d*e+a*b*d+A*B*C<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | C*e*F+B*C+a*d<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*C+a*d<->G |

