# n200_noise0.2_frag0.2_fz1_rep02

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=24002
- true model: `D*c+C*E+D*B<->G`  (irrelevant: A, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.350 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.551 |
| quantile | 0.189 | False | 0.931 | 0.252 | 1 | 0.038 | 0.969 | 0.029 | 0.536 |
| kde | 0.199 | False | 0.931 | 0.250 | 1 | 0.028 | 0.972 | 0.031 | 0.541 |
| expert | 0.355 | False | 0.000 | 0.000 | 0 | 0.129 | 0.853 | 0.147 | 0.578 |
| opt | 0.637 | True | 0.886 | 0.539 | 12 | 0.135 | 0.873 | 0.128 | 0.710 |
| opt_c6c7 | 0.312 | False | 0.885 | 0.441 | 4 | 0.085 | 0.867 | 0.136 | 0.550 |
| opt_expert | 0.321 | False | 0.883 | 0.456 | 5 | 0.086 | 0.869 | 0.128 | 0.542 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile | 1.000 | 0.031 | 0 |
| kde | 1.000 | 0.030 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.387 | 0 |
| opt_c6c7 | 1.000 | 0.143 | 0 |
| opt_expert | 1.000 | 0.172 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 1 | 1.000 | 1.000 | 0.333 | a*B*C*d*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 0.333 | a*B*C*d*E*f<->G |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | c*D*E*f+b*c*D*f+a*b*C*E*F+a*B*C*E*f+a*B*C*D*f+A*B*C*D*E*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*B*C*E*f+A*B*c*D*E*f+A*B*C*D*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+a*B*C*E*f+A*B*C*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*E*f<->G |
| kde | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*E*f<->G |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*E*f+b*c*D*f+a*C*E*f+a*C*D*e+a*b*C+A*D*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*E+a*C*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*E+a*B*C*E*f<->G |

