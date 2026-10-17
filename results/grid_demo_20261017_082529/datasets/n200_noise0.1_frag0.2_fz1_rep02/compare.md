# n200_noise0.1_frag0.2_fz1_rep02

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=20002
- true model: `d*f+e*F*D<->G`  (irrelevant: A, B, C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.479 | True | 0.873 | 0.536 | 5 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 0.492 | False | 0.879 | 0.486 | 4 | 0.039 | 0.978 | 0.029 | 0.524 |
| kde | 0.322 | False | 0.876 | 0.441 | 4 | 0.067 | 0.929 | 0.072 | 0.549 |
| expert | 0.272 | False | 0.859 | 0.412 | 4 | 0.126 | 0.841 | 0.159 | 0.580 |
| opt | 0.842 | True | 0.906 | 0.581 | 13 | 0.113 | 0.920 | 0.072 | 0.707 |
| opt_c6c7 | 0.585 | True | 0.873 | 0.536 | 5 | 0.064 | 0.873 | 0.122 | 0.537 |
| opt_expert | 0.602 | True | 0.859 | 0.543 | 6 | 0.065 | 0.899 | 0.098 | 0.543 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.238 | 0 |
| quantile | 1.000 | 0.182 | 0 |
| kde | 1.000 | 0.200 | 0 |
| expert | 1.000 | 0.222 | 0 |
| opt | 1.000 | 0.722 | 0 |
| opt_c6c7 | 1.000 | 0.263 | 0 |
| opt_expert | 1.000 | 0.316 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*B*c*D*e*F+A*B*d*e*f+A*B*C*d*f+A*B*C*D*e*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*B*c*D*e*F+A*B*d*e*f+A*B*C*d*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+a*B*c*D*e*F+A*B*d*e*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e*F+a*B*D*e*F+A*B*C*d*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*d*E*f+B*c*D*e*F+a*c*d*E*f+a*b*C*d*e*f+A*c*D*e*F+A*C*d*E*f+A*B*d*f+A*B*D*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*d*E*f+a*B*c*D*e*F+A*B*d*E*f+A*B*c*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*E*f+B*c*D*e*F+A*B*d*E*f+A*B*c*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*c*D+A*d*e*f+A*B*C*e*F+A*B*C*d*f<->G |
| quantile | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*e*f+B*C*d*f+a*B*D*e<->G |
| kde | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*e*f+B*c*D*e+A*e<->G |
| expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | e*F+A*d<->G |
| opt | 2 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | D*e*F+C*d*f+B*d*f+a*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d*f+a*B*D*e*F+A*d*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*f+B*D*e<->G |

