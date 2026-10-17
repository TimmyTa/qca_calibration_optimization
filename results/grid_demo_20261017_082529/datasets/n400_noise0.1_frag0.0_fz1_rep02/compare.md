# n400_noise0.1_frag0.0_fz1_rep02

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=30002
- true model: `d*b*a+c*f+A*C*F<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.532 | True | 0.847 | 0.612 | 12 | 0.000 | 1.000 | 0.000 | 0.554 |
| quantile | 0.489 | True | 0.839 | 0.595 | 10 | 0.031 | 0.986 | 0.022 | 0.539 |
| kde | 0.503 | True | 0.832 | 0.635 | 13 | 0.031 | 0.970 | 0.030 | 0.552 |
| expert | 0.599 | False | 0.830 | 0.681 | 15 | 0.104 | 0.880 | 0.120 | 0.560 |
| opt | 0.811 | True | 0.852 | 0.550 | 18 | 0.123 | 0.938 | 0.068 | 0.738 |
| opt_c6c7 | 0.645 | True | 0.825 | 0.611 | 9 | 0.070 | 0.874 | 0.127 | 0.540 |
| opt_expert | 0.596 | True | 0.828 | 0.635 | 11 | 0.046 | 0.935 | 0.067 | 0.545 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.400 | 0 |
| quantile | 1.000 | 0.333 | 0 |
| kde | 1.000 | 0.433 | 0 |
| expert | 1.000 | 0.517 | 0 |
| opt | 1.000 | 0.621 | 0 |
| opt_c6c7 | 1.000 | 0.310 | 0 |
| opt_expert | 1.000 | 0.367 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.500 | 0.929 | 1.000 | b*C*d*E*F+B*c*D*e*f+a*b*c*d*f+a*b*C*d*F+A*b*c*D*f+A*b*C*D*F+A*B*c*e*f<->G |
| quantile | 4 | 0.500 | 0.917 | 1.000 | b*C*d*E*F+a*b*c*e*f+a*b*C*d*F+A*c*D*e*f+A*b*C*D*F+A*B*c*e*f<->G |
| kde | 4 | 0.500 | 0.944 | 1.000 | b*c*d*E*f+b*C*d*E*F+a*b*c*d*f+a*b*C*d*F+a*b*C*d*E+A*c*D*e*f+A*b*C*D*F+A*B*c*e*f+A*B*c*D*f<->G |
| expert | 1 | 0.000 | 0.857 | 1.000 | c*d*E*f+b*C*d*E*F+B*c*E*f+a*c*E*f+a*b*c*d*e+a*B*c*f+A*C*D*E*F<->G |
| opt | 2 | 0.500 | 0.938 | 1.000 | c*d*E*f+b*c*f+a*c*E*f+a*c*d*f+a*b*C*d*F+A*c*D*e*f+A*b*C*E*F+A*b*C*D*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*e*f+a*b*d*e*F+A*c*D*e*f+A*b*C*D*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | b*c*e*f+a*b*c*d*f+a*b*C*d*F+A*c*D*e*f+A*b*c*D*f+A*b*C*D*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*e*f+b*C*d*F+a*c*d*f+A*b*D*f+A*b*C*D<->G |
| quantile | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*F+a*b*e*f+A*c*e*f+A*b*C*F<->G |
| kde | 2 | 0.000 | 0.200 | 0.333 | 0.000 | 1.000 | c*e*f+b*c*f+a*b*d+A*c*D*f+A*b*C*F<->G |
| expert | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | c*f+b*C*d*E*F+a*b*c*e+A*D<->G |
| opt | 3 | 0.000 | 0.444 | 0.444 | 0.000 | 0.000 | c*f+b*C*d*F+A*C*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*e*f+a*b*d*e+A*b*C*F<->G |
| opt_expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*e*f+a*c*d*f+a*b*C*d*F+A*c*D*f+A*b*C*D*F<->G |

