# n400_noise0.2_frag0.2_fz1_rep02

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=36002
- true model: `b*f+c*e*F+E*B*C<->G`  (irrelevant: A, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.655 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.547 |
| quantile | 0.695 | False | 0.000 | 0.000 | 0 | 0.037 | 0.975 | 0.025 | 0.546 |
| kde | 0.670 | False | 0.000 | 0.000 | 0 | 0.027 | 0.992 | 0.009 | 0.553 |
| expert | 0.490 | False | 0.000 | 0.000 | 0 | 0.096 | 0.900 | 0.100 | 0.549 |
| opt | 0.657 | True | 0.865 | 0.509 | 14 | 0.139 | 0.897 | 0.099 | 0.752 |
| opt_c6c7 | 0.392 | False | 0.916 | 0.334 | 4 | 0.063 | 0.902 | 0.091 | 0.557 |
| opt_expert | 0.331 | False | 0.905 | 0.344 | 3 | 0.062 | 0.892 | 0.100 | 0.547 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.467 | 0 |
| opt_c6c7 | 1.000 | 0.148 | 0 |
| opt_expert | 1.000 | 0.107 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 2 | 0.000 | 0.833 | 1.000 | b*c*d*e*F+b*C*d*E*f+a*b*c*f+A*b*c*D*e+A*b*C*f+A*B*C*d*E*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.333 | a*b*c*D*E*f+a*b*C*e*f+a*b*C*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.333 | a*b*c*D*E*f+a*b*C*d*E*f+a*b*C*D*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*f+b*c*e*F+b*C*f+B*C*E*F+a*c*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*e*f+b*c*D*f+b*C*d*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*E*f+b*D*e*f+b*C*d*E*f<->G |

