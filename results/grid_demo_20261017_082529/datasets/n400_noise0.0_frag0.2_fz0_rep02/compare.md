# n400_noise0.0_frag0.2_fz0_rep02

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=27002
- true model: `A*f+B*D<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 7, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.680 | True | 0.929 | 0.769 | 15 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.673 | False | 0.888 | 0.496 | 9 | 0.106 | 0.983 | 0.036 | 0.607 |
| kde | 0.661 | True | 0.875 | 0.745 | 15 | 0.056 | 1.000 | 0.000 | 0.691 |
| expert | 0.661 | True | 0.959 | 0.585 | 11 | 0.070 | 0.982 | 0.018 | 0.741 |
| opt | 0.869 | True | 0.873 | 0.503 | 9 | 0.122 | 0.910 | 0.098 | 0.705 |
| opt_c6c7 | 0.784 | True | 0.854 | 0.573 | 11 | 0.122 | 0.897 | 0.107 | 0.637 |
| opt_expert | 0.730 | True | 0.906 | 0.558 | 10 | 0.081 | 0.950 | 0.057 | 0.665 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.682 | 0 |
| quantile | 1.000 | 0.346 | 0 |
| kde | 1.000 | 0.682 | 0 |
| expert | 1.000 | 0.458 | 0 |
| opt | 1.000 | 0.333 | 0 |
| opt_c6c7 | 1.000 | 0.423 | 0 |
| opt_expert | 1.000 | 0.400 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+B*C*D*f+B*C*D*e+a*B*D*e+A*b*d*e*f+A*b*C*d*f+A*B*c*d*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+B*C*D*E*f+a*B*D*e*F+A*B*c*d*e*f+A*B*C*D*e<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+B*C*D*f+B*C*D*e+a*B*D*e+A*b*d*e*f+A*b*C*d*f+A*B*c*d*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+a*B*D*e*F+a*B*c*D*e+A*b*d*e*f+A*B*c*d*f+A*B*C*D*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*D*e+a*B*D*e+a*B*C*D*f+A*B*d*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*C*D*f+B*C*D*E+a*B*D*E*F+A*b*c*d*e*f+A*B*d*E*f+A*B*C*f<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+a*B*D*e*F+a*B*c*D*e+A*c*d*e*f+A*B*D*E*f+A*B*c*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*D+A*f<->G |
| quantile | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | B*D+B*c*e<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*D+A*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*D+A*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*D+A*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*e+B*D+A*B*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*D+A*f<->G |

