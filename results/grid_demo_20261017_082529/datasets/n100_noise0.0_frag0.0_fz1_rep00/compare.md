# n100_noise0.0_frag0.0_fz1_rep00

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=2000
- true model: `f*E*c+E*d*A<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.410 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.548 |
| quantile | 0.221 | False | 0.833 | 0.298 | 1 | 0.037 | 0.963 | 0.040 | 0.545 |
| kde | 0.315 | False | 0.000 | 0.000 | 0 | 0.046 | 0.970 | 0.033 | 0.562 |
| expert | 0.665 | False | 0.000 | 0.000 | 0 | 0.066 | 0.940 | 0.060 | 0.538 |
| opt | 0.761 | True | 0.869 | 0.544 | 7 | 0.147 | 0.953 | 0.038 | 0.804 |
| opt_c6c7 | 0.294 | True | 0.812 | 0.504 | 3 | 0.098 | 0.850 | 0.147 | 0.559 |
| opt_expert | 0.429 | True | 0.837 | 0.531 | 4 | 0.082 | 0.840 | 0.157 | 0.550 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile | 1.000 | 0.100 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.636 | 0 |
| opt_c6c7 | 1.000 | 0.300 | 0 |
| opt_expert | 0.750 | 0.600 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 1 | 1.000 | 1.000 | 0.500 | A*B*c*D*E*f<->G |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+A*C*d*E*F+A*b*c*E*f+A*B*C*d*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*B*c*D*E*f+A*b*c*D*E*f+A*b*C*d*E*F<->G |
| opt_expert | 1 | 0.000 | 0.750 | 1.000 | a*b*c*D*E*f+A*b*c*D*E*F+A*b*C*d*E*F+A*B*c*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*B*c*E<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*E*f+A*b*d*F+A*B*C*d*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | c*D*E*f+A*C*E<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | c*E*f+A*E*F<->G |

