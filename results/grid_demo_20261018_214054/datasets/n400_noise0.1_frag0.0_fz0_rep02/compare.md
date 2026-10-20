# n400_noise0.1_frag0.0_fz0_rep02

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=29002
- true model: `d*b*c+A*E<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.457 | False | 0.909 | 0.401 | 6 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.920 | False | 0.000 | 0.000 | 0 | 0.102 | 0.979 | 0.009 | 0.598 |
| kde | 0.860 | False | 0.000 | 0.000 | 0 | 0.050 | 1.000 | 0.000 | 0.698 |
| expert | 0.500 | False | 0.906 | 0.363 | 6 | 0.048 | 1.000 | 0.000 | 0.751 |
| opt | 0.850 | True | 0.905 | 0.517 | 11 | 0.104 | 0.920 | 0.075 | 0.834 |
| opt_c6c7 | 0.718 | True | 0.911 | 0.500 | 11 | 0.102 | 0.936 | 0.059 | 0.667 |
| opt_expert | 0.538 | False | 0.847 | 0.440 | 11 | 0.092 | 0.944 | 0.051 | 0.670 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.273 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.273 | 0 |
| opt | 1.000 | 0.524 | 0 |
| opt_c6c7 | 1.000 | 0.524 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | A*b*c*D*E*F+A*b*C*D*E*f+A*B*d*E*f+A*B*c*E*f+A*B*C*D*E*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | A*c*d*E*f+A*b*c*D*E*F+A*b*C*D*E*f+A*B*d*E*f+A*B*C*D*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*c*d*E*f+A*c*D*E+A*b*c*d*f+A*B*E*f+A*B*c*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*d*e*f+a*b*c*d*f+A*D*E*f+A*b*c*D*E+A*B*E*f+A*B*C*D*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*E*F+A*D*E*F+A*C*E*f+A*B*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*D*E*F+A*C*D*E+A*B*E*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*d*E*f+A*D*E*F+A*C*D*E<->G |
| opt | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 0.000 | b*c*d*E+A*E+A*b*c*d<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*c*d+A*D*E+A*B*E*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*E+A*E*f+A*D*E+A*B*E<->G |

