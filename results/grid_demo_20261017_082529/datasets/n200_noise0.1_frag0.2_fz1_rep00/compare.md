# n200_noise0.1_frag0.2_fz1_rep00

- data: n=200, noise=0.1, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=20000
- true model: `B*d+C*f*D<->G`  (irrelevant: A, E)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.618 | True | 0.841 | 0.711 | 14 | 0.000 | 1.000 | 0.000 | 0.550 |
| quantile | 0.520 | True | 0.842 | 0.683 | 14 | 0.038 | 0.962 | 0.042 | 0.521 |
| kde | 0.551 | False | 0.835 | 0.643 | 11 | 0.074 | 0.903 | 0.100 | 0.550 |
| expert | 0.556 | True | 0.822 | 0.684 | 11 | 0.085 | 0.892 | 0.108 | 0.556 |
| opt | 0.754 | True | 0.884 | 0.656 | 16 | 0.108 | 0.964 | 0.037 | 0.695 |
| opt_c6c7 | 0.595 | True | 0.823 | 0.611 | 9 | 0.076 | 0.846 | 0.144 | 0.530 |
| opt_expert | 0.598 | True | 0.825 | 0.617 | 9 | 0.077 | 0.858 | 0.140 | 0.526 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.700 | 0 |
| quantile | 1.000 | 0.667 | 0 |
| kde | 0.909 | 0.556 | 1 |
| expert | 1.000 | 0.478 | 0 |
| opt | 0.938 | 0.750 | 1 |
| opt_c6c7 | 0.778 | 0.389 | 2 |
| opt_expert | 0.778 | 0.350 | 2 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 1.000 | 1.000 | 1.000 | b*C*D*E*f+B*d*E*F+B*C*d*F+a*B*c*d*e+A*C*D*e*f+A*B*d*E<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | B*d*E*F+a*C*D*E*f+a*B*c*d+A*b*C*D*f+A*B*d*E+A*B*C*d*F<->G |
| kde | 1 | 0.000 | 0.750 | 1.000 | A*c*d*E*f+A*C*D*f+A*B*d*F+A*B*d*E<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*E*f+B*C*d*E*F+a*B*C*d*e*f+A*C*D*E*f+A*B*d*E+A*B*C*d*F+A*B*C*D*f<->G |
| opt | 1 | 0.000 | 0.750 | 1.000 | B*d*E*F+a*B*c*d*e+a*B*C*D*E*f+A*b*c*D*E*F+A*b*C*D*f+A*B*d*F+A*B*d*E+A*B*C*e*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.750 | 1.000 | A*d*E*f+A*b*C*D*f+A*B*d*E+A*B*C*d*F<->G |
| opt_expert | 1 | 0.000 | 0.750 | 1.000 | A*d*E*f+A*b*C*D*f+A*B*d*E+A*B*C*d*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 9 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | b*C*D*f+B*d+A*B*C*e<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | C*D*f+B*d<->G |
| kde | 1 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | c*d*E+C*D*f+B*d<->G |
| expert | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | B*d+A*D*E*f+A*B*C*e<->G |
| opt | 3 | 0.000 | 0.200 | 0.500 | 0.000 | 1.000 | d*E+c*E*F+C*D*f+B*c*d+A*B*d<->G |
| opt_c6c7 | 4 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | B*d+A*d*E*f+A*b*D*f<->G |
| opt_expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | C*D*e+B*d+A*b*E*f<->G |

