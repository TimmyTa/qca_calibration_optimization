# n100_noise0.2_frag0.2_fz0_rep02

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=11002
- true model: `D*e+a*b+E*a<->G`  (irrelevant: C, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.494 | True | 0.882 | 0.625 | 12 | 0.000 | 1.000 | 0.000 | 0.798 |
| quantile | 0.290 | False | 0.814 | 0.321 | 5 | 0.106 | 0.977 | 0.047 | 0.623 |
| kde | 0.418 | True | 0.832 | 0.535 | 10 | 0.057 | 1.000 | 0.000 | 0.691 |
| expert | 0.484 | True | 0.905 | 0.509 | 12 | 0.044 | 1.000 | 0.000 | 0.771 |
| opt | 0.598 | True | 0.902 | 0.562 | 11 | 0.109 | 0.932 | 0.083 | 0.866 |
| opt_c6c7 | 0.524 | True | 0.816 | 0.517 | 12 | 0.097 | 0.943 | 0.060 | 0.639 |
| opt_expert | 0.496 | True | 0.831 | 0.569 | 12 | 0.060 | 0.993 | 0.003 | 0.688 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.522 | 0 |
| quantile | 1.000 | 0.185 | 0 |
| kde | 1.000 | 0.435 | 0 |
| expert | 1.000 | 0.522 | 0 |
| opt | 0.909 | 0.500 | 1 |
| opt_c6c7 | 1.000 | 0.571 | 0 |
| opt_expert | 1.000 | 0.545 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e*F+a*b*d*e*f+a*b*D*E*F+a*b*c*D*E+a*B*C*E*f+A*c*D*e*F+A*B*D*e*F+A*B*c*D*e<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | B*C*D*e*F+a*b*D*E*F+a*B*D*e*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e*F+a*b*D*E*F+a*b*c*d*e*f+a*b*c*D*E+a*B*C*d*E*f+A*c*D*e*F+A*B*D*e*F+A*B*c*D*e<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e*F+a*C*D*E*F+a*b*c*d*e*f+a*b*c*D*E+a*B*C*E*f+A*c*D*e*F+A*B*D*e*F+A*B*c*D*e<->G |
| opt | 1 | 0.000 | 0.875 | 1.000 | B*c*D*e*F+a*c*D*E*f+a*b*D*E*F+a*b*c*d*e*f+a*B*C*d*E*f+A*c*D*e*F+A*B*c*D*e+A*B*C*d*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*D*e*F+a*C*D*E*F+a*b*c*E*F+a*b*C*d*e*f+a*B*D*E*f+a*B*C*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e*F+a*C*D*E*F+a*b*d*e*f+a*b*c*D*E+a*B*C*E*f+A*c*D*e*F+A*B*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | D*e+a*E*f+a*b<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*e+a*b*F<->G |
| kde | 24 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | D*e+c*d*f+a*C*d*E+a*b*D<->G |
| expert | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | D*e+a*C*E+a*b*c<->G |
| opt | 12 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | D*e+B*C*F+a*D*F+a*c*D+a*C*d*E+a*b*c*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*e+a*E+a*b<->G |
| opt_expert | 8 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | d*E*f+D*e+a*D+a*b*e<->G |

