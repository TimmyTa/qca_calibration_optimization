# n200_noise0.0_frag0.0_fz1_rep02

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=14002
- true model: `d*E+E*A<->G`  (irrelevant: B, C, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.365 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.350 | False | 0.000 | 0.000 | 0 | 0.048 | 0.965 | 0.035 | 0.551 |
| kde | 0.575 | False | 0.000 | 0.000 | 0 | 0.059 | 0.955 | 0.051 | 0.557 |
| expert | 0.595 | False | 0.000 | 0.000 | 0 | 0.043 | 0.993 | 0.007 | 0.560 |
| opt | 0.828 | True | 0.941 | 0.570 | 12 | 0.173 | 0.889 | 0.112 | 0.782 |
| opt_c6c7 | 0.405 | True | 0.916 | 0.538 | 8 | 0.089 | 0.893 | 0.115 | 0.550 |
| opt_expert | 0.374 | True | 0.916 | 0.553 | 7 | 0.062 | 0.917 | 0.093 | 0.547 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.571 | 0 |
| opt_c6c7 | 1.000 | 0.381 | 0 |
| opt_expert | 1.000 | 0.318 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | c*d*E*F+b*c*d*E+a*d*E*F+A*b*E*F+A*b*C*D*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | c*d*E*F+b*c*d*E+a*B*d*E*F+A*b*c*E*f<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | a*C*d*E*f+a*b*d*E*f+A*c*d*E*f+A*b*C*D*E*f+A*B*C*d*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E+A*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*E+B*d*E*F<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*E*F+c*d*E+b*D*E*f+a*d*E<->G |

