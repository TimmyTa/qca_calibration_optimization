# n100_noise0.0_frag0.2_fz0_rep00

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=3000
- true model: `f*d*A+C*a<->G`  (irrelevant: B, E)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.609 | True | 0.946 | 0.758 | 12 | 0.000 | 1.000 | 0.000 | 0.801 |
| quantile | 0.258 | False | 0.870 | 0.242 | 1 | 0.115 | 0.938 | 0.057 | 0.583 |
| kde | 0.251 | False | 0.877 | 0.358 | 3 | 0.051 | 1.000 | 0.000 | 0.700 |
| expert | 0.539 | True | 0.927 | 0.641 | 11 | 0.043 | 1.000 | 0.000 | 0.800 |
| opt | 0.729 | True | 0.970 | 0.594 | 11 | 0.083 | 0.928 | 0.057 | 0.790 |
| opt_c6c7 | 0.650 | True | 0.924 | 0.555 | 10 | 0.110 | 0.930 | 0.048 | 0.634 |
| opt_expert | 0.551 | True | 0.916 | 0.509 | 7 | 0.056 | 0.993 | 0.007 | 0.700 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.667 | 0 |
| quantile | 1.000 | 0.053 | 0 |
| kde | 1.000 | 0.167 | 0 |
| expert | 1.000 | 0.611 | 0 |
| opt | 1.000 | 0.733 | 0 |
| opt_c6c7 | 1.000 | 0.667 | 0 |
| opt_expert | 1.000 | 0.389 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 7 | 0.000 | 0.738 | 1.000 | b*C*d*E*f+B*C*d*e*f+a*C*d*e*f+a*C*D*E+a*B*C*D*f+A*B*c*d*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | a*B*C*d*e*f<->G |
| kde | 1 | 0.000 | 0.500 | 0.500 | b*C*d*E*f+a*B*C*d*e*f<->G |
| expert | 1 | 0.000 | 0.500 | 0.500 | b*C*d*E*f+B*C*d*e*f+a*C*e*f+a*C*D*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*C*D*E*f+a*B*C*f+a*B*C*D*E+A*C*d*E*f+A*B*d*f<->G |
| opt_c6c7 | 2 | 0.500 | 0.917 | 1.000 | B*C*d*e*f+a*C*D*E*f+a*B*C*f+a*B*C*D*E+A*b*C*d*E*f+A*B*c*d*f<->G |
| opt_expert | 1 | 0.000 | 0.667 | 0.500 | b*C*d*E*f+a*C*D*E+a*B*C*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.125 | 0.250 | 0.000 | 1.000 | C*d*f+B*c*d+a*E+a*B*C<->G |
| quantile | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*d*e<->G |
| kde | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*E*f+a*B*d<->G |
| expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | C*d*f+a*C<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | d*f+a*C<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | d*f+a*C<->G |
| opt_expert | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*E*f+a*E+a*B*d<->G |

