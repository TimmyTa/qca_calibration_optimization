# n200_noise0.1_frag0.2_fz0_rep01

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=19001
- true model: `E*D*f+C*b*e<->G`  (irrelevant: A)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.537 | False | 0.915 | 0.401 | 4 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.340 | False | 0.877 | 0.250 | 1 | 0.115 | 0.955 | 0.043 | 0.585 |
| kde | 0.435 | False | 0.000 | 0.000 | 0 | 0.057 | 1.000 | 0.000 | 0.686 |
| expert | 0.588 | False | 0.894 | 0.494 | 6 | 0.045 | 1.000 | 0.000 | 0.761 |
| opt | 0.810 | True | 0.882 | 0.524 | 7 | 0.074 | 0.960 | 0.045 | 0.843 |
| opt_c6c7 | 0.683 | False | 0.889 | 0.483 | 8 | 0.114 | 0.948 | 0.066 | 0.630 |
| opt_expert | 0.564 | True | 0.877 | 0.503 | 7 | 0.099 | 0.949 | 0.053 | 0.670 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.333 | 0 |
| quantile | 1.000 | 0.077 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.500 | 0 |
| opt | 1.000 | 0.538 | 0 |
| opt_c6c7 | 1.000 | 0.727 | 0 |
| opt_expert | 1.000 | 0.538 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | A*b*D*E*f+A*b*C*D*e<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | A*b*C*D*e*f<->G |
| kde | 0 |  |  |  | (none) |
| expert | 2 | 0.500 | 0.875 | 1.000 | a*C*D*E*f+a*b*C*d*e*f+A*b*C*D*f+A*b*C*D*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*C*D*E*f+a*b*C*e*f+A*b*c*D*E*f+A*b*C*D*e<->G |
| opt_c6c7 | 2 | 0.500 | 0.900 | 1.000 | a*b*C*e*f+a*b*C*D*f+a*B*D*E*f+A*b*c*D*E*f+A*b*C*D*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*C*D*E*f+a*b*C*d*e*f+A*b*D*E*f+A*b*C*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*D*E*f+A*b*C*e<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | A*b*C*e*f<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*D*E*f+b*C*d*e+A*b*C*e<->G |
| opt | 6 | 0.000 | 0.333 | 0.500 | 0.000 | 0.667 | D*E*f+C*D*e*F+b*C*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E*f+b*C*e<->G |
| opt_expert | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 0.667 | b*D*E*f+b*C*e+a*C*E*f<->G |

