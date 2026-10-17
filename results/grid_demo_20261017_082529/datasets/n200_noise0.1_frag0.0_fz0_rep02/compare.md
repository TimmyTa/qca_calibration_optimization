# n200_noise0.1_frag0.0_fz0_rep02

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=17002
- true model: `A*b+b*F*d<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.579 | True | 0.849 | 0.690 | 12 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.516 | False | 0.832 | 0.475 | 9 | 0.110 | 0.962 | 0.028 | 0.602 |
| kde | 0.478 | False | 0.844 | 0.412 | 5 | 0.056 | 1.000 | 0.000 | 0.690 |
| expert | 0.593 | True | 0.846 | 0.654 | 15 | 0.054 | 1.000 | 0.000 | 0.747 |
| opt | 0.791 | True | 0.896 | 0.534 | 9 | 0.099 | 0.900 | 0.093 | 0.730 |
| opt_c6c7 | 0.755 | True | 0.879 | 0.526 | 9 | 0.113 | 0.894 | 0.107 | 0.630 |
| opt_expert | 0.722 | True | 0.880 | 0.534 | 10 | 0.112 | 0.905 | 0.088 | 0.646 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.632 | 0 |
| quantile | 1.000 | 0.500 | 0 |
| kde | 1.000 | 0.263 | 0 |
| expert | 1.000 | 0.789 | 0 |
| opt | 1.000 | 0.529 | 0 |
| opt_c6c7 | 1.000 | 0.529 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*c*d*E*F+a*b*d*E*F+a*b*c*d*F+A*b*d*f+A*b*D*e*F+A*b*c*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | A*b*D*e*F+A*b*c*e+A*b*c*d*F+A*b*c*D*f+A*b*C*d*f<->G |
| kde | 1 | 1.000 | 1.000 | 0.500 | A*b*c*f+A*b*c*D*e<->G |
| expert | 6 | 1.000 | 1.000 | 1.000 | b*d*E*F+a*b*d*F+A*b*d*f+A*b*D*e*F+A*b*c*f+A*b*c*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*E*F+A*b*E*f+A*b*c*f+A*b*c*D<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*E*F+A*b*E*f+A*b*c*f+A*b*c*D<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*F+A*b*E*f+A*b*c*d*e*F+A*b*c*D*f+A*b*C*d*f+A*b*C*D*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*d*E*F+a*c*d*F+A*d*f+A*b*D+A*b*c*E<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*b*f+A*b*D+A*b*c<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*f+A*b*c*D<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*d*F+A*b<->G |
| opt | 2 | 0.500 | 0.750 | 0.750 | 0.500 | 0.000 | b*d*F+A*b<->G |
| opt_c6c7 | 2 | 0.500 | 0.750 | 0.750 | 0.500 | 0.000 | b*d*F+A*b<->G |
| opt_expert | 4 | 0.250 | 0.625 | 0.625 | 0.250 | 0.500 | b*d*F+A*b<->G |

