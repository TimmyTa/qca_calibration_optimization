# n100_noise0.2_frag0.2_fz1_rep01

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=12001
- true model: `E*C*A+C*b<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.542 | True | 0.838 | 0.504 | 5 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.356 | False | 0.861 | 0.398 | 2 | 0.039 | 0.977 | 0.023 | 0.538 |
| kde | 0.369 | False | 0.857 | 0.406 | 2 | 0.046 | 0.965 | 0.035 | 0.540 |
| expert | 0.446 | False | 0.847 | 0.456 | 5 | 0.068 | 0.928 | 0.072 | 0.555 |
| opt | 0.621 | True | 0.867 | 0.504 | 5 | 0.111 | 0.890 | 0.102 | 0.682 |
| opt_c6c7 | 0.330 | True | 0.813 | 0.500 | 4 | 0.061 | 0.912 | 0.093 | 0.534 |
| opt_expert | 0.402 | True | 0.825 | 0.504 | 4 | 0.057 | 0.933 | 0.062 | 0.534 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.455 | 0 |
| quantile | 1.000 | 0.167 | 0 |
| kde | 1.000 | 0.154 | 0 |
| expert | 1.000 | 0.357 | 0 |
| opt | 1.000 | 0.357 | 0 |
| opt_c6c7 | 1.000 | 0.235 | 0 |
| opt_expert | 1.000 | 0.286 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | b*C*d*E*F+a*b*C*E*F+A*b*C*D*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*E*F+A*b*C*D*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*E*F+A*b*C*D*E*f<->G |
| expert | 1 | 1.000 | 1.000 | 0.500 | b*C*d*E*F+a*b*C*E*F+A*b*C*D*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*E*F+A*b*C*d*E+A*b*C*D*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | a*b*C*E*F+A*b*C*D*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | a*b*C*E*F+A*b*C*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.750 | b*C*E+A*b*C<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*E<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*E<->G |
| expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*E+b*C*D<->G |
| opt | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | b*C<->G |
| opt_c6c7 | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D+a*C*E*F<->G |
| opt_expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E*F+A*b*C*f<->G |

