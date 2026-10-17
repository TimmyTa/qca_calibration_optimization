# n400_noise0.0_frag0.0_fz0_rep00

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=25000
- true model: `F*D+C*e*A<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.710 | True | 0.917 | 0.799 | 16 | 0.000 | 1.000 | 0.000 | 0.805 |
| quantile | 0.475 | False | 0.821 | 0.368 | 6 | 0.100 | 0.984 | 0.031 | 0.620 |
| kde | 0.541 | True | 0.829 | 0.701 | 13 | 0.056 | 1.000 | 0.000 | 0.696 |
| expert | 0.701 | True | 0.884 | 0.790 | 16 | 0.030 | 1.000 | 0.000 | 0.807 |
| opt | 0.891 | True | 0.894 | 0.501 | 11 | 0.103 | 0.919 | 0.093 | 0.762 |
| opt_c6c7 | 0.847 | True | 0.892 | 0.528 | 8 | 0.121 | 0.880 | 0.157 | 0.629 |
| opt_expert | 0.781 | True | 0.908 | 0.501 | 10 | 0.093 | 0.954 | 0.057 | 0.661 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.727 | 0 |
| quantile | 1.000 | 0.273 | 0 |
| kde | 1.000 | 0.591 | 0 |
| expert | 1.000 | 0.727 | 0 |
| opt | 1.000 | 0.524 | 0 |
| opt_c6c7 | 1.000 | 0.381 | 0 |
| opt_expert | 1.000 | 0.455 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*D*E*F+b*c*D*F+B*D*e*F+a*D*F+A*b*C*D*e*f+A*B*C*d*e<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | C*D*e*F+a*C*D*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*C*D*E*F+a*D*E*F+a*C*D*F+a*b*D*F+A*c*D*e*F+A*b*C*D*e*f+A*B*C*e*F<->G |
| expert | 2 | 1.000 | 1.000 | 1.000 | b*D*E*F+b*c*D*F+B*D*e*F+a*D*F+A*b*C*D*e*f+A*B*C*d*e<->G |
| opt | 1 | 1.000 | 1.000 | 0.500 | c*D*e*F+b*c*D*F+a*D*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | c*D*e*F+a*D*e*F+a*b*D*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | b*c*D*F+a*D*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+A*C*e<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | C*D*e*F+a*C*D*F<->G |
| kde | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*D*F+a*D*E*F+a*b*F+A*e*F+A*C*D*e<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+A*C*e<->G |
| opt | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*F<->G |

