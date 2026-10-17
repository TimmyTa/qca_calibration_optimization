# n200_noise0.1_frag0.2_fz0_rep01

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=19001
- true model: `E*D*f+C*b*e<->G`  (irrelevant: A)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.741 | True | 0.889 | 0.671 | 9 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.600 | False | 0.839 | 0.493 | 7 | 0.115 | 0.955 | 0.043 | 0.585 |
| kde | 0.664 | True | 0.847 | 0.661 | 9 | 0.057 | 1.000 | 0.000 | 0.686 |
| expert | 0.750 | True | 0.879 | 0.631 | 9 | 0.045 | 1.000 | 0.000 | 0.761 |
| opt | 0.832 | True | 0.895 | 0.522 | 8 | 0.081 | 0.968 | 0.043 | 0.802 |
| opt_c6c7 | 0.766 | True | 0.868 | 0.521 | 8 | 0.099 | 0.956 | 0.050 | 0.645 |
| opt_expert | 0.749 | True | 0.860 | 0.571 | 8 | 0.084 | 0.968 | 0.031 | 0.662 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.750 | 0 |
| quantile | 1.000 | 0.538 | 0 |
| kde | 1.000 | 0.750 | 0 |
| expert | 1.000 | 0.750 | 0 |
| opt | 1.000 | 0.571 | 0 |
| opt_c6c7 | 1.000 | 0.727 | 0 |
| opt_expert | 1.000 | 0.667 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.800 | 1.000 | b*C*D*f+a*b*C*e*f+a*B*D*E*f+A*b*D*E*f+A*b*C*D*e<->G |
| quantile | 2 | 0.500 | 0.900 | 1.000 | a*C*D*E*f+a*b*C*d*e*f+A*b*C*D*f+A*b*C*D*e+A*B*c*D*E*f<->G |
| kde | 1 | 0.000 | 0.800 | 1.000 | b*C*D*f+a*b*C*e*f+a*B*D*E*f+A*b*D*E*f+A*b*C*D*e<->G |
| expert | 1 | 0.000 | 0.800 | 1.000 | b*C*D*f+a*b*C*e*f+a*B*D*E*f+A*b*D*E*f+A*b*C*D*e<->G |
| opt | 1 | 0.000 | 0.750 | 1.000 | b*C*D*f+a*B*D*E*f+A*b*D*E*f+A*b*C*D*e<->G |
| opt_c6c7 | 2 | 0.500 | 0.900 | 1.000 | a*b*C*e*f+a*b*C*D*f+a*B*D*E*f+A*b*c*D*E*f+A*b*C*D*e<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | b*C*D*E*f+a*b*C*d*e*f+a*B*D*E*f+A*b*D*E*f+A*b*C*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E*f+b*C*e<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E*f+b*C*e<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E*f+b*C*e<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E*f+b*C*e<->G |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | D*E*f+b*C*D*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E*f+b*C*e<->G |
| opt_expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*D*E*f+b*C*e+a*E*f<->G |

