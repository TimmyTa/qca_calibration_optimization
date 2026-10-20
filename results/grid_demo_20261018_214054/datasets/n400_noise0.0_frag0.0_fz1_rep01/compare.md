# n400_noise0.0_frag0.0_fz1_rep01

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=26001
- true model: `E*b+E*a<->G`  (irrelevant: C, D, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.760 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.557 |
| quantile | 0.805 | False | 0.000 | 0.000 | 0 | 0.038 | 0.988 | 0.020 | 0.530 |
| kde | 0.835 | False | 0.000 | 0.000 | 0 | 0.032 | 0.982 | 0.021 | 0.532 |
| expert | 0.550 | False | 0.000 | 0.000 | 0 | 0.097 | 0.886 | 0.114 | 0.561 |
| opt | 0.865 | True | 0.940 | 0.512 | 14 | 0.148 | 0.887 | 0.104 | 0.770 |
| opt_c6c7 | 0.530 | True | 0.939 | 0.517 | 9 | 0.072 | 0.871 | 0.129 | 0.544 |
| opt_expert | 0.439 | True | 0.942 | 0.506 | 8 | 0.058 | 0.909 | 0.095 | 0.544 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.609 | 0 |
| opt_c6c7 | 1.000 | 0.429 | 0 |
| opt_expert | 1.000 | 0.364 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 2 | 1.000 | 1.000 | 1.000 | a*c*E*F+a*B*E*F+a*B*c*D*E+A*b*E*F+A*b*D*E+A*b*c*E<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | a*c*d*E+a*B*d*E+A*b*d*E*f+A*b*C*d*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*c*d*E*F+a*b*c*D*E*f+a*B*d*E*F+a*B*c*d*E+A*b*C*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E+a*E<->G |
| opt_c6c7 | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*f+b*C*E+a*d*E<->G |
| opt_expert | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*d*E*F+b*C*E*f+a*E<->G |

