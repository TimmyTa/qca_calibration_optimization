# n200_noise0.1_frag0.2_fz0_rep00

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=19000
- true model: `c*B+d*E*A+A*d*b<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.672 | True | 0.903 | 0.734 | 16 | 0.000 | 1.000 | 0.000 | 0.804 |
| quantile | 0.587 | True | 0.825 | 0.512 | 11 | 0.108 | 0.998 | 0.022 | 0.605 |
| kde | 0.660 | True | 0.862 | 0.692 | 14 | 0.063 | 1.000 | 0.000 | 0.677 |
| expert | 0.644 | True | 0.902 | 0.604 | 16 | 0.060 | 0.992 | 0.008 | 0.731 |
| opt | 0.808 | True | 0.875 | 0.564 | 13 | 0.107 | 0.907 | 0.084 | 0.745 |
| opt_c6c7 | 0.771 | True | 0.865 | 0.588 | 13 | 0.097 | 0.943 | 0.051 | 0.648 |
| opt_expert | 0.763 | True | 0.878 | 0.629 | 12 | 0.082 | 0.969 | 0.027 | 0.675 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.727 | 0 |
| quantile | 1.000 | 0.500 | 0 |
| kde | 1.000 | 0.636 | 0 |
| expert | 1.000 | 0.762 | 0 |
| opt | 1.000 | 0.591 | 0 |
| opt_c6c7 | 1.000 | 0.650 | 0 |
| opt_expert | 1.000 | 0.600 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 6 | 0.333 | 0.926 | 1.000 | a*B*c*F+a*B*c*d*E+A*C*d*E*F+A*b*d*e*F+A*b*c*d*E*f+A*b*C*d*e+A*B*c*d*e+A*B*c*D*f+A*B*C*d*E<->G |
| quantile | 3 | 1.000 | 1.000 | 1.000 | a*B*c*E*F+a*B*c*d*F+A*C*d*E*F+A*b*d*e*F+A*B*c*d*e+A*B*c*D*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*B*c*F+a*B*c*d*E+A*C*d*E*F+A*b*d*e*F+A*b*c*d*E*f+A*B*c*d*e+A*B*c*D*f<->G |
| expert | 6 | 0.333 | 0.926 | 1.000 | a*B*c*F+a*B*c*d*E+A*C*d*E*F+A*b*d*e*F+A*b*c*d*E*f+A*b*C*d*e+A*B*c*d*e+A*B*c*D*f+A*B*C*d*E<->G |
| opt | 1 | 0.000 | 0.857 | 1.000 | B*c*E*F+B*c*d*F+a*B*c*d*E+A*c*d*e*F+A*C*d*E*F+A*b*c*d*E*f+A*B*c*D*f<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+a*B*c*F+a*B*c*d*E+A*C*d*E*F+A*b*c*d*E*f+A*b*C*d*F+A*B*c*D*f+A*B*c*D*E<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+a*B*c*E+a*B*c*d*F+A*C*d*E*F+A*b*c*d*E*f+A*b*C*d*F+A*B*c*d*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*c+A*d*E+A*b*d<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*F+B*c*E*F+A*d*F+A*B*c<->G |
| kde | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | C*d*F+B*c+A*c*d<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*c+A*d*E+A*b*d<->G |
| opt | 12 | 0.000 | 0.200 | 0.333 | 0.000 | 0.833 | B*c*E+B*c*d+A*d*E+A*b*d+A*B*c<->G |
| opt_c6c7 | 2 | 0.500 | 0.833 | 0.833 | 0.500 | 0.500 | B*c+A*d*E+A*b*d<->G |
| opt_expert | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*F+B*c+A*b*d<->G |

