# n100_noise0.2_frag0.2_fz1_rep02

- data: n=100, noise=0.2, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=12002
- true model: `D*a*B+f*D<->G`  (irrelevant: C, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.755 | False | 0.000 | 0.000 | 0 | 0.000 | 1.000 | 0.000 | 0.542 |
| quantile | 0.650 | False | 0.000 | 0.000 | 0 | 0.045 | 0.950 | 0.063 | 0.546 |
| kde | 0.570 | False | 0.000 | 0.000 | 0 | 0.058 | 0.945 | 0.063 | 0.556 |
| expert | 0.800 | False | 0.000 | 0.000 | 0 | 0.108 | 0.860 | 0.140 | 0.558 |
| opt | 0.679 | True | 0.930 | 0.536 | 18 | 0.158 | 0.950 | 0.050 | 0.830 |
| opt_c6c7 | 0.292 | False | 0.924 | 0.286 | 2 | 0.074 | 0.887 | 0.120 | 0.586 |
| opt_expert | 0.364 | False | 0.916 | 0.293 | 2 | 0.082 | 0.847 | 0.168 | 0.577 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle |  | 0.000 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert |  | 0.000 | 0 |
| opt | 0.611 | 0.611 | 7 |
| opt_c6c7 | 0.500 | 0.067 | 1 |
| opt_expert | 0.500 | 0.067 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 0 |  |  |  | (none) |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 0 |  |  |  | (none) |
| opt | 2 | 0.000 | 0.364 | 1.000 | C*D*e*f+a*c*D*e*F+a*B*D*e+a*B*C*E*F+a*B*C*D+A*b*c*E*f+A*b*c*d*e*F+A*b*c*D*f+A*b*C*e*f+A*b*C*D*E*F+A*B*c*D*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.500 | a*b*c*D*e*f+A*b*C*d*e*f<->G |
| opt_expert | 1 | 0.000 | 0.500 | 0.500 | a*b*c*D*e*f+A*b*C*d*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 0 |  |  |  |  |  | (none) |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 0 |  |  |  |  |  | (none) |
| opt | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*D*e*f+b*c*e*F+a*B*D*e+a*B*C*E+A*C*e*f+A*b*c*f+A*b*C*E*F+A*B*c*E*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*b*c*D*e*f+A*C*d*e*f<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*D*e+A*b*C*d*e*f<->G |

