# n100_noise0.1_frag0.0_fz1_rep00

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=6000
- true model: `f*B+f*d<->G`  (irrelevant: A, C, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.398 | False | 0.904 | 0.474 | 4 | 0.000 | 1.000 | 0.000 | 0.544 |
| quantile | 0.476 | False | 0.909 | 0.455 | 5 | 0.065 | 0.945 | 0.058 | 0.540 |
| kde | 0.330 | False | 0.000 | 0.000 | 0 | 0.080 | 0.913 | 0.087 | 0.551 |
| expert | 0.592 | False | 0.935 | 0.474 | 9 | 0.110 | 0.860 | 0.140 | 0.558 |
| opt | 0.822 | True | 0.943 | 0.514 | 11 | 0.128 | 0.918 | 0.090 | 0.742 |
| opt_c6c7 | 0.622 | True | 0.908 | 0.503 | 8 | 0.057 | 0.918 | 0.077 | 0.529 |
| opt_expert | 0.663 | True | 0.923 | 0.534 | 10 | 0.059 | 0.898 | 0.097 | 0.537 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.222 | 0 |
| quantile | 1.000 | 0.278 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.818 | 0 |
| opt | 0.909 | 0.714 | 1 |
| opt_c6c7 | 1.000 | 0.571 | 0 |
| opt_expert | 0.900 | 0.643 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*f+a*B*C*E*f<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | a*b*c*d*f+a*B*d*E*f+a*B*C*E*f<->G |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*E*f+a*c*d*f+a*B*E*f+A*B*C*D*e*f<->G |
| opt | 1 | 0.000 | 0.833 | 1.000 | b*C*d*E*f+B*c*d*E*f+a*b*d*f+a*b*C*e*f+a*B*C*E*f+A*B*C*D*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*d*E*f+a*C*d*f+a*b*d*f+a*B*C*E*f<->G |
| opt_expert | 1 | 0.000 | 0.800 | 1.000 | a*d*E*f+a*C*E*f+a*C*d*f+a*b*d*f+A*B*C*D*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*c*f+a*B*E*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*d*f+a*B*C*E*f<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*E*f+C*e*f+a*f<->G |
| opt | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*E*f+B*E*f+B*C*D*f+a*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*d*f+a*B*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*e*f+a*f<->G |

