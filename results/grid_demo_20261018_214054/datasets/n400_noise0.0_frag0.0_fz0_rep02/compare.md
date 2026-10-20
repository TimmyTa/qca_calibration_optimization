# n400_noise0.0_frag0.0_fz0_rep02

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=25002
- true model: `F*e*C+a*F<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.754 | True | 0.939 | 0.826 | 17 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.644 | True | 0.916 | 0.633 | 18 | 0.114 | 0.978 | 0.033 | 0.587 |
| kde | 0.304 | False | 0.880 | 0.322 | 2 | 0.056 | 1.000 | 0.000 | 0.688 |
| expert | 0.859 | False | 0.951 | 0.580 | 8 | 0.061 | 0.937 | 0.063 | 0.743 |
| opt | 0.928 | True | 0.912 | 0.576 | 13 | 0.115 | 0.925 | 0.092 | 0.763 |
| opt_c6c7 | 0.878 | True | 0.921 | 0.579 | 12 | 0.121 | 0.883 | 0.112 | 0.627 |
| opt_expert | 0.853 | True | 0.947 | 0.619 | 14 | 0.086 | 0.965 | 0.034 | 0.651 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.850 | 0 |
| quantile | 1.000 | 0.900 | 0 |
| kde | 1.000 | 0.100 | 0 |
| expert | 1.000 | 0.444 | 0 |
| opt | 1.000 | 0.684 | 0 |
| opt_c6c7 | 1.000 | 0.632 | 0 |
| opt_expert | 1.000 | 0.700 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | C*d*e*F+B*C*e*F+a*e*F+a*D*F+a*b*c*F+a*B*C*F<->G |
| quantile | 4 | 1.000 | 1.000 | 1.000 | C*d*e*F+a*c*F+a*b*D*F+a*B*E*F+A*C*e*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*e*F+a*B*c*D*e*F<->G |
| expert | 1 | 1.000 | 1.000 | 0.500 | a*c*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*e*F+a*e*F+a*B*D*F+a*B*c*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | C*d*e*F+a*C*E*F+a*b*d*F+a*b*C*F+A*B*C*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*C*e*F+a*D*e*F+a*c*e*F+a*c*D*F+a*B*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e*F+a*F<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*E*F+a*d*F+a*c*F+a*b*F+A*C*e*F<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*e*F+a*B*c*D*e*F<->G |
| expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | a*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e*F+a*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | e*F+a*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e*F+a*F<->G |

