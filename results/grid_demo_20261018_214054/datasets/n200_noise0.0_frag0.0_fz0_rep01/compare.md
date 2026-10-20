# n200_noise0.0_frag0.0_fz0_rep01

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=13001
- true model: `E*C+b*A*f<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.711 | True | 0.941 | 0.763 | 12 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.580 | False | 0.000 | 0.000 | 0 | 0.111 | 0.967 | 0.022 | 0.587 |
| kde | 0.540 | False | 0.000 | 0.000 | 0 | 0.065 | 1.000 | 0.000 | 0.678 |
| expert | 0.684 | True | 0.935 | 0.726 | 11 | 0.029 | 1.000 | 0.000 | 0.788 |
| opt | 0.850 | True | 0.916 | 0.664 | 12 | 0.071 | 0.953 | 0.036 | 0.816 |
| opt_c6c7 | 0.694 | True | 0.923 | 0.569 | 11 | 0.112 | 0.912 | 0.098 | 0.636 |
| opt_expert | 0.674 | True | 0.899 | 0.620 | 10 | 0.085 | 0.970 | 0.034 | 0.676 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.632 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.579 | 0 |
| opt | 1.000 | 0.667 | 0 |
| opt_c6c7 | 1.000 | 0.611 | 0 |
| opt_expert | 1.000 | 0.476 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*F+B*C*d*E*f+a*b*C*D*E*f+A*C*d*E+A*b*D*e*f+A*b*c*D*f+A*B*C*E<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E*f+a*b*C*d*E*F+a*b*C*D*E*f+A*C*d*E*f+A*b*D*e*f+A*b*c*D*f+A*B*C*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | C*d*E*f+a*b*C*E*f+a*b*C*d*E+A*b*D*e*f+A*b*c*D*f+A*B*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*f+a*C*D*E*f+A*b*D*e*f+A*b*c*D*f+A*B*C*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*F+a*b*C*D*E*f+A*C*d*E*f+A*b*D*e*f+A*b*c*D*f+A*B*C*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | C*E+A*b*D*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E*f+B*C*E+a*C*E+A*b*D*f<->G |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | C*E+A*b*D<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | C*E+A*b*D<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | C*E+A*b*D<->G |

