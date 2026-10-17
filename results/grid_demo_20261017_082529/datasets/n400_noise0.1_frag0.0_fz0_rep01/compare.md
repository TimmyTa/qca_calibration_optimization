# n400_noise0.1_frag0.0_fz0_rep01

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=29001
- true model: `b*f*E+F*C*b<->G`  (irrelevant: A, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.665 | True | 0.876 | 0.622 | 11 | 0.000 | 1.000 | 0.000 | 0.798 |
| quantile | 0.575 | False | 0.000 | 0.000 | 0 | 0.105 | 0.981 | 0.018 | 0.597 |
| kde | 0.363 | False | 0.823 | 0.369 | 3 | 0.057 | 1.000 | 0.000 | 0.683 |
| expert | 0.601 | False | 0.836 | 0.408 | 6 | 0.053 | 1.000 | 0.000 | 0.755 |
| opt | 0.817 | True | 0.869 | 0.504 | 10 | 0.092 | 0.897 | 0.095 | 0.749 |
| opt_c6c7 | 0.760 | True | 0.860 | 0.501 | 10 | 0.097 | 0.943 | 0.069 | 0.658 |
| opt_expert | 0.694 | True | 0.832 | 0.543 | 11 | 0.094 | 0.965 | 0.048 | 0.660 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.688 | 0 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.188 | 0 |
| expert | 1.000 | 0.375 | 0 |
| opt | 1.000 | 0.625 | 0 |
| opt_c6c7 | 1.000 | 0.625 | 0 |
| opt_expert | 1.000 | 0.688 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.750 | 1.000 | b*C*d*e*F+b*C*D*E+A*b*E*f+A*b*C*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 0.500 | a*b*C*D*E*f+A*b*d*E*f<->G |
| expert | 1 | 0.000 | 0.667 | 0.500 | b*C*D*E*f+A*b*E*f+A*b*C*D*E<->G |
| opt | 1 | 0.000 | 0.750 | 1.000 | b*C*d*F+b*C*d*E+A*b*c*E*f+A*b*C*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*d*F+A*b*E*f+A*b*C*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*d*E*f+b*C*d*F+a*b*C*E*f+A*b*c*E*f+A*b*C*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | b*E*f+b*C*E+b*C*d*F+A*b*D*F<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*f+a*b*f<->G |
| expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*E*f+A*b*D*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E*f+b*C*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E*f+b*C*F<->G |
| opt_expert | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*E*f+b*D*E+b*C*d*F<->G |

