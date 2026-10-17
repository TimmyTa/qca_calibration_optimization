# n400_noise0.2_frag0.2_fz1_rep02

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=36002
- true model: `b*f+c*e*F+E*B*C<->G`  (irrelevant: A, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.600 | True | 0.805 | 0.696 | 19 | 0.000 | 1.000 | 0.000 | 0.547 |
| quantile | 0.543 | True | 0.812 | 0.651 | 15 | 0.037 | 0.975 | 0.025 | 0.546 |
| kde | 0.580 | True | 0.816 | 0.675 | 17 | 0.027 | 0.992 | 0.009 | 0.553 |
| expert | 0.648 | False | 0.785 | 0.660 | 13 | 0.096 | 0.900 | 0.100 | 0.549 |
| opt | 0.786 | True | 0.824 | 0.614 | 17 | 0.131 | 0.902 | 0.100 | 0.728 |
| opt_c6c7 | 0.686 | True | 0.808 | 0.669 | 17 | 0.050 | 0.911 | 0.086 | 0.541 |
| opt_expert | 0.682 | True | 0.805 | 0.621 | 15 | 0.046 | 0.911 | 0.087 | 0.535 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.895 | 0.567 | 2 |
| quantile | 0.933 | 0.438 | 1 |
| kde | 1.000 | 0.567 | 0 |
| expert | 0.846 | 0.367 | 2 |
| opt | 1.000 | 0.548 | 0 |
| opt_c6c7 | 1.000 | 0.531 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.500 | 0.667 | b*D*e*f+b*c*e*f+b*c*D*f+a*C*d*E*f+a*b*c*f+a*b*c*d*e+A*C*D*f+A*b*c*D*e+A*B*d*E*f+A*B*C*d*E<->G |
| quantile | 1 | 0.000 | 0.625 | 0.667 | b*D*e*f+b*c*e*f+B*C*d*E*f+a*b*c*f+a*b*c*d*e+A*b*c*D*e+A*B*C*d*E+A*B*C*D*f<->G |
| kde | 3 | 0.000 | 0.593 | 0.667 | b*D*e*f+b*c*e*f+a*C*d*E*f+a*b*c*f+a*b*c*d*e+A*b*D*f+A*b*c*D*e+A*B*C*E*f+A*B*C*d*E<->G |
| expert | 2 | 0.000 | 0.300 | 0.500 | a*c*d*e*f+a*C*d*E*f+a*b*f+a*b*c*d*e+A*B*C*d*f<->G |
| opt | 1 | 0.000 | 0.800 | 1.000 | C*d*E*f+b*c*d*e*F+b*C*f+a*b*f+A*B*C*d*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.800 | 1.000 | b*c*D*e*F+b*C*D*f+a*b*f+a*b*c*e+A*B*C*E<->G |
| opt_expert | 1 | 0.000 | 0.600 | 0.667 | C*d*E*f+b*C*D*f+a*b*f+A*C*E*f+A*B*C*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | d*E*f+b*f+b*c*e+B*C*d*E+A*C*D*f<->G |
| quantile | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | b*f+b*c*e+B*C*d*E+A*C*D*f<->G |
| kde | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | b*f+b*c*e+B*C*d*E+A*C*E*f<->G |
| expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*e*f+C*d*E*f+b*c*e+a*b*f+A*C*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | c*e+b*f+B*C*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | b*f+b*c*e+A*B*C<->G |
| opt_expert | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | b*f+B*C*d*E+A*C*E*f<->G |

