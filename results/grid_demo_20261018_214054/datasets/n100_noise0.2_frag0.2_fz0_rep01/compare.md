# n100_noise0.2_frag0.2_fz0_rep01

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=11001
- true model: `c*B+E*A<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.329 | False | 0.898 | 0.370 | 4 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.770 | False | 0.000 | 0.000 | 0 | 0.117 | 0.942 | 0.030 | 0.581 |
| kde | 0.490 | False | 0.000 | 0.000 | 0 | 0.059 | 1.000 | 0.000 | 0.685 |
| expert | 0.381 | False | 0.887 | 0.358 | 5 | 0.058 | 1.000 | 0.000 | 0.757 |
| opt | 0.513 | True | 0.852 | 0.536 | 9 | 0.088 | 0.933 | 0.062 | 0.821 |
| opt_c6c7 | 0.459 | False | 0.820 | 0.377 | 5 | 0.118 | 0.890 | 0.122 | 0.650 |
| opt_expert | 0.355 | False | 0.857 | 0.351 | 5 | 0.097 | 0.943 | 0.052 | 0.671 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.211 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.263 | 0 |
| opt | 1.000 | 0.429 | 0 |
| opt_c6c7 | 1.000 | 0.294 | 0 |
| opt_expert | 1.000 | 0.278 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*B*c*d*e*F+A*b*C*d*E*f+A*B*c*d*e*f+A*B*C*D*E*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*B*c*d*e*F+A*b*C*d*E*f+A*B*c*d*e*f+A*B*c*D*e*F+A*B*C*D*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+B*c*d*E*f+A*b*C*d*E*f+A*B*d*E*F+A*B*c*e*F+A*B*c*d<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+A*b*C*d*E*f+A*B*c*e*f+A*B*c*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+A*b*C*d*E*f+A*B*c*d*F+A*B*C*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*f+B*c*d*e+B*C*D*E<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*f+B*c*e+B*C*D*E<->G |
| opt | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*E*f+B*c*e+A*E*f+A*B*d*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | B*c*e+A*b*C*E+A*B*c<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*E*f+B*c*e+B*C*D*E+A*B*d*F<->G |

