# n200_noise0.1_frag0.0_fz0_rep00

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=17000
- true model: `E*f+d*f+E*c<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.567 | True | 0.907 | 0.617 | 16 | 0.000 | 1.000 | 0.000 | 0.796 |
| quantile | 0.406 | False | 0.865 | 0.466 | 9 | 0.098 | 0.966 | 0.037 | 0.605 |
| kde | 0.454 | False | 0.872 | 0.494 | 10 | 0.050 | 1.000 | 0.000 | 0.699 |
| expert | 0.594 | True | 0.912 | 0.569 | 16 | 0.039 | 1.000 | 0.000 | 0.781 |
| opt | 0.725 | True | 0.886 | 0.551 | 17 | 0.109 | 0.902 | 0.088 | 0.734 |
| opt_c6c7 | 0.681 | True | 0.892 | 0.559 | 17 | 0.140 | 0.882 | 0.110 | 0.635 |
| opt_expert | 0.696 | True | 0.878 | 0.510 | 14 | 0.100 | 0.942 | 0.050 | 0.645 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.516 | 0 |
| quantile | 1.000 | 0.281 | 0 |
| kde | 1.000 | 0.323 | 0 |
| expert | 1.000 | 0.516 | 0 |
| opt | 1.000 | 0.586 | 0 |
| opt_c6c7 | 1.000 | 0.586 | 0 |
| opt_expert | 1.000 | 0.452 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*C*d*f+B*c*d*e*f+B*c*D*E*f+a*b*c*d*E+A*d*f+A*B*E*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*f+B*c*d*e*f+a*B*c*D*E*f+A*d*e*f+A*B*C*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+a*b*c*d*E*f+A*c*d*e*f+A*C*d*E*f+A*B*E*f+A*B*d*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*C*d*f+B*c*d*e*f+B*c*D*E*f+a*b*c*d*E+A*d*f+A*B*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*E*f+B*c*d*E+B*C*d*f+a*c*d*E*F+a*C*E*f+a*B*d*f+a*B*c*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*d*E+B*C*d*f+a*d*E*f+a*c*E*F+a*B*d*f+a*B*C*E*f+A*b*c*d*e*f+A*B*c*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*E*f+a*b*c*d*E+A*d*E*f+A*C*E*f+A*C*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | d*f+B*E*f+a*b*c*d<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e*f+B*C*f+a*B*E*f<->G |
| kde | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*E*f+B*C*e+a*c*E*f+A*c*d*e*f+A*C*E*f<->G |
| expert | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | d*f+B*E*f+a*b*c*d<->G |
| opt | 2 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | E*f+d*f+c*d*E+B*c*E<->G |
| opt_c6c7 | 2 | 0.500 | 0.833 | 0.833 | 0.500 | 0.000 | d*f+c*E+C*f<->G |
| opt_expert | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | E*f+d*f+a*b*c*d<->G |

