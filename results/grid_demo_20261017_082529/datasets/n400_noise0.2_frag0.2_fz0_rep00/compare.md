# n400_noise0.2_frag0.2_fz0_rep00

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=35000
- true model: `D*E+B*f<->G`  (irrelevant: A, C)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.666 | True | 0.839 | 0.681 | 18 | 0.000 | 1.000 | 0.000 | 0.806 |
| quantile | 0.572 | False | 0.786 | 0.404 | 8 | 0.109 | 0.962 | 0.012 | 0.610 |
| kde | 0.614 | True | 0.808 | 0.633 | 16 | 0.055 | 1.000 | 0.000 | 0.696 |
| expert | 0.663 | True | 0.815 | 0.673 | 18 | 0.034 | 1.000 | 0.000 | 0.795 |
| opt | 0.801 | True | 0.809 | 0.540 | 17 | 0.087 | 0.958 | 0.050 | 0.728 |
| opt_c6c7 | 0.683 | True | 0.800 | 0.513 | 14 | 0.102 | 0.950 | 0.044 | 0.648 |
| opt_expert | 0.712 | True | 0.803 | 0.503 | 12 | 0.086 | 0.967 | 0.031 | 0.661 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.720 | 0 |
| quantile | 1.000 | 0.296 | 0 |
| kde | 1.000 | 0.640 | 0 |
| expert | 1.000 | 0.720 | 0 |
| opt | 1.000 | 0.630 | 0 |
| opt_c6c7 | 0.929 | 0.500 | 1 |
| opt_expert | 1.000 | 0.444 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 1.000 | 1.000 | 1.000 | C*D*E*F+b*D*E*F+B*c*d*e*f+B*c*D*E*f+a*c*D*E+a*B*d*f+a*B*c*f+A*C*D*E<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+B*c*D*E*f+a*c*D*E*f+a*B*c*D*f+a*B*C*d*E*f+A*b*c*D*E*F<->G |
| kde | 4 | 1.000 | 1.000 | 1.000 | C*D*E*F+b*D*E*F+B*c*d*e*f+B*c*D*E*f+a*c*D*E*f+a*B*d*E*f+a*B*c*f+A*C*D*E<->G |
| expert | 4 | 1.000 | 1.000 | 1.000 | C*D*E*F+b*D*E*F+B*c*d*e*f+B*c*D*E*f+a*c*D*E+a*B*d*f+a*B*c*f+A*C*D*E<->G |
| opt | 2 | 1.000 | 1.000 | 1.000 | C*D*E*F+b*D*E*F+B*c*E*f+B*c*d*f+a*c*D*E+a*B*d*E*f+A*C*D*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.857 | 1.000 | C*D*E*F+B*c*d*e*f+a*b*c*E*f+a*B*D*E*F+a*B*C*E*f+A*C*D*E+A*B*d*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*f+B*C*D*E*F+a*c*D*E*f+a*B*d*E*f+a*B*c*f+A*B*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E+B*f<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*E*f+B*c*f+a*D*f+A*c*D*E<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*E+B*c*f+B*C*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E+B*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*E+B*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | D*E+c*f+B*E*f+A*B*f<->G |
| opt_expert | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*D*f+B*f+B*C*E<->G |

