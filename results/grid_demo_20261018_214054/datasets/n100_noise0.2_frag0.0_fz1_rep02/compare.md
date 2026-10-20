# n100_noise0.2_frag0.0_fz1_rep02

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=10002
- true model: `E*d+C*f+E*c*F<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.473 | True | 0.883 | 0.646 | 19 | 0.000 | 1.000 | 0.000 | 0.549 |
| quantile | 0.434 | True | 0.844 | 0.630 | 21 | 0.047 | 0.958 | 0.037 | 0.517 |
| kde | 0.434 | True | 0.859 | 0.651 | 22 | 0.041 | 0.967 | 0.028 | 0.518 |
| expert | 0.562 | True | 0.900 | 0.604 | 17 | 0.072 | 0.927 | 0.073 | 0.545 |
| opt | 0.796 | True | 0.945 | 0.561 | 16 | 0.148 | 0.920 | 0.075 | 0.800 |
| opt_c6c7 | 0.542 | True | 0.869 | 0.643 | 19 | 0.081 | 0.872 | 0.128 | 0.508 |
| opt_expert | 0.537 | True | 0.871 | 0.644 | 22 | 0.067 | 0.912 | 0.088 | 0.515 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.947 | 0.643 | 1 |
| quantile | 0.857 | 0.600 | 3 |
| kde | 0.864 | 0.633 | 3 |
| expert | 0.941 | 0.800 | 1 |
| opt | 0.938 | 0.789 | 1 |
| opt_c6c7 | 0.842 | 0.842 | 3 |
| opt_expert | 0.864 | 0.905 | 3 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.889 | 1.000 | C*D*E*f+b*C*E*f+B*c*d*E*f+a*C*E*f+a*b*d*E+a*b*c*D*e*F+a*b*C*f+a*B*c*E*F+A*c*D*E*F<->G |
| quantile | 2 | 0.000 | 0.500 | 0.667 | C*E*f+B*E*f+B*c*D*E+a*b*d*E+a*b*C*f+a*B*c*E+A*D*E*f<->G |
| kde | 2 | 0.000 | 0.722 | 1.000 | C*E*f+B*d*E*f+B*c*D*E*F+a*c*d*E+a*C*d*f+a*b*d*E+a*b*c*D*e*F+a*b*C*f+A*D*E*f<->G |
| expert | 1 | 0.000 | 0.857 | 1.000 | b*C*f+b*C*d*E+a*d*E*F+a*C*d*E+a*b*d*E+a*b*c*D*e*F+A*b*c*D*E*F<->G |
| opt | 2 | 0.000 | 0.909 | 1.000 | b*d*E*F+b*C*D*E*f+a*c*d*E*F+a*b*c*D*e*F+a*b*C*d*e*f+a*B*C*d*E*f+A*c*D*E*F+A*C*d*E*F+A*C*D*E*f+A*b*C*E*f+A*b*C*D*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.818 | 1.000 | B*C*E*f+B*C*d*E+a*c*D*e*F+a*C*d*f+a*C*d*E+a*b*d*E*f+a*B*d*E*F+a*B*D*E*f+A*b*c*d*E*F+A*b*C*e*f+A*B*c*D*E*F<->G |
| opt_expert | 2 | 0.000 | 0.778 | 1.000 | C*d*E*F+b*C*e*f+B*C*D*f+a*d*E*F+a*c*D*e*F+a*C*d*E+a*B*C*E+A*C*D*f+A*b*c*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*E*F+C*E*f+B*c*d*E+a*b*d*E+a*b*c*D*F+a*b*C*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E*f+B*c*E+a*b*d*E+a*b*C*f+A*D*E*f<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E*f+B*c*E*F+B*c*d*E+a*C*d*f+a*b*d*E+a*b*c*D*e*F+a*b*C*f+A*D*E*f<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*E*F+b*C*f+b*C*d*E+a*d*E+a*b*c*D*F<->G |
| opt | 8 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | c*E*F+C*D*E*f+b*d*E*F+b*c*D*F+b*C*e*f+a*B*C*f+A*C*d*E<->G |
| opt_c6c7 | 16 | 0.000 | 0.125 | 0.333 | 0.000 | 1.000 | c*E*F+B*d*E+B*C*E*f+a*d*E+a*c*D*F+a*C*f+a*B*c*E+A*b*e*f<->G |
| opt_expert | 3 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | d*E*F+c*E*F+C*D*f+a*c*D*F+a*C*f+a*B*E+A*b*e*f<->G |

