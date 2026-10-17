# n400_noise0.0_frag0.0_fz0_rep01

- data: n=400, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=25001
- true model: `F*b+f*D<->G`  (irrelevant: A, C, E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.754 | True | 0.941 | 0.819 | 24 | 0.000 | 1.000 | 0.000 | 0.795 |
| quantile | 0.634 | True | 0.817 | 0.658 | 24 | 0.096 | 0.974 | 0.008 | 0.609 |
| kde | 0.743 | True | 0.890 | 0.776 | 24 | 0.057 | 1.000 | 0.000 | 0.681 |
| expert | 0.750 | True | 0.942 | 0.752 | 24 | 0.038 | 1.000 | 0.000 | 0.772 |
| opt | 0.855 | True | 0.906 | 0.674 | 23 | 0.090 | 0.944 | 0.075 | 0.734 |
| opt_c6c7 | 0.797 | True | 0.877 | 0.577 | 17 | 0.111 | 0.911 | 0.105 | 0.624 |
| opt_expert | 0.789 | True | 0.860 | 0.611 | 19 | 0.106 | 0.919 | 0.085 | 0.645 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.750 | 0 |
| quantile | 1.000 | 0.750 | 0 |
| kde | 1.000 | 0.750 | 0 |
| expert | 1.000 | 0.750 | 0 |
| opt | 1.000 | 0.742 | 0 |
| opt_c6c7 | 1.000 | 0.548 | 0 |
| opt_expert | 0.895 | 0.567 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.800 | 1.000 | c*D*E*f+b*d*e*F+b*c*D+b*C*d*F+a*C*D*e*f+a*b*D*f+A*c*D*f+A*b*d*F+A*b*D*e+A*B*D*E*f<->G |
| quantile | 3 | 0.000 | 0.815 | 1.000 | c*D*E*f+b*c*e*F+b*C*d*F+a*C*D*e*f+a*b*D*E+A*c*D*f+A*b*e*F+A*b*c*F+A*B*D*f<->G |
| kde | 4 | 0.000 | 0.800 | 1.000 | c*D*E*f+b*d*e*F+b*c*D+b*C*d*F+a*C*D*e*f+a*b*D*f+A*c*D*f+A*b*d*F+A*b*D*e+A*B*D*E*f<->G |
| expert | 4 | 0.000 | 0.800 | 1.000 | c*D*E*f+b*d*e*F+b*c*D+b*C*d*F+a*C*D*e*f+a*b*D*f+A*c*D*f+A*b*d*F+A*b*D*e+A*B*D*E*f<->G |
| opt | 2 | 0.000 | 0.812 | 1.000 | c*D*f+b*d*e*F+b*c*D+B*D*e*f+a*b*e*F+a*b*D*f+a*b*C*d*F+A*b*c*F<->G |
| opt_c6c7 | 4 | 0.500 | 0.929 | 1.000 | c*D*f+b*c*d*e*F+B*D*e*f+a*D*e*f+a*b*C*d*F+A*b*c*e*F+A*b*c*d*F<->G |
| opt_expert | 2 | 0.000 | 0.722 | 1.000 | b*d*e*F+B*c*D*f+a*c*D*E*F+a*b*e*F+a*b*C*d*F+a*B*D*e*f+A*c*D*e*f+A*b*c*F+A*B*C*D*e*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*f+b*F<->G |
| quantile | 2 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | D*e*f+b*F+b*D+a*c*D+A*D*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*f+b*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*f+b*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*f+b*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*f+b*F<->G |
| opt_expert | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | D*f+b*F+a*D*E+A*C*D*e<->G |

