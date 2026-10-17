# n100_noise0.2_frag0.2_fz1_rep00

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=12000
- true model: `e*a*b+B*C<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.263 | False | 0.869 | 0.446 | 3 | 0.000 | 1.000 | 0.000 | 0.539 |
| quantile | 0.268 | False | 0.866 | 0.493 | 4 | 0.046 | 0.958 | 0.038 | 0.551 |
| kde | 0.346 | False | 0.819 | 0.485 | 4 | 0.110 | 0.853 | 0.150 | 0.600 |
| expert | 0.318 | True | 0.853 | 0.507 | 5 | 0.051 | 0.953 | 0.047 | 0.541 |
| opt | 0.633 | True | 0.893 | 0.511 | 7 | 0.151 | 0.920 | 0.077 | 0.740 |
| opt_c6c7 | 0.480 | True | 0.839 | 0.571 | 7 | 0.068 | 0.897 | 0.098 | 0.581 |
| opt_expert | 0.493 | True | 0.836 | 0.589 | 7 | 0.068 | 0.892 | 0.103 | 0.574 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.176 | 0 |
| quantile | 1.000 | 0.211 | 0 |
| kde | 1.000 | 0.286 | 0 |
| expert | 1.000 | 0.312 | 0 |
| opt | 0.714 | 0.417 | 2 |
| opt_c6c7 | 1.000 | 0.467 | 0 |
| opt_expert | 1.000 | 0.467 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*f+a*B*C*D*E*f+A*B*C*d*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*f+a*B*C*d*E*f+a*B*C*D*E*F+A*B*C*d*e*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*e*f+a*B*C*d*e*f+a*B*C*D*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*D*e*f+a*B*C*E*F+A*B*C*d*e*f<->G |
| opt | 1 | 0.000 | 0.833 | 1.000 | a*b*c*d*e*F+a*b*c*D*e*f+a*B*c*D*E+a*B*C*d*E*f+A*B*C*d*e*f+A*B*C*D*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*D*e*f+a*B*C*E*F+a*B*C*d*e*f+a*B*C*D*E+A*B*C*d*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*D*e*f+a*B*C*E*F+a*B*C*d*e*f+a*B*C*D*E+A*B*C*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*E*f+b*c*D*f+B*C*d*f<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E*F+b*D*e*f+B*C*d*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e+B*C*E+a*b*C*e*f<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*f+B*C*E+a*D*e*f<->G |
| opt | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 0.500 | B*D*E+B*C*d+a*b*e<->G |
| opt_c6c7 | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*f+B*C*E+a*b*e*f+A*B*d<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*f+B*C*E+a*b*e*f+A*B*d<->G |

