# n100_noise0.1_frag0.2_fz1_rep02

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=8002
- true model: `b*a*e+a*d+b*D*F<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.474 | True | 0.829 | 0.630 | 13 | 0.000 | 1.000 | 0.000 | 0.537 |
| quantile | 0.442 | True | 0.849 | 0.563 | 12 | 0.037 | 0.967 | 0.037 | 0.522 |
| kde | 0.367 | False | 0.837 | 0.526 | 8 | 0.060 | 0.935 | 0.068 | 0.548 |
| expert | 0.414 | False | 0.780 | 0.586 | 10 | 0.073 | 0.878 | 0.122 | 0.523 |
| opt | 0.725 | True | 0.889 | 0.518 | 9 | 0.195 | 0.835 | 0.162 | 0.809 |
| opt_c6c7 | 0.570 | True | 0.803 | 0.610 | 12 | 0.074 | 0.843 | 0.158 | 0.508 |
| opt_expert | 0.584 | True | 0.826 | 0.597 | 11 | 0.084 | 0.853 | 0.143 | 0.540 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.846 | 0.579 | 2 |
| quantile | 1.000 | 0.571 | 0 |
| kde | 0.875 | 0.350 | 1 |
| expert | 0.900 | 0.474 | 1 |
| opt | 1.000 | 0.750 | 0 |
| opt_c6c7 | 0.917 | 0.647 | 1 |
| opt_expert | 1.000 | 0.647 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.750 | 1.000 | a*c*d*E*F+a*b*e*F+a*b*c*d*E+a*b*C*D*F+a*B*C*d*e+A*b*c*D*E*F+A*b*C*d*E*F+A*B*c*d*e*F<->G |
| quantile | 1 | 0.000 | 0.800 | 0.667 | b*c*D*E*F+a*c*d*E*F+a*C*d*e*F+a*b*F+a*b*c*d*E<->G |
| kde | 1 | 0.000 | 0.800 | 1.000 | a*b*c*D*E*F+a*b*C*D*e*F+a*B*d*F+a*B*C*E*F+a*B*C*d*e<->G |
| expert | 4 | 0.000 | 0.625 | 1.000 | a*c*d*E*f+a*c*D*E*F+a*b*d*e*f+a*b*C*E*F+a*b*C*D*F+a*B*c*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*d*e*F+a*b*C*e*F+a*b*C*d*F+a*B*c*d*F+a*B*C*d*e+A*b*C*D*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.667 | b*C*D*E*F+a*d*e*F+a*C*e*F+a*b*F<->G |
| opt_expert | 1 | 0.000 | 0.667 | 0.667 | b*C*D*E*F+a*d*e*F+a*b*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | d*e*F+b*D*F+b*C*E+a*d<->G |
| quantile | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | b*D*F+a*d<->G |
| kde | 4 | 0.000 | 0.667 | 0.667 | 0.000 | 0.500 | a*d+a*C*F+a*b<->G |
| expert | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | c*E*F+b*F+a*d<->G |
| opt | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | b*D+a*c*d*F+a*b*F+a*B*C*d*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E+B*C*e+a*c*d+a*b*F<->G |
| opt_expert | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | b*E*F+a*b*F+a*B*d*e<->G |

