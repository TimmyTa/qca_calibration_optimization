# n400_noise0.1_frag0.2_fz0_rep00

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=31000
- true model: `F*C+B*a*c+c*D*B<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.542 | True | 0.909 | 0.509 | 9 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.168 | False | 0.886 | 0.207 | 1 | 0.109 | 0.979 | 0.039 | 0.597 |
| kde | 0.690 | False | 0.000 | 0.000 | 0 | 0.062 | 1.000 | 0.000 | 0.677 |
| expert | 0.673 | False | 0.920 | 0.379 | 6 | 0.055 | 0.958 | 0.042 | 0.759 |
| opt | 0.766 | True | 0.898 | 0.520 | 12 | 0.106 | 0.925 | 0.065 | 0.842 |
| opt_c6c7 | 0.595 | False | 0.860 | 0.460 | 11 | 0.111 | 0.933 | 0.064 | 0.647 |
| opt_expert | 0.633 | False | 0.858 | 0.449 | 11 | 0.092 | 0.951 | 0.050 | 0.654 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.375 | 0 |
| quantile | 1.000 | 0.037 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.222 | 0 |
| opt | 1.000 | 0.444 | 0 |
| opt_c6c7 | 1.000 | 0.423 | 0 |
| opt_expert | 1.000 | 0.440 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.800 | 0.667 | B*C*D*E*F+a*B*c*d*E+A*C*D*e*F+A*B*D*F+A*B*C*e*F<->G |
| quantile | 1 | 1.000 | 1.000 | 0.333 | a*B*C*D*E*F<->G |
| kde | 0 |  |  |  | (none) |
| expert | 2 | 1.000 | 1.000 | 0.333 | B*C*d*e*F+a*B*C*E*F+A*B*C*D*F<->G |
| opt | 1 | 0.000 | 0.800 | 1.000 | B*C*E*F+B*C*d*F+a*B*c*d*E+A*B*D*e*F+A*B*c*D*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*C*D*E*F+a*B*c*d*E*f+A*b*C*D*F+A*B*c*D+A*B*C*d*F<->G |
| opt_expert | 1 | 0.000 | 0.600 | 0.667 | B*D*E*F+a*B*c*E*F+A*C*e*F+A*B*D*F+A*B*C*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.750 | C*D*F+B*c*d*E+A*B*D*F+A*B*C*F<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | a*C*D*F<->G |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*e*F+C*D*F+a*C*F<->G |
| opt | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | c*D*e+B*c*D*f+B*C*F+a*c<->G |
| opt_c6c7 | 5 | 0.000 | 0.250 | 0.333 | 0.000 | 0.200 | C*D*F+B*c*D+B*C*F+a*c*d<->G |
| opt_expert | 3 | 0.000 | 0.333 | 0.333 | 0.000 | 0.333 | C*F+B*D*F+a*E*F<->G |

