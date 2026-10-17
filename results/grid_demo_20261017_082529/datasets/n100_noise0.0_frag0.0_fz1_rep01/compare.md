# n100_noise0.0_frag0.0_fz1_rep01

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=2001
- true model: `E*c*A+a*f*E+e*C*F<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.279 | False | 0.830 | 0.369 | 3 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.297 | False | 0.827 | 0.371 | 3 | 0.039 | 0.970 | 0.030 | 0.537 |
| kde | 0.294 | False | 0.825 | 0.376 | 3 | 0.036 | 0.975 | 0.028 | 0.538 |
| expert | 0.320 | False | 0.843 | 0.366 | 4 | 0.075 | 0.915 | 0.085 | 0.560 |
| opt | 0.854 | True | 0.918 | 0.614 | 14 | 0.184 | 0.915 | 0.092 | 0.848 |
| opt_c6c7 | 0.310 | True | 0.807 | 0.536 | 4 | 0.059 | 0.892 | 0.112 | 0.535 |
| opt_expert | 0.331 | True | 0.813 | 0.529 | 4 | 0.051 | 0.902 | 0.092 | 0.534 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.143 | 0 |
| quantile | 1.000 | 0.158 | 0 |
| kde | 1.000 | 0.158 | 0 |
| expert | 1.000 | 0.250 | 0 |
| opt | 1.000 | 0.824 | 0 |
| opt_c6c7 | 1.000 | 0.222 | 0 |
| opt_expert | 1.000 | 0.235 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.500 | 0.333 | b*c*d*E*f+A*c*d*E*f<->G |
| quantile | 1 | 0.000 | 0.500 | 0.333 | b*c*d*E*f+A*c*d*E*f<->G |
| kde | 1 | 0.000 | 0.500 | 0.333 | b*c*d*E*f+A*c*d*E*f<->G |
| expert | 1 | 0.000 | 0.667 | 0.333 | B*c*d*E*f+A*c*d*E*f+A*B*c*d*E<->G |
| opt | 1 | 0.000 | 0.833 | 0.667 | c*d*E*f+C*d*e*F+B*C*e*F+a*d*E*f+a*C*e*F+a*B*c*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 0.667 | b*c*d*E*f+A*c*d*E*f+A*B*C*D*e*F<->G |
| opt_expert | 1 | 0.000 | 0.667 | 0.667 | b*c*d*E*f+A*c*d*E*f+A*B*C*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*E*f+A*c*d*E*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*f+A*c*d*E*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*f+A*c*d*E*f<->G |
| expert | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d*E+A*c*d*E<->G |
| opt | 11 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | c*d*E*f+C*e*F+a*C*E*f+a*B*E*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*E*f+A*c*d*E*f+A*B*C*D*F<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*E*f+A*c*d*E*f+A*B*C*D*F<->G |

