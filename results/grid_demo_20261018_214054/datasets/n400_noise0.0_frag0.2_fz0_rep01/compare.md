# n400_noise0.0_frag0.2_fz0_rep01

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=27001
- true model: `B*C+C*E+B*e*F<->G`  (irrelevant: A, D)
- OUT rule (same for every mode): n >= 7, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.681 | True | 0.936 | 0.749 | 14 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.257 | False | 0.876 | 0.212 | 1 | 0.107 | 0.953 | 0.027 | 0.601 |
| kde | 0.215 | False | 0.000 | 0.000 | 0 | 0.054 | 1.000 | 0.000 | 0.691 |
| expert | 0.609 | False | 0.908 | 0.430 | 7 | 0.046 | 1.000 | 0.000 | 0.776 |
| opt | 0.877 | True | 0.914 | 0.555 | 10 | 0.112 | 0.886 | 0.103 | 0.747 |
| opt_c6c7 | 0.845 | True | 0.890 | 0.500 | 6 | 0.125 | 0.867 | 0.113 | 0.628 |
| opt_expert | 0.637 | True | 0.896 | 0.528 | 10 | 0.097 | 0.975 | 0.020 | 0.682 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.667 | 0 |
| quantile | 1.000 | 0.037 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.333 | 0 |
| opt | 1.000 | 0.385 | 0 |
| opt_c6c7 | 1.000 | 0.222 | 0 |
| opt_expert | 1.000 | 0.385 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | C*d*E*f+a*C*E*f+a*b*C*d*E+a*B*c*d*e*F+a*B*C*D*F+A*B*C*E+A*B*C*D*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.667 | a*B*C*D*E*f<->G |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.667 | B*C*E*f+a*C*D*E*f+a*B*C*D*E+A*C*d*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 0.667 | C*D*E*f+B*C*D*f+A*C*E*f+A*B*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.667 | B*C*D*E+A*B*C*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | C*d*E*f+B*C*E*f+a*C*E*f+a*b*C*d*E+a*B*C*D*E+A*B*C*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*E+B*e*F+B*C<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*C*f<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*C*D*E+a*B*C*f+A*C*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | C*E+B*C<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | B*C*E<->G |
| opt_expert | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*C*E+A*E*f+A*C*d<->G |

