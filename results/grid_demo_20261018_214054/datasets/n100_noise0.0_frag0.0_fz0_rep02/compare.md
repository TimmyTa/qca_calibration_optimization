# n100_noise0.0_frag0.0_fz0_rep02

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=1002
- true model: `d*E+C*A+b*E<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.639 | True | 0.967 | 0.805 | 20 | 0.000 | 1.000 | 0.000 | 0.808 |
| quantile | 0.529 | True | 0.930 | 0.550 | 19 | 0.116 | 0.938 | 0.063 | 0.595 |
| kde | 0.639 | True | 0.953 | 0.760 | 20 | 0.048 | 1.000 | 0.000 | 0.714 |
| expert | 0.639 | True | 0.975 | 0.781 | 20 | 0.019 | 1.000 | 0.000 | 0.796 |
| opt | 0.714 | True | 0.918 | 0.576 | 17 | 0.118 | 0.897 | 0.115 | 0.748 |
| opt_c6c7 | 0.654 | True | 0.909 | 0.613 | 17 | 0.100 | 0.910 | 0.093 | 0.672 |
| opt_expert | 0.669 | True | 0.927 | 0.612 | 19 | 0.095 | 0.940 | 0.065 | 0.665 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.714 | 0 |
| quantile | 0.895 | 0.607 | 2 |
| kde | 1.000 | 0.714 | 0 |
| expert | 1.000 | 0.714 | 0 |
| opt | 1.000 | 0.739 | 0 |
| opt_c6c7 | 1.000 | 0.680 | 0 |
| opt_expert | 1.000 | 0.704 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 6 | 1.000 | 1.000 | 1.000 | b*D*E*f+B*c*d*E*f+a*b*C*d*E+A*c*d*E+A*b*E*f+A*b*D*E+A*b*C*e*F+A*B*C*E*F+A*B*C*d*f<->G |
| quantile | 2 | 0.000 | 0.750 | 1.000 | b*c*d*E*F+b*C*D*E+a*b*C*E*f+A*c*E*F+A*C*D*F+A*b*C*d*e+A*B*c*E+A*B*C*d*f<->G |
| kde | 6 | 1.000 | 1.000 | 1.000 | b*D*E*f+B*c*d*E*f+a*b*C*d*E+A*c*d*E+A*b*E*f+A*b*D*E+A*b*C*e*F+A*B*C*E*F+A*B*C*d*f<->G |
| expert | 6 | 1.000 | 1.000 | 1.000 | b*D*E*f+B*c*d*E*f+a*b*C*d*E+A*c*d*E+A*b*E*f+A*b*D*E+A*b*C*e*F+A*B*C*E*F+A*B*C*d*f<->G |
| opt | 4 | 1.000 | 1.000 | 1.000 | c*d*E*f+b*c*E*f+b*c*d*E+b*C*D*E+a*b*E*f+A*b*E*F+A*B*C*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | C*d*E*f+b*C*E*f+a*b*C*d*E+A*d*E*f+A*C*d*f+A*b*c*E*F+A*b*C*e+A*b*C*D<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | B*c*d*E*f+B*C*d*E*F+a*b*d*E*F+a*b*C*E*f+A*d*E*f+A*c*d*E+A*C*e*F+A*b*D*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E+b*E+A*C<->G |
| quantile | 2 | 0.000 | 0.667 | 0.667 | 0.000 | 0.000 | c*E+b*E+A*C<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E+b*E+A*C<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E+b*E+A*C<->G |
| opt | 8 | 0.125 | 0.583 | 0.583 | 0.125 | 0.250 | c*E+b*E+A*C<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | E+A*C<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*E+b*E+A*C<->G |

