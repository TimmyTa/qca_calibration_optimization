# n400_noise0.1_frag0.2_fz1_rep00

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=32000
- true model: `b*f*D+f*d*e+b*c*e<->G`  (irrelevant: A)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 1.000 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 1.000 | False | 0.000 | 0.000 | 0 | 0.032 | 0.987 | 0.027 | 0.525 |
| kde | 1.000 | False | 0.000 | 0.000 | 0 | 0.028 | 0.990 | 0.020 | 0.533 |
| expert | 1.000 | False | 0.000 | 0.000 | 0 | 0.049 | 0.943 | 0.057 | 0.541 |
| opt | 0.640 | True | 0.869 | 0.503 | 11 | 0.142 | 0.973 | 0.035 | 0.814 |
| opt_c6c7 | 0.435 | False | 0.915 | 0.247 | 2 | 0.078 | 0.896 | 0.097 | 0.573 |
| opt_expert | 0.449 | False | 0.903 | 0.340 | 4 | 0.093 | 0.889 | 0.108 | 0.577 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.579 | 0 |
| opt_c6c7 | 1.000 | 0.118 | 0 |
| opt_expert | 1.000 | 0.235 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*D*e*f+b*C*D*f+B*C*d*e*f+A*b*c*e*F+A*B*d*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*f+a*B*C*d*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | a*b*D*e*f+a*B*C*d*e*f+A*b*C*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 3 | 0.333 | 0.778 | 0.778 | 0.333 | 0.333 | d*e*f+b*c*e+b*C*D<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 0.000 | d*e*f+b*c*e*f<->G |
| opt_expert | 8 | 0.000 | 0.167 | 0.167 | 0.000 | 1.000 | C*e*f+b*e*f+A*b*D<->G |

