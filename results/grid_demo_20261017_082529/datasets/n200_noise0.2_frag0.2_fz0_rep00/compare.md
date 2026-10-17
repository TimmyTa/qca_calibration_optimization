# n200_noise0.2_frag0.2_fz0_rep00

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=23000
- true model: `C*a*b+B*A*F<->G`  (irrelevant: D, E)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.589 | True | 0.871 | 0.607 | 10 | 0.000 | 1.000 | 0.000 | 0.805 |
| quantile | 0.524 | True | 0.807 | 0.507 | 10 | 0.101 | 0.975 | 0.033 | 0.611 |
| kde | 0.561 | True | 0.821 | 0.602 | 9 | 0.059 | 1.000 | 0.000 | 0.688 |
| expert | 0.586 | True | 0.856 | 0.570 | 10 | 0.044 | 1.000 | 0.000 | 0.769 |
| opt | 0.709 | True | 0.857 | 0.516 | 10 | 0.081 | 0.916 | 0.077 | 0.781 |
| opt_c6c7 | 0.605 | True | 0.817 | 0.510 | 10 | 0.094 | 0.938 | 0.072 | 0.652 |
| opt_expert | 0.629 | True | 0.814 | 0.574 | 12 | 0.084 | 0.963 | 0.051 | 0.671 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.900 | 0.562 | 1 |
| quantile | 0.800 | 0.533 | 2 |
| kde | 0.889 | 0.500 | 1 |
| expert | 0.900 | 0.562 | 1 |
| opt | 0.900 | 0.692 | 1 |
| opt_c6c7 | 0.900 | 0.600 | 1 |
| opt_expert | 0.833 | 0.667 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.857 | 1.000 | b*C*d*E*F+a*b*C*E*F+a*b*C*d*F+a*b*C*d*E+A*B*d*E*F+A*B*D*e*F+A*B*C*E*F<->G |
| quantile | 2 | 0.000 | 0.750 | 1.000 | a*b*C*d*e*F+a*b*C*d*E*f+a*b*C*D*E*F+A*C*d*E*F+A*B*d*E*F+A*B*D*e*F+A*B*C*E*F+A*B*C*d*E<->G |
| kde | 2 | 0.000 | 0.857 | 1.000 | a*b*C*d*e*F+a*b*C*d*E*f+a*b*C*D*E*F+A*C*d*E*F+A*B*d*E*F+A*B*D*e*F+A*B*C*E*F<->G |
| expert | 4 | 0.000 | 0.857 | 1.000 | b*C*d*E*F+a*b*C*E*F+a*b*C*d*F+a*b*C*d*E+A*B*d*E*F+A*B*D*e*F+A*B*C*E*F<->G |
| opt | 1 | 0.000 | 0.800 | 1.000 | B*c*d*E*F+a*b*C*E*F+a*b*C*d*F+A*B*E*F+A*B*d*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.833 | 1.000 | a*b*C*d*e*F+a*b*C*D*E*F+A*C*d*E*F+A*B*e*F+A*B*d*F+A*B*C*F<->G |
| opt_expert | 2 | 0.000 | 0.750 | 1.000 | b*C*d*E*F+B*c*d*E*F+a*b*C*E*F+a*b*C*d*F+a*b*C*d*E+A*B*d*F+A*B*c*e*F+A*B*C*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | a*b*d*F+a*b*C*E+A*d*E*F+A*B*F<->G |
| quantile | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | a*b*C*E+a*b*C*d*F+A*C*d*E+A*B*F<->G |
| kde | 4 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | b*C*d*E*f+a*b*d*e*F+a*b*D*E*F+A*d*E*F+A*B*F<->G |
| expert | 4 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | a*b*d*F+a*b*C*E+A*d*E*F+A*B*F<->G |
| opt | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | B*c*d*F+a*b*C*F+A*B*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | d*E*F+a*b*F+A*B*F<->G |
| opt_expert | 3 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | b*C*E+a*c*F+a*b*F+A*B*F<->G |

