# n100_noise0.0_frag0.2_fz0_rep01

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=3001
- true model: `f*B*C+a*E*C+c*A*b<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.474 | True | 0.920 | 0.619 | 8 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.340 | False | 0.000 | 0.000 | 0 | 0.104 | 0.975 | 0.055 | 0.612 |
| kde | 0.340 | False | 0.000 | 0.000 | 0 | 0.046 | 1.000 | 0.000 | 0.710 |
| expert | 0.542 | True | 0.942 | 0.566 | 9 | 0.067 | 0.965 | 0.035 | 0.756 |
| opt | 0.772 | True | 0.948 | 0.596 | 9 | 0.093 | 0.913 | 0.098 | 0.791 |
| opt_c6c7 | 0.671 | True | 0.916 | 0.519 | 8 | 0.102 | 0.935 | 0.088 | 0.675 |
| opt_expert | 0.620 | True | 0.901 | 0.550 | 8 | 0.086 | 0.933 | 0.075 | 0.679 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.421 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.500 | 0 |
| opt | 1.000 | 0.562 | 0 |
| opt_c6c7 | 1.000 | 0.500 | 0 |
| opt_expert | 1.000 | 0.471 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.667 | a*C*d*E*f+a*b*C*E*f+a*b*C*d*E+A*b*c*d*f+A*b*c*D*e<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.667 | a*b*C*E*f+A*b*c*f+A*b*c*e+A*b*c*D<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*C*d*E*f+a*B*C*E*f+a*B*C*d*E+A*b*c*e+A*b*c*d*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*C*d*E*f+a*B*C*E*f+A*b*c*e+A*b*c*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | a*C*d*E*f+a*b*C*d*E+A*b*c*e+A*b*c*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*f+b*c*D*e+a*d*f+a*b*E<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.500 | 0.333 | 0.000 | 0.000 | a*b*E*f+A*b*c<->G |
| opt | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | a*C*E+A*b*c<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 0.000 | a*C*f+A*b*c<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | a*d*E+A*b*c<->G |

