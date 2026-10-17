# n200_noise0.0_frag0.0_fz0_rep00

- data: n=200, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=13000
- true model: `D*A+b*D*E<->G`  (irrelevant: C, F)
- OUT rule (same for every mode): n >= 3, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.701 | True | 0.912 | 0.839 | 14 | 0.000 | 1.000 | 0.000 | 0.794 |
| quantile | 0.125 | False | 0.806 | 0.201 | 1 | 0.120 | 0.953 | 0.042 | 0.573 |
| kde | 0.487 | True | 0.864 | 0.657 | 10 | 0.060 | 1.000 | 0.000 | 0.677 |
| expert | 0.691 | True | 0.887 | 0.719 | 14 | 0.060 | 1.000 | 0.000 | 0.775 |
| opt | 0.867 | True | 0.934 | 0.556 | 9 | 0.144 | 0.874 | 0.123 | 0.785 |
| opt_c6c7 | 0.819 | True | 0.912 | 0.517 | 9 | 0.128 | 0.874 | 0.124 | 0.601 |
| opt_expert | 0.754 | True | 0.878 | 0.548 | 9 | 0.101 | 0.938 | 0.072 | 0.645 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.875 | 0 |
| quantile | 1.000 | 0.053 | 0 |
| kde | 1.000 | 0.625 | 0 |
| expert | 1.000 | 0.875 | 0 |
| opt | 1.000 | 0.529 | 0 |
| opt_c6c7 | 1.000 | 0.562 | 0 |
| opt_expert | 1.000 | 0.562 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | b*D*E*F+a*b*C*D*E+A*c*D*F+A*c*D*e+A*b*D*F+A*b*c*D+A*B*C*D*f<->G |
| quantile | 1 | 1.000 | 1.000 | 0.500 | A*B*c*D*e*F<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | A*c*D*F+A*b*D*F+A*b*c*D*E+A*B*D*e*f+A*B*C*D*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | b*D*E*F+a*b*C*D*E+A*c*D*F+A*c*D*e+A*b*D*F+A*b*c*D+A*B*C*D*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*c*D*E*f+A*c*D*f+A*c*D*E+A*B*D*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | A*D*E*f+A*c*D*f+A*b*D*f+A*b*D*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | A*D*e*f+A*c*D*e+A*b*D*f+A*b*c*D<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*D*E+A*D<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*D*e*F<->G |
| kde | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | A*D*F+A*D*E+A*B*D<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*D*E+A*D<->G |
| opt | 2 | 0.500 | 0.750 | 0.750 | 0.500 | 0.500 | b*D*E+A*D<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | A*D<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | A*D<->G |

