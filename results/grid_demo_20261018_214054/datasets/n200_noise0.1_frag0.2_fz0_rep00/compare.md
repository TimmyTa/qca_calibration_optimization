# n200_noise0.1_frag0.2_fz0_rep00

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=19000
- true model: `c*B+d*E*A+A*d*b<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.709 | True | 0.929 | 0.613 | 10 | 0.000 | 1.000 | 0.000 | 0.804 |
| quantile | 0.479 | False | 0.861 | 0.268 | 2 | 0.108 | 0.998 | 0.022 | 0.605 |
| kde | 0.334 | False | 0.862 | 0.317 | 2 | 0.063 | 1.000 | 0.000 | 0.677 |
| expert | 0.670 | True | 0.927 | 0.503 | 10 | 0.060 | 0.992 | 0.008 | 0.731 |
| opt | 0.819 | True | 0.934 | 0.537 | 11 | 0.086 | 0.948 | 0.050 | 0.778 |
| opt_c6c7 | 0.735 | True | 0.906 | 0.521 | 13 | 0.114 | 0.943 | 0.057 | 0.657 |
| opt_expert | 0.678 | True | 0.891 | 0.504 | 8 | 0.093 | 0.943 | 0.062 | 0.648 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.455 | 0 |
| quantile | 1.000 | 0.091 | 0 |
| kde | 1.000 | 0.091 | 0 |
| expert | 1.000 | 0.476 | 0 |
| opt | 1.000 | 0.524 | 0 |
| opt_c6c7 | 0.923 | 0.600 | 1 |
| opt_expert | 1.000 | 0.381 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | a*B*c*E*F+a*B*c*d*F+A*C*d*E*F+A*b*c*d*E*f+A*b*C*d*F+A*B*c*d*e+A*B*c*D*E*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.333 | a*B*c*d*F<->G |
| kde | 1 | 1.000 | 1.000 | 0.667 | a*B*c*d*e*F+A*B*C*d*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*B*c*d*F+A*C*d*E*F+A*b*c*d*E*f+A*b*C*d*F+A*B*c*d*e+A*B*c*D*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+a*B*c*E*F+a*B*c*d*E+A*C*d*E*F+A*b*c*d*E*f+A*b*C*d*F+A*B*c*D*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.786 | 0.667 | B*c*d*e*F+a*B*c*e*F+a*B*c*d*F+a*B*c*d*e+A*C*d*F+A*b*c*d*f+A*B*c*D*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+a*B*c*E*F+a*B*c*d*E+A*b*c*d*E*f+A*B*c*D*E*f+A*B*C*d*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*F+B*d*F+B*c*D*E+A*c*d*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*d*F<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*F+a*B*c*d*e<->G |
| expert | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*F+A*c*d*f+A*C*d*F+A*B*c<->G |
| opt | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*F+B*c+A*b*d<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | d*F+B*c+A*c*d<->G |
| opt_expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d+a*B*c*F+A*d*f+A*B*d*E+A*B*c*f<->G |

