# n400_noise0.0_frag0.0_fz0_rep00

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=25000
- true model: `F*D+C*e*A<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.410 | False | 0.906 | 0.455 | 6 | 0.000 | 1.000 | 0.000 | 0.805 |
| quantile | 0.950 | False | 0.000 | 0.000 | 0 | 0.100 | 0.984 | 0.031 | 0.620 |
| kde | 0.950 | False | 0.000 | 0.000 | 0 | 0.056 | 1.000 | 0.000 | 0.696 |
| expert | 0.495 | False | 0.924 | 0.361 | 6 | 0.030 | 1.000 | 0.000 | 0.807 |
| opt | 0.881 | True | 0.898 | 0.509 | 8 | 0.138 | 0.878 | 0.141 | 0.781 |
| opt_c6c7 | 0.811 | True | 0.925 | 0.500 | 8 | 0.123 | 0.887 | 0.134 | 0.632 |
| opt_expert | 0.733 | True | 0.946 | 0.501 | 12 | 0.093 | 0.967 | 0.048 | 0.671 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.273 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.273 | 0 |
| opt | 1.000 | 0.381 | 0 |
| opt_c6c7 | 1.000 | 0.381 | 0 |
| opt_expert | 1.000 | 0.545 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | a*b*D*e*F+a*B*D*E*F+a*B*C*D*F+A*b*C*D*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 2 | 1.000 | 1.000 | 1.000 | B*C*D*e*F+a*C*D*e*F+A*b*C*D*e*f+A*B*C*d*e<->G |
| opt | 1 | 1.000 | 1.000 | 0.500 | c*D*e*F+a*D*e*F+a*b*D*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | c*D*e*F+a*D*e*F+a*b*D*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | b*c*D*F+B*D*e*F+a*D*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*E*F+a*b*e*F+a*B*C*D*F+A*b*C*e<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | C*D*e*F+A*C*e<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | D*e*F+a*D*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*F<->G |

