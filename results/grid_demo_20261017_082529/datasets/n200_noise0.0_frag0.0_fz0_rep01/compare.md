# n200_noise0.0_frag0.0_fz0_rep01

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=13001
- true model: `E*C+b*A*f<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.729 | True | 0.935 | 0.796 | 13 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.515 | False | 0.819 | 0.442 | 6 | 0.111 | 0.967 | 0.022 | 0.587 |
| kde | 0.675 | True | 0.855 | 0.751 | 12 | 0.065 | 1.000 | 0.000 | 0.678 |
| expert | 0.730 | True | 0.930 | 0.773 | 13 | 0.029 | 1.000 | 0.000 | 0.788 |
| opt | 0.845 | True | 0.889 | 0.651 | 12 | 0.078 | 0.947 | 0.058 | 0.768 |
| opt_c6c7 | 0.775 | True | 0.827 | 0.658 | 13 | 0.101 | 0.940 | 0.073 | 0.628 |
| opt_expert | 0.779 | True | 0.884 | 0.678 | 11 | 0.082 | 0.978 | 0.020 | 0.664 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.684 | 0 |
| quantile | 1.000 | 0.273 | 0 |
| kde | 1.000 | 0.632 | 0 |
| expert | 1.000 | 0.684 | 0 |
| opt | 1.000 | 0.667 | 0 |
| opt_c6c7 | 1.000 | 0.765 | 0 |
| opt_expert | 1.000 | 0.550 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*F+B*C*d*E*f+a*b*C*D*E*f+A*C*d*E+A*b*D*e*f+A*b*c*e*f+A*b*c*D*f+A*B*C*E<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*E*f+A*C*d*E*f+A*b*D*e*f+A*b*c*D*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*F+B*C*d*E*f+a*b*C*D*E*f+A*C*d*E+A*b*D*e*f+A*b*c*D*f+A*B*C*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*F+B*C*d*E*f+a*b*C*D*E*f+A*C*d*E+A*b*D*e*f+A*b*c*e*f+A*b*c*D*f+A*B*C*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | C*d*E*f+a*b*C*E*f+a*b*C*d*E+A*b*D*e*f+A*b*c*D*f+A*B*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | C*d*E*f+a*b*C*E*f+a*b*C*d*E+A*b*c*D*f+A*b*C*e*f+A*B*C*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*C*d*E*F+a*b*C*D*E*f+A*C*d*E*f+A*b*D*e*f+A*b*c*e*f+A*b*c*D*f+A*B*C*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*E+A*b*f<->G |
| quantile | 4 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | C*d*E*f+a*C*D*E+A*b*f<->G |
| kde | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | C*E+A*b*D*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*E+A*b*f<->G |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | C*E+b*D*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | C*E+A*b*D+A*b*C*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*E+A*b*f<->G |

