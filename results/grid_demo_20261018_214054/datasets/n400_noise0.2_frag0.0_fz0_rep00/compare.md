# n400_noise0.2_frag0.0_fz0_rep00

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=33000
- true model: `D*f*c+A*C*E<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.345 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.795 |
| quantile | 1.000 | False | 0.000 | 0.000 | 0 | 0.108 | 0.985 | 0.022 | 0.590 |
| kde | 1.000 | False | 0.000 | 0.000 | 0 | 0.055 | 1.000 | 0.000 | 0.686 |
| expert | 0.387 | False | 0.871 | 0.263 | 4 | 0.046 | 1.000 | 0.000 | 0.771 |
| opt | 0.555 | False | 0.824 | 0.445 | 13 | 0.073 | 0.976 | 0.040 | 0.840 |
| opt_c6c7 | 0.497 | False | 0.878 | 0.292 | 6 | 0.121 | 0.952 | 0.055 | 0.674 |
| opt_expert | 0.308 | False | 0.875 | 0.169 | 2 | 0.108 | 0.909 | 0.093 | 0.663 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.250 | 0 |
| opt | 1.000 | 0.812 | 0 |
| opt_c6c7 | 1.000 | 0.400 | 0 |
| opt_expert | 1.000 | 0.125 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*B*c*D*E*f+A*b*c*D*E*f+A*B*C*d*E*f+A*B*C*D*E*F<->G |
| opt | 2 | 0.500 | 0.917 | 1.000 | b*c*D*f+a*c*D*f+A*D*E*f+A*C*E*f+A*b*C*d*E+A*B*C*D*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+A*c*D*E*f+A*b*C*d*E*F+A*B*C*d*E*f+A*B*C*D*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | b*c*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*D*E*F+a*B*c*E*f+A*b*c*D*E*f+A*B*C*d*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D*f+A*C*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*E*f+A*C*d*E+A*B*C*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | c*D*f<->G |

