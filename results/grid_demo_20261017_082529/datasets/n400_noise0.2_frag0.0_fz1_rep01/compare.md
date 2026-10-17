# n400_noise0.2_frag0.0_fz1_rep01

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=34001
- true model: `d*e*f+F*b+e*f*C<->G`  (irrelevant: A)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.628 | True | 0.810 | 0.705 | 23 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.609 | False | 0.787 | 0.702 | 27 | 0.027 | 0.990 | 0.005 | 0.542 |
| kde | 0.605 | False | 0.791 | 0.702 | 27 | 0.018 | 0.995 | 0.000 | 0.542 |
| expert | 0.667 | False | 0.791 | 0.649 | 17 | 0.071 | 0.908 | 0.092 | 0.537 |
| opt | 0.843 | True | 0.805 | 0.598 | 17 | 0.110 | 0.912 | 0.088 | 0.662 |
| opt_c6c7 | 0.672 | True | 0.811 | 0.662 | 19 | 0.038 | 0.942 | 0.055 | 0.528 |
| opt_expert | 0.683 | True | 0.807 | 0.668 | 19 | 0.041 | 0.932 | 0.065 | 0.531 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.913 | 0.750 | 2 |
| quantile | 0.778 | 0.750 | 6 |
| kde | 0.778 | 0.750 | 6 |
| expert | 0.706 | 0.462 | 5 |
| opt | 1.000 | 0.607 | 0 |
| opt_c6c7 | 1.000 | 0.704 | 0 |
| opt_expert | 1.000 | 0.704 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.722 | 1.000 | b*C*e*f+b*C*D*F+B*d*e*f+a*c*D*e*F+a*b*C*E*F+A*C*e*f+A*C*d*e+A*b*d*e+A*b*c*F<->G |
| quantile | 5 | 0.000 | 0.620 | 1.000 | c*D*e*F+b*D*F+a*b*C*e*f+a*b*C*E*F+a*B*e*F+a*B*d*e+A*d*e*f+A*C*d*e+A*b*c*F+A*B*C*e*f<->G |
| kde | 5 | 0.000 | 0.620 | 1.000 | c*D*e*F+b*D*F+a*b*C*e*f+a*b*C*E*F+a*B*e*F+a*B*d*e+A*d*e*f+A*C*d*e+A*b*c*F+A*B*C*e*f<->G |
| expert | 2 | 0.000 | 0.429 | 1.000 | b*C*d*e*f+B*C*d*e*F+A*D*e*F+A*C*e+A*b*D*F+A*b*C*F+A*B*d*e<->G |
| opt | 1 | 0.000 | 0.600 | 0.333 | b*D*e*F+b*C*F+b*C*e+A*b*d*e+A*b*D*F<->G |
| opt_c6c7 | 4 | 0.250 | 0.875 | 1.000 | C*d*e*f+b*D*e*F+b*C*E*F+b*C*D*e+A*d*e*f+A*C*e*f+A*b*D*F+A*b*C*F<->G |
| opt_expert | 4 | 0.250 | 0.875 | 1.000 | C*d*e*f+b*D*e*F+b*C*E*F+b*C*D*e+A*d*e*f+A*C*e*f+A*b*D*F+A*b*C*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 6 | 0.000 | 0.278 | 0.556 | 0.000 | 1.000 | d*e*f+c*D*e*F+C*e*f+b*C*F+A*e*F+A*b*F<->G |
| quantile | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 0.000 | e*F+d*e+C*e+b*F<->G |
| kde | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 0.000 | e*F+d*e+C*e+b*F<->G |
| expert | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 0.000 | e*F+d*e+C*e+b*F<->G |
| opt | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 0.000 | b*F+b*d*e+b*C*e<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | d*e*f+b*F+b*C*e+A*C*e*f<->G |
| opt_expert | 2 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | d*e*f+b*F+b*C*e+A*C*e*f<->G |

