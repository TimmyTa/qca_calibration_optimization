# n200_noise0.0_frag0.2_fz0_rep01

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=15001
- true model: `e*F*c+E*A*c<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.608 | True | 0.913 | 0.514 | 4 | 0.000 | 1.000 | 0.000 | 0.801 |
| quantile | 0.910 | False | 0.000 | 0.000 | 0 | 0.120 | 0.965 | 0.025 | 0.591 |
| kde | 0.965 | False | 0.000 | 0.000 | 0 | 0.072 | 1.000 | 0.000 | 0.664 |
| expert | 0.491 | False | 0.937 | 0.280 | 3 | 0.070 | 0.963 | 0.037 | 0.760 |
| opt | 0.828 | True | 0.971 | 0.580 | 8 | 0.082 | 0.958 | 0.042 | 0.858 |
| opt_c6c7 | 0.595 | True | 0.893 | 0.516 | 7 | 0.120 | 0.953 | 0.073 | 0.649 |
| opt_expert | 0.567 | False | 0.891 | 0.495 | 5 | 0.087 | 0.991 | 0.009 | 0.662 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.333 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.250 | 0 |
| opt | 1.000 | 0.667 | 0 |
| opt_c6c7 | 1.000 | 0.500 | 0 |
| opt_expert | 1.000 | 0.417 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+A*b*c*D*E*F+A*B*c*D*e*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | b*c*d*e*F+a*B*c*D*e*F<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+B*c*D*e*F+A*b*c*D*E*F+A*B*c*e*F+A*B*c*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+B*c*D*e*F+A*b*c*D*E+A*B*c*d*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+B*c*D*e*F+A*b*c*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*e*F+A*c*D*F<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | c*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*e*F+A*c*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*d*e*F+B*e*F+A*c*E<->G |
| opt_expert | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*F+b*c*e*F+A*c*E*F<->G |

