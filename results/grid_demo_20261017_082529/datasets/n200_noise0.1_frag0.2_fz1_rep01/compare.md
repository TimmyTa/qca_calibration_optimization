# n200_noise0.1_frag0.2_fz1_rep01

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=20001
- true model: `E*c+E*d+C*B<->G`  (irrelevant: A, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.566 | True | 0.828 | 0.714 | 17 | 0.000 | 1.000 | 0.000 | 0.552 |
| quantile | 0.562 | False | 0.798 | 0.749 | 20 | 0.044 | 0.940 | 0.054 | 0.510 |
| kde | 0.545 | True | 0.814 | 0.736 | 19 | 0.031 | 0.973 | 0.030 | 0.518 |
| expert | 0.521 | False | 0.799 | 0.709 | 15 | 0.089 | 0.922 | 0.077 | 0.555 |
| opt | 0.731 | True | 0.841 | 0.633 | 16 | 0.103 | 0.904 | 0.095 | 0.665 |
| opt_c6c7 | 0.636 | True | 0.802 | 0.751 | 18 | 0.058 | 0.896 | 0.097 | 0.508 |
| opt_expert | 0.643 | True | 0.809 | 0.760 | 19 | 0.051 | 0.916 | 0.083 | 0.513 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.941 | 0.593 | 1 |
| quantile | 0.950 | 0.559 | 1 |
| kde | 0.947 | 0.600 | 1 |
| expert | 0.867 | 0.433 | 2 |
| opt | 1.000 | 0.500 | 0 |
| opt_c6c7 | 1.000 | 0.581 | 0 |
| opt_expert | 1.000 | 0.613 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.875 | 1.000 | b*c*D*E+B*C*D*e*f+a*B*c*d*E*f+a*B*C*D*F+A*d*E*F+A*c*D*E*f+A*b*E*F+A*B*C*d*e<->G |
| quantile | 2 | 0.000 | 0.875 | 0.667 | c*D*E*f+B*C*D*e*F+a*B*c*E*f+a*B*C*E*F+a*B*C*D*e+A*c*E*F+A*b*E*F+A*B*C*d<->G |
| kde | 2 | 0.000 | 0.875 | 0.667 | c*D*E*f+a*B*c*E*f+a*B*C*e*F+a*B*C*D*F+a*B*C*D*e+A*c*E*F+A*b*E*F+A*B*C*d<->G |
| expert | 1 | 0.000 | 0.750 | 1.000 | C*d*E*F+B*C*E*F+a*b*c*D*E*f+a*B*C*D*e+A*b*E*F+A*b*C*D*E+A*B*c*D*E*f+A*B*C*d*e*f<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | b*c*D*E*F+B*d*E*F+B*c*D*E*f+a*B*C*D*e+A*d*E*F+A*c*E*F+A*B*C*e*F+A*B*C*d*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*E*f+B*C*d*F+a*B*C*E*F+a*B*C*D*e*f+A*d*E*F+A*c*D*E+A*B*C*e*F+A*B*C*d*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*E*f+B*C*e*F+a*B*C*F+a*B*C*D*e+A*d*E*F+A*c*D*E+A*B*C*d*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | c*E+B*C+A*E*F<->G |
| quantile | 4 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | c*E+B*C*F+a*C*D*e+A*E*F+A*B*C*d<->G |
| kde | 3 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | E*F+c*E+a*B*F+a*B*C*D+A*B*C*d<->G |
| expert | 4 | 0.000 | 0.400 | 0.667 | 0.000 | 1.000 | d*E+c*E+B*C*D+A*E+A*B*f<->G |
| opt | 2 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | d*E+c*E+B*C*D*e+A*B*C<->G |
| opt_c6c7 | 6 | 0.000 | 0.400 | 0.667 | 0.000 | 1.000 | d*E+c*E+B*C*F+B*C*d+a*B*D<->G |
| opt_expert | 4 | 0.000 | 0.300 | 0.500 | 0.000 | 1.000 | E*F+c*E+B*C*F+B*C*d+a*B*D<->G |

