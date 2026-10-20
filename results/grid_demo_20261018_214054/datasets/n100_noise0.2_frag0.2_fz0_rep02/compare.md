# n100_noise0.2_frag0.2_fz0_rep02

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=11002
- true model: `D*e+a*b+E*a<->G`  (irrelevant: C, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.362 | False | 0.922 | 0.386 | 6 | 0.000 | 1.000 | 0.000 | 0.798 |
| quantile | 0.415 | False | 0.000 | 0.000 | 0 | 0.106 | 0.977 | 0.047 | 0.623 |
| kde | 0.285 | False | 0.000 | 0.000 | 0 | 0.057 | 1.000 | 0.000 | 0.691 |
| expert | 0.460 | False | 0.916 | 0.458 | 10 | 0.044 | 1.000 | 0.000 | 0.771 |
| opt | 0.612 | True | 0.919 | 0.571 | 12 | 0.106 | 0.930 | 0.078 | 0.841 |
| opt_c6c7 | 0.412 | False | 0.864 | 0.426 | 8 | 0.114 | 0.900 | 0.090 | 0.653 |
| opt_expert | 0.313 | False | 0.875 | 0.367 | 5 | 0.088 | 0.972 | 0.023 | 0.689 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.261 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.435 | 0 |
| opt | 0.917 | 0.550 | 1 |
| opt_c6c7 | 1.000 | 0.400 | 0 |
| opt_expert | 1.000 | 0.238 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*D*E*F+a*b*c*d*e*f+a*b*c*D*E+A*b*c*D*e*F+A*B*c*D*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e*F+a*b*D*E*F+a*b*c*d*e*f+a*b*c*D*E+a*B*C*D*E*f+A*c*D*e*F+A*B*D*e*F+A*B*c*D*e<->G |
| opt | 1 | 0.000 | 0.875 | 1.000 | B*c*D*e*F+a*c*D*E*f+a*b*D*E*F+a*b*c*d*f+a*B*C*d*E*f+A*c*D*e*F+A*B*c*D*e+A*B*C*d*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e*F+a*c*D*E*f+a*b*c*d*f+a*b*C*D*E*F+A*B*c*D*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*D*E*F+a*b*c*d*e*f+A*c*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*e*f+b*D*e+a*b*E<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 15 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | D*e+a*D*f+a*b*F+a*b*c<->G |
| opt | 40 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | D*e+C*d*E*f+B*C*F+a*c*E*f+a*b*D+a*b*c<->G |
| opt_c6c7 | 9 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | D*e+b*C*D+a*c*D+a*b*c<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*F+a*c*e+a*b*F<->G |

