# n100_noise0.0_frag0.2_fz0_rep01

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=3001
- true model: `f*B*C+a*E*C+c*A*b<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.643 | True | 0.919 | 0.769 | 11 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.520 | True | 0.821 | 0.612 | 9 | 0.104 | 0.975 | 0.055 | 0.612 |
| kde | 0.530 | True | 0.873 | 0.715 | 10 | 0.046 | 1.000 | 0.000 | 0.710 |
| expert | 0.637 | True | 0.896 | 0.739 | 12 | 0.067 | 0.965 | 0.035 | 0.756 |
| opt | 0.775 | True | 0.955 | 0.591 | 9 | 0.121 | 0.917 | 0.078 | 0.779 |
| opt_c6c7 | 0.712 | True | 0.904 | 0.591 | 9 | 0.104 | 0.908 | 0.093 | 0.651 |
| opt_expert | 0.690 | True | 0.939 | 0.507 | 9 | 0.090 | 0.987 | 0.028 | 0.670 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.579 | 0 |
| quantile | 1.000 | 0.474 | 0 |
| kde | 1.000 | 0.526 | 0 |
| expert | 1.000 | 0.667 | 0 |
| opt | 1.000 | 0.600 | 0 |
| opt_c6c7 | 1.000 | 0.600 | 0 |
| opt_expert | 1.000 | 0.450 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.667 | a*C*E*f+a*b*C*d*E+A*b*c*e+A*b*c*d*f+A*b*c*D*F<->G |
| quantile | 1 | 1.000 | 1.000 | 0.667 | a*C*E*f+a*b*C*d*E+A*b*c*e*f+A*b*c*d*f+A*b*c*d*e<->G |
| kde | 1 | 1.000 | 1.000 | 0.667 | a*C*E*f+a*b*C*d*E+A*b*c*e+A*b*c*d*f<->G |
| expert | 1 | 1.000 | 1.000 | 0.667 | a*C*E*f+a*b*C*d*E+A*b*c*f+A*b*c*e+A*b*c*D<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*C*d*E*f+a*B*C*E*f+a*B*C*d*E+A*b*c*e+A*b*c*d*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*C*d*E*f+a*B*C*E*f+a*B*C*d*E+A*b*c*e+A*b*c*d*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.667 | a*b*C*E*f+a*b*C*d*E+A*b*c*e+A*b*c*d*f+A*b*c*D*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | a*C*E+A*b*c<->G |
| quantile | 9 | 0.000 | 0.083 | 0.111 | 0.000 | 1.000 | b*c*f+a*d*E+a*C*f+A*b*c*d<->G |
| kde | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 0.500 | c*d*E+a*C*E+A*b*e<->G |
| expert | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | a*C*E+A*b*c<->G |
| opt | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | a*C*E+A*b*c<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | b*c+a*C*E<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 0.000 | a*b*E+A*b*c<->G |

