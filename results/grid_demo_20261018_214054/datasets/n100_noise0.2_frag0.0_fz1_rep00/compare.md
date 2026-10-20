# n100_noise0.2_frag0.0_fz1_rep00

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=10000
- true model: `D*A+b*C+c*E*B<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.350 | True | 0.915 | 0.508 | 7 | 0.000 | 1.000 | 0.000 | 0.580 |
| quantile | 0.241 | False | 0.908 | 0.428 | 4 | 0.066 | 0.933 | 0.065 | 0.547 |
| kde | 0.249 | False | 0.889 | 0.429 | 4 | 0.054 | 0.945 | 0.058 | 0.556 |
| expert | 0.395 | True | 0.912 | 0.509 | 12 | 0.072 | 0.920 | 0.080 | 0.575 |
| opt | 0.723 | True | 0.946 | 0.629 | 18 | 0.123 | 0.953 | 0.050 | 0.787 |
| opt_c6c7 | 0.459 | True | 0.911 | 0.530 | 10 | 0.074 | 0.860 | 0.138 | 0.544 |
| opt_expert | 0.459 | True | 0.905 | 0.539 | 13 | 0.087 | 0.845 | 0.148 | 0.554 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.241 | 0 |
| quantile | 0.750 | 0.103 | 1 |
| kde | 1.000 | 0.143 | 0 |
| expert | 0.833 | 0.400 | 2 |
| opt | 0.944 | 0.654 | 1 |
| opt_c6c7 | 1.000 | 0.385 | 0 |
| opt_expert | 1.000 | 0.542 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | A*b*C*e*F+A*b*C*D*F+A*b*C*D*e+A*B*c*E*f+A*B*c*D*e*F<->G |
| quantile | 1 | 0.000 | 0.500 | 0.667 | A*c*d*E*f+A*b*C*D*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*b*C*D*F+A*B*c*E*F<->G |
| expert | 2 | 0.000 | 0.667 | 1.000 | A*c*d*E*f+A*c*D*e*f+A*b*e*F+A*b*D*e+A*b*C*D*F+A*B*c*D*E<->G |
| opt | 1 | 0.000 | 0.889 | 1.000 | b*C*d*E*f+b*C*D*e*f+b*C*D*E*F+a*B*c*d*F+A*D*e*f+A*b*C*e*F+A*B*D*f+A*B*c*d*E+A*B*c*D*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | A*b*D*f+A*b*D*e+A*b*C*D+A*B*c*E*f+A*B*c*D*E<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | a*b*C*D*e*f+A*D*E*f+A*b*D*e*F+A*b*C*E*f+A*b*C*D*E+A*B*D*f+A*B*c*E*f+A*B*c*D*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*D*F+A*b*D*F+A*b*C*e+A*B*c*E*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*d*E*f+A*b*C*D*F<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*E*F+A*b*C*D*F<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*d*E*f+A*b*F+A*b*D*e+A*B*c*D<->G |
| opt | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*E*f+b*C*D*E*F+a*c*d*F+a*b*C*D*f+A*c*D*e+A*b*C*e+A*B*D*f+A*B*c*E<->G |
| opt_c6c7 | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*c*E*f+A*b*D*e+A*b*C*D+A*B*c*D*F<->G |
| opt_expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*f+A*E*f+A*C*f+A*b*D*e+A*b*C+A*B*c*D<->G |

