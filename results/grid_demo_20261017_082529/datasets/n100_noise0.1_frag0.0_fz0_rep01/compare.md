# n100_noise0.1_frag0.0_fz0_rep01

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=5001
- true model: `C*F*e+A*C*b<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.615 | True | 0.864 | 0.672 | 9 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.287 | False | 0.804 | 0.299 | 1 | 0.113 | 0.952 | 0.035 | 0.614 |
| kde | 0.198 | False | 0.819 | 0.280 | 1 | 0.060 | 1.000 | 0.000 | 0.695 |
| expert | 0.572 | True | 0.822 | 0.656 | 9 | 0.038 | 1.000 | 0.000 | 0.764 |
| opt | 0.728 | True | 0.890 | 0.557 | 6 | 0.087 | 0.947 | 0.060 | 0.841 |
| opt_c6c7 | 0.695 | True | 0.831 | 0.512 | 7 | 0.101 | 0.950 | 0.053 | 0.643 |
| opt_expert | 0.588 | True | 0.802 | 0.505 | 7 | 0.091 | 0.968 | 0.045 | 0.674 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.889 | 0.889 | 1 |
| quantile | 1.000 | 0.091 | 0 |
| kde | 1.000 | 0.111 | 0 |
| expert | 0.889 | 0.889 | 1 |
| opt | 0.833 | 0.556 | 1 |
| opt_c6c7 | 1.000 | 0.778 | 0 |
| opt_expert | 1.000 | 1.000 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.800 | 1.000 | a*B*C*e*F+A*C*D*e*F+A*b*C*d*e+A*b*C*D*E+A*B*c*D*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | a*B*C*d*e*F<->G |
| kde | 1 | 1.000 | 1.000 | 0.500 | a*B*C*D*e*F<->G |
| expert | 1 | 0.000 | 0.800 | 1.000 | a*B*C*e*F+A*C*D*e*F+A*b*C*d*e+A*b*C*D*E+A*B*c*D*e*f<->G |
| opt | 1 | 0.000 | 0.833 | 1.000 | a*b*C*d*e*F+a*B*C*D*e*F+A*b*C*d*e*f+A*b*C*D*e*F+A*b*C*D*E*f+A*B*c*D*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*D*e*F+a*C*e*F+A*b*C*d*e*f+A*b*C*D*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*C*D*e*F+a*B*C*e*F+A*b*C*d*e+A*b*C*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | B*C*e*F+A*b*C+A*B*c*D*f<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*C*d*e*F<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*C*D*e*F<->G |
| expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | B*C*e*F+A*b*C+A*B*c*D*f<->G |
| opt | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*e*F+B*c*D*e*f+B*C*D*e*F+A*C*D*E+A*b*C*e<->G |
| opt_c6c7 | 4 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | C*e*F+A*C*d*e+A*C*D*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e*F+A*b*C<->G |

