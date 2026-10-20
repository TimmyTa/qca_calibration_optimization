# n100_noise0.1_frag0.2_fz0_rep02

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=7002
- true model: `b*C+E*d*A<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.545 | True | 0.919 | 0.648 | 10 | 0.000 | 1.000 | 0.000 | 0.805 |
| quantile | 0.427 | False | 0.924 | 0.360 | 4 | 0.123 | 0.932 | 0.055 | 0.569 |
| kde | 0.451 | True | 0.884 | 0.532 | 6 | 0.060 | 1.000 | 0.000 | 0.686 |
| expert | 0.541 | True | 0.913 | 0.545 | 10 | 0.089 | 1.000 | 0.000 | 0.745 |
| opt | 0.730 | True | 0.913 | 0.550 | 7 | 0.115 | 0.928 | 0.060 | 0.791 |
| opt_c6c7 | 0.696 | True | 0.869 | 0.534 | 6 | 0.111 | 0.925 | 0.078 | 0.648 |
| opt_expert | 0.658 | True | 0.885 | 0.532 | 7 | 0.086 | 0.960 | 0.038 | 0.650 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.900 | 0.500 | 1 |
| quantile | 1.000 | 0.250 | 0 |
| kde | 1.000 | 0.333 | 0 |
| expert | 1.000 | 0.556 | 0 |
| opt | 1.000 | 0.438 | 0 |
| opt_c6c7 | 1.000 | 0.429 | 0 |
| opt_expert | 1.000 | 0.412 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.857 | 1.000 | a*b*C*d*F+a*b*C*D*e*f+A*C*d*E*F+A*b*d*E*F+A*b*c*E*f+A*b*C*E*F+A*b*C*d*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | A*C*d*E*F+A*b*c*d*E*f+A*b*C*E*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*F+A*C*d*E*F+A*b*c*d*E+A*b*C*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*C*d*F+a*b*C*D*e*f+A*C*d*E*F+A*b*c*d*E+A*b*C*E*F+A*b*C*d*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E+A*C*d*E*F+A*b*d*E*f+A*b*C*E*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E+a*b*C*E*F+A*b*d*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E+A*b*d*E+A*b*C*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | b*C*D+a*b*C*F+A*d*E+A*C*e*f+A*b*E*f<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E+A*C*E*F<->G |
| kde | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | b*C*E+A*d*E<->G |
| expert | 9 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | C*D*e+b*d*E+b*C*F+A*C*d<->G |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*f+b*C*E*F+A*C*d*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*F+b*d*E<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | b*d*E+b*C<->G |

