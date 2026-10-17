# n200_noise0.1_frag0.2_fz0_rep02

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=19002
- true model: `f*b*D+F*e*b<->G`  (irrelevant: A, C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.566 | True | 0.847 | 0.661 | 11 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.379 | False | 0.820 | 0.377 | 5 | 0.104 | 0.955 | 0.042 | 0.609 |
| kde | 0.222 | False | 0.817 | 0.317 | 2 | 0.053 | 1.000 | 0.000 | 0.697 |
| expert | 0.485 | False | 0.835 | 0.472 | 6 | 0.052 | 1.000 | 0.000 | 0.791 |
| opt | 0.724 | True | 0.894 | 0.519 | 11 | 0.100 | 0.954 | 0.041 | 0.814 |
| opt_c6c7 | 0.679 | True | 0.853 | 0.507 | 10 | 0.109 | 0.938 | 0.068 | 0.628 |
| opt_expert | 0.653 | True | 0.825 | 0.531 | 9 | 0.091 | 0.943 | 0.063 | 0.673 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.909 | 0.714 | 1 |
| quantile | 1.000 | 0.333 | 0 |
| kde | 1.000 | 0.143 | 0 |
| expert | 1.000 | 0.429 | 0 |
| opt | 1.000 | 0.786 | 0 |
| opt_c6c7 | 1.000 | 0.833 | 0 |
| opt_expert | 1.000 | 0.692 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.722 | 1.000 | b*c*d*e*F+b*c*D*E*f+a*b*D*f+a*b*C*E*f+A*b*c*e*F+A*b*C*D*e<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | b*c*D*E*f+a*b*D*E*f+a*b*c*D*f+A*b*C*D*e*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*b*c*D*E*f+A*b*C*D*e*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*c*d*e*F+a*b*c*D*e*f+A*b*D*e*F+A*b*c*D*E*f<->G |
| opt | 2 | 0.000 | 0.800 | 1.000 | b*c*d*e*F+b*c*D*E*f+b*C*D*e+a*b*D*f+a*b*C*e*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.800 | 1.000 | b*c*d*e*F+b*c*D*E*f+a*b*d*e*F+a*b*D*f+A*b*C*D*e<->G |
| opt_expert | 1 | 0.000 | 0.750 | 1.000 | b*c*D*E*f+b*C*D*e+a*b*D*f+a*b*c*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | b*e*F+b*D*f+a*b*C<->G |
| quantile | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*E*f+b*c*D*f+A*b*D*f<->G |
| kde | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*e*F+A*b*c*E*f<->G |
| expert | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*e*F+b*c*D*e+A*b*c*D<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*e*F+b*D*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*e*F+b*D*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*e*F+b*D*f<->G |

