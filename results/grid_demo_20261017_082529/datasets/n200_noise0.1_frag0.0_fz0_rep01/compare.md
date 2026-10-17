# n200_noise0.1_frag0.0_fz0_rep01

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=17001
- true model: `A*f+B*e+B*D*f<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.593 | True | 0.889 | 0.700 | 19 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.557 | True | 0.805 | 0.578 | 21 | 0.112 | 0.973 | 0.044 | 0.586 |
| kde | 0.589 | True | 0.844 | 0.684 | 19 | 0.050 | 1.000 | 0.000 | 0.703 |
| expert | 0.589 | True | 0.875 | 0.630 | 18 | 0.050 | 0.995 | 0.005 | 0.773 |
| opt | 0.729 | True | 0.844 | 0.543 | 17 | 0.099 | 0.922 | 0.106 | 0.729 |
| opt_c6c7 | 0.720 | True | 0.810 | 0.569 | 18 | 0.116 | 0.920 | 0.107 | 0.650 |
| opt_expert | 0.654 | True | 0.843 | 0.557 | 15 | 0.110 | 0.907 | 0.101 | 0.652 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.633 | 0 |
| quantile | 0.952 | 0.667 | 1 |
| kde | 1.000 | 0.633 | 0 |
| expert | 1.000 | 0.600 | 0 |
| opt | 1.000 | 0.607 | 0 |
| opt_c6c7 | 1.000 | 0.643 | 0 |
| opt_expert | 0.933 | 0.500 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 8 | 1.000 | 1.000 | 1.000 | B*d*e*F+B*D*E*f+a*B*c*D*e+A*c*D*f+A*b*c*E*f+A*b*C*d*f+A*B*c*d*e+A*B*C*e*F+A*B*C*E*f<->G |
| quantile | 2 | 0.000 | 0.875 | 1.000 | c*D*e*f+B*d*e*F+B*c*e+a*B*D*E*f+A*C*E*f+A*b*D*E*f+A*b*C*d*f+A*B*e*F<->G |
| kde | 8 | 1.000 | 1.000 | 1.000 | B*d*e*F+B*D*E*f+a*B*c*D*e+A*c*D*f+A*b*c*E*f+A*b*C*d*f+A*B*c*d*e+A*B*C*e*F+A*B*C*E*f<->G |
| expert | 2 | 1.000 | 1.000 | 1.000 | B*d*e*F+B*D*E*f+a*B*c*D*e+A*c*D*f+A*b*c*E*f+A*b*C*d*e*f+A*B*c*d*e+A*B*C*e*F+A*B*C*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*e+a*B*d*e*F+a*B*D*e*f+A*c*e*f+A*b*D*e*f+A*B*D*e*F+A*B*c*D*f+A*B*C*d*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*e+a*B*d*e*F+a*B*D*e*f+A*b*e*f+A*B*D*e*F+A*B*c*D*f+A*B*C*d*f<->G |
| opt_expert | 1 | 0.000 | 0.875 | 1.000 | B*D*e*F+B*c*e*F+B*c*D*e+a*B*e*F+a*B*D*E*f+a*B*c*e+A*c*D*e*F+A*b*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | B*e+B*D*f+A*d*f+A*c*f<->G |
| quantile | 2 | 0.000 | 0.625 | 0.833 | 0.000 | 1.000 | c*e+B*e+B*D*f+A*f<->G |
| kde | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | B*e+B*D*f+A*d*f+A*c*f<->G |
| expert | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | B*e+B*D*f+A*d*f+A*c*f<->G |
| opt | 3 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | B*e+A*D*f+A*c*e*f+A*B*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 0.000 | B*e+A*e*f+A*B*f<->G |
| opt_expert | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | B*e+B*D*f+A*f+A*c*e<->G |

