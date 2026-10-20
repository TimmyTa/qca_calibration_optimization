# n100_noise0.0_frag0.2_fz0_rep02

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=3002
- true model: `c*D+d*F*b<->G`  (irrelevant: A, E)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.699 | True | 0.946 | 0.829 | 12 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.445 | False | 0.873 | 0.471 | 5 | 0.109 | 0.953 | 0.047 | 0.620 |
| kde | 0.561 | True | 0.908 | 0.730 | 10 | 0.055 | 1.000 | 0.000 | 0.699 |
| expert | 0.674 | True | 0.925 | 0.786 | 12 | 0.038 | 1.000 | 0.000 | 0.779 |
| opt | 0.743 | True | 0.977 | 0.649 | 9 | 0.081 | 0.938 | 0.080 | 0.818 |
| opt_c6c7 | 0.706 | True | 0.925 | 0.578 | 9 | 0.098 | 0.933 | 0.068 | 0.646 |
| opt_expert | 0.659 | True | 0.905 | 0.682 | 11 | 0.081 | 0.975 | 0.025 | 0.696 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.800 | 0 |
| quantile | 1.000 | 0.263 | 0 |
| kde | 1.000 | 0.667 | 0 |
| expert | 1.000 | 0.800 | 0 |
| opt | 1.000 | 0.643 | 0 |
| opt_c6c7 | 1.000 | 0.643 | 0 |
| opt_expert | 1.000 | 0.733 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.833 | 1.000 | b*c*E*F+b*C*d*e*F+B*c*D*e*F+B*c*D*E*f+a*b*d*e*F+A*B*c*D*e<->G |
| quantile | 1 | 1.000 | 1.000 | 1.000 | b*c*D*E*F+a*b*d*e*F+a*B*c*D*E*f<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | b*c*D*E*F+b*C*d*e*F+B*c*D*E*f+a*b*c*d*F+a*B*c*D*e*F+A*B*c*D*f<->G |
| expert | 4 | 0.000 | 0.833 | 1.000 | b*c*E*F+b*C*d*e*F+B*c*D*e*F+B*c*D*E*f+a*b*d*e*F+A*B*c*D*e<->G |
| opt | 2 | 0.500 | 0.917 | 1.000 | b*c*D*E*F+B*c*D*E*f+a*b*d*e*F+a*b*c*E*F+a*B*c*D*e*F+A*B*c*D*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.833 | 1.000 | b*c*D*E*F+b*C*d*e*F+a*b*c*E*F+A*b*d*e*F+A*B*c*D*f+A*B*c*D*e<->G |
| opt_expert | 2 | 0.500 | 0.917 | 1.000 | b*d*e*F+b*c*D*E*F+B*c*D*E*f+a*b*c*E*F+a*B*c*D*e*F+A*B*c*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D+b*d*F<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*e*F+b*c*D+a*c*E*f<->G |
| kde | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | D*E*F+c*D*f+b*C*d*F+a*c*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D+b*d*F<->G |
| opt | 1 | 0.000 | 0.333 | 0.500 | 0.000 | 1.000 | c*D+b*c*F+a*b*d*e*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D+b*d*F<->G |
| opt_expert | 8 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | c*D*E+b*d*F+a*c*F+A*c*D<->G |

