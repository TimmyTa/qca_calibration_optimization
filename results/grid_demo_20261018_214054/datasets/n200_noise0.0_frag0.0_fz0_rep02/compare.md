# n200_noise0.0_frag0.0_fz0_rep02

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=13002
- true model: `d*E+F*d<->G`  (irrelevant: A, B, C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.649 | True | 0.934 | 0.747 | 14 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.325 | False | 0.000 | 0.000 | 0 | 0.111 | 0.977 | 0.024 | 0.592 |
| kde | 0.295 | False | 0.887 | 0.327 | 3 | 0.058 | 1.000 | 0.000 | 0.692 |
| expert | 0.618 | False | 0.954 | 0.479 | 10 | 0.063 | 0.979 | 0.021 | 0.733 |
| opt | 0.813 | True | 0.911 | 0.563 | 12 | 0.136 | 0.917 | 0.090 | 0.782 |
| opt_c6c7 | 0.761 | True | 0.971 | 0.534 | 10 | 0.135 | 0.855 | 0.145 | 0.617 |
| opt_expert | 0.733 | True | 0.929 | 0.542 | 9 | 0.104 | 0.900 | 0.083 | 0.670 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.609 | 0 |
| quantile |  | 0.000 | 0 |
| kde | 1.000 | 0.130 | 0 |
| expert | 1.000 | 0.455 | 0 |
| opt | 1.000 | 0.667 | 0 |
| opt_c6c7 | 1.000 | 0.625 | 0 |
| opt_expert | 1.000 | 0.450 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E+a*C*d*F+a*B*d*E+A*d*E*F+A*b*c*d*F+A*b*c*d*E<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*F+A*b*d*E*F<->G |
| expert | 2 | 1.000 | 1.000 | 1.000 | C*d*E*F+B*d*E*F+a*C*d*F+A*b*c*d*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*d*F+a*C*d*e*F+A*d*E<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+a*C*d*e*F+A*c*d*F+A*c*d*E+A*B*d*E*F<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | b*C*d*E*F+a*C*d*e*F+A*d*E*F+A*B*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*F+d*E<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | d*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*F+d*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*F+d*E<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*F+B*d*E<->G |

