# n100_noise0.1_frag0.2_fz0_rep01

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=7001
- true model: `D*C+e*d<->G`  (irrelevant: A, B, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.454 | True | 0.911 | 0.527 | 8 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.660 | False | 0.000 | 0.000 | 0 | 0.121 | 0.938 | 0.067 | 0.571 |
| kde | 0.247 | False | 0.889 | 0.223 | 1 | 0.056 | 1.000 | 0.000 | 0.690 |
| expert | 0.366 | False | 0.890 | 0.393 | 5 | 0.061 | 0.982 | 0.018 | 0.747 |
| opt | 0.636 | True | 0.926 | 0.527 | 10 | 0.119 | 0.865 | 0.135 | 0.827 |
| opt_c6c7 | 0.502 | False | 0.887 | 0.489 | 11 | 0.122 | 0.895 | 0.107 | 0.631 |
| opt_expert | 0.324 | False | 0.835 | 0.489 | 8 | 0.097 | 0.937 | 0.068 | 0.665 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.381 | 0 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.048 | 0 |
| expert | 1.000 | 0.263 | 0 |
| opt | 1.000 | 0.476 | 0 |
| opt_c6c7 | 1.000 | 0.500 | 0 |
| opt_expert | 1.000 | 0.400 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*d*e*F+a*b*C*D*E*F+a*B*c*d*e*f+A*b*C*D*e*F+A*B*C*d*e+A*B*C*D*E*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 0.500 | A*b*C*D*e*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*e*F+a*b*C*D*E*F+a*B*c*d*e*f+A*b*C*D*e*F+A*B*C*d*e*f<->G |
| opt | 1 | 0.000 | 0.750 | 1.000 | C*d*e*F+a*c*d*e*f+a*b*C*e+a*b*C*D*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.800 | 1.000 | C*d*e*F+b*C*e*F+B*c*d*e*f+a*d*e*F+a*b*C*D*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*c*d*e*F+a*b*d*e*F+a*b*c*d*e+a*b*C*D*e*f+a*b*C*D*E*F+A*B*C*d*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e+C*D*F+b*d*e+a*d*e*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*b*C<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*f+b*C+a*d*e*f<->G |
| opt | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | d*e+b*C*e+a*b*C*D*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*e+b*C*e<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e+C*D*F+a*d*e<->G |

