# n200_noise0.1_frag0.0_fz0_rep00

- data: n=200, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=17000
- true model: `E*f+d*f+E*c<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.653 | True | 0.873 | 0.757 | 22 | 0.000 | 1.000 | 0.000 | 0.796 |
| quantile | 0.589 | True | 0.830 | 0.609 | 22 | 0.098 | 0.966 | 0.037 | 0.605 |
| kde | 0.623 | True | 0.843 | 0.716 | 21 | 0.050 | 1.000 | 0.000 | 0.699 |
| expert | 0.648 | True | 0.855 | 0.720 | 22 | 0.039 | 1.000 | 0.000 | 0.781 |
| opt | 0.740 | True | 0.836 | 0.614 | 20 | 0.124 | 0.922 | 0.092 | 0.674 |
| opt_c6c7 | 0.700 | True | 0.813 | 0.582 | 18 | 0.106 | 0.910 | 0.088 | 0.648 |
| opt_expert | 0.688 | True | 0.827 | 0.538 | 16 | 0.101 | 0.939 | 0.056 | 0.639 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.710 | 0 |
| quantile | 0.955 | 0.656 | 1 |
| kde | 1.000 | 0.677 | 0 |
| expert | 1.000 | 0.710 | 0 |
| opt | 1.000 | 0.714 | 0 |
| opt_c6c7 | 1.000 | 0.621 | 0 |
| opt_expert | 0.938 | 0.484 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*d*E*f+b*c*D*E*F+b*C*d*f+B*c*d*e*f+B*c*D*E*f+a*c*d*E*F+a*b*C*E*f+A*d*f+A*c*D*E+A*B*E*f<->G |
| quantile | 4 | 0.000 | 0.900 | 1.000 | c*D*E*F+b*C*E*f+b*C*d*f+B*c*d*e*f+B*c*D*E+a*c*E*F+A*d*e*f+A*C*E*f+A*b*d*f+A*B*c*D*f<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | b*d*E*f+b*c*D*E*F+b*C*d*f+B*c*d*e*f+B*c*D*E*f+a*c*d*E*F+A*d*f+A*c*D*E+A*B*E*f<->G |
| expert | 2 | 1.000 | 1.000 | 1.000 | b*d*E*f+b*c*D*E*F+b*C*d*f+B*c*d*e*f+B*c*D*E*f+a*c*d*E*F+a*b*C*E*f+A*d*f+A*c*D*E+A*B*E*f<->G |
| opt | 6 | 1.000 | 1.000 | 1.000 | c*d*e*f+C*d*E*f+b*d*f+b*c*D*E*F+a*c*d*E*F+a*b*C*E*f+A*d*e*f+A*b*c*E*f+A*B*C*E*f<->G |
| opt_c6c7 | 12 | 1.000 | 1.000 | 1.000 | b*C*D*E*f+B*c*d*e*f+a*b*c*E*F+a*b*C*d*f+a*B*c*D*E+A*d*e*f+A*D*E*f+A*b*c*D*E+A*B*C*E*f<->G |
| opt_expert | 1 | 0.000 | 0.875 | 1.000 | b*c*d*E+b*C*E*f+a*c*d*E*F+A*d*E*f+A*C*E*f+A*C*d*f+A*b*E*f+A*B*C*d*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | E*f+d*f+c*E<->G |
| quantile | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | E*f+d*f+c*E+A*f<->G |
| kde | 4 | 0.000 | 0.667 | 0.667 | 0.000 | 1.000 | d*f+c*E+A*E*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | E*f+d*f+c*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | E*f+d*f+c*E<->G |
| opt_c6c7 | 2 | 0.500 | 0.833 | 0.833 | 0.500 | 0.000 | E*f+d*e+c*E<->G |
| opt_expert | 2 | 0.000 | 0.375 | 0.500 | 0.000 | 1.000 | E*f+d*f+c*d*E+B*d<->G |

