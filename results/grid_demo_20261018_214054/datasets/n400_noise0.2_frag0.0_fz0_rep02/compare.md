# n400_noise0.2_frag0.0_fz0_rep02

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=33002
- true model: `a*e+e*c*B<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.511 | False | 0.894 | 0.385 | 7 | 0.000 | 1.000 | 0.000 | 0.801 |
| quantile | 0.445 | False | 0.000 | 0.000 | 0 | 0.104 | 0.983 | 0.017 | 0.615 |
| kde | 0.530 | False | 0.000 | 0.000 | 0 | 0.056 | 1.000 | 0.000 | 0.693 |
| expert | 0.544 | False | 0.884 | 0.435 | 9 | 0.042 | 1.000 | 0.000 | 0.796 |
| opt | 0.588 | True | 0.830 | 0.501 | 14 | 0.079 | 0.953 | 0.050 | 0.776 |
| opt_c6c7 | 0.466 | False | 0.826 | 0.448 | 9 | 0.115 | 0.912 | 0.090 | 0.640 |
| opt_expert | 0.527 | False | 0.856 | 0.450 | 14 | 0.086 | 0.987 | 0.004 | 0.665 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.350 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.450 | 0 |
| opt | 1.000 | 0.700 | 0 |
| opt_c6c7 | 1.000 | 0.474 | 0 |
| opt_expert | 1.000 | 0.700 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e+a*B*D*e+A*B*c*e*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e+a*b*C*e*f+a*B*D*e+A*B*c*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*e*F+B*c*D*e+a*d*e*f+a*c*D*e*F+a*C*d*e+a*B*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e*f+a*b*d*e*f+a*b*c*D*e+a*B*C*e*f+A*B*c*d*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e+a*C*e*f+a*C*d*e+a*b*d*e*f+a*b*D*e*F+A*B*c*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | B*c*e+a*B*D*e<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | B*c*e+a*b*C*e*f+a*B*D*e<->G |
| opt | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*e*F+B*c*D*e+a*e*F+a*d*e+a*C*e<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*F+B*c*D*e+a*C*e+a*b*e<->G |
| opt_expert | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | B*c*e+a*e*F+a*d*e+a*C*e<->G |

