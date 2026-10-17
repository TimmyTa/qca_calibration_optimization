# n100_noise0.1_frag0.2_fz0_rep02

- data: n=100, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=7002
- true model: `b*C+E*d*A<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.542 | True | 0.859 | 0.754 | 14 | 0.000 | 1.000 | 0.000 | 0.805 |
| quantile | 0.450 | False | 0.771 | 0.542 | 11 | 0.123 | 0.932 | 0.055 | 0.569 |
| kde | 0.541 | True | 0.829 | 0.736 | 13 | 0.060 | 1.000 | 0.000 | 0.686 |
| expert | 0.557 | True | 0.872 | 0.609 | 12 | 0.089 | 1.000 | 0.000 | 0.745 |
| opt | 0.762 | True | 0.877 | 0.578 | 8 | 0.129 | 0.932 | 0.062 | 0.705 |
| opt_c6c7 | 0.660 | True | 0.829 | 0.572 | 9 | 0.116 | 0.897 | 0.127 | 0.615 |
| opt_expert | 0.682 | True | 0.848 | 0.649 | 10 | 0.087 | 0.947 | 0.058 | 0.646 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.786 | 0.611 | 3 |
| quantile | 0.636 | 0.438 | 4 |
| kde | 0.846 | 0.611 | 2 |
| expert | 0.917 | 0.611 | 1 |
| opt | 1.000 | 0.615 | 0 |
| opt_c6c7 | 1.000 | 0.692 | 0 |
| opt_expert | 0.900 | 0.529 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.625 | 1.000 | b*C*d*F+a*b*C*e*f+a*B*c*D*E*f+A*C*d*E*F+A*b*d*e*f+A*b*d*E*F+A*b*c*E*f+A*b*C*E*F<->G |
| quantile | 1 | 0.000 | 0.500 | 1.000 | B*C*d*E*F+a*b*C*e*F+A*c*d*E*f+A*b*c*E*f+A*b*C*E*F+A*B*C*d*e<->G |
| kde | 2 | 0.000 | 0.714 | 1.000 | b*C*d*F+a*b*C*e*f+A*C*d*E*F+A*b*d*e*f+A*b*d*E*F+A*b*c*E*f+A*b*C*E*F<->G |
| expert | 2 | 0.000 | 0.857 | 1.000 | b*C*d*F+b*C*d*e+a*b*C*e*f+A*C*d*E*F+A*b*d*E*F+A*b*c*E*f+A*b*C*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*C*d*E+A*C*d*E*F+A*b*d*E+A*b*C*E*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*d*F+A*C*d*E*F+A*b*c*d*E+A*b*C*e*F+A*b*C*d*e<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | b*C*d*E+A*C*d*E*F+A*b*d*E+A*b*c*E*f+A*b*C*E*F+A*b*C*d*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.400 | 1.000 | 0.000 | 1.000 | b*C+a*B*c*D*E+A*d*f+A*d*E+A*b*E*f<->G |
| quantile | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | C*d*F+b*C*F+A*d+A*b*E<->G |
| kde | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | b*C+A*d*f+A*d*E+A*b*E*f<->G |
| expert | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | b*C+A*d*E+A*b*E*f<->G |
| opt | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | b*E*F+b*d*E+A*C*d*E<->G |
| opt_c6c7 | 7 | 0.000 | 0.333 | 0.500 | 0.000 | 0.714 | b*d*E+b*C+A*C*d*E<->G |
| opt_expert | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 0.500 | b*C+A*C*d+A*b*E<->G |

