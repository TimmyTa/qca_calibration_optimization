# n400_noise0.2_frag0.0_fz1_rep00

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=34000
- true model: `c*E+F*E<->G`  (irrelevant: A, B, D)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.504 | True | 0.816 | 0.600 | 15 | 0.000 | 1.000 | 0.000 | 0.547 |
| quantile | 0.513 | True | 0.823 | 0.582 | 13 | 0.033 | 0.995 | 0.012 | 0.523 |
| kde | 0.518 | False | 0.795 | 0.606 | 14 | 0.035 | 0.978 | 0.029 | 0.531 |
| expert | 0.560 | False | 0.806 | 0.586 | 10 | 0.081 | 0.898 | 0.102 | 0.538 |
| opt | 0.804 | True | 0.807 | 0.524 | 14 | 0.095 | 0.911 | 0.090 | 0.652 |
| opt_c6c7 | 0.656 | True | 0.822 | 0.568 | 12 | 0.062 | 0.898 | 0.110 | 0.522 |
| opt_expert | 0.661 | True | 0.803 | 0.611 | 14 | 0.054 | 0.900 | 0.104 | 0.522 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.625 | 0 |
| quantile | 1.000 | 0.542 | 0 |
| kde | 1.000 | 0.583 | 0 |
| expert | 1.000 | 0.417 | 0 |
| opt | 1.000 | 0.583 | 0 |
| opt_c6c7 | 1.000 | 0.522 | 0 |
| opt_expert | 1.000 | 0.583 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*D*E*F+B*c*d*E*F+a*C*E*F+a*B*c*E*f+A*D*E*F+A*b*c*E*f<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | B*c*d*E*F+a*C*E*F+a*b*D*E*F+a*B*c*E*f+A*b*c*D*E+A*B*D*E*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | B*d*E*F+a*C*E*F+a*b*c*D*E+a*B*c*E*f+A*c*E*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | c*E*F+a*b*d*E*F+a*b*c*D*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | c*D*E+B*D*E*F+B*c*E*F+a*B*E*F+a*B*c*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | c*D*E*F+b*c*D*E+a*c*E*f+a*b*D*E*F+a*B*d*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | c*d*E*F+b*c*D*E+a*d*E*F+a*c*E*f+a*b*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | E*F+b*c*E+a*c*E<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*E+B*E*F+a*E*F+a*c*E<->G |
| kde | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*E*F+c*E*F+a*E*F+a*c*E<->G |
| expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*E*F+b*C*d*E+a*c*D*E<->G |
| opt | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | E*F+a*c*E+A*D*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | E*F+a*c*E+A*D*E<->G |
| opt_expert | 3 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | E*F+a*c*E+A*D*f<->G |

