# n400_noise0.2_frag0.0_fz0_rep02

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=33002
- true model: `a*e+e*c*B<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.626 | True | 0.825 | 0.627 | 16 | 0.000 | 1.000 | 0.000 | 0.801 |
| quantile | 0.521 | False | 0.754 | 0.518 | 15 | 0.104 | 0.983 | 0.017 | 0.615 |
| kde | 0.575 | True | 0.804 | 0.574 | 13 | 0.056 | 1.000 | 0.000 | 0.693 |
| expert | 0.623 | True | 0.819 | 0.590 | 17 | 0.042 | 1.000 | 0.000 | 0.796 |
| opt | 0.788 | True | 0.801 | 0.525 | 12 | 0.101 | 0.922 | 0.082 | 0.708 |
| opt_c6c7 | 0.744 | True | 0.803 | 0.504 | 11 | 0.105 | 0.900 | 0.084 | 0.644 |
| opt_expert | 0.687 | True | 0.816 | 0.544 | 13 | 0.083 | 0.967 | 0.030 | 0.680 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.875 | 0.700 | 2 |
| quantile | 0.933 | 0.700 | 1 |
| kde | 1.000 | 0.650 | 0 |
| expert | 0.882 | 0.750 | 2 |
| opt | 1.000 | 0.600 | 0 |
| opt_c6c7 | 1.000 | 0.579 | 0 |
| opt_expert | 1.000 | 0.650 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.714 | 1.000 | b*c*d*e*f+B*c*D*e+a*D*e*F+a*C*e*f+a*b*C*e+a*B*c*d*E*F+A*B*c*e*F<->G |
| quantile | 1 | 0.000 | 0.833 | 1.000 | a*D*e*f+a*C*e*F+a*b*e*f+a*b*D*e+A*B*c*d*F+A*B*c*D*e<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e+a*D*e*F+a*C*e*f+a*b*d*e*f+A*B*c*e*F<->G |
| expert | 1 | 0.000 | 0.714 | 1.000 | b*c*d*e*f+B*c*D*e+a*D*e+a*C*e*f+a*b*C*e+a*B*c*d*E*F+A*B*c*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*D*e+a*d*e*f+a*c*D*e+a*B*e*f+A*B*c*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*e*F+B*c*D*e+a*D*e*F+a*B*e*F+a*B*D*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*D*e*F+a*C*e*F+a*C*D*e+a*b*e*F+a*b*C*e+A*B*c*e*F+A*B*c*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | c*d*e*f+B*c*e+a*e*F+a*C*e+a*B*c*d*F<->G |
| quantile | 1 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | B*c*e+a*e*F+a*D*e+a*b*e+A*B*c*d*F<->G |
| kde | 4 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | B*c*e+a*d*e*f+a*c*e*F+a*C*D*e<->G |
| expert | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | c*d*e*f+B*c*e+a*e+a*B*c*d*F<->G |
| opt | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | d*e*F+B*c*D*e+a*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*c*e+a*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*c*e+a*e<->G |

