# n100_noise0.1_frag0.2_fz0_rep00

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=7000
- true model: `f*b*D+f*a<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.624 | True | 0.894 | 0.722 | 12 | 0.000 | 1.000 | 0.000 | 0.799 |
| quantile | 0.440 | False | 0.000 | 0.000 | 0 | 0.118 | 0.943 | 0.057 | 0.581 |
| kde | 0.444 | True | 0.838 | 0.533 | 6 | 0.061 | 1.000 | 0.000 | 0.679 |
| expert | 0.559 | True | 0.844 | 0.589 | 9 | 0.070 | 0.993 | 0.007 | 0.740 |
| opt | 0.841 | True | 0.945 | 0.547 | 10 | 0.124 | 0.923 | 0.093 | 0.806 |
| opt_c6c7 | 0.676 | True | 0.889 | 0.527 | 12 | 0.111 | 0.923 | 0.082 | 0.638 |
| opt_expert | 0.681 | True | 0.858 | 0.511 | 9 | 0.091 | 0.932 | 0.062 | 0.667 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.750 | 0 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.375 | 0 |
| expert | 0.889 | 0.500 | 1 |
| opt | 1.000 | 0.714 | 0 |
| opt_c6c7 | 1.000 | 0.750 | 0 |
| opt_expert | 0.889 | 0.667 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*c*d*f+a*b*d*E*f+a*B*e*f+a*B*c*f+A*b*D*E*f+A*b*c*D*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*e*f+a*B*D*e*f+a*B*c*E*f+A*b*c*D*e*f<->G |
| expert | 1 | 0.000 | 0.800 | 1.000 | a*c*d*e*f+a*B*D*e*f+a*B*c*f+A*b*c*d*E*F+A*b*c*D*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*e*f+a*b*C*d*E*f+a*B*D*f+a*B*c*E*f+a*B*C*e*f+A*b*c*D*e*f+A*b*C*D*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*d*E*f+a*b*c*d*f+a*B*D*f+a*B*C*f+A*b*c*D*e*f+A*b*C*D*E*f<->G |
| opt_expert | 1 | 0.000 | 0.750 | 1.000 | B*C*D*e*f+a*c*d*e*f+a*B*c*f+A*b*c*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*f+a*e*f+a*d*f+a*B*c*f+A*b*D*E*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*f+a*D*e*f+a*b*e*f+a*B*c*E*f<->G |
| expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*D*e*f+a*b*e*f+a*B*c*f+A*b*d*E*F+A*b*c*D*f<->G |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*f+a*d*f+a*B*f+A*C*D*E*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e+a*d*f+a*B*f+A*C*D*E*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*e*f+a*e*f+a*B*f+A*b*c*D*E<->G |

