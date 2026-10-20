# n400_noise0.0_frag0.2_fz1_rep00

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=28000
- true model: `D*c+A*c+f*C<->G`  (irrelevant: B, E)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.588 | True | 0.913 | 0.654 | 15 | 0.000 | 1.000 | 0.000 | 0.550 |
| quantile | 0.488 | True | 0.902 | 0.585 | 11 | 0.042 | 0.963 | 0.035 | 0.511 |
| kde | 0.525 | True | 0.915 | 0.577 | 11 | 0.038 | 0.967 | 0.032 | 0.515 |
| expert | 0.699 | False | 0.917 | 0.476 | 7 | 0.098 | 0.875 | 0.125 | 0.553 |
| opt | 0.859 | True | 0.928 | 0.602 | 18 | 0.116 | 0.944 | 0.055 | 0.743 |
| opt_c6c7 | 0.641 | True | 0.911 | 0.575 | 10 | 0.058 | 0.898 | 0.099 | 0.502 |
| opt_expert | 0.460 | True | 0.922 | 0.560 | 10 | 0.059 | 0.882 | 0.115 | 0.509 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.517 | 0 |
| quantile | 1.000 | 0.306 | 0 |
| kde | 1.000 | 0.297 | 0 |
| expert | 1.000 | 0.194 | 0 |
| opt | 1.000 | 0.500 | 0 |
| opt_c6c7 | 1.000 | 0.270 | 0 |
| opt_expert | 1.000 | 0.256 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.714 | 1.000 | b*c*D*f+a*D*E*f+A*c*D*E+A*b*c*E*f+A*b*C*d*e*f+A*B*D*e*f+A*B*c*e*f<->G |
| quantile | 1 | 0.000 | 0.667 | 0.667 | b*c*D*E*f+A*c*e*f+A*c*D*E*F+A*b*d*e*f+A*b*c*f+A*B*D*e*f<->G |
| kde | 1 | 0.000 | 0.833 | 1.000 | b*c*D*f+A*c*D*E*F+A*b*c*E*f+A*b*C*d*e*f+A*B*D*e*f+A*B*c*e*f<->G |
| expert | 1 | 0.000 | 0.667 | 0.333 | c*D*e*f+a*c*D*f+A*B*D*e*f<->G |
| opt | 2 | 0.000 | 0.625 | 1.000 | b*C*d*E*f+B*c*D*E+a*D*E*f+A*d*E*f+A*c*D*f+A*c*D*E+A*B*D*e*f+A*B*c*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.714 | 1.000 | a*b*c*D*E*f+a*b*C*D*e*f+A*c*D*e*F+A*b*d*e*f+A*b*c*d*f+A*B*D*e*f+A*B*c*e*f<->G |
| opt_expert | 1 | 0.000 | 0.667 | 0.667 | a*b*C*D*e*f+a*B*C*D*E*f+A*d*e*f+A*b*C*d*f+A*B*e*f+A*B*c*d*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*E*f+c*D*f+A*e*f+A*c*E<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*f+A*D*f+A*c*f+A*c*E+A*b*e*f<->G |
| kde | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.667 | c*D*f+A*f+A*c*E<->G |
| expert | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 0.000 | c*D*f+A<->G |
| opt | 2 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | c*D*E+C*f+A*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | D*f+A*f+A*c*D<->G |
| opt_expert | 1 | 0.000 | 0.333 | 0.333 | 0.000 | 0.000 | D*f+A*f+A*c<->G |

