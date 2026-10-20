# n100_noise0.1_frag0.2_fz0_rep00

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=7000
- true model: `f*b*D+f*a<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.399 | False | 0.902 | 0.448 | 4 | 0.000 | 1.000 | 0.000 | 0.799 |
| quantile | 0.935 | False | 0.000 | 0.000 | 0 | 0.118 | 0.943 | 0.057 | 0.581 |
| kde | 0.685 | False | 0.000 | 0.000 | 0 | 0.061 | 1.000 | 0.000 | 0.679 |
| expert | 0.330 | False | 0.877 | 0.317 | 3 | 0.070 | 0.993 | 0.007 | 0.740 |
| opt | 0.833 | True | 0.968 | 0.555 | 10 | 0.095 | 0.933 | 0.085 | 0.823 |
| opt_c6c7 | 0.543 | False | 0.898 | 0.488 | 8 | 0.119 | 0.873 | 0.113 | 0.656 |
| opt_expert | 0.515 | False | 0.896 | 0.478 | 8 | 0.092 | 0.963 | 0.032 | 0.675 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.250 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.188 | 0 |
| opt | 1.000 | 0.714 | 0 |
| opt_c6c7 | 1.000 | 0.615 | 0 |
| opt_expert | 1.000 | 0.571 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*e*f+a*B*c*E*f+A*b*c*D*E*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*e*f+a*B*c*d*E*f+A*b*c*D*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*e*f+a*b*C*d*E*f+a*B*D*f+a*B*c*E*f+a*B*C*e*f+A*b*c*D*e*f+A*b*C*D*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*d*E*f+a*b*c*d*f+a*B*c*E*f+a*B*C*D*f+A*b*c*D*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*c*d*e*f+a*B*D*e*f+a*B*c*f+A*b*c*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*c*e+a*B*c*E*f+A*b*c*D*E*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d*E*f+a*b*c*e+A*b*c*D*E*f<->G |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*f+a*d*f+a*B*f+A*C*D*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*f+a*d*f+a*B*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*e*f+a*B*c*f+A*b*c*D*f<->G |

