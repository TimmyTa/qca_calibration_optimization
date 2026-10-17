# n200_noise0.2_frag0.0_fz1_rep02

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=22002
- true model: `e*A+B*A+e*C<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.487 | True | 0.809 | 0.664 | 17 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 0.509 | False | 0.786 | 0.699 | 22 | 0.041 | 0.982 | 0.025 | 0.541 |
| kde | 0.560 | False | 0.793 | 0.693 | 17 | 0.068 | 0.937 | 0.065 | 0.577 |
| expert | 0.497 | False | 0.800 | 0.629 | 15 | 0.048 | 0.973 | 0.027 | 0.568 |
| opt | 0.708 | True | 0.840 | 0.599 | 14 | 0.117 | 0.927 | 0.071 | 0.696 |
| opt_c6c7 | 0.640 | True | 0.805 | 0.642 | 14 | 0.067 | 0.892 | 0.115 | 0.530 |
| opt_expert | 0.645 | True | 0.823 | 0.630 | 14 | 0.062 | 0.891 | 0.102 | 0.555 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.548 | 0 |
| quantile | 0.909 | 0.645 | 2 |
| kde | 1.000 | 0.630 | 0 |
| expert | 0.933 | 0.438 | 1 |
| opt | 0.929 | 0.464 | 1 |
| opt_c6c7 | 0.786 | 0.478 | 3 |
| opt_expert | 0.857 | 0.500 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*C*D*e*f+B*C*d*e*f+B*C*D*e*F+a*b*C*d*e*F+A*b*D*e+A*B*d*e+A*B*c*d*F+A*B*c*D*E*f+A*B*C*e+A*B*C*D*F<->G |
| quantile | 6 | 0.000 | 0.778 | 1.000 | b*c*d*e*F+a*C*d*e*f+a*b*C*e+a*B*C*D*F+A*b*D*e+A*B*e*f+A*B*c*d*F+A*B*c*D*f+A*B*C*e<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+a*B*C*d*e*f+A*e*F+A*c*d*e+A*C*D*e+A*b*d*e+A*B*c*d*F+A*B*C*D*F<->G |
| expert | 1 | 0.000 | 0.857 | 1.000 | b*d*e*F+b*C*e*F+a*b*C*d*e+A*C*e*F+A*b*D*e+A*B*c*d*F+A*B*C*d*e<->G |
| opt | 1 | 0.000 | 0.857 | 1.000 | C*d*e*F+b*d*e*F+b*C*e*F+A*C*e*F+A*b*c*D*e+A*B*c*d*F+A*B*c*D*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.667 | D*e*F+b*c*e*F+A*b*c*D*e+A*B*c*F<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | C*D*e*F+b*c*e*F+A*b*e*F+A*b*c*D*e+A*B*D*F+A*B*c*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e+A*e+A*B<->G |
| quantile | 2 | 0.000 | 0.600 | 1.000 | 0.000 | 1.000 | d*e+C*e+B*C*D*F+A*e+A*B<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | e*F+c*d*e+C*D*e+b*d*e+B*c*d*F+B*C*D*F+a<->G |
| expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | e*F+b*d*e+A*d*e+A*b*e+A*B*d*F<->G |
| opt | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*F+b*e*F+A*b*e+A*B*c<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | e*F+A*b*e+A*B*F<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | e*F+A*b*e+A*B*F<->G |

