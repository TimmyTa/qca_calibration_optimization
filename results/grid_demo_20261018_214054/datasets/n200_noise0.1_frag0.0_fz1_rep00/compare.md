# n200_noise0.1_frag0.0_fz1_rep00

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=18000
- true model: `d*a+a*c+e*A<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.430 | True | 0.922 | 0.526 | 9 | 0.000 | 1.000 | 0.000 | 0.537 |
| quantile | 0.499 | True | 0.924 | 0.536 | 10 | 0.041 | 0.958 | 0.048 | 0.522 |
| kde | 0.489 | True | 0.907 | 0.580 | 13 | 0.070 | 0.943 | 0.059 | 0.548 |
| expert | 0.321 | False | 0.930 | 0.419 | 4 | 0.089 | 0.881 | 0.119 | 0.530 |
| opt | 0.765 | True | 0.907 | 0.595 | 13 | 0.131 | 0.849 | 0.159 | 0.648 |
| opt_c6c7 | 0.639 | True | 0.907 | 0.605 | 14 | 0.055 | 0.901 | 0.110 | 0.520 |
| opt_expert | 0.672 | True | 0.912 | 0.594 | 13 | 0.067 | 0.887 | 0.114 | 0.533 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.237 | 0 |
| quantile | 1.000 | 0.278 | 0 |
| kde | 1.000 | 0.351 | 0 |
| expert | 1.000 | 0.143 | 0 |
| opt | 1.000 | 0.361 | 0 |
| opt_c6c7 | 1.000 | 0.400 | 0 |
| opt_expert | 1.000 | 0.419 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*F+a*B*d*E*f+a*B*c*d*F+a*B*C*d*e+A*b*d*e*f<->G |
| quantile | 3 | 1.000 | 1.000 | 1.000 | a*c*d*E*F+a*b*C*d*e+a*B*c*d*F+a*B*c*d*E+a*B*C*d*f+A*b*d*e*f<->G |
| kde | 1 | 0.000 | 0.857 | 0.667 | b*C*d*e+a*d*E*F+a*C*d*e*f+a*b*c*D*e*F+a*b*C*d+a*B*c*d*F+a*B*c*d*E<->G |
| expert | 1 | 1.000 | 1.000 | 0.667 | a*B*d*E*f+a*B*c*d*E+a*B*c*D*e*F<->G |
| opt | 1 | 0.000 | 0.800 | 0.667 | b*d*e*f+a*c*d*E+a*b*c*e*f+a*B*d*f+a*B*c*d<->G |
| opt_c6c7 | 1 | 0.000 | 0.800 | 0.667 | b*d*e*f+a*d*f+a*c*d*E+a*b*c*e*f+a*B*c*d<->G |
| opt_expert | 1 | 0.000 | 0.800 | 0.667 | b*c*d*e*f+a*d*f+a*c*d*E+a*b*c*e*f+a*B*c*d<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e*f+a*d*F+a*B*d<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*e*f+a*d*F+a*B*d<->G |
| kde | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | b*C*d*e+a*d+a*b*c*e<->G |
| expert | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 0.000 | a*d+a*c*e<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*e*f+a*c*d+a*B*d<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | d*e+a*d+a*b*c*e<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | b*c*e+a*d<->G |

