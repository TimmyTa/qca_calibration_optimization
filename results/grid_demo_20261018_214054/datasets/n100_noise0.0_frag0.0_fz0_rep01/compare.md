# n100_noise0.0_frag0.0_fz0_rep01

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=1001
- true model: `c*d+D*F<->G`  (irrelevant: A, B, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.749 | True | 0.958 | 0.884 | 26 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.427 | False | 0.895 | 0.428 | 7 | 0.102 | 0.960 | 0.048 | 0.617 |
| kde | 0.543 | True | 0.922 | 0.693 | 15 | 0.046 | 1.000 | 0.000 | 0.712 |
| expert | 0.676 | True | 0.961 | 0.567 | 22 | 0.062 | 0.958 | 0.042 | 0.732 |
| opt | 0.869 | True | 0.987 | 0.667 | 20 | 0.091 | 0.932 | 0.072 | 0.767 |
| opt_c6c7 | 0.808 | True | 0.947 | 0.631 | 21 | 0.103 | 0.918 | 0.082 | 0.662 |
| opt_expert | 0.786 | True | 0.933 | 0.706 | 22 | 0.087 | 0.923 | 0.077 | 0.693 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.963 | 0 |
| quantile | 1.000 | 0.280 | 0 |
| kde | 1.000 | 0.556 | 0 |
| expert | 0.909 | 0.741 | 2 |
| opt | 1.000 | 1.000 | 0 |
| opt_c6c7 | 1.000 | 1.000 | 0 |
| opt_expert | 1.000 | 1.000 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.778 | 1.000 | c*d*F+c*d*E+b*D*E*F+B*c*F+B*c*d+a*c*F+a*c*d+a*B*D*e*F+A*b*C*D*F<->G |
| quantile | 1 | 0.000 | 0.750 | 1.000 | b*c*d*E*F+a*b*c*e*F+a*B*c*d*E*f+A*c*D*E*F<->G |
| kde | 1 | 0.000 | 0.778 | 1.000 | b*c*E*F+b*c*d*F+a*b*D*E*F+a*b*c*F+a*b*c*d*e+a*B*D*e*F+a*B*c*d*E*f+A*b*C*D*e*F+A*B*c*D*F<->G |
| expert | 1 | 0.000 | 0.500 | 1.000 | c*D*F+b*c*F+B*c*d*E+a*b*c*e+A*c*d*E+A*B*c*e<->G |
| opt | 2 | 0.000 | 0.857 | 1.000 | C*D*e*F+b*D*F+b*c*F+b*c*d*E+a*c*d*E*f+A*c*d*e*f+A*c*D*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.857 | 1.000 | c*D*E*F+b*D*E*F+b*c*F+B*c*d*E*f+B*C*D*e*F+A*D*e*F+A*c*d*f<->G |
| opt_expert | 1 | 0.000 | 0.875 | 1.000 | c*D*E*F+b*D*E*F+b*c*F+b*c*d*e+B*c*d*E*f+B*C*D*e*F+A*D*e*F+A*c*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | c*F+c*d+b*D*F+a*D*F<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*E*F+a*b*c*F+a*B*c*d*f+A*c*D*E*F<->G |
| kde | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*e*F+b*c*F+a*D*e*F+a*b*D*F+a*b*c*e+a*B*c*d*E*f+A*c*D*F<->G |
| expert | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | c*F+c*d+a*b*c*e+A*B*c*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*d<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*d<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*d<->G |

