# n200_noise0.0_frag0.2_fz1_rep00

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=16000
- true model: `e*d+e*c+e*a<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.727 | True | 0.907 | 0.728 | 20 | 0.000 | 1.000 | 0.000 | 0.547 |
| quantile | 0.624 | True | 0.878 | 0.723 | 24 | 0.053 | 0.944 | 0.052 | 0.533 |
| kde | 0.589 | True | 0.914 | 0.700 | 19 | 0.039 | 0.970 | 0.030 | 0.544 |
| expert | 0.729 | False | 0.858 | 0.732 | 17 | 0.091 | 0.887 | 0.113 | 0.558 |
| opt | 0.848 | True | 0.893 | 0.708 | 22 | 0.106 | 0.944 | 0.059 | 0.734 |
| opt_c6c7 | 0.701 | True | 0.884 | 0.681 | 15 | 0.092 | 0.848 | 0.154 | 0.532 |
| opt_expert | 0.714 | True | 0.901 | 0.690 | 17 | 0.050 | 0.928 | 0.077 | 0.531 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.833 | 0 |
| quantile | 0.833 | 0.769 | 4 |
| kde | 0.947 | 0.692 | 1 |
| expert | 1.000 | 0.654 | 0 |
| opt | 1.000 | 0.815 | 0 |
| opt_c6c7 | 0.867 | 0.591 | 2 |
| opt_expert | 0.941 | 0.640 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | d*e*F+c*d*e+b*d*e+b*c*e*F+a*b*c*e+a*B*C*D*e*f+A*d*e+A*B*c*e*f<->G |
| quantile | 1 | 0.000 | 0.667 | 1.000 | d*e*F+b*c*e*F+a*C*D*e+a*b*D*e+a*b*C*d*E*f+A*d*e+A*b*d*F+A*B*c*e*f+A*B*c*D*E*F<->G |
| kde | 2 | 0.000 | 0.875 | 1.000 | b*d*e*f+B*c*d*e+a*b*c*D*e+a*B*C*D*e+A*c*e*f+A*b*c*d*F+A*B*d*e+A*B*c*e<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | d*e*f+b*d*e+b*c*e+a*c*d*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | d*e*F+c*d*e+b*c*e*F+a*b*e*f+a*B*C*D*e+A*d*e+A*B*c*e*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.857 | 1.000 | b*d*e*f+b*c*e*f+b*C*d*E*F+a*d*e*f+a*C*e*f+a*b*d*e+a*b*c*e<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | c*d*e*f+b*c*e*F+a*d*e+a*b*c*e+a*B*C*e+A*b*c*d*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*e+c*e+a*e<->G |
| quantile | 2 | 0.000 | 0.250 | 1.000 | 0.000 | 1.000 | e+b*d*F+a*b*d+A*c*D<->G |
| kde | 2 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | e+b*d*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*e+c*e+a*e<->G |
| opt_c6c7 | 2 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | e+b*d*F<->G |
| opt_expert | 2 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | e+A*b*c<->G |

