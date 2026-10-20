# n400_noise0.1_frag0.2_fz0_rep01

- data: n=400, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=31001
- true model: `D*b+E*B<->G`  (irrelevant: A, C, F)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.692 | True | 0.914 | 0.705 | 18 | 0.000 | 1.000 | 0.000 | 0.795 |
| quantile | 0.681 | True | 0.901 | 0.512 | 14 | 0.103 | 0.966 | 0.028 | 0.627 |
| kde | 0.689 | True | 0.912 | 0.611 | 16 | 0.053 | 1.000 | 0.000 | 0.700 |
| expert | 0.753 | True | 0.929 | 0.668 | 20 | 0.053 | 1.000 | 0.000 | 0.772 |
| opt | 0.818 | True | 0.876 | 0.578 | 16 | 0.112 | 0.932 | 0.067 | 0.754 |
| opt_c6c7 | 0.787 | True | 0.881 | 0.567 | 16 | 0.104 | 0.945 | 0.070 | 0.656 |
| opt_expert | 0.783 | True | 0.916 | 0.556 | 15 | 0.076 | 0.958 | 0.047 | 0.684 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.643 | 0 |
| quantile | 1.000 | 0.452 | 0 |
| kde | 1.000 | 0.571 | 0 |
| expert | 1.000 | 0.714 | 0 |
| opt | 1.000 | 0.571 | 0 |
| opt_c6c7 | 1.000 | 0.552 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*c*D*e*F+b*C*D*E*f+B*C*d*E*f+a*b*D*F+a*b*D*E+a*B*E*F+A*B*c*E<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | B*D*E*F+a*b*c*D*E+a*b*C*D*F+a*B*C*E*F+A*b*C*D*E+A*B*c*E*F+A*B*c*D*E+A*B*C*d*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*C*D*E*f+B*C*d*E*f+a*b*D*E+a*b*C*D*F+a*B*E*F+A*B*c*E<->G |
| expert | 2 | 1.000 | 1.000 | 1.000 | b*c*D*e+b*C*D*E*f+B*C*d*E*f+a*b*D*F+a*b*c*D+a*B*E*F+A*B*c*E<->G |
| opt | 2 | 0.000 | 0.833 | 1.000 | C*D*E*F+b*c*D*e*F+B*c*E*F+a*b*D*F+a*B*C*d*E+A*B*c*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.833 | 1.000 | C*D*E*F+b*c*D*e*F+B*c*E*F+a*b*D*F+a*B*C*d*E+A*B*c*E<->G |
| opt_expert | 2 | 0.500 | 0.938 | 1.000 | b*C*D*E*f+B*C*d*E*f+B*C*D*E*F+a*b*D*E+a*b*C*D*F+a*B*E*F+a*B*C*E+A*B*c*D*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | D*E+b*D*F+B*E<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*E+b*C*D+B*E*F+A*C*E*f<->G |
| kde | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | D*E+b*C*D+B*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*D+B*E<->G |
| opt | 1 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | C*E+b*D+B*E*F+A*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*D+B*E<->G |
| opt_expert | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*E+b*C*D+B*C*E+a*E*F<->G |

