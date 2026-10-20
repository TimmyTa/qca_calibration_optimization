# n200_noise0.0_frag0.2_fz1_rep00

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=16000
- true model: `e*d+e*c+e*a<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.447 | True | 0.910 | 0.565 | 9 | 0.000 | 1.000 | 0.000 | 0.547 |
| quantile | 0.511 | True | 0.922 | 0.543 | 11 | 0.053 | 0.944 | 0.052 | 0.533 |
| kde | 0.424 | True | 0.925 | 0.529 | 9 | 0.039 | 0.970 | 0.030 | 0.544 |
| expert | 0.484 | False | 0.901 | 0.489 | 3 | 0.091 | 0.887 | 0.113 | 0.558 |
| opt | 0.847 | True | 0.917 | 0.648 | 13 | 0.170 | 0.883 | 0.126 | 0.795 |
| opt_c6c7 | 0.695 | True | 0.926 | 0.591 | 11 | 0.080 | 0.854 | 0.136 | 0.533 |
| opt_expert | 0.692 | True | 0.926 | 0.603 | 10 | 0.079 | 0.861 | 0.139 | 0.534 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.375 | 0 |
| quantile | 1.000 | 0.423 | 0 |
| kde | 1.000 | 0.346 | 0 |
| expert | 1.000 | 0.115 | 0 |
| opt | 1.000 | 0.591 | 0 |
| opt_c6c7 | 1.000 | 0.550 | 0 |
| opt_expert | 1.000 | 0.435 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*d*e*F+a*b*c*e*F+A*c*d*e+A*B*d*e*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.667 | b*d*e*F+A*d*e+A*b*c*e*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*f+a*b*c*D*e*F+A*c*d*e+A*B*d*e<->G |
| expert | 1 | 1.000 | 1.000 | 0.667 | b*c*d*e*F+A*b*c*d*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*d*e*f+b*c*e*f+b*c*d*e+a*d*e*f+a*b*d*e+a*b*c*e+a*B*C*e*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.667 | b*d*e*F+b*C*d*e+A*C*d*e+A*b*c*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | b*d*e*F+A*c*d*e*f+A*C*d*e*F+A*b*d*e+A*b*c*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*F+B*C*d*e*f+a*b*e*F+A*c*d*e<->G |
| quantile | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*e+A*d*e+A*b*e<->G |
| kde | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e+b*e*F+A*d*e<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*e*F+A*b*c*d*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | e<->G |
| opt_c6c7 | 3 | 0.000 | 0.500 | 0.333 | 0.000 | 0.333 | d*e+A*b*c<->G |
| opt_expert | 2 | 0.000 | 0.500 | 0.333 | 0.000 | 0.500 | d*e+A*b*e<->G |

