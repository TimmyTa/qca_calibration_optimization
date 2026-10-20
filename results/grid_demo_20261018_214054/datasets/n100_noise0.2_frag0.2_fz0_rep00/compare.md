# n100_noise0.2_frag0.2_fz0_rep00

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=11000
- true model: `a*E*b+a*f+A*D<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.557 | True | 0.910 | 0.630 | 13 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.434 | False | 0.859 | 0.471 | 11 | 0.107 | 0.970 | 0.048 | 0.605 |
| kde | 0.502 | False | 0.918 | 0.494 | 10 | 0.059 | 1.000 | 0.000 | 0.689 |
| expert | 0.542 | False | 0.950 | 0.490 | 11 | 0.042 | 1.000 | 0.000 | 0.818 |
| opt | 0.695 | True | 0.911 | 0.625 | 15 | 0.100 | 0.947 | 0.070 | 0.792 |
| opt_c6c7 | 0.607 | True | 0.902 | 0.513 | 14 | 0.112 | 0.985 | 0.025 | 0.648 |
| opt_expert | 0.545 | True | 0.907 | 0.536 | 12 | 0.061 | 0.988 | 0.012 | 0.689 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.448 | 0 |
| quantile | 1.000 | 0.333 | 0 |
| kde | 1.000 | 0.345 | 0 |
| expert | 1.000 | 0.379 | 0 |
| opt | 0.867 | 0.481 | 2 |
| opt_c6c7 | 1.000 | 0.483 | 0 |
| opt_expert | 1.000 | 0.414 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.833 | 1.000 | b*C*D*f+a*b*D*e*f+a*b*C*E+a*B*c*d*f+A*b*C*D*e+A*B*c*D*e<->G |
| quantile | 1 | 0.000 | 0.667 | 0.667 | b*D*e*f+b*C*D*f+a*c*d*e*f+a*b*e*f+A*b*C*D*e+A*B*c*D*e*F<->G |
| kde | 1 | 0.000 | 0.833 | 1.000 | b*C*D*f+a*b*D*e*f+a*b*C*E*F+a*B*c*d*e*f+A*b*C*D*e+A*B*c*D*e*f<->G |
| expert | 1 | 0.000 | 0.833 | 1.000 | b*C*D*f+a*b*D*e*f+a*b*C*E+a*B*c*d*e*f+A*b*C*D*e+A*B*c*D*e*f<->G |
| opt | 1 | 0.000 | 0.500 | 1.000 | b*D*e*f+b*C*D*f+b*C*D*e+a*b*c*d*e*F+a*b*C*f+a*b*C*d*E+a*B*c*d*e*f+A*B*c*D*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 1.000 | b*D*e*f+b*C*D*f+a*b*C*E+a*B*c*d*f+A*b*C*D*e+A*B*c*D*e<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | b*C*D*f+a*b*D*e*f+a*b*C*E+a*B*c*d*f+A*b*C*D*e+A*B*c*D*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C+B*c*D*e+a*e*f+a*B*f<->G |
| quantile | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*e*f+C*D*f+b*e*f+A*c*D*e+A*b*e<->G |
| kde | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*F+b*C*D+B*D*e*f+a*e*f<->G |
| expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C+B*c*e*f+a*e*f<->G |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*F+b*C+a*c*e*f+A*D*e<->G |
| opt_c6c7 | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | c*D*e+b*C+a*f<->G |
| opt_expert | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C+B*c*e*f+a*b*e+a*B*f<->G |

