# n400_noise0.2_frag0.2_fz1_rep00

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=36000
- true model: `f*d*C+a*B*D<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.612 | True | 0.815 | 0.653 | 13 | 0.000 | 1.000 | 0.000 | 0.552 |
| quantile | 0.538 | True | 0.811 | 0.616 | 10 | 0.036 | 0.976 | 0.031 | 0.525 |
| kde | 0.558 | True | 0.828 | 0.621 | 12 | 0.027 | 0.985 | 0.015 | 0.543 |
| expert | 0.466 | False | 0.802 | 0.657 | 15 | 0.078 | 0.927 | 0.073 | 0.566 |
| opt | 0.800 | True | 0.815 | 0.553 | 14 | 0.113 | 0.896 | 0.101 | 0.701 |
| opt_c6c7 | 0.626 | True | 0.811 | 0.603 | 10 | 0.047 | 0.922 | 0.077 | 0.523 |
| opt_expert | 0.635 | True | 0.813 | 0.617 | 11 | 0.047 | 0.950 | 0.050 | 0.537 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.846 | 0.733 | 2 |
| quantile | 0.900 | 0.562 | 1 |
| kde | 0.833 | 0.667 | 2 |
| expert | 0.533 | 0.571 | 7 |
| opt | 0.929 | 0.867 | 1 |
| opt_c6c7 | 0.900 | 0.600 | 1 |
| opt_expert | 0.909 | 0.667 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.625 | 1.000 | C*d*e*f+a*B*e*f+a*B*c*D*E+a*B*C*E*F+a*B*C*d*E+A*b*C*d*f<->G |
| quantile | 1 | 0.000 | 0.800 | 1.000 | C*d*e*f+a*B*e*f+a*B*C*d*f+a*B*C*D*E*F+A*b*C*d*f<->G |
| kde | 1 | 0.000 | 0.500 | 1.000 | b*C*d*f+a*B*e*f+a*B*D*E*F+a*B*C*d*E<->G |
| expert | 3 | 0.000 | 0.208 | 0.500 | b*c*d*E*f+a*b*C*d*e+a*B*c*e*f+a*B*c*D*E+a*B*C*E*F+a*B*C*d*E+A*b*d*f+A*B*C*d*e*F<->G |
| opt | 1 | 0.000 | 0.500 | 1.000 | C*d*f+a*B*D*E+a*B*C*f+a*B*C*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.750 | 1.000 | B*C*d*e*f+a*C*d*e*f+a*B*D*f+a*B*C*E<->G |
| opt_expert | 2 | 0.000 | 0.700 | 1.000 | b*C*d*f+a*C*d*f+a*B*D*e*f+a*B*c*D*f+a*B*C*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | C*e*f+B*C*E+a*B*f+a*B*D+A*C*d*f<->G |
| quantile | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | C*d*f+a*B*c*e+a*B*C*D<->G |
| kde | 2 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | C*d*f+B*C*E+a*e*f+a*B*D<->G |
| expert | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*f+a*e*f+a*C*E+a*b*C+a*B*D*E+A*B*C*d<->G |
| opt | 3 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | C*d*f+a*C*E*F+a*B*D<->G |
| opt_c6c7 | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*f+a*e*f+a*B*f+a*B*C<->G |
| opt_expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | C*d*f+a*B*f+a*B*C*E<->G |

