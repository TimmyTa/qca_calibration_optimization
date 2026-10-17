# n200_noise0.0_frag0.2_fz0_rep01

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=15001
- true model: `e*F*c+E*A*c<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.747 | True | 0.899 | 0.780 | 9 | 0.000 | 1.000 | 0.000 | 0.801 |
| quantile | 0.276 | False | 0.812 | 0.329 | 1 | 0.120 | 0.965 | 0.025 | 0.591 |
| kde | 0.317 | False | 0.805 | 0.328 | 1 | 0.072 | 1.000 | 0.000 | 0.664 |
| expert | 0.428 | False | 0.857 | 0.382 | 5 | 0.070 | 0.963 | 0.037 | 0.760 |
| opt | 0.837 | True | 0.921 | 0.584 | 8 | 0.086 | 0.953 | 0.055 | 0.765 |
| opt_c6c7 | 0.742 | True | 0.869 | 0.568 | 6 | 0.104 | 0.922 | 0.083 | 0.637 |
| opt_expert | 0.837 | True | 0.879 | 0.507 | 6 | 0.083 | 0.991 | 0.016 | 0.661 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.750 | 0 |
| quantile | 1.000 | 0.083 | 0 |
| kde | 1.000 | 0.083 | 0 |
| expert | 0.800 | 0.333 | 1 |
| opt | 1.000 | 0.667 | 0 |
| opt_c6c7 | 1.000 | 0.500 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+B*c*D*e*F+A*b*c*D*E+A*B*c*e*F+A*B*c*E*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | A*b*c*D*E*F<->G |
| kde | 1 | 1.000 | 1.000 | 0.500 | A*b*c*D*E*F<->G |
| expert | 1 | 0.000 | 0.750 | 1.000 | b*c*d*e*F+a*b*c*d*e+a*B*c*D*e*F+A*B*c*d*E*f<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+B*c*D*e*F+A*b*c*D*E*F+A*B*c*e*F+A*B*c*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+B*c*D*e*F+A*b*c*D*E*F+A*B*c*D*E*f<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+B*c*D*e*F+A*c*d*e*F+A*b*c*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*e*F+A*c*E<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | A*c*E*F<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | A*c*E*F<->G |
| expert | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*F+a*b*d*f+A*c*d*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*e*F+A*c*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*e*F+A*c*E<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | c*e*F+A*c*F<->G |

