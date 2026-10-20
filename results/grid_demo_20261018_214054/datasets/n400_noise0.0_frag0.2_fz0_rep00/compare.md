# n400_noise0.0_frag0.2_fz0_rep00

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=27000
- true model: `c*E*A+b*E<->G`  (irrelevant: D, F)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.711 | True | 0.927 | 0.799 | 12 | 0.000 | 1.000 | 0.000 | 0.800 |
| quantile | 0.985 | False | 0.000 | 0.000 | 0 | 0.113 | 0.965 | 0.030 | 0.584 |
| kde | 0.935 | False | 0.000 | 0.000 | 0 | 0.059 | 1.000 | 0.000 | 0.682 |
| expert | 0.528 | False | 0.875 | 0.416 | 6 | 0.064 | 0.992 | 0.008 | 0.765 |
| opt | 0.922 | True | 0.933 | 0.593 | 11 | 0.101 | 0.911 | 0.089 | 0.821 |
| opt_c6c7 | 0.840 | True | 0.940 | 0.547 | 10 | 0.120 | 0.918 | 0.083 | 0.624 |
| opt_expert | 0.531 | False | 0.878 | 0.496 | 7 | 0.079 | 0.970 | 0.032 | 0.692 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.800 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.400 | 0 |
| opt | 1.000 | 0.611 | 0 |
| opt_c6c7 | 1.000 | 0.588 | 0 |
| opt_expert | 1.000 | 0.438 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | a*b*d*E*f+a*b*C*E+A*c*D*E+A*b*E*F<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 0.500 | b*C*E*F+a*b*C*d*E+A*b*d*E*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | b*d*E*f+b*C*E*f+A*c*D*E*f+A*b*d*E+A*b*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*C*E*f+a*b*d*E*f+A*c*D*E*f+A*b*d*E*F+A*b*C*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 0.500 | b*c*D*E*f+a*b*E*f+A*b*d*E*F<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E+A*c*E<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*E+b*C*E*F+A*d*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E+A*c*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | b*E+A*c*E<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*E*f+b*d*E<->G |

