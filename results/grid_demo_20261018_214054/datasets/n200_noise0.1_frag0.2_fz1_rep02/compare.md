# n200_noise0.1_frag0.2_fz1_rep02

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=20002
- true model: `d*f+e*F*D<->G`  (irrelevant: A, B, C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.850 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 0.845 | False | 0.000 | 0.000 | 0 | 0.039 | 0.978 | 0.029 | 0.524 |
| kde | 0.780 | False | 0.000 | 0.000 | 0 | 0.067 | 0.929 | 0.072 | 0.549 |
| expert | 0.700 | False | 0.000 | 0.000 | 0 | 0.126 | 0.841 | 0.159 | 0.580 |
| opt | 0.758 | True | 0.936 | 0.502 | 12 | 0.128 | 0.957 | 0.046 | 0.752 |
| opt_c6c7 | 0.462 | False | 0.937 | 0.374 | 4 | 0.066 | 0.889 | 0.107 | 0.533 |
| opt_expert | 0.449 | False | 0.933 | 0.357 | 3 | 0.072 | 0.887 | 0.117 | 0.558 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.571 | 0 |
| opt_c6c7 | 1.000 | 0.182 | 0 |
| opt_expert | 1.000 | 0.143 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*D*e*F+a*c*d*E*f+a*b*C*d*e*f+A*C*d*E*f+A*B*d*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | a*B*c*d*E*f+A*B*d*e*f+A*B*C*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | a*B*c*d*E*f+A*B*c*d*e*f+A*B*C*d*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*E*f+B*d*f+B*D*e*F+a*d*f<->G |
| opt_c6c7 | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*E*f+B*d*e*f+a*c*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e*f+a*B*c*d*f+A*C*d<->G |

