# n400_noise0.2_frag0.0_fz1_rep02

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=34002
- true model: `b*E*a+F*b*A<->G`  (irrelevant: C, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.980 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.556 |
| quantile | 0.985 | False | 0.000 | 0.000 | 0 | 0.031 | 0.980 | 0.015 | 0.533 |
| kde | 0.985 | False | 0.000 | 0.000 | 0 | 0.029 | 0.980 | 0.014 | 0.535 |
| expert | 0.980 | False | 0.000 | 0.000 | 0 | 0.020 | 0.995 | 0.005 | 0.550 |
| opt | 0.447 | False | 0.894 | 0.377 | 6 | 0.125 | 0.897 | 0.108 | 0.703 |
| opt_c6c7 | 0.360 | False | 0.902 | 0.286 | 3 | 0.074 | 0.896 | 0.107 | 0.574 |
| opt_expert | 0.303 | False | 0.916 | 0.288 | 2 | 0.081 | 0.876 | 0.123 | 0.560 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.400 | 0 |
| opt_c6c7 | 1.000 | 0.200 | 0 |
| opt_expert | 1.000 | 0.125 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 0.000 | 0.667 | 1.000 | b*C*d*E*F+a*b*d*E*f+A*b*c*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | b*c*D*E*F+a*b*C*d*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*F+A*b*c*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*d*E+A*b*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E+b*D*E<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*E+a*b*C*E<->G |

