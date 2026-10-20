# n100_noise0.1_frag0.0_fz1_rep02

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=6002
- true model: `B*d+a*E+A*f*B<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.368 | False | 0.898 | 0.445 | 5 | 0.000 | 1.000 | 0.000 | 0.544 |
| quantile | 0.390 | False | 0.894 | 0.431 | 5 | 0.036 | 0.962 | 0.038 | 0.529 |
| kde | 0.401 | True | 0.906 | 0.510 | 6 | 0.031 | 0.963 | 0.037 | 0.534 |
| expert | 0.367 | False | 0.896 | 0.419 | 5 | 0.046 | 0.960 | 0.040 | 0.531 |
| opt | 0.678 | True | 0.878 | 0.533 | 10 | 0.137 | 0.883 | 0.117 | 0.732 |
| opt_c6c7 | 0.475 | True | 0.867 | 0.533 | 6 | 0.105 | 0.817 | 0.202 | 0.521 |
| opt_expert | 0.464 | True | 0.853 | 0.545 | 7 | 0.094 | 0.820 | 0.183 | 0.528 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.227 | 0 |
| quantile | 1.000 | 0.200 | 0 |
| kde | 1.000 | 0.250 | 0 |
| expert | 1.000 | 0.227 | 0 |
| opt | 1.000 | 0.455 | 0 |
| opt_c6c7 | 1.000 | 0.261 | 0 |
| opt_expert | 1.000 | 0.318 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.667 | A*B*d*e*f+A*B*c*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.667 | A*B*d*e*f+A*B*c*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*E*F+A*B*d*e*f+A*B*c*f<->G |
| expert | 1 | 1.000 | 1.000 | 0.667 | A*B*c*E*f+A*B*c*D*f+A*B*C*d*e<->G |
| opt | 1 | 0.000 | 0.800 | 1.000 | B*c*E*f+a*c*d*E*f+A*B*d*e*f+A*B*c*f+A*B*c*d<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.667 | B*c*d*f+a*c*d*E*f+a*B*c*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*f+a*c*d*E*f+a*B*c*E*f+A*B*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.333 | 0.000 | 0.000 | A*B*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.333 | 0.000 | 0.000 | A*B*f<->G |
| kde | 3 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | a*b*c*E*F+A*B*f<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*e+A*B*c*f<->G |
| opt | 2 | 0.000 | 0.500 | 0.333 | 0.000 | 0.500 | a*c*E+A*B<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d*f+a*c*E<->G |
| opt_expert | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | B*c*f+a*c*E+A*B*f<->G |

