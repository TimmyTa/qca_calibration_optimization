# n100_noise0.0_frag0.2_fz0_rep02

- data: n=100, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=3002
- true model: `c*D+d*F*b<->G`  (irrelevant: A, E)
- OUT rule (same for every mode): n >= 2, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.712 | True | 0.946 | 0.829 | 12 | 0.000 | 1.000 | 0.000 | 0.802 |
| quantile | 0.536 | False | 0.793 | 0.618 | 13 | 0.109 | 0.953 | 0.047 | 0.620 |
| kde | 0.698 | True | 0.907 | 0.779 | 12 | 0.055 | 1.000 | 0.000 | 0.699 |
| expert | 0.708 | True | 0.925 | 0.786 | 12 | 0.038 | 1.000 | 0.000 | 0.779 |
| opt | 0.774 | True | 0.940 | 0.619 | 11 | 0.085 | 0.955 | 0.078 | 0.761 |
| opt_c6c7 | 0.721 | True | 0.845 | 0.626 | 11 | 0.095 | 0.955 | 0.070 | 0.654 |
| opt_expert | 0.734 | True | 0.881 | 0.705 | 11 | 0.062 | 0.978 | 0.028 | 0.690 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.800 | 0 |
| quantile | 0.846 | 0.579 | 2 |
| kde | 1.000 | 0.800 | 0 |
| expert | 1.000 | 0.800 | 0 |
| opt | 1.000 | 0.733 | 0 |
| opt_c6c7 | 1.000 | 0.733 | 0 |
| opt_expert | 1.000 | 0.688 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.833 | 1.000 | b*c*E*F+b*C*d*e*F+B*c*D*e*F+B*c*D*E*f+a*b*d*e*F+A*B*c*D*e<->G |
| quantile | 1 | 0.000 | 0.714 | 1.000 | b*C*D*e*F+B*c*D*E*f+a*c*D*E*F+a*b*d*e*F+a*b*C*d*F+A*b*c*E*F+A*B*c*D*e<->G |
| kde | 4 | 0.000 | 0.833 | 1.000 | b*c*E*F+b*C*d*e*F+B*c*D*e*F+B*c*D*E*f+a*b*d*e*F+A*B*c*D*e<->G |
| expert | 4 | 0.000 | 0.833 | 1.000 | b*c*E*F+b*C*d*e*F+B*c*D*e*F+B*c*D*E*f+a*b*d*e*F+A*B*c*D*e<->G |
| opt | 4 | 0.500 | 0.929 | 1.000 | b*c*d*e*F+b*c*D*E*F+B*c*D*e*F+B*c*D*E*f+a*b*d*e*F+a*b*c*E*F+A*B*c*D*e<->G |
| opt_c6c7 | 4 | 0.500 | 0.929 | 1.000 | b*c*d*e*F+b*c*D*E*F+B*c*D*e*F+B*c*D*E*f+a*b*d*e*F+a*b*c*E*F+A*B*c*D*e<->G |
| opt_expert | 4 | 0.500 | 0.929 | 1.000 | b*c*d*e*F+b*c*D*E*F+B*c*D*e*F+B*c*D*E*f+a*b*d*e*F+a*b*c*E*F+A*B*c*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D+b*d*F<->G |
| quantile | 2 | 0.000 | 0.250 | 0.500 | 0.000 | 1.000 | c*D*E+b*e*F+b*d*F+A*c*D<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D+b*d*F<->G |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D+b*d*F<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D+b*d*F<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D+b*d*F<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D+b*d*F<->G |

