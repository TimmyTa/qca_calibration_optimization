# n200_noise0.2_frag0.2_fz0_rep01

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=23001
- true model: `F*b+f*e*a<->G`  (irrelevant: C, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.566 | True | 0.845 | 0.667 | 12 | 0.000 | 1.000 | 0.000 | 0.803 |
| quantile | 0.356 | False | 0.775 | 0.393 | 7 | 0.108 | 0.965 | 0.023 | 0.606 |
| kde | 0.465 | True | 0.830 | 0.513 | 8 | 0.058 | 1.000 | 0.000 | 0.691 |
| expert | 0.578 | True | 0.867 | 0.581 | 12 | 0.034 | 1.000 | 0.000 | 0.806 |
| opt | 0.699 | True | 0.893 | 0.548 | 11 | 0.070 | 0.952 | 0.040 | 0.843 |
| opt_c6c7 | 0.584 | True | 0.809 | 0.517 | 12 | 0.102 | 0.952 | 0.056 | 0.650 |
| opt_expert | 0.596 | True | 0.829 | 0.553 | 10 | 0.069 | 0.997 | 0.003 | 0.687 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.545 | 0 |
| quantile | 1.000 | 0.318 | 0 |
| kde | 1.000 | 0.364 | 0 |
| expert | 1.000 | 0.545 | 0 |
| opt | 1.000 | 0.550 | 0 |
| opt_c6c7 | 1.000 | 0.545 | 0 |
| opt_expert | 1.000 | 0.455 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.833 | 1.000 | b*c*d*E*F+a*b*d*e*f+a*b*C*D*e+a*B*D*e*f+A*b*c*D*F+A*b*C*e*F<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | a*C*d*e*f+a*b*d*e*f+A*b*c*F<->G |
| kde | 1 | 0.000 | 0.833 | 1.000 | a*b*d*e*f+a*b*C*D*e+a*B*c*D*e*f+A*b*c*d*E*F+A*b*c*D*e*F+A*b*C*d*e*F<->G |
| expert | 4 | 0.500 | 0.917 | 1.000 | b*C*D*e*F+a*D*e*f+a*b*e*f+A*b*c*E*F+A*b*c*D*F+A*b*C*e*F<->G |
| opt | 1 | 0.000 | 0.833 | 1.000 | a*D*e*f+a*b*e*f+a*b*C*D*e+A*b*c*E*F+A*b*c*D*F+A*b*C*d*e*F<->G |
| opt_c6c7 | 2 | 1.000 | 1.000 | 1.000 | a*c*d*e*f+a*b*C*e*f+a*B*D*e*f+A*b*e*F+A*b*c*F<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | a*b*d*e*f+a*b*C*D*e+a*B*D*e*f+A*b*c*E*F+A*b*c*D*F+A*b*C*d*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*e*F+b*D*F+b*c*E*F+a*d*e*f+a*C*e*f+a*B*e*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*d*e*f+A*b*c*F<->G |
| kde | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*e*F+C*d*e*F+a*d*e*f+a*b*C*e+a*B*c*D*e+A*b*d*E*F<->G |
| expert | 7 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | C*d*e*F+b*D*F+a*e*f+A*b*E*F<->G |
| opt | 6 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | C*d*e*F+a*e+A*c*D*F+A*b*d*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 0.000 | a*e*f+A*b*F<->G |
| opt_expert | 8 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | c*D*e*F+C*d*e*F+a*e*f+a*b*e+A*b*E*F<->G |

