# n100_noise0.1_frag0.2_fz1_rep00

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=8000
- true model: `D*C+f*C*b+a*C<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.251 | False | 0.918 | 0.307 | 2 | 0.000 | 1.000 | 0.000 | 0.563 |
| quantile | 0.346 | False | 0.931 | 0.456 | 6 | 0.066 | 0.925 | 0.070 | 0.525 |
| kde | 0.403 | False | 0.922 | 0.444 | 5 | 0.050 | 0.948 | 0.043 | 0.530 |
| expert | 0.179 | False | 0.918 | 0.283 | 1 | 0.046 | 0.958 | 0.042 | 0.564 |
| opt | 0.758 | True | 0.920 | 0.641 | 12 | 0.099 | 0.945 | 0.055 | 0.666 |
| opt_c6c7 | 0.457 | True | 0.919 | 0.578 | 10 | 0.076 | 0.883 | 0.112 | 0.516 |
| opt_expert | 0.469 | True | 0.931 | 0.572 | 10 | 0.069 | 0.903 | 0.097 | 0.524 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.095 | 0 |
| quantile | 1.000 | 0.286 | 0 |
| kde | 1.000 | 0.217 | 0 |
| expert | 1.000 | 0.050 | 0 |
| opt | 1.000 | 0.706 | 0 |
| opt_c6c7 | 1.000 | 0.526 | 0 |
| opt_expert | 1.000 | 0.526 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.333 | A*b*C*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*C*D*e*f+a*b*C*d*e*F+A*b*C*d*f+A*b*C*D*e<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*C*D*e*f+a*b*C*d*e*F+A*b*C*e*f+A*b*C*D*e<->G |
| expert | 1 | 1.000 | 1.000 | 0.667 | A*b*C*D*e*f<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | b*C*e*f+a*C*d*e*F+a*C*D*e*f+a*b*C*e+a*b*C*d*f+A*C*D*e*F+A*b*C*D*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*f+a*C*d*e*F+a*C*D*e*f+A*b*C*f+A*B*C*D*e*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*f+a*C*d*e*F+a*C*D*e*f+A*b*C*f+A*B*C*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*b*e*f<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D+a*b*C*e+A*b*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*e*f+a*b*d*e+A*b*C*D<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*C*D*e*f<->G |
| opt | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | C*f+C*e<->G |
| opt_c6c7 | 5 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | b*C*f+B*e*F+a*C*e<->G |
| opt_expert | 5 | 0.000 | 0.667 | 0.667 | 0.000 | 0.600 | C*D*e+b*C*f+a*C<->G |

