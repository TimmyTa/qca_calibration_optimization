# n100_noise0.2_frag0.0_fz0_rep02

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=9002
- true model: `a*c*b+d*b<->G`  (irrelevant: E, F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.581 | True | 0.899 | 0.628 | 16 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.159 | False | 0.804 | 0.236 | 1 | 0.101 | 0.982 | 0.030 | 0.615 |
| kde | 0.339 | False | 0.834 | 0.342 | 4 | 0.060 | 1.000 | 0.000 | 0.683 |
| expert | 0.507 | True | 0.847 | 0.581 | 13 | 0.031 | 1.000 | 0.000 | 0.797 |
| opt | 0.695 | True | 0.906 | 0.508 | 12 | 0.093 | 0.955 | 0.053 | 0.847 |
| opt_c6c7 | 0.530 | True | 0.809 | 0.506 | 14 | 0.105 | 0.932 | 0.058 | 0.652 |
| opt_expert | 0.419 | False | 0.833 | 0.474 | 9 | 0.059 | 0.992 | 0.008 | 0.688 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.812 | 0.812 | 3 |
| quantile | 1.000 | 0.067 | 0 |
| kde | 0.750 | 0.188 | 1 |
| expert | 0.769 | 0.625 | 3 |
| opt | 0.833 | 0.769 | 2 |
| opt_c6c7 | 0.571 | 0.667 | 6 |
| opt_expert | 0.778 | 0.467 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.625 | 1.000 | a*c*d*e*f+a*b*c*E*f+a*b*c*D*F+a*b*C*d*F+a*B*C*d*E*f+A*b*d*e+A*b*c*d+A*B*C*d*E*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*b*c*d*e*f<->G |
| kde | 1 | 0.000 | 0.500 | 0.500 | a*c*d*e*f+a*b*c*E*f<->G |
| expert | 2 | 0.000 | 0.625 | 1.000 | a*c*d*e*f+a*b*c*E*f+a*b*c*D*F+a*b*C*d*F+a*B*C*d*E*f+A*b*d*e*F+A*b*c*d*F+A*B*C*d*E*F<->G |
| opt | 1 | 0.000 | 0.714 | 1.000 | b*c*d*e+a*c*d*e*f+a*b*c*e*F+a*b*c*E*f+a*b*C*d*F+a*B*C*d*E*f+A*b*d*e*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.429 | 1.000 | b*c*d*e+a*c*d*f+a*b*d*e*F+a*b*c*E*f+a*b*C*E*F+a*B*c*D*e*F+a*B*C*d*E<->G |
| opt_expert | 1 | 0.000 | 0.600 | 1.000 | a*c*d*e*f+a*b*c*E*f+a*b*c*D*F+a*b*C*d*F+a*B*C*d*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*E*F+b*C*d*e+a*c*d*f+a*b*c*D+a*B*C*d*E+A*b*c*d<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*c*e*f<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*d*f+a*b*c*f<->G |
| expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*E*F+b*C*d*F+a*c*d*f+a*b*c*D+a*B*C*d*E+A*b*d*F<->G |
| opt | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*F+b*d*e+B*C*d*E+a*c*d*f+a*b*e*F+a*b*c*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.167 | 0.500 | 0.000 | 1.000 | b*c*d+a*c*d*f+a*c*D*e*F+a*b*F+a*b*c+a*B*C*d*E<->G |
| opt_expert | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*F+a*c*d*f+a*c*D*e*F+a*b*c*E+a*B*C*d*E<->G |

