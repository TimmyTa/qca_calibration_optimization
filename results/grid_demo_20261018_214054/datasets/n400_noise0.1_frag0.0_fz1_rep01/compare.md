# n400_noise0.1_frag0.0_fz1_rep01

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=30001
- true model: `f*E+c*D*E<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.985 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.970 | False | 0.000 | 0.000 | 0 | 0.033 | 0.995 | 0.014 | 0.546 |
| kde | 0.910 | False | 0.000 | 0.000 | 0 | 0.035 | 0.973 | 0.027 | 0.557 |
| expert | 0.875 | False | 0.000 | 0.000 | 0 | 0.047 | 0.982 | 0.018 | 0.567 |
| opt | 0.718 | True | 0.897 | 0.505 | 12 | 0.131 | 0.960 | 0.039 | 0.775 |
| opt_c6c7 | 0.508 | False | 0.911 | 0.460 | 8 | 0.086 | 0.907 | 0.101 | 0.591 |
| opt_expert | 0.434 | False | 0.919 | 0.362 | 4 | 0.084 | 0.885 | 0.117 | 0.566 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.632 | 0 |
| opt_c6c7 | 1.000 | 0.400 | 0 |
| opt_expert | 1.000 | 0.211 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*E*f+B*c*D*E+a*c*D*E*f+a*C*d*E*f+A*b*d*E*f+A*B*D*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*d*E*f+a*d*E*f+a*b*c*E*f+a*B*c*D*E*F+A*b*C*D*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+A*B*D*E*f+A*B*c*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*E*f+b*E*f+B*c*D*E+a*d*E*f+A*D*E*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*f+B*d*f+B*c*D<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*E*f+A*B*E*f<->G |

