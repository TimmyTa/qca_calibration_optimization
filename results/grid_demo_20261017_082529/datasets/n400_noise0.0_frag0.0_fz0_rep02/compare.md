# n400_noise0.0_frag0.0_fz0_rep02

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=25002
- true model: `F*e*C+a*F<->G`  (irrelevant: B, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.785 | True | 0.939 | 0.826 | 17 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.695 | True | 0.877 | 0.639 | 21 | 0.114 | 0.978 | 0.033 | 0.587 |
| kde | 0.784 | True | 0.887 | 0.790 | 17 | 0.056 | 1.000 | 0.000 | 0.688 |
| expert | 0.777 | False | 0.915 | 0.611 | 9 | 0.061 | 0.937 | 0.063 | 0.743 |
| opt | 0.935 | True | 0.911 | 0.601 | 13 | 0.097 | 0.921 | 0.100 | 0.750 |
| opt_c6c7 | 0.917 | True | 0.854 | 0.591 | 13 | 0.119 | 0.914 | 0.108 | 0.630 |
| opt_expert | 0.875 | True | 0.858 | 0.665 | 17 | 0.083 | 0.959 | 0.051 | 0.672 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.850 | 0 |
| quantile | 0.905 | 0.950 | 2 |
| kde | 1.000 | 0.850 | 0 |
| expert | 0.889 | 0.444 | 1 |
| opt | 1.000 | 0.684 | 0 |
| opt_c6c7 | 1.000 | 0.722 | 0 |
| opt_expert | 1.000 | 0.850 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | C*d*e*F+B*C*e*F+a*e*F+a*D*F+a*b*c*F+a*B*C*F<->G |
| quantile | 1 | 0.000 | 0.800 | 1.000 | D*e*F+C*e*F+a*D*F+a*c*F+a*B*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | C*d*e*F+B*C*e*F+a*e*F+a*D*F+a*b*c*F+a*B*C*F<->G |
| expert | 1 | 0.000 | 0.500 | 0.500 | B*c*D*e*F+a*c*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*e*F+a*e*F+a*B*D*F+a*B*c*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*C*e*F+a*e*F+a*B*D*F+a*B*c*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*C*e*F+a*e*F+a*D*F+a*c*F+a*B*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e*F+a*F<->G |
| quantile | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | D*e*F+C*e*F+a*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e*F+a*F<->G |
| expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | B*D*e*F+a*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e*F+a*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e*F+a*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*e*F+a*F<->G |

