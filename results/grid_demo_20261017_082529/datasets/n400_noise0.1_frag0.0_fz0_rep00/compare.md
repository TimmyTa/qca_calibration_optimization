# n400_noise0.1_frag0.0_fz0_rep00

- data: n=400, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=29000
- true model: `a*f*d+c*f*B<->G`  (irrelevant: E)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.656 | True | 0.840 | 0.602 | 8 | 0.000 | 1.000 | 0.000 | 0.799 |
| quantile | 0.955 | False | 0.000 | 0.000 | 0 | 0.106 | 0.981 | 0.017 | 0.606 |
| kde | 0.520 | False | 0.000 | 0.000 | 0 | 0.062 | 1.000 | 0.000 | 0.680 |
| expert | 0.649 | True | 0.840 | 0.586 | 9 | 0.036 | 1.000 | 0.000 | 0.804 |
| opt | 0.786 | True | 0.844 | 0.520 | 10 | 0.090 | 0.938 | 0.054 | 0.769 |
| opt_c6c7 | 0.660 | True | 0.816 | 0.507 | 7 | 0.118 | 0.946 | 0.060 | 0.634 |
| opt_expert | 0.659 | True | 0.821 | 0.507 | 7 | 0.088 | 0.963 | 0.019 | 0.661 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.571 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.643 | 0 |
| opt | 1.000 | 0.769 | 0 |
| opt_c6c7 | 1.000 | 0.500 | 0 |
| opt_expert | 1.000 | 0.500 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+a*b*d*e*f+a*b*c*d*f+a*B*C*d*E*f+A*B*c*d*f<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 3 | 1.000 | 1.000 | 1.000 | B*c*d*e*f+B*c*D*E*f+a*b*d*e*f+a*b*c*d*f+a*B*C*d*E*f+A*B*c*d*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | B*c*e*f+B*c*D*f+a*d*e*f+a*b*c*d*f<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+a*C*d*e*f+a*b*c*d*f+A*B*c*d*e*f<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | B*c*D*E*f+a*b*d*e*f+a*b*c*d*f+A*B*c*d*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*E*f+a*b*d*e*f+a*B*E*f+A*B*c*f<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 2 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | c*d*f+B*c*f+a*d*e*f+a*B*E*f<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | B*c*f+a*d*f<->G |
| opt_c6c7 | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | a*c*E+a*b*d*e*f+a*B*C*d*f+A*B*c*f<->G |
| opt_expert | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*d*f+B*c*f+a*d*e*f<->G |

