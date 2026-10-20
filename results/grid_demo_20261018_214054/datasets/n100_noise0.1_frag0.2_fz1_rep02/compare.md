# n100_noise0.1_frag0.2_fz1_rep02

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=8002
- true model: `b*a*e+a*d+b*D*F<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.265 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.537 |
| quantile | 0.308 | False | 0.883 | 0.346 | 4 | 0.037 | 0.967 | 0.037 | 0.522 |
| kde | 0.253 | False | 0.908 | 0.295 | 2 | 0.060 | 0.935 | 0.068 | 0.548 |
| expert | 0.241 | False | 0.886 | 0.250 | 1 | 0.073 | 0.878 | 0.122 | 0.523 |
| opt | 0.647 | True | 0.953 | 0.504 | 12 | 0.158 | 0.923 | 0.072 | 0.817 |
| opt_c6c7 | 0.498 | False | 0.892 | 0.495 | 6 | 0.085 | 0.853 | 0.140 | 0.546 |
| opt_expert | 0.438 | False | 0.895 | 0.483 | 6 | 0.071 | 0.895 | 0.117 | 0.537 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile | 1.000 | 0.190 | 0 |
| kde | 1.000 | 0.100 | 0 |
| expert | 1.000 | 0.053 | 0 |
| opt | 1.000 | 0.750 | 0 |
| opt_c6c7 | 1.000 | 0.333 | 0 |
| opt_expert | 1.000 | 0.333 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 1 | 0.000 | 0.500 | 0.333 | a*C*d*e*F+a*b*C*E*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*b*C*D*e*F+a*B*C*d*e*F<->G |
| expert | 1 | 1.000 | 1.000 | 0.333 | a*b*C*D*E*F<->G |
| opt | 5 | 1.000 | 1.000 | 1.000 | a*c*d*E*F+a*b*D*e*F+a*b*C*d*F+a*b*C*D*e+a*B*c*d*F+a*B*C*d*e+A*b*C*D*F<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | a*C*d*e*F+a*b*D*e*F+a*b*C*D*F+a*B*d*e*F<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | a*C*d*e*F+a*b*D*e*F+a*b*C*D*F+a*B*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*C*d+a*b*C*E<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*F<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*D*E*F<->G |
| opt | 8 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | b*C*D*F+a*c*d+a*C*e+a*b<->G |
| opt_c6c7 | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*d*e*F+a*b*e*F+a*b*C*F<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | a*d*e*F+a*b*D*F<->G |

