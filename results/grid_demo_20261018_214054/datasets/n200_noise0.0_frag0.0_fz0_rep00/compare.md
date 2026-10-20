# n200_noise0.0_frag0.0_fz0_rep00

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=13000
- true model: `D*A+b*D*E<->G`  (irrelevant: C, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.401 | True | 0.899 | 0.504 | 5 | 0.000 | 1.000 | 0.000 | 0.794 |
| quantile | 0.910 | False | 0.000 | 0.000 | 0 | 0.120 | 0.953 | 0.042 | 0.573 |
| kde | 0.695 | False | 0.000 | 0.000 | 0 | 0.060 | 1.000 | 0.000 | 0.677 |
| expert | 0.630 | True | 0.923 | 0.561 | 10 | 0.060 | 1.000 | 0.000 | 0.775 |
| opt | 0.864 | True | 0.972 | 0.511 | 8 | 0.123 | 0.889 | 0.126 | 0.701 |
| opt_c6c7 | 0.765 | True | 0.935 | 0.505 | 6 | 0.133 | 0.877 | 0.145 | 0.617 |
| opt_expert | 0.581 | True | 0.919 | 0.506 | 8 | 0.085 | 0.969 | 0.044 | 0.673 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.312 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.625 | 0 |
| opt | 1.000 | 0.500 | 0 |
| opt_c6c7 | 1.000 | 0.400 | 0 |
| opt_expert | 1.000 | 0.444 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | A*c*D*E*F+A*b*c*D*E+A*B*D*e*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | A*c*D*F+A*c*D*e+A*b*D*E*F+A*b*c*D+A*B*C*D*f<->G |
| opt | 1 | 1.000 | 1.000 | 0.500 | A*c*D*f+A*c*D*E+A*B*D*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | A*c*D*e*f+A*b*D*f+A*b*c*D*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | A*c*D*F+A*b*c*D+A*B*D*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*D*E+A*B*D*e*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*D*E+A*c*D+A*B*D<->G |
| opt | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | A*D<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | A*D<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*D*e+A*c*D<->G |

