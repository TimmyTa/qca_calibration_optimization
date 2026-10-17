# n400_noise0.0_frag0.2_fz1_rep01

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=28001
- true model: `d*F*E+e*C*d<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.431 | False | 0.860 | 0.459 | 3 | 0.000 | 1.000 | 0.000 | 0.551 |
| quantile | 0.422 | False | 0.851 | 0.340 | 1 | 0.042 | 0.975 | 0.027 | 0.529 |
| kde | 0.330 | False | 0.861 | 0.368 | 2 | 0.024 | 0.993 | 0.005 | 0.538 |
| expert | 0.512 | False | 0.838 | 0.537 | 3 | 0.053 | 0.955 | 0.045 | 0.559 |
| opt | 0.862 | True | 0.854 | 0.505 | 9 | 0.123 | 0.917 | 0.081 | 0.743 |
| opt_c6c7 | 0.631 | True | 0.861 | 0.513 | 4 | 0.057 | 0.900 | 0.101 | 0.528 |
| opt_expert | 0.677 | True | 0.863 | 0.506 | 4 | 0.058 | 0.889 | 0.102 | 0.532 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.231 | 0 |
| quantile | 1.000 | 0.067 | 0 |
| kde | 1.000 | 0.154 | 0 |
| expert | 1.000 | 0.214 | 0 |
| opt | 1.000 | 0.562 | 0 |
| opt_c6c7 | 1.000 | 0.267 | 0 |
| opt_expert | 1.000 | 0.250 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | A*b*C*d*e*F+A*B*d*E*F<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | A*B*C*d*E*F<->G |
| kde | 1 | 1.000 | 1.000 | 0.500 | A*B*d*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | A*b*C*d*e*F+A*B*d*E*F<->G |
| opt | 2 | 0.500 | 0.875 | 1.000 | c*d*E*F+b*C*d*e*F+A*B*d*E*F+A*B*C*d*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | A*C*d*e*F+A*B*d*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | A*C*d*e*F+A*B*d*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*b*C*F+A*B*d*E*F<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*C*d*E*F<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*B*d*E*F<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*E*F+A*b*C*d<->G |
| opt | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*d*E*F+C*d*e+B*d*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | d*E+C*d*F<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | d*E+C*d*F<->G |

