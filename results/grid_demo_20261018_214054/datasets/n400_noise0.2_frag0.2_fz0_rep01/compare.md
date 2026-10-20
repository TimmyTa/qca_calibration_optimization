# n400_noise0.2_frag0.2_fz0_rep01

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=35001
- true model: `c*d*B+E*f+D*b<->G`  (irrelevant: A)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.564 | True | 0.891 | 0.574 | 15 | 0.000 | 1.000 | 0.000 | 0.799 |
| quantile | 0.465 | False | 0.000 | 0.000 | 0 | 0.124 | 0.955 | 0.045 | 0.582 |
| kde | 0.304 | False | 0.857 | 0.300 | 3 | 0.063 | 1.000 | 0.000 | 0.680 |
| expert | 0.561 | False | 0.854 | 0.440 | 9 | 0.081 | 0.955 | 0.045 | 0.739 |
| opt | 0.774 | True | 0.880 | 0.529 | 14 | 0.112 | 0.910 | 0.107 | 0.743 |
| opt_c6c7 | 0.562 | False | 0.852 | 0.498 | 15 | 0.102 | 0.930 | 0.069 | 0.633 |
| opt_expert | 0.570 | False | 0.853 | 0.480 | 15 | 0.101 | 0.938 | 0.048 | 0.642 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.469 | 0 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.094 | 0 |
| expert | 1.000 | 0.281 | 0 |
| opt | 1.000 | 0.424 | 0 |
| opt_c6c7 | 1.000 | 0.455 | 0 |
| opt_expert | 1.000 | 0.469 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*c*d*E*f+B*c*D*E*f+a*b*C*E*f+a*B*c*d*e+A*b*c*D*e+A*b*C*D*E+A*B*d*E*f+A*B*c*d*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 0.667 | a*b*C*d*E*f+a*B*c*d*e*f+a*B*c*D*E*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+A*c*d*E*f+A*b*c*D*e*f+A*b*C*D*E*f+A*B*d*E*f+A*B*c*E*f+A*B*c*d*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*D*e+a*b*d*E*f+a*b*D*e*F+a*b*C*D+a*B*D*E*f+a*B*c*d*e+A*B*C*d*E*f<->G |
| opt_c6c7 | 4 | 1.000 | 1.000 | 1.000 | b*C*D*e*F+a*b*d*E*f+a*b*C*E*f+a*B*c*d*e+A*b*D*e*F+A*b*C*D+A*B*d*E*f+A*B*c*E*f+A*B*c*d*f<->G |
| opt_expert | 4 | 1.000 | 1.000 | 1.000 | b*c*d*E*f+B*c*d*e+B*c*D*E*f+a*b*C*E*f+a*b*C*D*f+a*B*D*E*f+A*b*C*D*E+A*B*C*d*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | E*f+b*c*D*e+b*C*E+B*c*f+a*c*e<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*E+a*B*f<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | d*E*f+c*D*e*f+C*E*f+B*c*f+B*c*d*e<->G |
| opt | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | E*f+b*D+a*c*d*e<->G |
| opt_c6c7 | 2 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | E*f+b*D+B*c*f+a*c*e<->G |
| opt_expert | 2 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | E*f+b*C*D*E+B*c*d+a*f<->G |

