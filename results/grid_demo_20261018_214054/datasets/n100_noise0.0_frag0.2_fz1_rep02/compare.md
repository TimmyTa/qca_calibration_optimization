# n100_noise0.0_frag0.2_fz1_rep02

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=4002
- true model: `F*B+e*F*D+B*a<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.365 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.543 |
| quantile | 0.465 | False | 0.000 | 0.000 | 0 | 0.049 | 0.952 | 0.048 | 0.526 |
| kde | 0.460 | False | 0.000 | 0.000 | 0 | 0.072 | 0.908 | 0.092 | 0.540 |
| expert | 0.510 | False | 0.000 | 0.000 | 0 | 0.058 | 0.922 | 0.078 | 0.519 |
| opt | 0.734 | True | 0.936 | 0.508 | 9 | 0.124 | 0.905 | 0.087 | 0.710 |
| opt_c6c7 | 0.459 | True | 0.921 | 0.505 | 6 | 0.064 | 0.907 | 0.097 | 0.539 |
| opt_expert | 0.389 | True | 0.917 | 0.505 | 6 | 0.058 | 0.912 | 0.093 | 0.534 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.391 | 0 |
| opt_c6c7 | 1.000 | 0.316 | 0 |
| opt_expert | 1.000 | 0.316 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*C*D*e*F+a*B*D*e*F+a*B*C*E+a*B*C*d<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*B*D*e*F+a*B*C*E*f+a*B*C*d*f+a*B*C*d*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*B*D*e*F+a*B*C*E*f+a*B*C*d*f+a*B*C*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*D*e*F+a*B*C<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | e*F+a*B*C<->G |
| opt_expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*F+B*D*E+a*B*C*d<->G |

