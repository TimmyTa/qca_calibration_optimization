# n400_noise0.0_frag0.2_fz1_rep01

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=28001
- true model: `d*F*E+e*C*d<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.975 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.551 |
| quantile | 1.000 | False | 0.000 | 0.000 | 0 | 0.042 | 0.975 | 0.027 | 0.529 |
| kde | 1.000 | False | 0.000 | 0.000 | 0 | 0.024 | 0.993 | 0.005 | 0.538 |
| expert | 1.000 | False | 0.000 | 0.000 | 0 | 0.053 | 0.955 | 0.045 | 0.559 |
| opt | 0.795 | True | 0.907 | 0.510 | 8 | 0.159 | 0.940 | 0.056 | 0.806 |
| opt_c6c7 | 0.467 | False | 0.914 | 0.402 | 4 | 0.070 | 0.917 | 0.083 | 0.575 |
| opt_expert | 0.406 | False | 0.915 | 0.398 | 4 | 0.064 | 0.925 | 0.078 | 0.564 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.571 | 0 |
| opt_c6c7 | 1.000 | 0.286 | 0 |
| opt_expert | 1.000 | 0.286 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 2 | 0.500 | 0.875 | 1.000 | b*c*d*E*F+b*C*d*e*F+a*b*C*d*e+A*d*E*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | A*c*d*E*F+A*b*C*d*e*F+A*B*d*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | A*c*d*E*F+A*b*C*d*e*F+A*B*d*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E*F+C*d*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*E+A*b*C*d<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*E*F+A*b*C*d<->G |

