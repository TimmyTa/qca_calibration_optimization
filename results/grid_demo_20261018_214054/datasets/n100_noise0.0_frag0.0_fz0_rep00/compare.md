# n100_noise0.0_frag0.0_fz0_rep00

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=1000
- true model: `C*f+f*E+a*e*B<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.469 | True | 0.928 | 0.564 | 8 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.570 | False | 0.000 | 0.000 | 0 | 0.118 | 0.953 | 0.035 | 0.583 |
| kde | 0.285 | False | 0.000 | 0.000 | 0 | 0.062 | 1.000 | 0.000 | 0.674 |
| expert | 0.543 | True | 0.895 | 0.631 | 11 | 0.052 | 1.000 | 0.000 | 0.773 |
| opt | 0.814 | True | 0.966 | 0.757 | 20 | 0.076 | 0.970 | 0.020 | 0.896 |
| opt_c6c7 | 0.670 | True | 0.912 | 0.569 | 14 | 0.116 | 0.893 | 0.105 | 0.634 |
| opt_expert | 0.513 | True | 0.851 | 0.515 | 8 | 0.087 | 0.960 | 0.050 | 0.656 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.364 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.500 | 0 |
| opt | 1.000 | 1.000 | 0 |
| opt_c6c7 | 1.000 | 0.933 | 0 |
| opt_expert | 1.000 | 0.364 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*C*D*f+a*B*c*d*E*f+a*B*C*d*e*F+A*C*D*e*f+A*B*C*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 0.000 | 0.714 | 1.000 | a*b*C*d*E*f+a*B*D*f+a*B*c*f+a*B*c*D*e+a*B*C*d*e*F+A*b*C*D*e*f+A*B*C*d*e*f<->G |
| opt | 8 | 0.000 | 0.861 | 1.000 | C*D*e*f+b*c*D*E*f+B*c*d*E*f+B*C*D*f+a*b*C*E*f+a*B*D*e+a*B*c*f+a*B*C*e*F+A*B*C*f<->G |
| opt_c6c7 | 4 | 1.000 | 1.000 | 1.000 | b*C*D*e*f+a*c*D*E*f+a*B*D*e*F+a*B*c*e+A*C*D*e*f+A*B*c*E*f+A*B*C*d*f<->G |
| opt_expert | 1 | 0.000 | 0.800 | 0.667 | a*B*c*d*f+a*B*C*d*e*F+a*B*C*D*f+A*C*D*e*f+A*B*C*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*D*f+a*C*d*e*F+a*B*d*E*f+A*C*e*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*e*f+a*C*E*f+a*B*f+a*B*d*e+a*B*c*e+A*b*C*e*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | E*f+C*f+a*B*e<->G |
| opt_c6c7 | 8 | 0.000 | 0.250 | 0.333 | 0.000 | 0.500 | D*E*f+C*e*f+a*B*e+A*E*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*e*f+a*B*f+a*B*d*e+A*C*D*e*f<->G |

