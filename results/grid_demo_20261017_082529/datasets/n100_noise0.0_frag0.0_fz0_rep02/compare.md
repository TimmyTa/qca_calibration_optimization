# n100_noise0.0_frag0.0_fz0_rep02

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=1002
- true model: `d*E+C*A+b*E<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.639 | True | 0.967 | 0.805 | 20 | 0.000 | 1.000 | 0.000 | 0.808 |
| quantile | 0.492 | False | 0.779 | 0.576 | 26 | 0.116 | 0.938 | 0.063 | 0.595 |
| kde | 0.529 | True | 0.847 | 0.769 | 25 | 0.048 | 1.000 | 0.000 | 0.714 |
| expert | 0.638 | True | 0.975 | 0.781 | 20 | 0.019 | 1.000 | 0.000 | 0.796 |
| opt | 0.746 | True | 0.886 | 0.657 | 18 | 0.089 | 0.933 | 0.068 | 0.702 |
| opt_c6c7 | 0.680 | True | 0.858 | 0.600 | 16 | 0.122 | 0.877 | 0.118 | 0.661 |
| opt_expert | 0.678 | True | 0.915 | 0.654 | 20 | 0.080 | 0.970 | 0.037 | 0.706 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.714 | 0 |
| quantile | 0.654 | 0.607 | 9 |
| kde | 0.800 | 0.714 | 5 |
| expert | 1.000 | 0.714 | 0 |
| opt | 1.000 | 0.720 | 0 |
| opt_c6c7 | 0.812 | 0.650 | 3 |
| opt_expert | 1.000 | 0.769 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 6 | 1.000 | 1.000 | 1.000 | b*D*E*f+B*c*d*E*f+a*b*C*d*E+A*c*d*E+A*b*E*f+A*b*D*E+A*b*C*e*F+A*B*C*E*F+A*B*C*d*f<->G |
| quantile | 2 | 0.000 | 0.364 | 0.667 | b*C*D*E+a*C*D*E+a*b*D*e*f+a*b*c*d*F+a*b*C*f+A*c*E*F+A*C*D*F+A*b*d*e*f+A*b*C*e*F+A*B*c*E+A*B*C*d*f<->G |
| kde | 32 | 0.000 | 0.562 | 1.000 | b*D*E*f+B*c*d*E*f+B*C*D*E*F+a*b*C*d*E+a*B*C*d*e*F+A*D*E*F+A*c*E*F+A*b*E*f+A*b*C*e*F+A*B*d*f+A*B*d*E+A*B*c*D*F<->G |
| expert | 6 | 1.000 | 1.000 | 1.000 | b*D*E*f+B*c*d*E*f+a*b*C*d*E+A*c*d*E+A*b*E*f+A*b*D*E+A*b*C*e*F+A*B*C*E*F+A*B*C*d*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | C*d*E*f+b*E*f+b*C*d*E+A*d*E*f+A*b*E+A*b*C*F<->G |
| opt_c6c7 | 2 | 0.000 | 0.714 | 1.000 | b*C*D*E*f+B*d*E*f+B*c*d*E+a*c*D*E*f+a*b*C*D*E+A*b*C*D*e*F+A*B*D*E<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | c*d*E*f+b*d*E*f+b*c*E*f+a*C*d*E*F+a*b*E*f+A*c*d*E+A*C*D*e*F+A*b*C*e*F+A*b*C*D*F+A*B*d*E+A*B*C*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E+b*E+A*C<->G |
| quantile | 9 | 0.000 | 0.333 | 1.000 | 0.000 | 1.000 | E+C*d+b*d*F+b*D*f+A*C+A*b<->G |
| kde | 2 | 0.000 | 0.375 | 0.500 | 0.000 | 1.000 | c*E+C*F+b*E+A*B<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E+b*E+A*C<->G |
| opt | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | F+d*E+b*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 0.000 | d*E+c*E+b*E+A*C<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E+b*E+A*C<->G |

