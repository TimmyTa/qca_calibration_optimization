# n200_noise0.2_frag0.2_fz1_rep02

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=24002
- true model: `D*c+C*E+D*B<->G`  (irrelevant: A, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.581 | True | 0.834 | 0.729 | 19 | 0.000 | 1.000 | 0.000 | 0.551 |
| quantile | 0.544 | True | 0.825 | 0.688 | 18 | 0.038 | 0.969 | 0.029 | 0.536 |
| kde | 0.549 | True | 0.823 | 0.735 | 21 | 0.028 | 0.972 | 0.031 | 0.541 |
| expert | 0.562 | False | 0.806 | 0.719 | 18 | 0.129 | 0.853 | 0.147 | 0.578 |
| opt | 0.704 | True | 0.820 | 0.689 | 20 | 0.108 | 0.892 | 0.112 | 0.656 |
| opt_c6c7 | 0.621 | True | 0.810 | 0.710 | 17 | 0.052 | 0.916 | 0.082 | 0.523 |
| opt_expert | 0.645 | True | 0.804 | 0.717 | 20 | 0.069 | 0.898 | 0.107 | 0.529 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.613 | 0 |
| quantile | 1.000 | 0.562 | 0 |
| kde | 0.952 | 0.606 | 1 |
| expert | 0.944 | 0.500 | 1 |
| opt | 1.000 | 0.606 | 0 |
| opt_c6c7 | 1.000 | 0.515 | 0 |
| opt_expert | 0.950 | 0.613 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.500 | 0.955 | 1.000 | b*c*D*f+B*C*d*E*f+B*C*D*e*f+a*b*C*E*F+a*B*D*e*f+a*B*c*D*E*F+A*c*D*E*f+A*C*d*E+A*b*D*E*f+A*b*c*D*E+A*B*C*E*F<->G |
| quantile | 8 | 0.500 | 0.955 | 1.000 | b*c*D*e*f+B*C*d*E+B*C*D*e*f+a*b*D*E*f+a*b*C*D*E+a*B*D*e*f+a*B*c*D*E*F+A*C*d*E+A*b*C*E*f+A*B*c*D*E*f+A*B*C*E*F<->G |
| kde | 4 | 0.000 | 0.923 | 1.000 | b*c*D*e*f+b*c*D*E*F+B*C*D*e*f+a*c*D*E*F+a*b*c*D*f+a*b*C*E*F+a*B*D*e*f+a*B*C*d*f+a*B*C*D*e+A*C*d*E+A*b*C*E*f+A*B*c*D*E*f+A*B*C*E*F<->G |
| expert | 2 | 0.000 | 0.833 | 1.000 | b*c*D*E*F+B*C*E*F+a*c*D*f+a*c*D*E+a*C*E*F+a*B*D*e*f+a*B*C*d*E+A*B*d*E*F+A*B*D*E*f<->G |
| opt | 2 | 0.000 | 0.778 | 1.000 | c*D*E*f+b*D*E*f+b*c*D*f+B*C*d*E+B*C*D*e*f+a*c*D*f+a*C*E*f+a*b*D*E+A*B*C*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.889 | 1.000 | b*D*E*f+b*c*D*f+B*C*d*E*f+a*b*C*E*F+a*B*C*D*e*f+A*c*D*E*f+A*C*d*E+A*b*c*D*E+A*B*C*E*F<->G |
| opt_expert | 1 | 0.000 | 0.625 | 1.000 | b*D*E*f+b*c*D*f+B*C*d*E+B*C*D*e*f+a*b*D*E+a*B*D*f+A*B*c*E*f+A*B*C*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | D*E+c*D*f+C*E+B*D*f<->G |
| quantile | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | c*D*e*f+C*E+B*D*f+a*D*E<->G |
| kde | 1 | 0.000 | 0.400 | 0.667 | 0.000 | 1.000 | D*E+c*D*f+C*E+B*f+B*D<->G |
| expert | 4 | 0.000 | 0.125 | 0.167 | 0.000 | 1.000 | D*E+a*e*f+a*C+A*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | D+C*E<->G |
| opt_c6c7 | 3 | 0.000 | 0.333 | 0.444 | 0.000 | 1.000 | D*E+c*D*f+C*E+a*D<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D+B*C+a*D+A*B*E*f<->G |

