# n200_noise0.0_frag0.2_fz0_rep00

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=15000
- true model: `F*E+e*b*a+E*c*B<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.711 | True | 0.932 | 0.870 | 19 | 0.000 | 1.000 | 0.000 | 0.794 |
| quantile | 0.493 | True | 0.815 | 0.564 | 11 | 0.102 | 0.963 | 0.028 | 0.606 |
| kde | 0.621 | True | 0.861 | 0.811 | 18 | 0.046 | 1.000 | 0.000 | 0.702 |
| expert | 0.710 | True | 0.943 | 0.808 | 19 | 0.037 | 1.000 | 0.000 | 0.764 |
| opt | 0.833 | True | 0.945 | 0.581 | 12 | 0.128 | 0.950 | 0.067 | 0.810 |
| opt_c6c7 | 0.777 | True | 0.895 | 0.573 | 14 | 0.097 | 0.971 | 0.052 | 0.666 |
| opt_expert | 0.744 | True | 0.901 | 0.666 | 17 | 0.088 | 0.957 | 0.033 | 0.673 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.905 | 0 |
| quantile | 1.000 | 0.458 | 0 |
| kde | 1.000 | 0.857 | 0 |
| expert | 1.000 | 0.905 | 0 |
| opt | 1.000 | 0.500 | 0 |
| opt_c6c7 | 1.000 | 0.667 | 0 |
| opt_expert | 1.000 | 0.680 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.750 | 1.000 | b*D*E*F+B*c*d*E+B*C*E*F+a*E*F+a*b*c*d*F+a*b*c*D*e*f+a*b*C*d*e*f+a*b*C*D*F<->G |
| quantile | 1 | 0.000 | 0.833 | 1.000 | C*D*E*F+a*C*E*F+a*b*d*e*F+a*b*c*D*e*f+a*b*C*F+A*B*c*d*E*F<->G |
| kde | 1 | 0.000 | 0.750 | 1.000 | b*D*E*F+B*C*E*F+a*E*F+a*b*c*d*F+a*b*c*D*e*f+a*b*C*d*e*f+a*b*C*D*F+A*B*c*d*E<->G |
| expert | 1 | 0.000 | 0.750 | 1.000 | b*D*E*F+B*c*d*E+B*C*E*F+a*E*F+a*b*c*d*F+a*b*c*D*e*f+a*b*C*d*e*f+a*b*C*D*F<->G |
| opt | 1 | 0.000 | 0.800 | 0.667 | b*C*D*E*F+B*c*d*E+a*d*E*F+a*c*E*F+a*b*c*d*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.833 | 0.667 | b*D*E*F+B*c*d*E+a*d*E*F+a*c*E*F+a*b*c*d*F+A*C*D*E*F<->G |
| opt_expert | 1 | 0.000 | 0.714 | 1.000 | C*D*E*F+b*D*E*F+B*c*d*E+a*E*F+a*b*c*d*F+a*b*c*D*e*f+a*b*C*D*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | E*F+B*c*E+a*b*e<->G |
| quantile | 2 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | C*D*E*F+a*C*E*F+a*b*e+A*c*d*F<->G |
| kde | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 0.000 | E*F+a*b*e+A*B*c*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | E*F+B*c*E+a*b*e<->G |
| opt | 2 | 0.000 | 0.667 | 0.667 | 0.000 | 0.500 | E*F+B*c*E+a*b*c*F<->G |
| opt_c6c7 | 2 | 0.000 | 0.667 | 0.667 | 0.000 | 0.500 | E*F+B*c*E+a*b*F<->G |
| opt_expert | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | E*F+B*c*d*E+a*b*e<->G |

