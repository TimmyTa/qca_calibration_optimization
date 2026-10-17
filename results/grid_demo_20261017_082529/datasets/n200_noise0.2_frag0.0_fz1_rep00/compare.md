# n200_noise0.2_frag0.0_fz1_rep00

- data: n=200, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=22000
- true model: `c*D+d*f*E+e*d*A<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.561 | False | 0.798 | 0.757 | 28 | 0.000 | 1.000 | 0.000 | 0.543 |
| quantile | 0.555 | False | 0.769 | 0.746 | 30 | 0.034 | 0.970 | 0.019 | 0.530 |
| kde | 0.601 | False | 0.782 | 0.721 | 20 | 0.067 | 0.930 | 0.067 | 0.567 |
| expert | 0.575 | False | 0.780 | 0.725 | 25 | 0.062 | 0.931 | 0.069 | 0.541 |
| opt | 0.687 | True | 0.815 | 0.688 | 19 | 0.139 | 0.865 | 0.125 | 0.726 |
| opt_c6c7 | 0.633 | True | 0.804 | 0.736 | 25 | 0.061 | 0.901 | 0.098 | 0.534 |
| opt_expert | 0.641 | True | 0.812 | 0.738 | 23 | 0.049 | 0.929 | 0.070 | 0.544 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.786 | 0.688 | 6 |
| quantile | 0.700 | 0.677 | 9 |
| kde | 0.750 | 0.556 | 5 |
| expert | 0.720 | 0.581 | 7 |
| opt | 0.842 | 0.593 | 3 |
| opt_c6c7 | 0.760 | 0.594 | 6 |
| opt_expert | 0.870 | 0.625 | 3 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 6 | 0.000 | 0.500 | 1.000 | d*E*f+c*D*e*f+a*c*d*f+a*c*D*e+a*b*d*f+a*b*c*d*E+a*B*c*D+A*b*D*e*f+A*b*c*e*F+A*b*c*D+A*B*c*d*E+A*B*C*d*e<->G |
| quantile | 1 | 0.000 | 0.455 | 1.000 | C*d*E*f+b*c*D*e+B*c*d*E+a*c*D*F+a*b*d*e*f+a*b*C*D*E+A*d*e*F+A*c*e*F+A*c*d*E+A*C*D*e*f+A*b*c*D<->G |
| kde | 4 | 0.000 | 0.429 | 1.000 | B*d*E*f+B*c*D+a*b*C*d*e*f+a*B*c*e+A*B*D*e*f+A*B*c*F+A*B*C*d*e<->G |
| expert | 2 | 0.000 | 0.500 | 0.667 | b*D*E*f+b*c*D*E+B*c*E*f+a*d*E*f+a*c*D*f+a*c*D*E+a*b*d*f+a*b*c*D+a*B*c*d*e*F+A*b*c*d*F+A*B*D*e*f+A*B*c*D*e<->G |
| opt | 1 | 0.000 | 0.714 | 1.000 | c*D*e+b*D*e*f+b*c*D*F+b*C*d*E*f+A*C*d*e*F+A*b*e*F+A*b*c*D<->G |
| opt_c6c7 | 3 | 0.000 | 0.400 | 0.667 | c*D*E+b*D*e*f+b*c*D+b*C*d*E*f+a*b*c*e*f+a*B*c*E*f+A*c*D*f+A*b*e*F+A*b*E*f+A*b*c*F<->G |
| opt_expert | 12 | 0.000 | 0.576 | 1.000 | c*D*e*f+b*d*e*f+b*c*D*f+B*d*E*f+a*c*D*e+a*b*C*d*f+A*b*e*f+A*b*d*e+A*b*c*f+A*b*c*e+A*B*C*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 6 | 0.000 | 0.429 | 1.000 | 0.000 | 1.000 | d*E*f+c*f+c*D+b*e+b*c+A*d*e+A*c<->G |
| quantile | 2 | 0.000 | 0.600 | 1.000 | 0.000 | 1.000 | d*E*f+D*e*f+c+b+A*d*e<->G |
| kde | 2 | 0.000 | 0.429 | 1.000 | 0.000 | 1.000 | d*E*f+D*e*f+c*e+c*D+b+A*d*e+A*c<->G |
| expert | 2 | 0.000 | 0.500 | 0.833 | 0.000 | 1.000 | d*E*f+c*e+c*D+b+A*f<->G |
| opt | 1 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | d*e*F+d*E*f+c*D*e+a*D*e*f+a*c*E+A*b*D<->G |
| opt_c6c7 | 3 | 0.000 | 0.333 | 0.444 | 0.000 | 1.000 | d*E*f+c+b*D*e+A*b<->G |
| opt_expert | 3 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | d*E*f+c*D+b*e+A*d*e<->G |

