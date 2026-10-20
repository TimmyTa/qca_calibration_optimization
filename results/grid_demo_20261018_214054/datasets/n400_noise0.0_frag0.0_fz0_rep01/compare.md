# n400_noise0.0_frag0.0_fz0_rep01

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=25001
- true model: `F*b+f*D<->G`  (irrelevant: A, C, E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.719 | True | 0.941 | 0.819 | 24 | 0.000 | 1.000 | 0.000 | 0.795 |
| quantile | 0.448 | False | 0.882 | 0.271 | 3 | 0.096 | 0.974 | 0.008 | 0.609 |
| kde | 0.383 | False | 0.885 | 0.415 | 7 | 0.057 | 1.000 | 0.000 | 0.681 |
| expert | 0.706 | True | 0.943 | 0.731 | 23 | 0.038 | 1.000 | 0.000 | 0.772 |
| opt | 0.851 | True | 0.949 | 0.646 | 23 | 0.096 | 0.946 | 0.073 | 0.759 |
| opt_c6c7 | 0.797 | True | 0.904 | 0.562 | 17 | 0.117 | 0.904 | 0.115 | 0.626 |
| opt_expert | 0.828 | True | 0.900 | 0.567 | 15 | 0.109 | 0.907 | 0.095 | 0.630 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.750 | 0 |
| quantile | 1.000 | 0.094 | 0 |
| kde | 1.000 | 0.219 | 0 |
| expert | 1.000 | 0.719 | 0 |
| opt | 1.000 | 0.742 | 0 |
| opt_c6c7 | 1.000 | 0.548 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.800 | 1.000 | c*D*E*f+b*d*e*F+b*c*D+b*C*d*F+a*C*D*e*f+a*b*D*f+A*c*D*f+A*b*d*F+A*b*D*e+A*B*D*E*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | b*c*D*E*F+A*b*c*D*F<->G |
| kde | 1 | 0.000 | 0.750 | 1.000 | b*c*D*E*F+a*b*C*D*e*f+A*c*D*E*f+A*b*c*D<->G |
| expert | 1 | 0.000 | 0.778 | 1.000 | c*D*E*f+b*d*e*F+b*c*D+a*C*D*e*f+a*b*D*f+A*c*D*f+A*b*d*F+A*b*D*e+A*B*D*E*f<->G |
| opt | 2 | 0.000 | 0.812 | 1.000 | c*D*f+b*d*e*F+b*c*D+B*D*e*f+a*b*e*F+a*b*D*f+a*b*C*d*F+A*b*c*F<->G |
| opt_c6c7 | 4 | 0.500 | 0.929 | 1.000 | c*D*f+b*c*d*e*F+B*D*e*f+a*D*e*f+a*b*C*d*F+A*b*c*e*F+A*b*c*d*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*d*e*F+b*c*D*F+B*c*D*f+a*b*C*d*F+a*B*D*e*f+A*b*c*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*f+b*F<->G |
| quantile | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*c*E*F+A*b*c*D*F<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*D*E*F+a*b*C*D*e+A*c*D*E*f+A*b*c*D<->G |
| expert | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | D*f+b*e*F+b*D+A*b*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*f+b*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*f+b*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*f+b*F<->G |

