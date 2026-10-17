# n100_noise0.1_frag0.0_fz1_rep00

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=6000
- true model: `f*B+f*d<->G`  (irrelevant: A, C, E)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.613 | True | 0.880 | 0.662 | 16 | 0.000 | 1.000 | 0.000 | 0.544 |
| quantile | 0.645 | True | 0.862 | 0.658 | 15 | 0.065 | 0.945 | 0.058 | 0.540 |
| kde | 0.514 | False | 0.800 | 0.603 | 11 | 0.080 | 0.913 | 0.087 | 0.551 |
| expert | 0.581 | False | 0.845 | 0.567 | 14 | 0.110 | 0.860 | 0.140 | 0.558 |
| opt | 0.852 | True | 0.921 | 0.511 | 15 | 0.134 | 0.910 | 0.082 | 0.715 |
| opt_c6c7 | 0.729 | True | 0.904 | 0.579 | 14 | 0.074 | 0.865 | 0.147 | 0.531 |
| opt_expert | 0.755 | True | 0.900 | 0.595 | 14 | 0.053 | 0.905 | 0.093 | 0.533 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.938 | 0.833 | 1 |
| quantile | 0.933 | 0.778 | 1 |
| kde | 1.000 | 0.550 | 0 |
| expert | 0.786 | 1.000 | 3 |
| opt | 0.933 | 0.875 | 1 |
| opt_c6c7 | 0.929 | 1.000 | 1 |
| opt_expert | 0.929 | 0.929 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.875 | 1.000 | C*d*E*f+b*c*d*e*f+a*d*e*f+a*C*e*f+a*b*d*f+a*B*C*f+A*B*d*E*f+A*B*D*e*f<->G |
| quantile | 1 | 0.000 | 0.833 | 1.000 | c*d*E*f+b*c*d*f+B*C*D*f+a*d*E*f+a*c*E*f+a*B*C*f<->G |
| kde | 2 | 1.000 | 1.000 | 1.000 | b*c*d*e*f+B*C*D*E*f+a*b*d*E*f+a*B*d*e*f+a*B*D*E*f+a*B*C*f<->G |
| expert | 1 | 0.000 | 0.625 | 1.000 | B*c*E*f+B*c*d*f+a*c*d*f+a*b*c*d*E+a*B*E*f+a*B*C*d*E+A*b*C*D*E*f+A*B*C*D*e*f<->G |
| opt | 1 | 0.000 | 0.857 | 1.000 | c*d*E*f+b*d*E*f+b*c*d*f+a*b*C*D*e*f+a*B*E*f+a*B*C*d*f+A*B*D*e*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.857 | 1.000 | b*c*d*f+B*c*D*E*f+B*C*d*e*f+a*C*D*E*f+a*B*E*f+A*b*d*E*f+A*B*C*e*f<->G |
| opt_expert | 1 | 0.000 | 0.833 | 1.000 | b*d*E*f+b*c*d*f+a*d*E*f+a*C*E*f+a*C*d*f+A*B*C*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | C*d*E*f+b*d*e*f+B*E*f+B*D*f+a*f<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*f+B*E*f+B*C*D*f+a*E*f+a*d*f<->G |
| kde | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*c*d*e+B*C*D*E+a*d*E*f+a*B*f<->G |
| expert | 1 | 0.000 | 0.333 | 1.000 | 0.000 | 1.000 | f+b*c*d*E+a*B*C*d*E<->G |
| opt | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*e*f+c*d*f+b*d*f+a*f<->G |
| opt_c6c7 | 2 | 0.000 | 0.667 | 1.000 | 0.000 | 1.000 | d*f+C*f+B*f<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*f+B*D*f+a*f<->G |

