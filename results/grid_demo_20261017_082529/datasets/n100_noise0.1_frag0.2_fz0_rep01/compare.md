# n100_noise0.1_frag0.2_fz0_rep01

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=7001
- true model: `D*C+e*d<->G`  (irrelevant: A, B, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.532 | True | 0.899 | 0.631 | 10 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.247 | False | 0.802 | 0.279 | 2 | 0.121 | 0.938 | 0.067 | 0.571 |
| kde | 0.436 | True | 0.834 | 0.587 | 9 | 0.056 | 1.000 | 0.000 | 0.690 |
| expert | 0.498 | True | 0.858 | 0.527 | 9 | 0.061 | 0.982 | 0.018 | 0.747 |
| opt | 0.647 | True | 0.923 | 0.524 | 10 | 0.127 | 0.878 | 0.113 | 0.773 |
| opt_c6c7 | 0.553 | True | 0.863 | 0.511 | 10 | 0.102 | 0.915 | 0.075 | 0.636 |
| opt_expert | 0.549 | True | 0.841 | 0.542 | 10 | 0.094 | 0.932 | 0.063 | 0.656 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.476 | 0 |
| quantile | 1.000 | 0.080 | 0 |
| kde | 1.000 | 0.429 | 0 |
| expert | 1.000 | 0.474 | 0 |
| opt | 1.000 | 0.455 | 0 |
| opt_c6c7 | 1.000 | 0.526 | 0 |
| opt_expert | 1.000 | 0.435 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 3 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+a*c*d*e*F+a*b*d*e*F+a*b*C*D*E*F+A*b*C*D*e*F+A*B*C*d*e+A*B*C*D*E*F<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | A*B*c*d*e*f+A*B*C*d*e*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*b*d*e*F+a*b*C*D*E*F+a*B*c*d*e+A*b*C*D*e*F+A*B*C*d*e+A*B*C*D*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*d*e*F+a*b*C*D*E*F+a*B*c*d*e+A*b*C*D*e*F+A*B*C*d*e+A*B*C*D*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | C*d*e*F+a*d*e*F+a*b*C*D*e+a*B*d*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.800 | 1.000 | C*d*e*F+b*C*e*F+a*d*e*F+a*b*C*D*e+A*B*c*d*e*f<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | b*C*d*e*F+B*c*d*e*f+a*C*d*e*F+a*b*C*e+a*b*C*D*F+A*B*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*e+C*D*F<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*B*d*e<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e+C*D*F+a*d*e<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e+C*D*F+a*d*e<->G |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*e+b*C*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*e+b*C*e<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*e+a*b*C*D<->G |

