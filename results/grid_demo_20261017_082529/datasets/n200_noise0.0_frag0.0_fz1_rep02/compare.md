# n200_noise0.0_frag0.0_fz1_rep02

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=14002
- true model: `d*E+E*A<->G`  (irrelevant: B, C, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.581 | True | 0.872 | 0.734 | 19 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.525 | True | 0.864 | 0.669 | 14 | 0.048 | 0.965 | 0.035 | 0.551 |
| kde | 0.491 | True | 0.822 | 0.686 | 14 | 0.059 | 0.955 | 0.051 | 0.557 |
| expert | 0.491 | True | 0.857 | 0.689 | 14 | 0.043 | 0.993 | 0.007 | 0.560 |
| opt | 0.836 | True | 0.856 | 0.616 | 14 | 0.141 | 0.883 | 0.119 | 0.725 |
| opt_c6c7 | 0.685 | True | 0.913 | 0.609 | 10 | 0.094 | 0.861 | 0.153 | 0.548 |
| opt_expert | 0.725 | True | 0.888 | 0.679 | 11 | 0.084 | 0.880 | 0.127 | 0.546 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.947 | 0.750 | 1 |
| quantile | 0.857 | 0.500 | 2 |
| kde | 0.857 | 0.522 | 2 |
| expert | 1.000 | 0.583 | 0 |
| opt | 1.000 | 0.636 | 0 |
| opt_c6c7 | 1.000 | 0.526 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.857 | 1.000 | b*c*d*E+B*c*E*f+B*C*d*E+a*d*E+A*b*C*D*E+A*B*E*f+A*B*c*D*E<->G |
| quantile | 1 | 0.000 | 0.833 | 1.000 | c*d*E*F+a*d*E*F+a*b*c*E+A*b*D*E*f+A*B*c*E*f+A*B*C*D*E*F<->G |
| kde | 1 | 0.000 | 0.857 | 1.000 | b*c*d*E+a*d*E*F+a*c*d*E+a*b*d*E+a*b*c*E+A*b*C*D*E*f+A*B*c*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*c*d*E+B*C*d*E*F+a*d*E+A*b*C*D*E*f+A*B*c*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | d*E*F+b*c*d*E+A*b*E*F+A*b*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | c*d*E*f+a*b*C*d*E*F+A*c*d*E+A*b*D*E*f+A*b*c*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | c*d*E*F+b*c*d*E+a*b*d*E*F+A*c*d*E+A*b*D*E*f+A*b*c*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | d*E+c*E*f+A*E<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*E+a*d*E+A*D*E+A*c*E<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*E+a*d*E+A*c*E*F+A*b*D*f<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*E*F+b*E*f+a*d*E+A*c*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E+A*E<->G |
| opt_c6c7 | 2 | 0.500 | 0.750 | 0.750 | 0.500 | 0.500 | d*E+b*E<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*E+b*E<->G |

