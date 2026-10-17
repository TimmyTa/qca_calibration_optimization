# n400_noise0.0_frag0.2_fz0_rep00

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=27000
- true model: `c*E*A+b*E<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.847 | True | 0.927 | 0.799 | 12 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.253 | False | 0.794 | 0.304 | 2 | 0.113 | 0.965 | 0.030 | 0.584 |
| kde | 0.603 | True | 0.833 | 0.628 | 8 | 0.059 | 1.000 | 0.000 | 0.682 |
| expert | 0.842 | True | 0.868 | 0.734 | 12 | 0.064 | 0.992 | 0.008 | 0.765 |
| opt | 0.930 | True | 0.893 | 0.560 | 11 | 0.109 | 0.902 | 0.095 | 0.766 |
| opt_c6c7 | 0.856 | True | 0.874 | 0.526 | 7 | 0.114 | 0.897 | 0.114 | 0.595 |
| opt_expert | 0.690 | True | 0.822 | 0.696 | 11 | 0.069 | 0.993 | 0.012 | 0.680 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.800 | 0 |
| quantile | 1.000 | 0.111 | 0 |
| kde | 1.000 | 0.533 | 0 |
| expert | 1.000 | 0.800 | 0 |
| opt | 1.000 | 0.611 | 0 |
| opt_c6c7 | 1.000 | 0.368 | 0 |
| opt_expert | 1.000 | 0.688 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*d*E*f+a*b*C*E+A*c*D*E+A*b*E*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | A*b*c*d*E*F+A*b*c*D*E*f<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | b*C*d*E*F+a*b*d*E*f+a*b*C*E*f+A*b*d*E*F+A*b*c*D*E*f+A*b*C*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*b*d*E*f+a*b*C*E+A*c*D*E+A*b*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*d*E*f+b*C*E*f+A*c*D*E*f+A*b*d*E+A*b*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*d*E*f+A*b*d*E+A*b*c*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*b*d*E*f+a*b*C*E+A*c*D*E*F+A*b*E*F+A*b*c*D*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E+A*c*E<->G |
| quantile | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*f+A*c*d*E<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*f+b*d*E+A*b*C*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E+A*c*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E+A*c*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | b*E<->G |
| opt_expert | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*E+A*c*E*F<->G |

