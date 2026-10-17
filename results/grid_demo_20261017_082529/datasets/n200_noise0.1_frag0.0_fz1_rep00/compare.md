# n200_noise0.1_frag0.0_fz1_rep00

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=18000
- true model: `d*a+a*c+e*A<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.560 | True | 0.845 | 0.753 | 27 | 0.000 | 1.000 | 0.000 | 0.537 |
| quantile | 0.557 | True | 0.827 | 0.754 | 30 | 0.041 | 0.958 | 0.048 | 0.522 |
| kde | 0.555 | True | 0.847 | 0.754 | 30 | 0.070 | 0.943 | 0.059 | 0.548 |
| expert | 0.558 | False | 0.834 | 0.711 | 20 | 0.089 | 0.881 | 0.119 | 0.530 |
| opt | 0.765 | True | 0.854 | 0.684 | 21 | 0.144 | 0.859 | 0.143 | 0.680 |
| opt_c6c7 | 0.662 | True | 0.858 | 0.706 | 20 | 0.067 | 0.865 | 0.138 | 0.520 |
| opt_expert | 0.681 | True | 0.839 | 0.714 | 20 | 0.061 | 0.870 | 0.123 | 0.522 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.852 | 0.605 | 4 |
| quantile | 0.833 | 0.694 | 5 |
| kde | 0.867 | 0.703 | 4 |
| expert | 0.650 | 0.464 | 7 |
| opt | 1.000 | 0.618 | 0 |
| opt_c6c7 | 1.000 | 0.588 | 0 |
| opt_expert | 0.900 | 0.529 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.692 | 1.000 | B*c*d*E*F+B*C*d*e*F+a*c*D*E+a*b*C*d*E+a*b*C*D*e*f+a*B*c*F+a*B*c*E+a*B*c*D+a*B*C*d*f+A*c*D*e*f+A*b*d*f+A*b*d*e+A*B*C*D*e<->G |
| quantile | 34 | 0.000 | 0.604 | 0.882 | c*d*E*F+C*d*f+b*C*d*e+a*c*D*e*F+a*b*c*D*E+a*B*c*E*f+a*B*c*d*F+a*B*c*D*f+A*c*D*e*f+A*b*c*d+A*B*C*e<->G |
| kde | 1 | 0.000 | 0.636 | 1.000 | c*d*E*F+c*D*e*F+b*C*d*f+B*d*E*F+a*C*d*e*f+a*b*c*D*E+a*b*C*d+a*B*c*F+a*B*c*d*E+A*C*e*F+A*b*e<->G |
| expert | 4 | 0.000 | 0.350 | 0.667 | B*c*d*E*F+B*C*D*e*f+a*D*E*f+a*c*D*E+a*b*C*D*e*F+a*B*E*f+a*B*c*D*F+A*c*D*e*f+A*b*c*d*E+A*B*D*e<->G |
| opt | 1 | 0.000 | 0.714 | 1.000 | b*d*e+b*c*e*f+a*c*d*E+a*C*d*f+a*b*d+a*B*c*e*F+A*c*d*e*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.714 | 1.000 | b*d*e*f+B*c*D*e+a*d*f+a*c*d*E+a*c*D*e+a*B*c*e+A*b*c*d*e<->G |
| opt_expert | 1 | 0.000 | 0.571 | 0.667 | b*c*d*E*f+B*c*D*e+a*d*E*f+a*c*E+a*c*D+a*B*D*e*f+a*B*c<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | c+b*f+a*d+A*e<->G |
| quantile | 16 | 0.000 | 0.031 | 0.083 | 0.000 | 1.000 | d*e+c*d*F+C*d*f+b*f+a*E*f+a*c*e+a*b*c+A*B*e<->G |
| kde | 2 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | c*F+C*d*f+B*d+a*d+a*c+A*e<->G |
| expert | 1 | 0.000 | 0.333 | 0.667 | 0.000 | 1.000 | d*F+b*e+b*d+a*f+a*c+A*e<->G |
| opt | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | d*e+c*e+a*d<->G |
| opt_c6c7 | 2 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | d*e+B*c*e+a*d+a*c*e<->G |
| opt_expert | 12 | 0.000 | 0.400 | 0.667 | 0.000 | 1.000 | e*f+C*d+a*c+A*e+A*b*f<->G |

