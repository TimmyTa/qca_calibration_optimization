# n400_noise0.0_frag0.2_fz1_rep00

- data: n=400, noise=0.0, frag=0.2, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=28000
- true model: `D*c+A*c+f*C<->G`  (irrelevant: B, E)
- OUT rule (same for every mode): n >= 6, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.740 | True | 0.887 | 0.760 | 23 | 0.000 | 1.000 | 0.000 | 0.550 |
| quantile | 0.650 | True | 0.874 | 0.734 | 22 | 0.042 | 0.963 | 0.035 | 0.511 |
| kde | 0.659 | True | 0.845 | 0.717 | 23 | 0.038 | 0.967 | 0.032 | 0.515 |
| expert | 0.755 | False | 0.815 | 0.715 | 19 | 0.098 | 0.875 | 0.125 | 0.553 |
| opt | 0.906 | True | 0.874 | 0.710 | 21 | 0.090 | 0.920 | 0.080 | 0.643 |
| opt_c6c7 | 0.722 | True | 0.836 | 0.668 | 18 | 0.069 | 0.853 | 0.155 | 0.506 |
| opt_expert | 0.542 | True | 0.830 | 0.662 | 18 | 0.071 | 0.862 | 0.141 | 0.504 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.957 | 0.759 | 1 |
| quantile | 0.955 | 0.583 | 1 |
| kde | 0.826 | 0.514 | 4 |
| expert | 0.789 | 0.417 | 4 |
| opt | 1.000 | 0.600 | 0 |
| opt_c6c7 | 0.778 | 0.389 | 4 |
| opt_expert | 0.667 | 0.324 | 6 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.545 | 1.000 | c*D*E+b*c*E*f+a*D*E*f+a*b*E*f+a*b*D*f+a*B*c*D*F+A*c*D*f+A*b*C*d*e*f+A*B*D*e*f+A*B*c*d*e+A*B*C*d*E*f<->G |
| quantile | 4 | 0.000 | 0.773 | 1.000 | b*C*d*E*f+a*C*D*E*f+a*b*D*E*f+a*b*C*D*f+a*B*c*d*E*f+a*B*c*D*F+A*c*D*E*F+A*C*d*f+A*b*c*f+A*B*e*f+A*B*c*d*e<->G |
| kde | 1 | 0.000 | 0.545 | 1.000 | c*D*E*F+b*c*E*f+b*c*D*f+a*c*d*f+a*C*D*E*f+a*b*E*f+a*b*D*f+a*B*c*D*F+A*b*C*d*e*f+A*B*D*e*f+A*B*c*d*e<->G |
| expert | 1 | 0.000 | 0.429 | 0.333 | c*D*e*f+B*D*e*f+a*c*f+a*c*D*E+a*b*d*f+a*B*E*f+a*B*c*D<->G |
| opt | 2 | 0.000 | 0.700 | 1.000 | b*C*d*E*f+B*c*D*f+B*c*D*E+a*D*E*f+A*d*E*f+A*c*D*f+A*c*D*E+A*b*C*d*f+A*B*D*f+A*B*c*f<->G |
| opt_c6c7 | 3 | 0.000 | 0.476 | 0.667 | B*c*D*e+a*c*d*f+a*b*c*E*f+A*c*e*F+A*c*d*e+A*B*e*f+A*B*c*d<->G |
| opt_expert | 2 | 0.000 | 0.500 | 1.000 | d*e*f+B*c*D*e*F+a*b*c*d*E*F+a*b*C*e*f+a*b*C*d*f+a*B*c*d*f+a*B*C*D*E*F+A*b*C*D*e*F+A*B*c*d*e+A*B*C*e*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | c*D+C*f+b*E*f+A*c<->G |
| quantile | 2 | 0.000 | 0.750 | 1.000 | 0.000 | 1.000 | E*f+c*D+C*f+A*c<->G |
| kde | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | f+c*D+A*c<->G |
| expert | 1 | 1.000 | 1.000 | 0.667 | 0.000 | 0.000 | f+c*D<->G |
| opt | 2 | 0.500 | 0.833 | 0.833 | 0.500 | 0.000 | c*D+C*f+A*c<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | f+c*D+A*c<->G |
| opt_expert | 1 | 0.000 | 0.500 | 1.000 | 0.000 | 1.000 | f+D*E+c*D+b*c*E+A*c+A*b*D<->G |

