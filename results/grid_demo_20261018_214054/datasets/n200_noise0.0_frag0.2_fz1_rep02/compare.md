# n200_noise0.0_frag0.2_fz1_rep02

- data: n=200, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=16002
- true model: `C*d+E*F+E*D<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.503 | True | 0.926 | 0.593 | 11 | 0.000 | 1.000 | 0.000 | 0.552 |
| quantile | 0.517 | True | 0.929 | 0.550 | 11 | 0.051 | 0.942 | 0.063 | 0.523 |
| kde | 0.494 | False | 0.920 | 0.578 | 9 | 0.060 | 0.947 | 0.053 | 0.554 |
| expert | 0.435 | True | 0.907 | 0.551 | 8 | 0.089 | 0.923 | 0.077 | 0.578 |
| opt | 0.839 | True | 0.946 | 0.518 | 13 | 0.156 | 0.887 | 0.123 | 0.759 |
| opt_c6c7 | 0.666 | True | 0.940 | 0.545 | 10 | 0.069 | 0.892 | 0.126 | 0.534 |
| opt_expert | 0.716 | True | 0.921 | 0.583 | 11 | 0.057 | 0.891 | 0.113 | 0.514 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.407 | 0 |
| quantile | 1.000 | 0.324 | 0 |
| kde | 1.000 | 0.321 | 0 |
| expert | 1.000 | 0.250 | 0 |
| opt | 1.000 | 0.382 | 0 |
| opt_c6c7 | 1.000 | 0.303 | 0 |
| opt_expert | 1.000 | 0.333 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*c*D*E*F+B*C*E*F+a*c*D*E*F+a*b*c*E*F+a*b*C*d*E*f+A*C*d*E*F+A*b*C*D*E*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.667 | b*D*E*F+B*C*E*F+a*b*c*E*F+a*b*C*D*E+A*C*E*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*c*D*E*F+a*c*D*E*F+a*b*c*E*F+a*b*C*d*e*f+a*b*C*D*E*f+a*B*C*d*E*F+A*B*C*d*e*f+A*B*C*D*E*F<->G |
| expert | 1 | 0.000 | 0.750 | 1.000 | B*C*D*E*F+a*b*d*E*F+a*b*C*E*f+A*C*d*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | C*E*F+b*D*E*F+a*b*E*F+a*b*C*d*E+A*b*C*D*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*D*E+B*C*d*E*F+a*C*E*F+a*b*E*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | C*E*F+a*b*d*E*F+a*b*C*d*E+A*b*C*D*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 26 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E*F+b*E*F+b*C*E+a*E*F<->G |
| quantile | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | E*F+b*D*E<->G |
| kde | 2 | 0.000 | 0.333 | 0.333 | 0.000 | 1.000 | C+b*E*F+a*D*E*F<->G |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*C*D*E+a*b*d*E+A*C*E*F<->G |
| opt | 4 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | E*F+D*f+a*b*E<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.333 | 0.000 | 1.000 | E*F+b*C*D*E<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*E*F+b*D*E+a*E*F+a*C*d*E<->G |

