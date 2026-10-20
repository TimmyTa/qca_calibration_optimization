# n400_noise0.2_frag0.2_fz0_rep00

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=35000
- true model: `D*E+B*f<->G`  (irrelevant: A, C)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.569 | True | 0.892 | 0.536 | 11 | 0.000 | 1.000 | 0.000 | 0.806 |
| quantile | 0.319 | False | 0.862 | 0.199 | 1 | 0.109 | 0.962 | 0.012 | 0.610 |
| kde | 0.323 | False | 0.875 | 0.187 | 1 | 0.055 | 1.000 | 0.000 | 0.696 |
| expert | 0.502 | False | 0.903 | 0.342 | 6 | 0.034 | 1.000 | 0.000 | 0.795 |
| opt | 0.729 | True | 0.881 | 0.503 | 14 | 0.067 | 0.980 | 0.029 | 0.827 |
| opt_c6c7 | 0.557 | False | 0.858 | 0.466 | 13 | 0.109 | 0.918 | 0.094 | 0.668 |
| opt_expert | 0.492 | False | 0.838 | 0.471 | 9 | 0.076 | 0.961 | 0.048 | 0.703 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.440 | 0 |
| quantile | 1.000 | 0.037 | 0 |
| kde | 1.000 | 0.040 | 0 |
| expert | 1.000 | 0.240 | 0 |
| opt | 1.000 | 0.538 | 0 |
| opt_c6c7 | 1.000 | 0.520 | 0 |
| opt_expert | 1.000 | 0.333 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+B*c*D*E*f+B*C*D*E*F+a*c*D*E*f+a*C*D*E*F+a*B*C*d*E*f+A*b*c*D*E*F+A*b*C*D*E*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | A*B*c*D*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*B*c*D*E*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+B*c*D*E*f+a*B*C*d*E*f+A*B*C*D*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | C*D*E*F+B*c*d*e*f+a*c*D*E*f+a*B*C*d*E*f+A*C*D*E+A*b*D*E*F+A*B*c*E*f<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | b*D*E*F+B*c*d*e*f+a*c*D*E+a*B*c*d*f+A*C*D*E*F+A*b*D*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+B*c*D*E*f+a*c*D*E*f+a*B*C*d*E*f+a*B*C*D*E*F+A*b*c*D*E*F+A*b*C*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*E*f+b*D*E*f+B*c*d*e*f+a*C*D*E+a*B*C*E+A*c*E+A*B*E*F<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*D*f<->G |
| kde | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*D*f<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d*e*f+B*c*D*E*f+B*C*d*E+A*B*E*F<->G |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*E*f+C*D*E+B*c*d*f+B*C*E+A*D*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E+B*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*E*f+B*c*e*f+B*C*E+A*c*D*E<->G |

