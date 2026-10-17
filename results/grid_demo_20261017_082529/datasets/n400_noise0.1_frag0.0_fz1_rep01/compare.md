# n400_noise0.1_frag0.0_fz1_rep01

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=30001
- true model: `f*E+c*D*E<->G`  (irrelevant: A, B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.455 | False | 0.840 | 0.488 | 6 | 0.000 | 1.000 | 0.000 | 0.555 |
| quantile | 0.491 | True | 0.856 | 0.556 | 10 | 0.033 | 0.995 | 0.014 | 0.546 |
| kde | 0.538 | True | 0.860 | 0.572 | 10 | 0.035 | 0.973 | 0.027 | 0.557 |
| expert | 0.441 | False | 0.848 | 0.465 | 4 | 0.047 | 0.982 | 0.018 | 0.567 |
| opt | 0.919 | True | 0.838 | 0.534 | 13 | 0.128 | 0.900 | 0.101 | 0.698 |
| opt_c6c7 | 0.641 | True | 0.835 | 0.561 | 9 | 0.069 | 0.878 | 0.128 | 0.537 |
| opt_expert | 0.689 | True | 0.842 | 0.558 | 9 | 0.068 | 0.891 | 0.113 | 0.539 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.300 | 0 |
| quantile | 1.000 | 0.500 | 0 |
| kde | 1.000 | 0.556 | 0 |
| expert | 1.000 | 0.200 | 0 |
| opt | 1.000 | 0.650 | 0 |
| opt_c6c7 | 1.000 | 0.474 | 0 |
| opt_expert | 1.000 | 0.450 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*c*E*f+a*B*c*D*E+A*B*D*E*f<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | c*D*E*f+a*B*d*E*f+a*B*c*D*E+A*c*E*f+A*B*D*E*f<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | B*c*D*E*F+a*c*D*E*f+a*B*d*E*f+A*c*d*E*f+A*b*d*E*f+A*B*C*D*E*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | B*c*d*E*f+a*B*c*D*E*F+A*B*C*D*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | c*E*f+b*D*E*f+B*c*D*E+A*D*E*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | C*D*E*f+a*D*E*f+a*B*c*D*E+a*B*C*E*f+A*B*c*d*E*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | C*D*E*f+a*D*E*f+a*B*c*D*E+a*B*C*E*f+A*B*c*d*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*E*f+a*c*D*F+A*B*E*f<->G |
| quantile | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*E*f+B*d*E*f+a*c*D*E+A*D*E*f<->G |
| kde | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | d*E*f+c*D*E+A*E*f<->G |
| expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*c*E*f+a*c*D*F+A*C*D*E*f<->G |
| opt | 1 | 0.000 | 0.500 | 0.500 | 0.000 | 1.000 | E*f+B*c*D*E<->G |
| opt_c6c7 | 2 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | D*E*f+c*E+B*d*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | E*f+c*E<->G |

