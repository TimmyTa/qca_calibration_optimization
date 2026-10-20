# n100_noise0.2_frag0.0_fz1_rep01

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=10001
- true model: `e*d+A*c*E<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.915 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.557 |
| quantile | 0.970 | False | 0.000 | 0.000 | 0 | 0.058 | 0.960 | 0.043 | 0.512 |
| kde | 0.955 | False | 0.000 | 0.000 | 0 | 0.078 | 0.925 | 0.078 | 0.528 |
| expert | 0.860 | False | 0.000 | 0.000 | 0 | 0.069 | 0.912 | 0.088 | 0.545 |
| opt | 0.414 | False | 0.878 | 0.476 | 10 | 0.147 | 0.902 | 0.095 | 0.763 |
| opt_c6c7 | 0.418 | False | 0.907 | 0.245 | 4 | 0.106 | 0.855 | 0.138 | 0.582 |
| opt_expert | 0.253 | False | 0.911 | 0.303 | 2 | 0.107 | 0.872 | 0.130 | 0.577 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 0.800 | 0.400 | 2 |
| opt_c6c7 | 0.750 | 0.188 | 1 |
| opt_expert | 0.500 | 0.067 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 2 | 0.000 | 0.667 | 1.000 | B*c*d*E*F+B*C*d*e*f+a*c*d*E*F+a*b*d*e*F+A*c*D*E*f+A*B*C*d*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 0.500 | a*b*C*d*e*F+a*B*C*D*e*F+A*B*C*d*e<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | a*B*c*d*E*F+A*B*C*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*E*F+c*D*f+C*d*e*f+a*b*e+A*B*C*d*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | C*e<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*E*F+A*e<->G |

