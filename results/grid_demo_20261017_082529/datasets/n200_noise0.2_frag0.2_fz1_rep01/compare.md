# n200_noise0.2_frag0.2_fz1_rep01

- data: n=200, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=24001
- true model: `B+E*f<->G`  (irrelevant: A, C, D)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.643 | False | 0.784 | 0.755 | 38 | 0.000 | 1.000 | 0.000 | 0.545 |
| quantile | 0.647 | False | 0.793 | 0.743 | 36 | 0.039 | 0.981 | 0.017 | 0.536 |
| kde | 0.667 | True | 0.811 | 0.743 | 32 | 0.055 | 0.948 | 0.051 | 0.545 |
| expert | 0.714 | False | 0.816 | 0.724 | 24 | 0.104 | 0.864 | 0.136 | 0.552 |
| opt | 0.782 | True | 0.834 | 0.674 | 24 | 0.124 | 0.877 | 0.122 | 0.692 |
| opt_c6c7 | 0.723 | True | 0.812 | 0.747 | 28 | 0.079 | 0.863 | 0.140 | 0.529 |
| opt_expert | 0.737 | True | 0.818 | 0.733 | 28 | 0.077 | 0.876 | 0.127 | 0.533 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.658 | 0.714 | 13 |
| quantile | 0.667 | 0.649 | 12 |
| kde | 0.750 | 0.632 | 8 |
| expert | 0.792 | 0.633 | 5 |
| opt | 1.000 | 0.706 | 0 |
| opt_c6c7 | 0.857 | 0.686 | 4 |
| opt_expert | 0.857 | 0.686 | 4 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.529 | 1.000 | c*e*F+b*C*D*E*f+B*C*E*F+B*C*D*e*f+a*C*d*F+a*b*d*e+a*b*c*F+a*b*c*d+a*B*D*E*f+a*B*C*E+A*D*e*F+A*C*e*f+A*b*D*E*f+A*b*C*f+A*B*D*e+A*B*c*E*f+A*B*c*d*F<->G |
| quantile | 10 | 0.000 | 0.575 | 1.000 | b*c*D*e+b*C*E*f+B*D*E*f+B*c*e*F+B*C*D*f+B*C*D*E+a*C*E*f+a*C*d*e*F+a*b*d*f+a*b*d*E+a*b*c*D*F+A*D*f+A*c*e*F+A*B*D*e+A*B*c*E*f+A*B*C*e*f<->G |
| kde | 3 | 0.000 | 0.611 | 1.000 | b*c*D*e+b*C*E*f+B*c*e*F+B*c*E*f+B*C*D*f+a*d*E*f+a*C*d*e*F+a*b*C*d*e+a*b*C*D*E+A*D*f+A*B*C*e*f+A*B*C*D<->G |
| expert | 1 | 0.000 | 0.600 | 1.000 | b*c*d*e*f+B*c*d*e*F+B*c*d*E*f+B*C*D*e*f+a*e*f+a*d*f+a*C*f+a*B*f+a*B*e+a*B*C*d<->G |
| opt | 5 | 1.000 | 1.000 | 1.000 | B*E*f+B*c*d*F+a*c*d*E*f+a*C*D*E*f+a*B*E+a*B*d+a*B*c*F+a*B*C*f+A*B*c*D*e<->G |
| opt_c6c7 | 3 | 0.000 | 0.769 | 1.000 | c*d*E*f+B*D*E*f+B*c*e*F+a*c*d*E+a*c*D*e+a*C*D*E*f+a*B*E*f+a*B*d*e*F+a*B*D*f+a*B*D*E+a*B*c+A*c*D*f+A*B*C*d*E*F<->G |
| opt_expert | 2 | 0.000 | 0.727 | 1.000 | B*c*e*F+B*c*E*f+B*C*d*E*F+a*c*e*F+a*c*d*E*f+a*c*D*e+a*C*D*E*f+a*B*f+a*B*E+a*B*d+A*c*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | f+e+B+a<->G |
| quantile | 4 | 0.000 | 0.375 | 0.750 | 0.000 | 1.000 | f+c+B+a<->G |
| kde | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | f+e+C*D<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | f+B<->G |
| opt | 4 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*d*f+B+a*D<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | f+e+d+B<->G |
| opt_expert | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 0.000 | f+e+B<->G |

