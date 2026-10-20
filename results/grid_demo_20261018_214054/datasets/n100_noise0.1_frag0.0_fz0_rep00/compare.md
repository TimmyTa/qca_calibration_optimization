# n100_noise0.1_frag0.0_fz0_rep00

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=5000
- true model: `C*E*b+A*D<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.355 | False | 0.882 | 0.447 | 5 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.810 | False | 0.000 | 0.000 | 0 | 0.102 | 0.973 | 0.023 | 0.634 |
| kde | 0.625 | False | 0.000 | 0.000 | 0 | 0.052 | 1.000 | 0.000 | 0.705 |
| expert | 0.421 | False | 0.883 | 0.424 | 6 | 0.071 | 0.945 | 0.055 | 0.770 |
| opt | 0.797 | True | 0.958 | 0.517 | 11 | 0.130 | 0.875 | 0.143 | 0.769 |
| opt_c6c7 | 0.673 | True | 0.911 | 0.506 | 12 | 0.107 | 0.900 | 0.115 | 0.664 |
| opt_expert | 0.566 | True | 0.869 | 0.506 | 10 | 0.083 | 0.942 | 0.047 | 0.698 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.294 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.375 | 0 |
| opt | 1.000 | 1.000 | 0 |
| opt_c6c7 | 1.000 | 1.000 | 0 |
| opt_expert | 1.000 | 0.667 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*E*f+A*b*c*D*e*F+A*b*C*d*E*f+A*b*C*D*e*f+A*b*C*D*E*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*C*D*E*f+A*C*D*E*F+A*b*c*D*e*F+A*b*C*D*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*D*E*f+A*c*D*e*F+A*c*D*E*f+A*b*D*e*F+A*b*c*D+A*b*C*E*f+A*B*C*D*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*E*f+A*b*c*D+A*b*C*d*E*f+A*B*D*f+A*B*D*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*E*f+A*c*D*e+A*b*D*e*f+A*b*c*D*f+A*b*C*d*E*f+A*b*C*D*E*F+A*B*C*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*e*F+b*C*D*E+A*b*C*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*E*f+A*C*D*E*F+A*b*D*f+A*b*c*D<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*C*E+A*D<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*C*E+A*D<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*E+A*D*E+A*c*D+A*b*C*f<->G |

