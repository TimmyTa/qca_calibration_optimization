# n400_noise0.2_frag0.2_fz0_rep01

- data: n=400, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=35001
- true model: `c*d*B+E*f+D*b<->G`  (irrelevant: A)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.688 | True | 0.844 | 0.713 | 22 | 0.000 | 1.000 | 0.000 | 0.799 |
| quantile | 0.406 | False | 0.789 | 0.456 | 10 | 0.124 | 0.955 | 0.045 | 0.582 |
| kde | 0.659 | True | 0.805 | 0.678 | 22 | 0.063 | 1.000 | 0.000 | 0.680 |
| expert | 0.684 | False | 0.816 | 0.587 | 15 | 0.081 | 0.955 | 0.045 | 0.739 |
| opt | 0.738 | True | 0.839 | 0.577 | 19 | 0.129 | 0.907 | 0.095 | 0.765 |
| opt_c6c7 | 0.757 | True | 0.814 | 0.547 | 16 | 0.128 | 0.879 | 0.116 | 0.631 |
| opt_expert | 0.674 | True | 0.808 | 0.640 | 21 | 0.072 | 0.994 | 0.002 | 0.664 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.955 | 0.656 | 1 |
| quantile | 1.000 | 0.294 | 0 |
| kde | 0.955 | 0.656 | 1 |
| expert | 1.000 | 0.469 | 0 |
| opt | 0.895 | 0.515 | 2 |
| opt_c6c7 | 0.938 | 0.455 | 1 |
| opt_expert | 1.000 | 0.677 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.909 | 1.000 | b*c*d*E*f+b*C*D*e*F+B*c*d*e+B*c*D*E*f+a*b*c*D*E*F+a*b*C*E*f+a*B*c*d*F+A*C*D*E*F+A*b*D*e+A*b*C*D+A*B*d*E*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+a*c*D*E*f+a*b*E*f+a*b*c*D*f+a*B*c*d*e+A*b*c*D*e*F<->G |
| kde | 1 | 0.000 | 0.909 | 1.000 | b*c*d*E*f+b*C*D*e*F+B*c*d*e+B*c*D*E*f+a*b*c*D*E*F+a*b*C*E*f+a*B*c*d*F+A*C*D*E*F+A*b*D*e+A*b*C*D+A*B*d*E*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+A*c*E*f+A*b*D+A*B*d*E*f+A*B*c*d*e<->G |
| opt | 1 | 0.000 | 0.800 | 1.000 | b*C*D*e+B*c*d*e*F+B*C*d*E*f+a*b*d*E*f+a*b*D*e*F+a*b*C*D+a*B*d*e*f+a*B*D*E*f+a*B*c*d*F+A*B*C*D*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.875 | 1.000 | b*C*D*e*F+B*C*d*E*f+a*d*E*f+a*b*D*E*F+a*b*C*D+a*B*E*f+a*B*d*f+a*B*c*d*e<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*c*d*E*f+b*C*D*e*F+B*c*d*e+B*c*D*E*f+a*b*c*D*E*F+a*b*C*E*f+a*B*c*d*F+A*b*D*e+A*b*C*D+A*B*d*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | E*f+b*D+B*c*d+A*C*D*E<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*e*f+c*D*e*F+a*f+a*c*d<->G |
| kde | 2 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | E*f+b*D+B*c*d+A*C*D*E<->G |
| expert | 1 | 0.000 | 0.667 | 0.667 | 0.000 | 0.000 | E*f+b*D+B*c*d*e<->G |
| opt | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | b*D+B*c*d+a*f+A*B*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | E*f+c*e+b*D+a*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | E*f+b*D+B*c*d<->G |

