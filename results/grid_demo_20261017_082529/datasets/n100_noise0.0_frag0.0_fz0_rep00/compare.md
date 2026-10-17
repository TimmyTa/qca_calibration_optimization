# n100_noise0.0_frag0.0_fz0_rep00

- data: n=100, noise=0.0, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=1000
- true model: `C*f+f*E+a*e*B<->G`  (irrelevant: D)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.715 | True | 0.923 | 0.890 | 22 | 0.000 | 1.000 | 0.000 | 0.797 |
| quantile | 0.377 | False | 0.805 | 0.413 | 6 | 0.118 | 0.953 | 0.035 | 0.583 |
| kde | 0.466 | True | 0.838 | 0.610 | 12 | 0.062 | 1.000 | 0.000 | 0.674 |
| expert | 0.672 | True | 0.870 | 0.807 | 20 | 0.052 | 1.000 | 0.000 | 0.773 |
| opt | 0.817 | True | 0.958 | 0.680 | 18 | 0.110 | 0.910 | 0.107 | 0.853 |
| opt_c6c7 | 0.735 | True | 0.917 | 0.597 | 16 | 0.113 | 0.893 | 0.105 | 0.643 |
| opt_expert | 0.663 | True | 0.843 | 0.685 | 16 | 0.075 | 0.988 | 0.012 | 0.666 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 1.000 | 0 |
| quantile | 1.000 | 0.250 | 0 |
| kde | 1.000 | 0.545 | 0 |
| expert | 1.000 | 0.909 | 0 |
| opt | 0.944 | 0.944 | 1 |
| opt_c6c7 | 1.000 | 1.000 | 0 |
| opt_expert | 1.000 | 0.762 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 4 | 0.000 | 0.850 | 1.000 | C*D*e*f+B*c*d*E*f+B*C*D*f+a*c*E*f+a*b*C*d*f+a*B*D*e+a*B*c*f+a*B*C*e*F+A*b*D*E*f+A*B*C*f<->G |
| quantile | 2 | 1.000 | 1.000 | 1.000 | B*C*d*e*f+a*B*D*e*F+a*B*C*d*e+a*B*C*D*E*f<->G |
| kde | 1 | 0.000 | 0.800 | 0.667 | B*C*D*f+a*B*D*e+a*B*c*f+a*B*C*e*F+A*B*C*e*f<->G |
| expert | 4 | 0.000 | 0.850 | 1.000 | C*D*e*f+B*c*d*E*f+B*C*D*f+a*c*D*E*f+a*b*C*d*f+a*B*D*e+a*B*c*f+a*B*C*e*F+A*C*D*f+A*B*C*f<->G |
| opt | 4 | 0.000 | 0.833 | 1.000 | c*d*E*f+b*C*e*f+a*b*c*D*f+a*b*C*d*f+a*B*d*e*F+a*B*c*e*F+a*B*c*d*e+A*b*C*D*f+A*B*C*d*f<->G |
| opt_c6c7 | 4 | 0.500 | 0.955 | 1.000 | c*D*E*f+b*C*D*e*f+a*b*C*d*E*f+a*B*c*d*f+a*B*c*d*e+a*B*C*D*e*F+A*C*D*e*f+A*b*c*E*f+A*b*C*e*f+A*b*C*D*f+A*B*C*d*E*f<->G |
| opt_expert | 4 | 0.000 | 0.812 | 1.000 | B*c*d*E*f+B*C*D*f+a*b*C*d*E*f+a*B*D*e+a*B*c*f+a*B*C*e*F+A*C*D*e*f+A*B*C*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | E*f+C*f+a*B*e<->G |
| quantile | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | B*C*d*e*f+a*B*e*F+a*B*C*E*f<->G |
| kde | 2 | 0.000 | 0.250 | 0.333 | 0.000 | 1.000 | B*C*e*f+B*C*D*f+a*B*f+a*B*e<->G |
| expert | 2 | 0.000 | 0.500 | 0.667 | 0.000 | 1.000 | C*f+B*E*f+a*D*E*f+a*B*e<->G |
| opt | 3 | 0.000 | 0.400 | 0.667 | 0.000 | 1.000 | E*f+C*f+a*D*f+a*B*d*e+a*B*c*e<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | E*f+C*f+a*B*e<->G |
| opt_expert | 1 | 0.000 | 0.250 | 0.333 | 0.000 | 0.000 | C*E*f+B*E*f+a*B*e+A*C*f<->G |

