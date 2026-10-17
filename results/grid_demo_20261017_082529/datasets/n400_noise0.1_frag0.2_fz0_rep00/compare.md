# n400_noise0.1_frag0.2_fz0_rep00

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=31000
- true model: `F*C+B*a*c+c*D*B<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.664 | True | 0.885 | 0.689 | 16 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.592 | True | 0.820 | 0.556 | 17 | 0.109 | 0.979 | 0.039 | 0.597 |
| kde | 0.579 | True | 0.829 | 0.639 | 15 | 0.062 | 1.000 | 0.000 | 0.677 |
| expert | 0.698 | False | 0.833 | 0.661 | 13 | 0.055 | 0.958 | 0.042 | 0.759 |
| opt | 0.769 | True | 0.801 | 0.520 | 16 | 0.100 | 0.964 | 0.045 | 0.696 |
| opt_c6c7 | 0.717 | True | 0.824 | 0.560 | 15 | 0.105 | 0.918 | 0.088 | 0.640 |
| opt_expert | 0.742 | True | 0.826 | 0.541 | 14 | 0.092 | 0.965 | 0.030 | 0.655 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.667 | 0 |
| quantile | 0.941 | 0.593 | 1 |
| kde | 1.000 | 0.625 | 0 |
| expert | 1.000 | 0.481 | 0 |
| opt | 1.000 | 0.615 | 0 |
| opt_c6c7 | 1.000 | 0.536 | 0 |
| opt_expert | 1.000 | 0.538 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.714 | 1.000 | b*C*d*e*F+B*c*D*e*f+a*B*E*F+a*B*c*d*E+A*C*e*F+A*B*D*F+A*B*c*D<->G |
| quantile | 2 | 0.000 | 0.625 | 0.667 | b*C*d*e*F+B*D*E*F+B*c*D*e*f+a*B*E*F+A*C*d*e*F+A*b*D*e*F+A*b*C*F+A*B*c*D<->G |
| kde | 2 | 0.000 | 0.667 | 1.000 | B*c*D*e*f+a*B*E*F+a*B*c*d*E+A*C*e*F+A*B*D*F+A*B*c*D<->G |
| expert | 2 | 0.000 | 0.600 | 1.000 | B*C*d*F+a*B*E*F+a*B*c*d*E+a*B*c*D*e*f+A*B*D*F<->G |
| opt | 2 | 0.000 | 0.833 | 0.667 | C*d*e*F+B*c*D*F+a*B*E*F+A*C*e*F+A*B*c*D*e+A*B*C*F<->G |
| opt_c6c7 | 2 | 0.500 | 0.917 | 1.000 | b*C*e*F+B*c*D*e+B*C*D*E*F+a*C*e*F+a*B*D*F+a*B*c*E*f<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | B*D*E*F+B*c*D*F+B*C*d*e*F+a*B*c*d*E+A*C*e*F+A*B*C*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 12 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | C*F+B*c*d*f+a*B*F+a*B*e+A*B*c*D<->G |
| quantile | 4 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | C*F+a*B*F+a*B*e+A*D*e*F+A*B*c*D<->G |
| kde | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*d*f+a*B*F+a*B*e+A*C*F+A*B*c*D<->G |
| expert | 2 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | E*F+C*F+a*D*e*f+a*c*d*E+A*D*F<->G |
| opt | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 0.000 | C*F+a*B*F+A*B*c*D<->G |
| opt_c6c7 | 7 | 0.143 | 0.667 | 0.667 | 0.143 | 0.286 | C*F+B*c*E+B*c*D<->G |
| opt_expert | 3 | 0.000 | 0.333 | 0.333 | 0.000 | 0.667 | C*F+B*D*F+a*c*d*E<->G |

