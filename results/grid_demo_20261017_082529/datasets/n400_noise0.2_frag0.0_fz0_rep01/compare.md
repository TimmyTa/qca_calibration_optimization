# n400_noise0.2_frag0.0_fz0_rep01

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=33001
- true model: `B*A+A*c*d<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.581 | False | 0.798 | 0.585 | 14 | 0.000 | 1.000 | 0.000 | 0.798 |
| quantile | 0.587 | False | 0.813 | 0.463 | 14 | 0.112 | 0.971 | 0.039 | 0.585 |
| kde | 0.398 | False | 0.789 | 0.457 | 8 | 0.062 | 1.000 | 0.000 | 0.674 |
| expert | 0.625 | True | 0.806 | 0.546 | 15 | 0.047 | 1.000 | 0.000 | 0.772 |
| opt | 0.732 | True | 0.834 | 0.500 | 12 | 0.086 | 0.953 | 0.051 | 0.772 |
| opt_c6c7 | 0.659 | False | 0.801 | 0.498 | 16 | 0.095 | 0.967 | 0.030 | 0.655 |
| opt_expert | 0.620 | False | 0.798 | 0.500 | 16 | 0.085 | 0.975 | 0.038 | 0.658 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.700 | 0 |
| quantile | 1.000 | 0.700 | 0 |
| kde | 1.000 | 0.400 | 0 |
| expert | 1.000 | 0.750 | 0 |
| opt | 1.000 | 0.632 | 0 |
| opt_c6c7 | 1.000 | 0.800 | 0 |
| opt_expert | 1.000 | 0.800 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 1.000 | 1.000 | 1.000 | A*c*d*e*F+A*c*d*E*f+A*B*e*F+A*B*E*f+A*B*d*e+A*B*c*e+A*B*c*d<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | A*c*d*e*F+A*B*F+A*B*d*e+A*B*D*E+A*B*c*D<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | A*c*d*e*F+A*B*D*E*f+A*B*c*e*F+A*B*c*d*F+A*B*C*d*e<->G |
| expert | 2 | 1.000 | 1.000 | 1.000 | A*c*d*e*F+A*c*d*E*f+A*B*e*F+A*B*E*f+A*B*d+A*B*c*e<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | A*c*d*e*F+A*B*e+A*B*c*d*F+A*B*C*d*f+A*B*C*D*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | A*c*d*e+A*B*e+A*B*d*F+A*B*D*f+A*B*C<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | A*c*d*F+A*B*e*F+A*B*E*f+A*B*d+A*B*c<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*d*e*F+A*c*d*E+A*B*f+A*B*e<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*d*F+A*B*e+A*B*D<->G |
| kde | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*e*f+A*d*e*F+A*B*D*E+A*B*c*F<->G |
| expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | A*d*F+A*c*d*E+A*B<->G |
| opt | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*E*f+A*D*E+A*c*d*F+A*B*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | A*c*d+A*B<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | A*d*F+A*B<->G |

