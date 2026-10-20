# n200_noise0.0_frag0.2_fz0_rep02

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=15002
- true model: `f*c+a*C+D*F<->G`  (irrelevant: B, E)
- OUT rule (same for every mode): n >= 4, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.629 | True | 0.964 | 0.769 | 23 | 0.000 | 1.000 | 0.000 | 0.792 |
| quantile | 0.538 | True | 0.917 | 0.521 | 17 | 0.124 | 0.950 | 0.051 | 0.582 |
| kde | 0.621 | True | 0.931 | 0.711 | 23 | 0.061 | 1.000 | 0.000 | 0.676 |
| expert | 0.621 | True | 0.945 | 0.727 | 23 | 0.043 | 1.000 | 0.000 | 0.747 |
| opt | 0.770 | True | 0.893 | 0.518 | 13 | 0.157 | 0.874 | 0.141 | 0.700 |
| opt_c6c7 | 0.786 | True | 0.871 | 0.530 | 12 | 0.143 | 0.862 | 0.151 | 0.629 |
| opt_expert | 0.706 | True | 0.888 | 0.538 | 12 | 0.093 | 0.935 | 0.055 | 0.647 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.657 | 0 |
| quantile | 1.000 | 0.459 | 0 |
| kde | 1.000 | 0.657 | 0 |
| expert | 1.000 | 0.657 | 0 |
| opt | 1.000 | 0.351 | 0 |
| opt_c6c7 | 1.000 | 0.343 | 0 |
| opt_expert | 1.000 | 0.316 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 14 | 0.000 | 0.702 | 1.000 | c*d*e*f+C*D*E*F+a*c*D*E*f+a*C*D*F+a*b*C*d*E*f+a*b*C*D*e+a*B*d*e*f+a*B*D*E+a*B*c*D+a*B*C*E*F+A*b*c*e*f+A*b*c*D*E<->G |
| quantile | 6 | 0.333 | 0.926 | 1.000 | C*D*E*F+B*D*E*F+a*C*D*F+a*b*C*d*e*f+a*B*c*e*f+a*B*C*D*E+A*c*D*e*f+A*b*c*e*f+A*b*c*D*E<->G |
| kde | 14 | 0.000 | 0.702 | 1.000 | c*d*e*f+C*D*E*F+a*c*D*E*f+a*C*D*F+a*b*C*d*E*f+a*b*C*D*e+a*B*d*e*f+a*B*D*E+a*B*c*D+a*B*C*E*F+A*b*c*e*f+A*b*c*D*E<->G |
| expert | 14 | 0.000 | 0.702 | 1.000 | c*d*e*f+C*D*E*F+a*c*D*E*f+a*C*D*F+a*b*C*d*E*f+a*b*C*D*e+a*B*d*e*f+a*B*D*E+a*B*c*D+a*B*C*E*F+A*b*c*e*f+A*b*c*D*E<->G |
| opt | 1 | 0.000 | 0.600 | 1.000 | b*c*D*e*f+a*D*f+a*b*C*D+a*B*c*D*e+A*b*c*D*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.750 | 1.000 | b*c*D*e*f+a*D*f+a*b*C*D+A*b*c*D*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*C*D*F+a*C*D*E+a*b*c*d*e*f+a*b*C*E*f+a*B*D*E*F+a*B*C*d*e*f+A*b*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*f+a*C<->G |
| quantile | 2 | 0.500 | 0.833 | 0.833 | 0.500 | 0.000 | D*F+c*f+a*C<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*f+a*C<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*f+a*C<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | c*D+a*D<->G |
| opt_c6c7 | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.778 | E*F+c*D*f+a*C*D<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 0.000 | D*F+a*f<->G |

