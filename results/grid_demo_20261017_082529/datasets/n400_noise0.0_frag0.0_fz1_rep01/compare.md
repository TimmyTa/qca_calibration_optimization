# n400_noise0.0_frag0.0_fz1_rep01

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=26001
- true model: `E*b+E*a<->G`  (irrelevant: C, D, F)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.606 | True | 0.868 | 0.721 | 17 | 0.000 | 1.000 | 0.000 | 0.557 |
| quantile | 0.539 | True | 0.876 | 0.650 | 12 | 0.038 | 0.988 | 0.020 | 0.530 |
| kde | 0.547 | True | 0.884 | 0.670 | 14 | 0.032 | 0.982 | 0.021 | 0.532 |
| expert | 0.684 | False | 0.880 | 0.640 | 8 | 0.097 | 0.886 | 0.114 | 0.561 |
| opt | 0.909 | True | 0.888 | 0.572 | 16 | 0.101 | 0.885 | 0.115 | 0.655 |
| opt_c6c7 | 0.733 | True | 0.873 | 0.627 | 9 | 0.074 | 0.858 | 0.146 | 0.520 |
| opt_expert | 0.690 | True | 0.875 | 0.645 | 10 | 0.059 | 0.893 | 0.106 | 0.527 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.708 | 0 |
| quantile | 1.000 | 0.500 | 0 |
| kde | 1.000 | 0.583 | 0 |
| expert | 1.000 | 0.333 | 0 |
| opt | 1.000 | 0.727 | 0 |
| opt_c6c7 | 1.000 | 0.375 | 0 |
| opt_expert | 1.000 | 0.435 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*c*E*f+a*d*E*F+a*c*E*f+a*C*E*F+a*b*D*E+A*b*d*E<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*d*E*f+b*C*d*E+a*c*d*E*f+a*C*d*E*F+a*b*E*F+a*b*c*E<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | a*c*E*f+a*C*E*F+a*b*c*E+A*b*d*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E*F+a*C*d*E*F+a*b*E*F+a*b*c*D*E+a*b*C*d*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*d*E*f+a*E*f+a*b*d*E+a*B*C*E+A*b*C*D*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*d*E*f+a*d*E*f+a*c*d*E+a*b*c*E*f+a*B*d*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*d*E*F+a*d*E*F+a*c*d*E+a*b*d*E+a*b*c*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*d*E+b*c*E*f+a*E<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*f+b*C*d*E+a*d*E+a*b*E<->G |
| kde | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*d*E+a*E<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*E+a*C*d*E+a*b*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E+a*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*E+a*d*E<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | b*E+a*d*E<->G |

