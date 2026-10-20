# n400_noise0.1_frag0.0_fz0_rep00

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=29000
- true model: `a*f*d+c*f*B<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.302 | False | 0.883 | 0.202 | 1 | 0.000 | 1.000 | 0.000 | 0.799 |
| quantile | 1.000 | False | 0.000 | 0.000 | 0 | 0.106 | 0.981 | 0.017 | 0.606 |
| kde | 1.000 | False | 0.000 | 0.000 | 0 | 0.062 | 1.000 | 0.000 | 0.680 |
| expert | 0.543 | False | 0.916 | 0.258 | 3 | 0.036 | 1.000 | 0.000 | 0.804 |
| opt | 0.659 | True | 0.859 | 0.503 | 9 | 0.080 | 0.983 | 0.014 | 0.861 |
| opt_c6c7 | 0.502 | False | 0.878 | 0.375 | 5 | 0.135 | 0.893 | 0.105 | 0.644 |
| opt_expert | 0.407 | False | 0.864 | 0.383 | 5 | 0.099 | 0.926 | 0.055 | 0.693 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.071 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.214 | 0 |
| opt | 1.000 | 0.643 | 0 |
| opt_c6c7 | 1.000 | 0.385 | 0 |
| opt_expert | 1.000 | 0.357 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | A*B*c*d*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*d*e*f+A*B*c*d*e*f<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+a*C*d*e*f+a*b*c*d*f+a*B*C*d*f+A*B*c*d*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*C*d*e*f+A*B*c*e*f+A*B*c*D*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*E*f+a*b*C*d*e*f+A*B*c*E*f+A*B*c*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*B*c*d*e<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*d*e*f+A*B*c*d*e<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*f+a*C*d*e*f+a*B*E*f+A*B*c*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | a*d*f+A*B*c*f<->G |
| opt_expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*E*f+a*C*e+A*B*c*f<->G |

