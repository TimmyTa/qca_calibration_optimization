# n400_noise0.1_frag0.2_fz1_rep00

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=32000
- true model: `b*f*D+f*d*e+b*c*e<->G`  (irrelevant: A)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.218 | False | 0.848 | 0.368 | 2 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 0.265 | False | 0.000 | 0.000 | 0 | 0.032 | 0.987 | 0.027 | 0.525 |
| kde | 0.266 | False | 0.837 | 0.394 | 2 | 0.028 | 0.990 | 0.020 | 0.533 |
| expert | 0.292 | False | 0.841 | 0.448 | 3 | 0.049 | 0.943 | 0.057 | 0.541 |
| opt | 0.854 | True | 0.866 | 0.522 | 8 | 0.121 | 0.955 | 0.038 | 0.754 |
| opt_c6c7 | 0.383 | True | 0.822 | 0.518 | 5 | 0.060 | 0.895 | 0.107 | 0.528 |
| opt_expert | 0.368 | True | 0.826 | 0.515 | 4 | 0.054 | 0.914 | 0.086 | 0.520 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.105 | 0 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.100 | 0 |
| expert | 1.000 | 0.158 | 0 |
| opt | 1.000 | 0.421 | 0 |
| opt_c6c7 | 1.000 | 0.278 | 0 |
| opt_expert | 1.000 | 0.211 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | A*b*c*D*e*f+A*B*c*d*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*b*c*D*e*f+A*B*c*d*e*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*f+A*b*C*D*E*f+A*B*c*d*e*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e*f+A*b*c*e*F+A*b*C*D*f+A*B*d*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*D*e*f+a*b*c*D*e+a*B*C*d*e*f+A*B*c*d*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*F+a*b*C*D*e*f+a*B*C*d*e*f+A*B*c*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*e*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*e*f<->G |
| expert | 54 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*e+A*c*e*f+A*C*D*E<->G |
| opt | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*c*e+B*d*e+A*b*D*f<->G |
| opt_c6c7 | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D+a*C*d*f+a*b*D*f+A*c*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*e+a*C*d*f+A*c*f<->G |

