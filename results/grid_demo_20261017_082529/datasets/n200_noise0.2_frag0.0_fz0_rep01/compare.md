# n200_noise0.2_frag0.0_fz0_rep01

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=21001
- true model: `c*B+D*c+a*b*C<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.683 | True | 0.856 | 0.774 | 25 | 0.000 | 1.000 | 0.000 | 0.796 |
| quantile | 0.620 | False | 0.789 | 0.590 | 24 | 0.091 | 0.991 | 0.013 | 0.629 |
| kde | 0.650 | True | 0.821 | 0.744 | 26 | 0.046 | 1.000 | 0.000 | 0.704 |
| expert | 0.672 | True | 0.844 | 0.724 | 25 | 0.059 | 1.000 | 0.000 | 0.800 |
| opt | 0.775 | True | 0.806 | 0.501 | 18 | 0.098 | 0.923 | 0.085 | 0.706 |
| opt_c6c7 | 0.729 | True | 0.813 | 0.538 | 20 | 0.105 | 0.901 | 0.090 | 0.654 |
| opt_expert | 0.723 | True | 0.837 | 0.633 | 21 | 0.074 | 0.977 | 0.020 | 0.691 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.920 | 0.767 | 2 |
| quantile | 0.917 | 0.688 | 2 |
| kde | 0.885 | 0.767 | 3 |
| expert | 0.920 | 0.767 | 2 |
| opt | 1.000 | 0.621 | 0 |
| opt_c6c7 | 1.000 | 0.690 | 0 |
| opt_expert | 1.000 | 0.700 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 1.000 | c*D*F+b*c*D+B*c*e*F+a*c*D+a*b*E*F+a*b*D*F+a*b*C*d*f+A*B*D*e*F+A*B*c*d*E<->G |
| quantile | 1 | 0.000 | 0.750 | 1.000 | c*D*F+b*c*D+B*c*e*F+a*c*D+a*b*D*F+a*b*c*F+a*b*C*E+a*b*C*d*f<->G |
| kde | 1 | 0.000 | 0.556 | 1.000 | b*c*D+a*c*e*F+a*c*D+a*b*E*F+a*b*D*F+a*b*C*d*f+A*b*c*e*f+A*B*c*F+A*B*c*d*E<->G |
| expert | 1 | 0.000 | 0.667 | 1.000 | c*D*F+b*c*D+B*c*e*F+a*c*D+a*b*E*F+a*b*D*F+a*b*C*d*f+A*b*D*e*f+A*B*c*d*E<->G |
| opt | 1 | 1.000 | 1.000 | 0.667 | b*c*D+B*c*F+a*c*D*E+A*B*c*d*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.857 | 0.667 | c*D*e+B*c*e*F+B*c*E*f+B*c*D+a*c*D+a*b*D*E*F+a*B*c*E<->G |
| opt_expert | 1 | 0.000 | 0.857 | 1.000 | c*D*F+b*c*D+B*c*e*F+a*c*D*e+a*b*D*F+a*b*C*d*f+A*B*c*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | D*e*F+c*D+B*c*F+a*b*E+a*b*C*d*f+A*B*c<->G |
| quantile | 2 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | c*D+b*D*F+a*c*F+a*b*E+a*b*C*d*f+A*B*c*e<->G |
| kde | 1 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | c*D+b*D*F+a*c*F+a*b*E+a*b*C*d*f+A*c*e*f+A*B*c<->G |
| expert | 1 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | c*D+b*D*F+B*c*F+a*b*E+a*b*C*d*f+A*b*D+A*B*c<->G |
| opt | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | c*D+B*c*F+A*B*c*E<->G |
| opt_c6c7 | 3 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | c*D+b*D*F+B*c*F+B*c*E<->G |
| opt_expert | 1 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | c*D+B*c*F+a*C*d*f+a*b*D*F+A*B*c<->G |

