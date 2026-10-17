# n200_noise0.0_frag0.0_fz1_rep00

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=14000
- true model: `a*D*c+E*D<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.633 | True | 0.883 | 0.680 | 12 | 0.000 | 1.000 | 0.000 | 0.546 |
| quantile | 0.604 | True | 0.885 | 0.638 | 11 | 0.034 | 0.977 | 0.025 | 0.530 |
| kde | 0.632 | True | 0.883 | 0.626 | 10 | 0.049 | 0.956 | 0.043 | 0.538 |
| expert | 0.508 | False | 0.912 | 0.508 | 9 | 0.101 | 0.877 | 0.123 | 0.567 |
| opt | 0.892 | True | 0.872 | 0.544 | 11 | 0.109 | 0.883 | 0.108 | 0.661 |
| opt_c6c7 | 0.769 | True | 0.869 | 0.645 | 9 | 0.061 | 0.892 | 0.106 | 0.520 |
| opt_expert | 0.693 | True | 0.851 | 0.677 | 12 | 0.042 | 0.938 | 0.060 | 0.529 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.667 | 0 |
| quantile | 1.000 | 0.579 | 0 |
| kde | 1.000 | 0.526 | 0 |
| expert | 0.778 | 0.500 | 2 |
| opt | 1.000 | 0.611 | 0 |
| opt_c6c7 | 1.000 | 0.529 | 0 |
| opt_expert | 1.000 | 0.750 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 1.000 | 1.000 | 0.500 | b*D*E*f+B*D*E*F+a*C*D*E*F+A*c*D*E+A*B*D*E<->G |
| quantile | 8 | 1.000 | 1.000 | 0.500 | b*D*E*f+B*D*E*F+a*C*D*E*F+A*c*D*E*F+A*B*C*D*E<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | c*D*E*F+B*D*E*F+a*D*E*F+a*b*c*D*E+A*C*D*E*f<->G |
| expert | 1 | 0.000 | 0.800 | 1.000 | b*C*D*E+a*C*D*E*F+a*b*C*D+a*B*c*D*e*F+A*C*D*E*f<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | b*D*E*f+b*C*D*E+a*B*c*D*E+A*D*E*f+A*b*D*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | C*D*E*f+B*C*D*E+A*b*D*E*F+A*B*D*E*f<->G |
| opt_expert | 4 | 1.000 | 1.000 | 0.750 | c*D*E*f+C*D*E*F+b*C*D*E+a*B*c*D*E+A*b*D*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*E<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*E<->G |
| kde | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | D*E+a*D<->G |
| opt | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | D*E<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*E*F+b*D*E+B*c*D<->G |

