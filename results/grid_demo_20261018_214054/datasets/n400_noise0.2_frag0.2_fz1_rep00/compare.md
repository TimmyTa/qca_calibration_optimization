# n400_noise0.2_frag0.2_fz1_rep00

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=36000
- true model: `f*d*C+a*B*D<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.533 | False | 0.941 | 0.260 | 1 | 0.000 | 1.000 | 0.000 | 0.552 |
| quantile | 0.685 | False | 0.000 | 0.000 | 0 | 0.036 | 0.976 | 0.031 | 0.525 |
| kde | 0.477 | False | 0.941 | 0.257 | 1 | 0.027 | 0.985 | 0.015 | 0.543 |
| expert | 0.125 | False | 0.000 | 0.000 | 0 | 0.078 | 0.927 | 0.073 | 0.566 |
| opt | 0.535 | False | 0.871 | 0.463 | 10 | 0.118 | 0.948 | 0.044 | 0.742 |
| opt_c6c7 | 0.451 | False | 0.928 | 0.296 | 2 | 0.065 | 0.883 | 0.119 | 0.547 |
| opt_expert | 0.397 | False | 0.923 | 0.302 | 2 | 0.075 | 0.880 | 0.123 | 0.541 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.067 | 0 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.067 | 0 |
| expert |  | 0.000 | 0 |
| opt | 0.900 | 0.600 | 1 |
| opt_c6c7 | 1.000 | 0.125 | 0 |
| opt_expert | 1.000 | 0.125 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | a*B*C*D*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 0.500 | a*B*C*D*e*f<->G |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 0.000 | 0.667 | 1.000 | B*C*d*e*f+a*b*C*d*e+a*B*D*E*f+a*B*C*f+a*B*C*D*E+A*b*C*d*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | a*B*C*e*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | a*B*C*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | C*D*e*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.333 | B*C*D*f<->G |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*f+a*b*e+a*B*E*f+a*B*C*D+A*C*d*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*C*e*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*C*e*f<->G |

