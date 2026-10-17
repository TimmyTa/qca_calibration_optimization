# n200_noise0.0_frag0.0_fz0_rep02

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=13002
- true model: `d*E+F*d<->G`  (irrelevant: A, B, C)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.686 | True | 0.934 | 0.747 | 14 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.568 | False | 0.785 | 0.561 | 11 | 0.111 | 0.977 | 0.024 | 0.592 |
| kde | 0.676 | True | 0.873 | 0.730 | 14 | 0.058 | 1.000 | 0.000 | 0.692 |
| expert | 0.686 | True | 0.897 | 0.694 | 15 | 0.063 | 0.979 | 0.021 | 0.733 |
| opt | 0.838 | True | 0.918 | 0.638 | 13 | 0.113 | 0.911 | 0.098 | 0.802 |
| opt_c6c7 | 0.763 | True | 0.880 | 0.627 | 13 | 0.110 | 0.919 | 0.079 | 0.640 |
| opt_expert | 0.792 | True | 0.897 | 0.575 | 10 | 0.096 | 0.922 | 0.068 | 0.643 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.609 | 0 |
| quantile | 1.000 | 0.478 | 0 |
| kde | 1.000 | 0.609 | 0 |
| expert | 1.000 | 0.682 | 0 |
| opt | 1.000 | 0.722 | 0 |
| opt_c6c7 | 1.000 | 0.619 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E+a*C*d*F+a*B*d*E+A*d*E*F+A*b*c*d*F+A*b*c*d*E<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | C*d*E*F+B*d*E*F+B*C*d*E+a*b*C*d*F+A*b*c*d*E<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | B*C*d*E+a*C*d*F+a*B*d*E+A*d*E*F+A*b*c*d*F+A*b*c*d*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*d*E*F+B*C*d*E+a*C*d*F+A*d*E+A*b*c*d*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*d*F+a*C*d*e*F+A*d*E+A*b*d*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | c*d*E*F+b*d*E*F+a*C*d*F+a*b*d*F+a*B*c*d*E+A*b*c*d*E+A*B*C*d*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | a*C*d*e*F+A*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*F+d*E<->G |
| quantile | 3 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*E+b*C*d*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*F+d*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*F+d*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | d*F+d*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | d*E+a*d*F<->G |
| opt_expert | 2 | 0.500 | 0.750 | 0.750 | 0.500 | 0.500 | d*F+d*E<->G |

