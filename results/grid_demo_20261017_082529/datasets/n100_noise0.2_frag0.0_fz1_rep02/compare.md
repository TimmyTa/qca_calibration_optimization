# n100_noise0.2_frag0.0_fz1_rep02

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=10002
- true model: `E*d+C*f+E*c*F<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.626 | False | 0.719 | 0.791 | 50 | 0.000 | 1.000 | 0.000 | 0.549 |
| quantile | 0.627 | False | 0.736 | 0.769 | 50 | 0.047 | 0.958 | 0.037 | 0.517 |
| kde | 0.616 | False | 0.729 | 0.770 | 53 | 0.041 | 0.967 | 0.028 | 0.518 |
| expert | 0.680 | False | 0.723 | 0.764 | 42 | 0.072 | 0.927 | 0.073 | 0.545 |
| opt | 0.779 | True | 0.900 | 0.660 | 20 | 0.146 | 0.910 | 0.085 | 0.778 |
| opt_c6c7 | 0.642 | False | 0.780 | 0.752 | 34 | 0.081 | 0.865 | 0.133 | 0.512 |
| opt_expert | 0.624 | False | 0.774 | 0.752 | 35 | 0.085 | 0.850 | 0.145 | 0.511 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.560 | 1.000 | 22 |
| quantile | 0.600 | 1.000 | 20 |
| kde | 0.566 | 1.000 | 23 |
| expert | 0.476 | 1.000 | 22 |
| opt | 0.900 | 0.857 | 2 |
| opt_c6c7 | 0.618 | 0.955 | 13 |
| opt_expert | 0.600 | 0.913 | 14 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.318 | 0.667 | C*d*E*F+C*D*f+b*e*F+b*c*d+b*C*E+B*c*E*f+B*c*D+B*C*e*f+a*f+a*B*E+A*b*F<->G |
| quantile | 6 | 0.000 | 0.283 | 0.611 | E*f+C*d*E+C*D*f+b*c*d*f+B*D*E+B*c*D+B*C*f+a*c+a*b*e+A*b*E<->G |
| kde | 2 | 0.000 | 0.182 | 0.333 | E*f+c*D*F+C*E+C*D*f+b*E+b*c*d*f+b*C*d*F+B*D*f+B*C*f+a*c+a*b<->G |
| expert | 6 | 0.000 | 0.273 | 0.667 | c*D*e*F+C*E*F+b*C+B*c*D*f+a*d*E*F+a*C*d*F+a*C*d*E+a*b*f+a*b*d+A*C*e*f+A*b*F<->G |
| opt | 1 | 0.000 | 0.778 | 1.000 | b*C*d*f+a*d*E*f+a*C*d*E+a*b*d*E+a*b*c*D*e*F+a*b*C*f+A*c*D*E*F+A*C*E*f+A*b*C*E<->G |
| opt_c6c7 | 6 | 0.000 | 0.385 | 1.000 | b*d*f+b*C*e*f+B*C*D*E+a*c*E*f+a*c*D*e*F+a*C*E*F+a*C*d*f+a*b*c*d*e+A*c*d*E*F+A*C*E*f+A*b*e*f+A*b*c*E*F+A*B*D*f<->G |
| opt_expert | 2 | 0.000 | 0.300 | 0.667 | D*E*f+b*d*f+b*C*f+B*C*E+a*E*f+a*c*e*F+a*C*E+a*C*d*f+A*b*d*E+A*B*c*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.400 | 1.000 | 0.000 | 1.000 | E+c*D+C*f+b+a*f<->G |
| quantile | 1 | 0.000 | 0.250 | 0.667 | 0.000 | 1.000 | d*E+C*f+b*f+B*E+B*c*D+a*c+a*b*e+A*E<->G |
| kde | 2 | 0.000 | 0.286 | 1.000 | 0.000 | 1.000 | E+c*D+C*f+b*f+b*C*d+a*D+a*c<->G |
| expert | 1 | 0.000 | 0.400 | 1.000 | 0.000 | 1.000 | E+c*D+C*f+b+a*C*d<->G |
| opt | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | d*E+b*c*D*F+b*C*f+A*E<->G |
| opt_c6c7 | 3 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | D*f+c*E+b*f+B*E+a*D+a*C*f+a*b<->G |
| opt_expert | 3 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | d*E+c*D+b*f+B*E+a*D+a*c*F+a*C*f<->G |

