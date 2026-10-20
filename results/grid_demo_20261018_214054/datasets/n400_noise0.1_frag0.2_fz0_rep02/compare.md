# n400_noise0.1_frag0.2_fz0_rep02

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=31002
- true model: `a*C+B*C*e<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.601 | True | 0.896 | 0.626 | 11 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.483 | False | 0.887 | 0.285 | 2 | 0.113 | 0.953 | 0.052 | 0.588 |
| kde | 0.475 | False | 0.000 | 0.000 | 0 | 0.057 | 1.000 | 0.000 | 0.686 |
| expert | 0.619 | True | 0.882 | 0.553 | 11 | 0.041 | 0.977 | 0.023 | 0.766 |
| opt | 0.843 | True | 0.908 | 0.507 | 10 | 0.099 | 0.910 | 0.112 | 0.730 |
| opt_c6c7 | 0.720 | True | 0.878 | 0.506 | 10 | 0.107 | 0.935 | 0.083 | 0.652 |
| opt_expert | 0.521 | True | 0.872 | 0.501 | 10 | 0.094 | 0.966 | 0.039 | 0.678 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.611 | 0 |
| quantile | 1.000 | 0.105 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.550 | 0 |
| opt | 1.000 | 0.500 | 0 |
| opt_c6c7 | 1.000 | 0.526 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*C*d*e*f+B*C*D*e*F+a*C*d*f+a*b*C*D*E*F+a*B*C*e+a*B*C*d<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | a*B*C*d*F<->G |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | a*C*E*f+a*b*C*d*e+a*b*C*D*E+a*B*C*d*F+A*B*C*d*e*f+A*B*C*D*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*C*d*e*f+a*C*d*e+a*b*C*E*f+a*B*C*e*f+a*B*C*d<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*C*d*e*f+a*C*d*f+a*b*C*E*f+a*b*C*D*e*F+a*B*C*e*f+a*B*C*d<->G |
| opt_expert | 4 | 1.000 | 1.000 | 1.000 | a*C*d*E*f+a*b*C*d*e+a*b*C*D*E*F+a*B*C*d*E+a*B*C*D*f+a*B*C*D*e+A*B*C*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | C*d*f+B*C*e+a*C*E*F<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*B*d*F<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*C*e+a*C<->G |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | B*C*d*f+a*C<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | B*C*d*f+a*C<->G |
| opt_expert | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*f+a*C*d+a*b*D*E*F+a*B*e*F+a*B*C*f<->G |

