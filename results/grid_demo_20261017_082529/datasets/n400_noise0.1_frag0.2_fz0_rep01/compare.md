# n400_noise0.1_frag0.2_fz0_rep01

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=31001
- true model: `D*b+E*B<->G`  (irrelevant: A, C, F)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.732 | True | 0.897 | 0.766 | 21 | 0.000 | 1.000 | 0.000 | 0.795 |
| quantile | 0.727 | True | 0.836 | 0.609 | 21 | 0.103 | 0.966 | 0.028 | 0.627 |
| kde | 0.732 | True | 0.881 | 0.712 | 21 | 0.053 | 1.000 | 0.000 | 0.700 |
| expert | 0.751 | True | 0.929 | 0.668 | 20 | 0.053 | 1.000 | 0.000 | 0.772 |
| opt | 0.823 | True | 0.879 | 0.598 | 19 | 0.080 | 0.958 | 0.049 | 0.743 |
| opt_c6c7 | 0.807 | True | 0.830 | 0.613 | 19 | 0.100 | 0.928 | 0.052 | 0.661 |
| opt_expert | 0.807 | True | 0.842 | 0.677 | 21 | 0.068 | 0.958 | 0.029 | 0.690 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.952 | 0.714 | 1 |
| quantile | 0.952 | 0.645 | 1 |
| kde | 0.952 | 0.714 | 1 |
| expert | 1.000 | 0.714 | 0 |
| opt | 1.000 | 0.594 | 0 |
| opt_c6c7 | 1.000 | 0.594 | 0 |
| opt_expert | 1.000 | 0.700 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.875 | 1.000 | b*c*D*e+b*C*D*E*f+B*C*d*E*f+a*b*D*F+a*b*c*D+a*B*E*F+A*b*C*d*E*F+A*B*c*E<->G |
| quantile | 3 | 0.000 | 0.889 | 1.000 | b*c*D*e+B*D*E*F+B*C*d*E*f+a*b*D*F+a*b*c*D+a*B*C*E*F+A*b*C*E*F+A*b*C*D*E+A*B*c*E<->G |
| kde | 2 | 0.000 | 0.875 | 1.000 | b*c*D*e+b*C*D*E*f+B*C*d*E*f+a*b*D*F+a*b*c*D+a*B*E*F+A*b*C*d*E*F+A*B*c*E<->G |
| expert | 2 | 1.000 | 1.000 | 1.000 | b*c*D*e+b*C*D*E*f+B*C*d*E*f+a*b*D*F+a*b*c*D+a*B*E*F+A*B*c*E<->G |
| opt | 5 | 0.000 | 0.829 | 1.000 | C*D*E+a*b*D*E+a*b*C*D*F+a*B*E*F+a*B*C*E+A*B*E*f+A*B*c*d*E<->G |
| opt_c6c7 | 6 | 0.000 | 0.833 | 1.000 | a*D*E*F+a*b*D*F+a*b*c*D*E+a*B*C*d*E+A*C*D*E+A*b*c*D*e+A*B*D*E+A*B*c*E*F+A*B*C*E*f<->G |
| opt_expert | 3 | 0.667 | 0.952 | 1.000 | b*c*D*e+B*D*E*F+a*b*D*F+a*b*D*E+a*B*C*d*E+A*C*D*E+A*B*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | C*E+b*D+B*E<->G |
| quantile | 3 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | b*D+B*E+A*C*E<->G |
| kde | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | C*E+b*D+B*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*D+B*E<->G |
| opt | 4 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | b*D+B*E*F+B*C*E+A*B*c<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | E+b*D<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*D+B*E<->G |

