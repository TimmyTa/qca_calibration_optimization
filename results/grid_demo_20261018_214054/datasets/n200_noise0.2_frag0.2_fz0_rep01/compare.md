# n200_noise0.2_frag0.2_fz0_rep01

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=23001
- true model: `F*b+f*e*a<->G`  (irrelevant: C, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.369 | False | 0.888 | 0.326 | 4 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.685 | False | 0.000 | 0.000 | 0 | 0.108 | 0.965 | 0.023 | 0.606 |
| kde | 0.695 | False | 0.000 | 0.000 | 0 | 0.058 | 1.000 | 0.000 | 0.691 |
| expert | 0.552 | True | 0.882 | 0.552 | 10 | 0.034 | 1.000 | 0.000 | 0.806 |
| opt | 0.699 | True | 0.890 | 0.502 | 9 | 0.081 | 0.944 | 0.054 | 0.819 |
| opt_c6c7 | 0.504 | False | 0.846 | 0.455 | 9 | 0.111 | 0.935 | 0.071 | 0.659 |
| opt_expert | 0.354 | False | 0.849 | 0.383 | 6 | 0.087 | 0.962 | 0.044 | 0.686 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.182 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.455 | 0 |
| opt | 1.000 | 0.429 | 0 |
| opt_c6c7 | 1.000 | 0.429 | 0 |
| opt_expert | 1.000 | 0.273 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | a*b*C*D*e*F+A*b*c*d*E*F+A*b*c*D*e*F+A*b*C*d*e*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 0.000 | 0.833 | 1.000 | a*b*d*e*f+a*b*C*D*e+a*B*D*e*f+A*b*c*E*F+A*b*c*D*F+A*b*C*d*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*c*d*E*F+a*b*c*d*e*f+a*b*C*D*e*F+a*B*D*e*f+A*b*c*D*F+A*b*C*d*e*F<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | a*C*D*e*f+a*b*d*e*f+a*B*D*e*f+A*b*d*e*F+A*b*c*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*d*e*f+a*B*D*e*f+A*b*c*d*E*F+A*b*c*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*F+C*d*e*F+a*b*D*F+A*b*d*E*F<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*F+C*d*e*F+a*d*e*f+a*b*C*e+a*B*e*f+A*b*E*F<->G |
| opt | 12 | 0.000 | 0.133 | 0.333 | 0.000 | 1.000 | C*d*e*F+b*c*d*E*F+a*e*f+a*C*e+A*c*D*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*e*F+a*e+A*b*c*F<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*F+a*D*e*f+a*b*e*f+A*b*c*d*E*F<->G |

