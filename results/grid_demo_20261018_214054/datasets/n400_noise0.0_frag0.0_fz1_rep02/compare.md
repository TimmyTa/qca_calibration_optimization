# n400_noise0.0_frag0.0_fz1_rep02

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=26002
- true model: `C*f+C*A+e*f<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.362 | False | 0.927 | 0.315 | 3 | 0.000 | 1.000 | 0.000 | 0.549 |
| quantile | 0.451 | False | 0.908 | 0.359 | 3 | 0.036 | 0.978 | 0.023 | 0.540 |
| kde | 0.354 | False | 0.922 | 0.326 | 3 | 0.017 | 0.997 | 0.003 | 0.548 |
| expert | 0.279 | False | 0.909 | 0.287 | 1 | 0.056 | 0.943 | 0.057 | 0.556 |
| opt | 0.810 | True | 0.936 | 0.547 | 18 | 0.143 | 0.966 | 0.032 | 0.807 |
| opt_c6c7 | 0.423 | True | 0.906 | 0.519 | 8 | 0.073 | 0.881 | 0.131 | 0.544 |
| opt_expert | 0.514 | True | 0.910 | 0.504 | 8 | 0.062 | 0.913 | 0.090 | 0.549 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.094 | 0 |
| quantile | 1.000 | 0.097 | 0 |
| kde | 1.000 | 0.094 | 0 |
| expert | 1.000 | 0.031 | 0 |
| opt | 1.000 | 0.562 | 0 |
| opt_c6c7 | 1.000 | 0.267 | 0 |
| opt_expert | 1.000 | 0.250 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | A*C*d*e*f+A*b*C*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | A*C*d*e*f+A*b*C*e*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*C*d*e*f+A*b*C*e*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | A*B*C*d*e*f<->G |
| opt | 3 | 1.000 | 1.000 | 1.000 | c*D*e*f+a*C*D*f+A*C*D*F+A*b*C*D+A*B*C*E*f+A*B*C*d*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*f+A*C*d*E*f+A*b*d*e*f+A*b*C*d*e+A*b*C*D*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | A*d*e*f+A*C*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | A*C*e*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | A*C*e*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | A*C*e*f<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*B*C*e*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | e*f+C*f+A*C<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*f+A*e*f+A*C*e+A*C*D<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e*f+A*C*f<->G |

