# n200_noise0.2_frag0.2_fz1_rep01

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=24001
- true model: `B+E*f<->G`  (irrelevant: A, C, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.437 | True | 0.894 | 0.614 | 16 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 0.439 | True | 0.894 | 0.602 | 16 | 0.039 | 0.981 | 0.017 | 0.536 |
| kde | 0.409 | True | 0.899 | 0.556 | 13 | 0.055 | 0.948 | 0.051 | 0.545 |
| expert | 0.457 | False | 0.870 | 0.598 | 11 | 0.104 | 0.864 | 0.136 | 0.552 |
| opt | 0.703 | True | 0.862 | 0.615 | 17 | 0.147 | 0.858 | 0.146 | 0.712 |
| opt_c6c7 | 0.593 | True | 0.875 | 0.653 | 18 | 0.060 | 0.887 | 0.118 | 0.528 |
| opt_expert | 0.576 | True | 0.875 | 0.641 | 17 | 0.056 | 0.897 | 0.107 | 0.533 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.457 | 0 |
| quantile | 1.000 | 0.432 | 0 |
| kde | 1.000 | 0.342 | 0 |
| expert | 1.000 | 0.367 | 0 |
| opt | 1.000 | 0.472 | 0 |
| opt_c6c7 | 1.000 | 0.514 | 0 |
| opt_expert | 1.000 | 0.472 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 7 | 1.000 | 1.000 | 1.000 | B*C*D*E*F+a*C*D*E*f+a*b*c*d*E*f+a*B*d*e*F+a*B*D*E*f+a*B*C*E*f+a*B*C*D*f+A*B*c*e*F+A*B*c*d*E+A*B*c*D*f<->G |
| quantile | 3 | 1.000 | 1.000 | 1.000 | B*D*E*f+B*c*d*e*F+B*C*D*E+a*C*D*E*f+a*b*c*d*E*f+a*B*d*e*F+a*B*C*E*f+A*B*c*E*f+A*B*c*D*e+A*B*C*d*e*f<->G |
| kde | 14 | 1.000 | 1.000 | 1.000 | B*c*d*e*F+B*c*d*E*f+a*c*d*E*f+a*B*d*e*F+a*B*C*E*f+A*B*D*E*f+A*B*c*D*e+A*B*C*d*e*f<->G |
| expert | 2 | 1.000 | 1.000 | 1.000 | B*c*d*E*f+a*C*D*E*f+a*B*E*f+a*B*d*e+a*B*c*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*D*E*f+B*c*f+a*c*d*E*f+a*C*D*E*f+a*B*f+a*B*c*d*e+a*B*C*D*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*E*f+B*c*d*E+a*c*d*E*f+a*C*D*E*f+a*B*d*e+a*B*C*D*E+A*B*c*D*f<->G |
| opt_expert | 2 | 1.000 | 1.000 | 1.000 | B*D*E*f+B*c*d*E+a*c*d*E*f+a*C*D*E*f+a*B*E*f+a*B*d*e+a*B*C*D*E+A*B*c*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*d*e*F+B*D*E+a*E*f+a*C*D+A*B*c<->G |
| quantile | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*E*f+B*E+B*d+a*C*D*E+A*B*c<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d+B*d+B*C*E*f+A*B*c<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*E+B*d*f+B*c*f+a*B*d*e<->G |
| opt | 2 | 0.000 | 0.125 | 0.250 | 0.000 | 1.000 | d*f+C*E+B*f+B*c*d*e<->G |
| opt_c6c7 | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*f+C*D*E+B*d*f+B*d*e+B*c*f+B*c*d<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*f+C*D*E+B*d*f+B*c*f+B*c*d*E+a*B*d*e<->G |

