# n100_noise0.2_frag0.2_fz1_rep00

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=12000
- true model: `e*a*b+B*C<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.685 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.539 |
| quantile | 0.555 | False | 0.000 | 0.000 | 0 | 0.046 | 0.958 | 0.038 | 0.551 |
| kde | 0.625 | False | 0.000 | 0.000 | 0 | 0.110 | 0.853 | 0.150 | 0.600 |
| expert | 0.665 | False | 0.000 | 0.000 | 0 | 0.051 | 0.953 | 0.047 | 0.541 |
| opt | 0.641 | True | 0.925 | 0.504 | 7 | 0.126 | 0.935 | 0.053 | 0.720 |
| opt_c6c7 | 0.397 | False | 0.911 | 0.380 | 4 | 0.088 | 0.907 | 0.088 | 0.602 |
| opt_expert | 0.366 | False | 0.899 | 0.353 | 3 | 0.079 | 0.898 | 0.093 | 0.584 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 0.714 | 0.357 | 2 |
| opt_c6c7 | 1.000 | 0.250 | 0 |
| opt_expert | 0.667 | 0.111 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 0.000 | 0.833 | 1.000 | a*b*c*d*e*F+a*b*c*D*e*f+a*B*c*D*E+a*B*C*d*E*f+A*B*C*d*e*f+A*B*C*D*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*f+a*B*C*E*f+a*B*C*D*E<->G |
| opt_expert | 1 | 0.000 | 0.667 | 1.000 | a*b*c*D*e*f+a*b*C*D*E*F+a*B*C*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 4 | 0.000 | 0.333 | 0.500 | 0.000 | 0.750 | B*D*E+B*C*d+a*b*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*E+a*b*c*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*C*E+a*b*c*f<->G |

