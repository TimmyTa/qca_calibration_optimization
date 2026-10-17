# n100_noise0.0_frag0.0_fz0_rep01

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=1001
- true model: `c*d+D*F<->G`  (irrelevant: A, B, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.772 | True | 0.958 | 0.899 | 27 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.632 | False | 0.799 | 0.643 | 24 | 0.102 | 0.960 | 0.048 | 0.617 |
| kde | 0.760 | True | 0.916 | 0.850 | 27 | 0.046 | 1.000 | 0.000 | 0.712 |
| expert | 0.676 | True | 0.872 | 0.676 | 26 | 0.062 | 0.958 | 0.042 | 0.732 |
| opt | 0.883 | True | 0.943 | 0.720 | 20 | 0.083 | 0.957 | 0.058 | 0.800 |
| opt_c6c7 | 0.801 | True | 0.880 | 0.659 | 18 | 0.106 | 0.903 | 0.082 | 0.656 |
| opt_expert | 0.815 | True | 0.883 | 0.710 | 22 | 0.094 | 0.910 | 0.078 | 0.665 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 1.000 | 0 |
| quantile | 0.917 | 0.880 | 2 |
| kde | 1.000 | 1.000 | 0 |
| expert | 0.846 | 0.815 | 4 |
| opt | 1.000 | 1.000 | 0 |
| opt_c6c7 | 1.000 | 1.000 | 0 |
| opt_expert | 1.000 | 1.000 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.778 | 1.000 | c*E*F+c*d*F+c*d*E+b*D*E*F+B*D*e*F+B*c*d+a*c*F+a*c*d+A*C*D*e*F<->G |
| quantile | 1 | 0.000 | 0.625 | 1.000 | b*c*d+b*C*D*E*F+a*c*D*e*F+a*B*c*E+A*c*E*F+A*c*d*f+A*b*C*D*F+A*B*c*D*e<->G |
| kde | 4 | 0.000 | 0.778 | 1.000 | c*E*F+c*d*F+c*d*E+b*D*E*F+B*D*e*F+B*c*d+a*c*F+a*c*d+A*C*D*e*F<->G |
| expert | 1 | 0.000 | 0.556 | 1.000 | c*D*F+b*c*F+B*c*d*E+a*b*D*E*F+a*b*c*e+a*b*c*D+A*c*d*E+A*b*D*e*F+A*B*c<->G |
| opt | 1 | 0.000 | 0.875 | 1.000 | C*D*e*F+b*D*F+b*c*F+b*c*d*E+a*c*d*E*f+a*b*c*d+A*c*D*E*F+A*B*c*d*e*f<->G |
| opt_c6c7 | 4 | 0.000 | 0.778 | 1.000 | b*c*d*F+B*c*d*E*f+B*C*D*e*F+a*b*c*e*F+a*B*D*E*F+A*c*E*F+A*b*C*D*F+A*B*c*d*f+A*B*c*D*F<->G |
| opt_expert | 4 | 0.000 | 0.778 | 1.000 | c*D*E*F+b*D*E*F+b*c*d*e+B*c*d*E*f+B*C*D*e*F+a*b*c*F+A*c*d*E+A*C*D*e*F+A*B*c*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*d<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*E+c*D*F+b*D*F+b*c*d+a*B*c*E+A*B*c*e*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*d<->G |
| expert | 1 | 0.000 | 0.167 | 0.500 | 0.000 | 1.000 | c*F+c*d+b*D*e*F+a*b*F+a*b*c+A*B*c<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*d<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*d<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | D*F+c*d<->G |

