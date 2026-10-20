# n100_noise0.0_frag0.2_fz1_rep00

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=4000
- true model: `c*E+D*e+C*B<->G`  (irrelevant: A, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.595 | True | 0.938 | 0.756 | 24 | 0.000 | 1.000 | 0.000 | 0.551 |
| quantile | 0.540 | True | 0.936 | 0.693 | 24 | 0.065 | 0.935 | 0.057 | 0.520 |
| kde | 0.592 | False | 0.941 | 0.679 | 14 | 0.129 | 0.845 | 0.155 | 0.601 |
| expert | 0.581 | True | 0.947 | 0.710 | 25 | 0.083 | 0.932 | 0.068 | 0.579 |
| opt | 0.704 | True | 0.976 | 0.684 | 20 | 0.111 | 0.922 | 0.068 | 0.679 |
| opt_c6c7 | 0.612 | True | 0.903 | 0.713 | 26 | 0.066 | 0.885 | 0.102 | 0.520 |
| opt_expert | 0.626 | True | 0.931 | 0.686 | 22 | 0.074 | 0.862 | 0.135 | 0.522 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.686 | 0 |
| quantile | 0.917 | 0.629 | 2 |
| kde | 0.857 | 0.429 | 2 |
| expert | 0.920 | 0.767 | 2 |
| opt | 1.000 | 0.667 | 0 |
| opt_c6c7 | 0.808 | 0.700 | 5 |
| opt_expert | 0.955 | 0.750 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 8 | 0.000 | 0.864 | 1.000 | b*c*D*E*f+b*C*D*e*f+B*c*D*e+B*C*d*F+B*C*d*e+a*D*e*F+a*c*d*E*F+a*B*c*E*F+A*B*d*E*f+A*B*D*e*f+A*B*C*E*F<->G |
| quantile | 4 | 0.000 | 0.682 | 1.000 | b*c*D*E+b*C*D*e+B*c*D*e*f+a*c*E*F+a*b*C*D*f+a*B*d*E*F+a*B*D*e*F+a*B*C*d*e*f+A*D*E*F+A*b*D*F+A*B*C*d*E<->G |
| kde | 1 | 0.000 | 0.200 | 0.333 | B*d*E*f+a*b*D*e*f+a*B*c*f+A*c*D*f+A*B*c*d*e*F<->G |
| expert | 2 | 0.000 | 0.773 | 1.000 | b*D*e*F+B*c*D*e*f+a*c*d*E*F+a*b*C*e+a*B*d*E*F+a*B*c*E*F+A*D*e*f+A*c*d*E*f+A*c*D*e+A*b*c*D+A*B*C*d<->G |
| opt | 2 | 0.000 | 0.875 | 0.667 | B*d*E*F+B*c*D*e+B*C*e*F+a*b*C*D*e+A*D*e*F+A*B*C*F+A*B*C*e+A*B*C*d<->G |
| opt_c6c7 | 8 | 0.000 | 0.458 | 0.667 | b*C*D*f+B*c*D*e*f+a*D*e*F+a*c*D*F+a*b*C*d*E+a*B*d*E*F+A*b*D*F+A*B*D*e*f+A*B*c*D*f+A*B*C*E*F+A*B*C*d*F+A*B*C*d*E<->G |
| opt_expert | 1 | 0.000 | 0.778 | 1.000 | b*c*D*F+b*C*D*e+B*c*D*e*f+B*C*d*e*F+a*D*e*F+a*c*E*F+a*c*D*E+a*b*D*F+A*B*C*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | D+c*E+B*C<->G |
| quantile | 3 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | D+c*E*F+B*C<->G |
| kde | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | F+D*e+a*B+A*E<->G |
| expert | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | D+c*E+B*C+a*C*e<->G |
| opt | 2 | 0.500 | 0.833 | 0.833 | 0.000 | 0.000 | D+c*E+B*C<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | E+D+B*C<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | D+c*E+B*C<->G |

