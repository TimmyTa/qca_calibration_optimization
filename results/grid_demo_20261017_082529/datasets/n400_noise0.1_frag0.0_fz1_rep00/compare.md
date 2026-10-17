# n400_noise0.1_frag0.0_fz1_rep00

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=30000
- true model: `E*C*d+A*f<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.386 | False | 0.844 | 0.456 | 4 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 0.474 | True | 0.845 | 0.501 | 7 | 0.027 | 0.982 | 0.012 | 0.529 |
| kde | 0.430 | False | 0.842 | 0.448 | 3 | 0.040 | 0.971 | 0.031 | 0.545 |
| expert | 0.407 | False | 0.839 | 0.476 | 4 | 0.029 | 0.982 | 0.018 | 0.546 |
| opt | 0.869 | True | 0.824 | 0.555 | 15 | 0.107 | 0.927 | 0.071 | 0.696 |
| opt_c6c7 | 0.618 | True | 0.845 | 0.516 | 8 | 0.068 | 0.887 | 0.115 | 0.535 |
| opt_expert | 0.585 | True | 0.843 | 0.515 | 8 | 0.051 | 0.899 | 0.098 | 0.526 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.182 | 0 |
| quantile | 1.000 | 0.318 | 0 |
| kde | 1.000 | 0.136 | 0 |
| expert | 1.000 | 0.182 | 0 |
| opt | 1.000 | 0.714 | 0 |
| opt_c6c7 | 1.000 | 0.381 | 0 |
| opt_expert | 1.000 | 0.381 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | A*c*D*E*f+A*B*c*D*f+A*B*C*d*E*f<->G |
| quantile | 4 | 1.000 | 1.000 | 0.750 | A*c*D*E*f+A*b*C*E*f+A*B*d*E*f+A*B*c*D*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*b*c*D*E*f+A*B*c*D*e*f+A*B*C*d*E*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | A*c*D*E*f+A*B*c*D*f+A*B*C*d*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*f+A*D*E*f+A*C*f+A*B*f+A*B*C*d*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | A*d*E*f+A*c*E*f+A*B*c*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | A*c*D*E*f+A*C*d*E*f+A*B*d*f+A*B*c*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*E*f+A*c*D*E*f+A*B*D*f<->G |
| quantile | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*E*f+A*B*c*f<->G |
| kde | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*D*E*f+A*C*d*E+A*B*c*D*f<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*D*E*f+A*B*D*e*f+A*B*C*d*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*d*E+A*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | A*d*f+A*c*f<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*d*E*f+A*c*f+A*B*e*f<->G |

