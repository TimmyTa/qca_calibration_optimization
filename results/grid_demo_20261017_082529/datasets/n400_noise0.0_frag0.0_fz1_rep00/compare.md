# n400_noise0.0_frag0.0_fz1_rep00

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=26000
- true model: `d*C*b+B*A<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.489 | True | 0.868 | 0.551 | 8 | 0.000 | 1.000 | 0.000 | 0.548 |
| quantile | 0.519 | True | 0.860 | 0.584 | 10 | 0.032 | 0.982 | 0.021 | 0.542 |
| kde | 0.484 | True | 0.863 | 0.568 | 9 | 0.019 | 0.990 | 0.010 | 0.547 |
| expert | 0.646 | False | 0.873 | 0.588 | 10 | 0.074 | 0.912 | 0.087 | 0.542 |
| opt | 0.868 | True | 0.848 | 0.644 | 18 | 0.101 | 0.897 | 0.101 | 0.677 |
| opt_c6c7 | 0.751 | True | 0.860 | 0.599 | 8 | 0.068 | 0.904 | 0.100 | 0.541 |
| opt_expert | 0.759 | True | 0.856 | 0.606 | 8 | 0.068 | 0.904 | 0.104 | 0.539 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.333 | 0 |
| quantile | 1.000 | 0.417 | 0 |
| kde | 1.000 | 0.375 | 0 |
| expert | 1.000 | 0.417 | 0 |
| opt | 1.000 | 0.750 | 0 |
| opt_c6c7 | 1.000 | 0.348 | 0 |
| opt_expert | 1.000 | 0.333 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*f+A*B*d*E+A*B*C*d<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*f+A*B*d<->G |
| kde | 1 | 0.000 | 0.667 | 0.500 | A*C*d*e*f+A*B*d*E+A*B*C*F<->G |
| expert | 1 | 0.000 | 0.667 | 0.500 | A*C*d*e*F+A*B*d+A*B*C*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*d*F+b*C*d*e+A*B*e*F+A*B*d+A*B*C*F+A*B*C*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*e*f+A*B*d*f+A*B*d*e+A*B*c*d<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*e*f+A*B*d*f+A*B*d*e+A*B*c*d<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e*f+A*B*d<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e*f+A*B*d<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*C*d*f+A*B*d+A*B*C*F<->G |
| expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | A*C*e*F+A*B<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*C*d+A*B<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*C*d*e+A*B*d<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*C*d*e+A*B*d<->G |

