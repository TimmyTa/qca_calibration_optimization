# n100_noise0.1_frag0.0_fz0_rep02

- data: n=100, noise=0.1, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=5002
- true model: `A*B*C+c*d*B+b*E<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.700

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.687 | True | 0.938 | 0.816 | 22 | 0.000 | 1.000 | 0.000 | 0.798 |
| quantile | 0.534 | True | 0.902 | 0.558 | 20 | 0.089 | 0.977 | 0.025 | 0.629 |
| kde | 0.514 | True | 0.911 | 0.618 | 14 | 0.044 | 1.000 | 0.000 | 0.711 |
| expert | 0.656 | True | 0.937 | 0.705 | 22 | 0.046 | 0.990 | 0.010 | 0.752 |
| opt | 0.810 | True | 0.943 | 0.703 | 20 | 0.112 | 0.947 | 0.058 | 0.850 |
| opt_c6c7 | 0.770 | True | 0.883 | 0.508 | 16 | 0.133 | 0.868 | 0.138 | 0.633 |
| opt_expert | 0.703 | True | 0.918 | 0.699 | 22 | 0.070 | 0.992 | 0.012 | 0.693 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.955 | 0.750 | 1 |
| quantile | 0.950 | 0.679 | 1 |
| kde | 1.000 | 0.500 | 0 |
| expert | 0.909 | 0.714 | 2 |
| opt | 0.900 | 0.750 | 2 |
| opt_c6c7 | 0.875 | 0.737 | 2 |
| opt_expert | 0.955 | 0.750 | 1 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.750 | 1.000 | d*E*F+c*d*E+b*C*E*f+B*c*d*F+a*B*c*d+A*b*E*f+A*B*C*d*e*f+A*B*C*D*e*F<->G |
| quantile | 1 | 0.000 | 0.667 | 0.667 | d*E*F+c*d*E+b*C*E*f+B*c*d*F+A*b*E*f+A*b*C*E<->G |
| kde | 1 | 0.000 | 0.750 | 0.667 | c*d*E*f+b*C*d*E+a*b*C*E*f+a*B*c*d*f+A*C*d*E*F+A*b*d*E+A*b*c*E*f+A*B*c*d*e*F<->G |
| expert | 2 | 0.000 | 0.643 | 1.000 | d*E*F+b*d*E+b*C*E*f+B*c*d*F+a*B*c*d+A*c*E*f+A*B*C*D*e*F<->G |
| opt | 1 | 0.000 | 0.600 | 1.000 | b*C*E*f+B*c*d*E+a*d*E*f+a*b*C*d*E+a*B*c*d*f+A*c*E*f+A*c*d*E+A*B*d*E*F+A*B*c*d*F+A*B*C*e*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.778 | 1.000 | b*C*E*f+B*d*E*f+a*b*C*d*E+a*B*c*d*f+a*B*c*d*E+A*c*D*E*f+A*b*C*D*E+A*B*c*d*e*F+A*B*C*d*E<->G |
| opt_expert | 1 | 0.000 | 0.778 | 1.000 | d*E*F+c*d*E+b*d*E+B*c*d*F+a*b*C*E*f+a*B*c*d+A*b*c*E*f+A*B*C*e*f+A*B*C*D*e<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 6 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | d*E*F+b*d*E+b*C*E*f+B*c*d+A*b*c*E+A*B*d*e*f+A*B*C*D*F<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | d*E*F+c*d*E+b*C*E*f+B*c*d*F+A*b*E<->G |
| kde | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*d*E*f+b*C*d*E+B*c*d*f+a*b*C*E*f+A*C*d*E*F+A*b*c*E+A*B*c*d*e<->G |
| expert | 3 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | d*E*F+b*d*E+b*C*E*f+B*c*d+A*c*E+A*B*C*D*F<->G |
| opt | 1 | 0.000 | 0.167 | 0.333 | 0.000 | 1.000 | d*E*F+b*C*E+B*c*d+a*d*E+A*c*E*f+A*B*C*e*f<->G |
| opt_c6c7 | 1 | 0.000 | 0.500 | 0.667 | 0.000 | 0.000 | d*E+b*E+B*c*d+A*c*E<->G |
| opt_expert | 12 | 0.000 | 0.143 | 0.333 | 0.000 | 1.000 | d*E*F+b*d*E+b*C*E*f+B*c*d+A*b*c*E+A*B*e*f+A*B*C*D*e<->G |

