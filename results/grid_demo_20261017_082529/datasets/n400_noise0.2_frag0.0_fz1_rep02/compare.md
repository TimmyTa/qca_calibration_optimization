# n400_noise0.2_frag0.0_fz1_rep02

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=34002
- true model: `b*E*a+F*b*A<->G`  (irrelevant: C, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.442 | False | 0.842 | 0.463 | 6 | 0.000 | 1.000 | 0.000 | 0.556 |
| quantile | 0.413 | False | 0.835 | 0.482 | 6 | 0.031 | 0.980 | 0.015 | 0.533 |
| kde | 0.427 | False | 0.836 | 0.480 | 6 | 0.029 | 0.980 | 0.014 | 0.535 |
| expert | 0.466 | False | 0.835 | 0.496 | 7 | 0.020 | 0.995 | 0.005 | 0.550 |
| opt | 0.744 | True | 0.819 | 0.529 | 8 | 0.131 | 0.937 | 0.069 | 0.734 |
| opt_c6c7 | 0.586 | True | 0.823 | 0.503 | 5 | 0.067 | 0.857 | 0.139 | 0.512 |
| opt_expert | 0.592 | True | 0.824 | 0.504 | 5 | 0.066 | 0.869 | 0.132 | 0.520 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.375 | 0 |
| quantile | 1.000 | 0.375 | 0 |
| kde | 1.000 | 0.375 | 0 |
| expert | 1.000 | 0.438 | 0 |
| opt | 1.000 | 0.500 | 0 |
| opt_c6c7 | 1.000 | 0.312 | 0 |
| opt_expert | 1.000 | 0.312 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.500 | 0.500 | b*c*D*E*F+b*C*d*E*F+a*b*C*E*F+a*b*C*d*E<->G |
| quantile | 2 | 0.500 | 0.875 | 1.000 | b*C*d*E*F+a*b*C*E*F+a*b*C*d*E+A*b*c*E*F<->G |
| kde | 2 | 0.500 | 0.875 | 1.000 | b*C*d*E*F+a*b*C*E*F+a*b*C*d*E+A*b*c*E*F<->G |
| expert | 2 | 0.000 | 0.500 | 0.500 | b*c*D*E*F+b*C*d*E*F+a*b*d*E*f+a*b*C*E*F<->G |
| opt | 1 | 0.000 | 0.750 | 1.000 | b*c*D*E*F+a*b*d*E*f+a*b*C*d*E+A*b*c*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.667 | 1.000 | b*c*D*E*F+a*b*C*d*E+A*b*c*E*F<->G |
| opt_expert | 1 | 0.000 | 0.667 | 1.000 | b*c*D*E*F+a*b*C*d*E+A*b*c*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*F+a*b*C*d*f<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*F+a*b*C*d*f<->G |
| kde | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*F+a*b*C*d*f<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*F+a*b*d*E<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*F+a*b*d*E+A*b*c*F<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*F+a*b*C*d+A*b*E*F<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*F+a*b*C*d+A*b*E*F<->G |

