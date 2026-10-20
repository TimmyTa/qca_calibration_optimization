# n400_noise0.2_frag0.0_fz1_rep00

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=34000
- true model: `c*E+F*E<->G`  (irrelevant: A, B, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.705 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.547 |
| quantile | 0.810 | False | 0.000 | 0.000 | 0 | 0.033 | 0.995 | 0.012 | 0.523 |
| kde | 0.920 | False | 0.000 | 0.000 | 0 | 0.035 | 0.978 | 0.029 | 0.531 |
| expert | 0.920 | False | 0.000 | 0.000 | 0 | 0.081 | 0.898 | 0.102 | 0.538 |
| opt | 0.537 | False | 0.846 | 0.458 | 16 | 0.146 | 0.914 | 0.099 | 0.748 |
| opt_c6c7 | 0.334 | False | 0.886 | 0.324 | 3 | 0.094 | 0.869 | 0.133 | 0.539 |
| opt_expert | 0.320 | False | 0.894 | 0.321 | 3 | 0.087 | 0.875 | 0.135 | 0.540 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.667 | 0 |
| opt_c6c7 | 1.000 | 0.130 | 0 |
| opt_expert | 1.000 | 0.125 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | c*D*E*F+b*D*E*F+b*c*E*F+b*c*D*E+B*c*d*E*f+a*c*E+a*b*E*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*d*E*F+a*b*c*D*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*E*F+a*b*c*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*E+b*E*F+a*c*E+A*B*d<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*E+B*c*d*E*F<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d*E*F+a*b*c*D*E<->G |

