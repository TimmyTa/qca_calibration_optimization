# n100_noise0.2_frag0.2_fz0_rep00

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=11000
- true model: `a*E*b+a*f+A*D<->G`  (irrelevant: C)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.587 | True | 0.853 | 0.787 | 19 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.507 | True | 0.818 | 0.610 | 21 | 0.107 | 0.970 | 0.048 | 0.605 |
| kde | 0.565 | True | 0.834 | 0.707 | 19 | 0.059 | 1.000 | 0.000 | 0.689 |
| expert | 0.568 | True | 0.842 | 0.704 | 18 | 0.042 | 1.000 | 0.000 | 0.818 |
| opt | 0.674 | True | 0.885 | 0.658 | 17 | 0.123 | 0.917 | 0.090 | 0.810 |
| opt_c6c7 | 0.620 | True | 0.810 | 0.667 | 18 | 0.100 | 0.968 | 0.023 | 0.633 |
| opt_expert | 0.611 | True | 0.827 | 0.655 | 18 | 0.066 | 0.990 | 0.000 | 0.680 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.655 | 0 |
| quantile | 0.952 | 0.606 | 1 |
| kde | 0.947 | 0.621 | 1 |
| expert | 0.944 | 0.586 | 1 |
| opt | 0.824 | 0.583 | 3 |
| opt_c6c7 | 0.889 | 0.552 | 2 |
| opt_expert | 0.944 | 0.586 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.714 | 1.000 | b*D*e*f+b*C*D*f+a*b*d*E+a*b*C*E+a*B*c*d*f+A*C*D*e*F+A*B*c*D<->G |
| quantile | 1 | 0.000 | 0.571 | 1.000 | b*D*e*f+b*C*D*f+b*C*D*e+a*d*f+a*b*C*d*E+A*B*D*e*F+A*B*c*D*E<->G |
| kde | 4 | 0.000 | 0.667 | 1.000 | b*D*e*f+b*C*D*f+B*C*D*e*F+a*b*d*E+a*b*C*E+a*B*c*d*f+A*C*D*e*F+A*B*c*D*f+A*B*c*D*e<->G |
| expert | 2 | 0.000 | 0.667 | 1.000 | b*D*e*f+b*C*D*f+a*b*d*E+a*b*C*E+a*B*c*d*f+a*B*c*d*e+A*b*C*D*e+A*B*c*D*f+A*B*c*D*e<->G |
| opt | 1 | 0.000 | 0.500 | 0.667 | b*D*e*f+b*C*D*f+b*C*D*e+a*c*d*e*f+a*b*d*e+a*b*C*f+A*c*D*e*F+A*B*c*D*E*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.650 | 1.000 | b*c*D*e*f+a*b*d*E*F+a*b*C*E+a*B*c*d*e*F+a*B*c*d*E*f+A*c*D*E*F+A*b*C*D*f+A*b*C*D*e+A*B*c*e*f+A*B*c*D<->G |
| opt_expert | 2 | 0.000 | 0.667 | 1.000 | b*D*e*f+b*C*D*f+a*b*d*E+a*b*C*E+a*B*c*d*f+a*B*c*d*e+A*b*C*D*e+A*B*c*D*f+A*B*c*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.300 | 0.500 | 0.000 | 1.000 | D*f+b*C+a*f+a*b*E+A*B*D<->G |
| quantile | 20 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | D*f+a*f+a*b*C+A*b*e+A*B*D<->G |
| kde | 12 | 0.000 | 0.300 | 0.500 | 0.000 | 1.000 | D*f+a*f+a*C+a*b*E+A*D*e<->G |
| expert | 4 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | D*f+b*C+a*f+a*d*e+a*b*E+A*c*D*e<->G |
| opt | 2 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | D*f+b*C*D+a*f+a*b*d*e+A*c*D*e<->G |
| opt_c6c7 | 4 | 0.000 | 0.333 | 0.667 | 0.000 | 1.000 | c*e*f+c*D+b*D+a*f+a*d*e+a*b<->G |
| opt_expert | 17 | 0.000 | 0.088 | 0.118 | 0.000 | 0.824 | D*f+c*D*e+b*C+a*c<->G |

