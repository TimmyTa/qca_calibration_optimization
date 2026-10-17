# n400_noise0.0_frag0.2_fz0_rep01

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=27001
- true model: `B*C+C*E+B*e*F<->G`  (irrelevant: A, D)
- OUT rule (same for every mode): n >= 7, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.708 | True | 0.936 | 0.749 | 14 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.565 | False | 0.846 | 0.458 | 7 | 0.107 | 0.953 | 0.027 | 0.601 |
| kde | 0.692 | True | 0.884 | 0.732 | 14 | 0.054 | 1.000 | 0.000 | 0.691 |
| expert | 0.686 | True | 0.867 | 0.699 | 13 | 0.046 | 1.000 | 0.000 | 0.776 |
| opt | 0.880 | True | 0.888 | 0.567 | 10 | 0.136 | 0.878 | 0.100 | 0.761 |
| opt_c6c7 | 0.843 | True | 0.894 | 0.546 | 11 | 0.129 | 0.873 | 0.122 | 0.632 |
| opt_expert | 0.762 | True | 0.859 | 0.665 | 16 | 0.072 | 0.977 | 0.020 | 0.677 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.667 | 0 |
| quantile | 1.000 | 0.259 | 0 |
| kde | 1.000 | 0.667 | 0 |
| expert | 1.000 | 0.619 | 0 |
| opt | 1.000 | 0.385 | 0 |
| opt_c6c7 | 1.000 | 0.407 | 0 |
| opt_expert | 1.000 | 0.615 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | C*d*E*f+a*C*E*f+a*b*C*d*E+a*B*c*d*e*F+a*B*C*D*F+A*B*C*E+A*B*C*D*f<->G |
| quantile | 2 | 1.000 | 1.000 | 0.667 | a*C*D*E*f+a*B*C*D*E+A*C*d*E*f+A*B*C*E*f+A*B*C*d*E<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | C*d*E*f+a*C*E*f+a*b*C*d*E+a*B*c*d*e*F+a*B*C*D*F+A*B*C*E+A*B*C*D*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | C*d*E*f+a*C*E*f+a*b*C*d*E+a*B*c*d*e*F+a*B*C*D*F+A*B*C*E<->G |
| opt | 1 | 1.000 | 1.000 | 0.667 | C*D*E*f+B*C*D*f+A*C*E*f+A*B*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.667 | B*C*D+A*C*D*E*f+A*B*C*E<->G |
| opt_expert | 14 | 1.000 | 1.000 | 0.667 | C*d*E*f+b*C*d*E+a*C*D*E+a*B*C*D*F+A*B*C*E+A*B*C*d*F+A*B*C*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*E+B*e*F+B*C<->G |
| quantile | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*E+a*C*E+A*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*E+B*e*F+B*C<->G |
| expert | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | C*E+B*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | C*E+B*C<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | C*E+B*C<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | C*E+B*C<->G |

