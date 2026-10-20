# n200_noise0.2_frag0.0_fz1_rep00

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=22000
- true model: `c*D+d*f*E+e*d*A<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.381 | False | 0.919 | 0.419 | 4 | 0.000 | 1.000 | 0.000 | 0.543 |
| quantile | 0.422 | False | 0.916 | 0.446 | 6 | 0.034 | 0.970 | 0.019 | 0.530 |
| kde | 0.120 | False | 0.910 | 0.266 | 1 | 0.067 | 0.930 | 0.067 | 0.567 |
| expert | 0.351 | False | 0.893 | 0.404 | 6 | 0.062 | 0.931 | 0.069 | 0.541 |
| opt | 0.649 | True | 0.877 | 0.510 | 9 | 0.149 | 0.900 | 0.096 | 0.764 |
| opt_c6c7 | 0.540 | True | 0.888 | 0.531 | 9 | 0.061 | 0.912 | 0.083 | 0.557 |
| opt_expert | 0.553 | True | 0.888 | 0.533 | 9 | 0.056 | 0.915 | 0.087 | 0.545 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.125 | 0 |
| quantile | 1.000 | 0.194 | 0 |
| kde | 1.000 | 0.037 | 0 |
| expert | 0.833 | 0.161 | 1 |
| opt | 1.000 | 0.281 | 0 |
| opt_c6c7 | 0.889 | 0.296 | 1 |
| opt_expert | 0.889 | 0.286 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.667 | a*b*c*D*e*f+A*b*c*d*e*F+A*b*c*D*E<->G |
| quantile | 2 | 1.000 | 1.000 | 0.667 | b*c*D*e*f+b*c*D*E*F+A*b*c*d*e*F+A*b*c*D*f<->G |
| kde | 1 | 1.000 | 1.000 | 0.333 | a*B*c*D*e*f<->G |
| expert | 1 | 0.000 | 0.667 | 0.333 | a*b*c*D*f+A*b*c*d*F+A*b*c*D*E<->G |
| opt | 2 | 0.500 | 0.917 | 1.000 | b*c*D*e*f+b*C*d*E*f+A*c*D*e*f+A*b*c*E*f+A*b*c*d*e*F+A*b*c*D*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.833 | 0.667 | b*c*D*e*f+b*c*D*E*F+A*c*D*e*f+A*b*d*e*F+A*b*D*e*f+A*b*c*D*f<->G |
| opt_expert | 2 | 0.000 | 0.833 | 0.667 | b*c*D*e*f+b*c*D*E*F+A*c*D*e*f+A*b*d*e*F+A*b*D*e*f+A*b*c*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*e*F+a*b*D*e*f+A*b*D*E<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*f+b*c*d*e*F+b*c*D*E<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | a*D*e*f<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*f+A*b*F<->G |
| opt | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | d*E*f+c*d*e*F+c*D*e*f+A*b*c*D*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*f+c*d+b*c*E+A*b*C<->G |
| opt_expert | 4 | 0.000 | 0.125 | 0.167 | 0.000 | 1.000 | d*e*F+c*D*f+b*c*D*E+A*b*f<->G |

