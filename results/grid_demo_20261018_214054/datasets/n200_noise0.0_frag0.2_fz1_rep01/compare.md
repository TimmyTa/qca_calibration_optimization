# n200_noise0.0_frag0.2_fz1_rep01

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=16001
- true model: `C*e*d+c*a*D<->G`  (irrelevant: B, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.915 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.548 |
| quantile | 0.815 | False | 0.000 | 0.000 | 0 | 0.039 | 0.970 | 0.023 | 0.541 |
| kde | 0.830 | False | 0.000 | 0.000 | 0 | 0.033 | 0.980 | 0.017 | 0.543 |
| expert | 0.905 | False | 0.000 | 0.000 | 0 | 0.071 | 0.901 | 0.099 | 0.537 |
| opt | 0.798 | True | 0.917 | 0.513 | 7 | 0.160 | 0.948 | 0.053 | 0.820 |
| opt_c6c7 | 0.366 | False | 0.925 | 0.337 | 3 | 0.071 | 0.905 | 0.090 | 0.566 |
| opt_expert | 0.352 | False | 0.916 | 0.341 | 3 | 0.049 | 0.946 | 0.045 | 0.564 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 1.000 | 0.636 | 0 |
| opt_c6c7 | 1.000 | 0.214 | 0 |
| opt_expert | 1.000 | 0.231 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*d*e*F+a*c*D*e*f+a*c*D*E*F+a*b*C*d*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | a*c*D*e*f+a*B*c*D*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | a*b*c*D*e*f+a*B*c*D*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | C*d*e+a*c*D*f+a*c*D*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | a*c*D<->G |
| opt_expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*D*e+a*B*c<->G |

