# n400_noise0.2_frag0.2_fz0_rep02

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=35002
- true model: `e*D+f*A*e<->G`  (irrelevant: B, C)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.493 | False | 0.890 | 0.402 | 6 | 0.000 | 1.000 | 0.000 | 0.796 |
| quantile | 0.935 | False | 0.000 | 0.000 | 0 | 0.090 | 0.985 | 0.018 | 0.623 |
| kde | 0.750 | False | 0.000 | 0.000 | 0 | 0.048 | 1.000 | 0.000 | 0.702 |
| expert | 0.637 | False | 0.887 | 0.468 | 10 | 0.041 | 1.000 | 0.000 | 0.768 |
| opt | 0.703 | True | 0.853 | 0.504 | 12 | 0.079 | 0.952 | 0.044 | 0.825 |
| opt_c6c7 | 0.600 | False | 0.876 | 0.450 | 9 | 0.102 | 0.947 | 0.065 | 0.667 |
| opt_expert | 0.548 | False | 0.863 | 0.463 | 12 | 0.091 | 0.945 | 0.046 | 0.667 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.333 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.556 | 0 |
| opt | 1.000 | 0.600 | 0 |
| opt_c6c7 | 1.000 | 0.500 | 0 |
| opt_expert | 0.917 | 0.550 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*c*D*e*F+a*b*C*D*e*f+a*B*c*D*e*f+A*b*c*e*f+A*B*c*D*e*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e+a*c*D*e*f+a*b*D*e*f+A*c*d*e*f+A*B*D*e*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e+a*b*D*e*F+a*B*D*e*f+A*c*e*f+A*B*D*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*c*D*e*f+a*b*D*e+A*c*d*e*f+A*c*D*e*F<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | b*c*D*e*F+a*C*D*e+a*B*D*e*f+a*B*C*D*f+A*c*d*e*f+A*B*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*D*e+a*c*D*F+a*C*D*f+A*b*c*e*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*e*f+c*D*e+A*D*e+A*c*d*f<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*e*f+b*D*e+A*D*e+A*c*e*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*e+a*B*f+A*c*e*f+A*c*D*e<->G |
| opt_expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | D*e+c*e*f+C*D*f<->G |

