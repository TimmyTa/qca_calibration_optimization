# n100_noise0.1_frag0.0_fz0_rep02

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=5002
- true model: `A*B*C+c*d*B+b*E<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.758 | True | 0.928 | 0.877 | 26 | 0.000 | 1.000 | 0.000 | 0.798 |
| quantile | 0.631 | True | 0.810 | 0.676 | 36 | 0.089 | 0.977 | 0.025 | 0.629 |
| kde | 0.669 | True | 0.867 | 0.839 | 30 | 0.044 | 1.000 | 0.000 | 0.711 |
| expert | 0.721 | True | 0.894 | 0.780 | 30 | 0.046 | 0.990 | 0.010 | 0.752 |
| opt | 0.804 | True | 0.932 | 0.716 | 21 | 0.109 | 0.940 | 0.065 | 0.877 |
| opt_c6c7 | 0.752 | True | 0.828 | 0.586 | 21 | 0.118 | 0.898 | 0.090 | 0.657 |
| opt_expert | 0.739 | True | 0.847 | 0.705 | 27 | 0.081 | 0.933 | 0.052 | 0.684 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.923 | 0.857 | 2 |
| quantile | 0.778 | 1.000 | 8 |
| kde | 0.867 | 0.929 | 4 |
| expert | 0.900 | 0.964 | 3 |
| opt | 0.905 | 0.760 | 2 |
| opt_c6c7 | 0.857 | 0.857 | 3 |
| opt_expert | 0.889 | 0.923 | 3 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.667 | 1.000 | d*E*F+c*d*E+b*d*E+B*c*d*F+a*b*C*E+a*B*c*d+A*D*E*f+A*B*C*e*f+A*B*C*D*e<->G |
| quantile | 16 | 0.000 | 0.400 | 1.000 | d*E+b*E*f+b*C*E+B*c*d*F+B*C*d*f+a*c*d*f+A*E*f+A*C*d*f+A*b*c*d+A*B*C*e<->G |
| kde | 2 | 0.000 | 0.500 | 1.000 | d*E*F+b*d*E+b*C*E+B*c*d*F+a*b*C*D*f+a*B*c*d+A*E*f+A*C*d*f+A*B*C*D*e<->G |
| expert | 2 | 0.000 | 0.562 | 1.000 | d*E*F+b*E*f+b*C*E+a*B*c*d+A*c*E*f+A*C*D*f+A*B*d*F+A*B*C*e<->G |
| opt | 1 | 0.000 | 0.600 | 1.000 | b*C*E*f+B*c*d*f+B*c*d*E+a*d*E*f+a*b*C*d*E+A*c*E*f+A*c*d*E+A*B*d*E*F+A*B*c*d+A*B*C*e*f<->G |
| opt_c6c7 | 4 | 0.000 | 0.562 | 1.000 | C*E*f+B*d*E*f+a*b*C*d*E+a*B*c*d+A*D*E*f+A*b*C*D*E+A*B*d*e*F+A*B*C*d<->G |
| opt_expert | 2 | 0.000 | 0.643 | 1.000 | C*d*E+b*D*E*f+a*B*c*d+A*E*f+A*b*C*E+A*B*d*F+A*B*C*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | d*E*F+b*d*E+B*c*d+a*b*C*E+A*D*E*f+A*B*e*f+A*B*C*D<->G |
| quantile | 1 | 0.000 | 0.429 | 1.000 | 0.000 | 1.000 | d*f+d*E+b*E+B*c*d+A*E+A*d+A*B*C<->G |
| kde | 2 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | d*E+b*C*E+B*c*d+a*b*C*f+A*E+A*C*d*f+A*B*C*D<->G |
| expert | 2 | 0.000 | 0.333 | 0.667 | 0.000 | 1.000 | d*E*F+b*E+B*c*d+A*c*E+A*C*D*f+A*B*C*e<->G |
| opt | 1 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | d*E*F+b*C*E+B*c*d+a*d*E+A*c*E*f+A*B*C*e*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.400 | 0.667 | 0.000 | 1.000 | C*E*f+b*E+B*c*d+A*E*f+A*B*d<->G |
| opt_expert | 1 | 0.000 | 0.400 | 0.667 | 0.000 | 1.000 | d*E+b*E*f+B*c*d+A*E+A*B*C<->G |

