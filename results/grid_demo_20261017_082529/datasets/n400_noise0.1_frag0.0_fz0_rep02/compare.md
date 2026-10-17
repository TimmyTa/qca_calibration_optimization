# n400_noise0.1_frag0.0_fz0_rep02

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=29002
- true model: `d*b*c+A*E<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.682 | True | 0.877 | 0.722 | 17 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.454 | False | 0.798 | 0.402 | 8 | 0.102 | 0.979 | 0.009 | 0.598 |
| kde | 0.589 | True | 0.841 | 0.602 | 12 | 0.050 | 1.000 | 0.000 | 0.698 |
| expert | 0.678 | True | 0.844 | 0.649 | 16 | 0.048 | 1.000 | 0.000 | 0.751 |
| opt | 0.869 | True | 0.885 | 0.519 | 12 | 0.119 | 0.927 | 0.068 | 0.748 |
| opt_c6c7 | 0.848 | True | 0.868 | 0.545 | 12 | 0.104 | 0.937 | 0.070 | 0.646 |
| opt_expert | 0.752 | True | 0.809 | 0.541 | 14 | 0.090 | 0.936 | 0.053 | 0.678 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.773 | 0 |
| quantile | 1.000 | 0.364 | 0 |
| kde | 1.000 | 0.545 | 0 |
| expert | 1.000 | 0.727 | 0 |
| opt | 1.000 | 0.571 | 0 |
| opt_c6c7 | 1.000 | 0.571 | 0 |
| opt_expert | 0.929 | 0.591 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*c*d*f+b*c*d*E+A*d*E*F+A*c*E*f+A*b*D*E*f+A*b*c*E+A*b*c*d+A*B*d*E+A*B*C*E*F<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | b*c*d*e*f+A*c*d*E*f+A*C*D*E*f+A*B*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*c*d*f+A*c*E*f+A*b*D*E*f+A*b*c*E+A*B*d*E*f+A*B*C*D*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*c*d*f+b*c*d*E+A*d*E*F+A*c*E*f+A*b*D*E*f+A*b*c*E+A*B*d*E+A*B*C*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*c*d*f+A*c*D*E+A*B*E*f+A*B*c*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*d*f+A*c*D*E+A*B*E*f+A*B*c*E<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | b*C*d*E*f+a*b*c*d*E*F+A*D*E*F+A*C*E+A*b*c*d*e*f+A*B*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | b*c*d*f+b*c*d*E+A*E+A*b*c*d<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*f+A*E*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*f+A*E*f+A*D*E+A*b*c*E<->G |
| expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*c*d*f+b*c*d*E+A*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*c*d+A*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*c*d+A*E<->G |
| opt_expert | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | b*d*E*f+b*c*d+A*E<->G |

