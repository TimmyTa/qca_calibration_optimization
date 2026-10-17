# n400_noise0.1_frag0.2_fz1_rep02

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=32002
- true model: `a*e*F+d*C+e*c<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.748 | True | 0.862 | 0.679 | 16 | 0.000 | 1.000 | 0.000 | 0.537 |
| quantile | 0.661 | True | 0.852 | 0.644 | 13 | 0.048 | 0.964 | 0.036 | 0.531 |
| kde | 0.656 | True | 0.852 | 0.656 | 15 | 0.045 | 0.971 | 0.033 | 0.537 |
| expert | 0.695 | False | 0.843 | 0.557 | 11 | 0.138 | 0.850 | 0.150 | 0.621 |
| opt | 0.862 | True | 0.851 | 0.662 | 19 | 0.091 | 0.943 | 0.063 | 0.680 |
| opt_c6c7 | 0.769 | True | 0.831 | 0.662 | 17 | 0.049 | 0.910 | 0.087 | 0.514 |
| opt_expert | 0.597 | True | 0.817 | 0.646 | 12 | 0.070 | 0.894 | 0.111 | 0.527 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.938 | 0.517 | 1 |
| quantile | 1.000 | 0.394 | 0 |
| kde | 1.000 | 0.469 | 0 |
| expert | 0.909 | 0.357 | 1 |
| opt | 0.947 | 0.545 | 1 |
| opt_c6c7 | 0.941 | 0.485 | 1 |
| opt_expert | 0.917 | 0.333 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.643 | 1.000 | B*C*D*e*F+a*c*d*e*f+a*b*d*e*F+A*b*d*e*f+A*b*c*e+A*B*e*F+A*B*C*d*f<->G |
| quantile | 2 | 0.500 | 0.929 | 1.000 | a*c*d*e*f+a*b*d*e*F+a*B*C*D*e*F+A*c*e*F+A*C*d*e*f+A*b*c*D*e+A*B*C*d*e<->G |
| kde | 1 | 0.000 | 0.833 | 1.000 | b*d*e*F+a*c*d*e*f+a*B*C*D*e*F+A*c*e*F+A*C*d*e+A*b*c*e<->G |
| expert | 1 | 0.000 | 0.400 | 0.333 | C*d*e*F+b*d*e*f+A*C*d*e+A*b*d*e+A*b*C*e*F<->G |
| opt | 2 | 0.000 | 0.500 | 0.667 | c*d*e*f+b*d*e*F+B*C*e*F+A*d*e+A*c*e*F+A*b*c*e+A*B*C*d*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.400 | 0.333 | b*d*e*F+B*c*d*e*f+B*C*D*e*F+A*d*e+A*c*e<->G |
| opt_expert | 2 | 0.000 | 0.714 | 0.667 | b*c*d*e*f+b*C*d*e*F+B*C*d*e*f+A*c*d*e+A*b*d*e+A*b*c*e*f+A*B*C*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e+b*c*e+B*e*F+B*C*d<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e*F+c*d*e+a*B*e*F+A*d*e+A*c*e<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e*F+c*d*e+a*B*e*F+A*d*e+A*c*e<->G |
| expert | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 0.000 | e*F+d*e<->G |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e+b*c*e+B*e*F+B*C*d<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*e+B*e*F+A*c*e<->G |
| opt_expert | 9 | 0.000 | 0.067 | 0.111 | 0.000 | 1.000 | d*e*F+b*c*e+B*e*F+B*d*e+A*d*e<->G |

