# n100_noise0.0_frag0.2_fz0_rep00

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=3000
- true model: `f*d*A+C*a<->G`  (irrelevant: B, E)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.653 | True | 0.945 | 0.791 | 13 | 0.000 | 1.000 | 0.000 | 0.801 |
| quantile | 0.400 | False | 0.831 | 0.494 | 7 | 0.115 | 0.938 | 0.057 | 0.583 |
| kde | 0.623 | True | 0.882 | 0.772 | 13 | 0.051 | 1.000 | 0.000 | 0.700 |
| expert | 0.644 | True | 0.916 | 0.757 | 13 | 0.043 | 1.000 | 0.000 | 0.800 |
| opt | 0.728 | True | 0.959 | 0.606 | 11 | 0.120 | 0.930 | 0.055 | 0.821 |
| opt_c6c7 | 0.672 | True | 0.905 | 0.597 | 11 | 0.097 | 0.933 | 0.048 | 0.633 |
| opt_expert | 0.670 | True | 0.857 | 0.691 | 11 | 0.067 | 0.958 | 0.038 | 0.700 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.722 | 0 |
| quantile | 1.000 | 0.368 | 0 |
| kde | 1.000 | 0.722 | 0 |
| expert | 1.000 | 0.722 | 0 |
| opt | 1.000 | 0.733 | 0 |
| opt_c6c7 | 1.000 | 0.688 | 0 |
| opt_expert | 1.000 | 0.611 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.700 | 1.000 | b*C*d*E*f+B*C*d*e*f+a*C*e*f+a*C*D*E+A*B*c*d*f<->G |
| quantile | 1 | 0.000 | 0.500 | 0.500 | b*C*d*E*f+B*C*d*e*f+a*C*D*E*F+a*b*C*D*F<->G |
| kde | 2 | 0.000 | 0.700 | 1.000 | b*C*d*E*f+B*C*d*e*f+a*C*e*f+a*C*D*E+A*B*c*d*f<->G |
| expert | 2 | 0.000 | 0.700 | 1.000 | b*C*d*E*f+B*C*d*e*f+a*C*e*f+a*C*D*E+A*B*c*d*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | a*C*D*E*f+a*B*C*f+a*B*C*D*E+A*C*d*E*f+A*B*d*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | a*C*D*E*f+a*B*C*f+a*B*C*D*E+A*C*d*E*f+A*B*d*f<->G |
| opt_expert | 2 | 0.500 | 0.875 | 1.000 | a*C*E*f+a*C*D*E+a*B*C*d*f+A*d*E*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | a*C+A*d*f<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | C*d*f+a*C*F<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | a*C+A*d*f<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | a*C+A*d*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | d*f+a*C<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | d*f+a*C<->G |
| opt_expert | 12 | 0.000 | 0.167 | 0.250 | 0.000 | 1.000 | d*E*f+B*d*f+a*C*E<->G |

