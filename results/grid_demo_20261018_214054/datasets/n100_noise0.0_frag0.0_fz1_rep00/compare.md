# n100_noise0.0_frag0.0_fz1_rep00

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=2000
- true model: `f*E*c+E*d*A<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.975 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.548 |
| quantile | 0.960 | False | 0.000 | 0.000 | 0 | 0.037 | 0.963 | 0.040 | 0.545 |
| kde | 0.935 | False | 0.000 | 0.000 | 0 | 0.046 | 0.970 | 0.033 | 0.562 |
| expert | 1.000 | False | 0.000 | 0.000 | 0 | 0.066 | 0.940 | 0.060 | 0.538 |
| opt | 0.700 | True | 0.913 | 0.517 | 6 | 0.162 | 0.927 | 0.062 | 0.824 |
| opt_c6c7 | 0.405 | False | 0.922 | 0.371 | 3 | 0.091 | 0.857 | 0.152 | 0.574 |
| opt_expert | 0.416 | False | 0.910 | 0.457 | 5 | 0.102 | 0.840 | 0.158 | 0.584 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.750 | 0 |
| opt_c6c7 | 0.667 | 0.333 | 1 |
| opt_expert | 0.800 | 0.571 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+A*C*d*E*F+A*b*c*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 1.000 | A*b*c*D*E*F+A*b*C*d*E*F+A*B*c*D*E*f<->G |
| opt_expert | 1 | 0.000 | 0.750 | 1.000 | B*c*D*E*f+a*c*D*E*f+A*b*c*D*E*F+A*b*C*d*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | c*E*f+A*C*d*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*E+A*b*E*F<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | c*E*f+A*E*F<->G |

