# n400_noise0.1_frag0.2_fz0_rep02

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=31002
- true model: `a*C+B*C*e<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.768 | True | 0.885 | 0.713 | 14 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.666 | True | 0.842 | 0.539 | 11 | 0.113 | 0.953 | 0.052 | 0.588 |
| kde | 0.711 | True | 0.832 | 0.696 | 14 | 0.057 | 1.000 | 0.000 | 0.686 |
| expert | 0.697 | True | 0.882 | 0.553 | 11 | 0.041 | 0.977 | 0.023 | 0.766 |
| opt | 0.860 | True | 0.881 | 0.507 | 10 | 0.111 | 0.909 | 0.116 | 0.736 |
| opt_c6c7 | 0.775 | True | 0.859 | 0.504 | 11 | 0.111 | 0.898 | 0.089 | 0.637 |
| opt_expert | 0.784 | True | 0.825 | 0.626 | 14 | 0.078 | 0.978 | 0.027 | 0.667 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.778 | 0 |
| quantile | 1.000 | 0.579 | 0 |
| kde | 1.000 | 0.778 | 0 |
| expert | 1.000 | 0.550 | 0 |
| opt | 1.000 | 0.500 | 0 |
| opt_c6c7 | 0.909 | 0.526 | 1 |
| opt_expert | 1.000 | 0.778 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 3 | 1.000 | 1.000 | 1.000 | B*C*d*e*f+B*C*D*e*F+a*C*d*f+a*C*d*e+a*b*C*D*E+a*B*C*f+a*B*C*d<->G |
| quantile | 4 | 1.000 | 1.000 | 1.000 | a*C*d*e*F+a*b*C*d*e+a*b*C*D*E+a*B*C*E*F+a*B*C*d*E+a*B*C*D*e*f+A*B*C*d*e*f+A*B*C*D*e*F<->G |
| kde | 3 | 1.000 | 1.000 | 1.000 | B*C*d*e*f+B*C*D*e*F+a*C*d*f+a*C*d*e+a*b*C*D*E+a*B*C*f+a*B*C*d<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*C*E*f+a*b*C*d*e+a*b*C*D*E+a*B*C*d*F+A*B*C*d*e*f+A*B*C*D*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*d*e*f+a*C*d*e+a*b*C*E*f+a*B*C*e*f+a*B*C*d<->G |
| opt_c6c7 | 1 | 0.000 | 0.750 | 1.000 | B*C*d*E*f+a*C*D*E*F+a*B*C*F+A*B*C*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*C*D*e+a*C*E*f+a*C*D*E+a*b*C*d*e+a*B*C*E+A*B*C*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*C*e+a*C<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*C*e+a*C<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*C*e+a*C<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*C*e+a*C<->G |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | B*C*d*f+a*C<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | C*d*f+B*C*e+a*C<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*C*e+a*C<->G |

