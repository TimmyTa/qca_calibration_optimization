# n100_noise0.2_frag0.0_fz1_rep00

- data: n=100, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.45, 0.01)`, seed=10000
- true model: `D*A+b*C+c*E*B<->G`  (irrelevant: F)
- OUT rule (same for every mode): n >= 1, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.559 | False | 0.797 | 0.790 | 30 | 0.000 | 1.000 | 0.000 | 0.580 |
| quantile | 0.548 | False | 0.788 | 0.775 | 31 | 0.066 | 0.933 | 0.065 | 0.547 |
| kde | 0.572 | False | 0.783 | 0.765 | 27 | 0.054 | 0.945 | 0.058 | 0.556 |
| expert | 0.557 | False | 0.750 | 0.755 | 32 | 0.072 | 0.920 | 0.080 | 0.575 |
| opt | 0.778 | True | 0.883 | 0.563 | 15 | 0.168 | 0.892 | 0.103 | 0.817 |
| opt_c6c7 | 0.607 | True | 0.807 | 0.724 | 21 | 0.078 | 0.840 | 0.155 | 0.548 |
| opt_expert | 0.611 | True | 0.803 | 0.747 | 23 | 0.071 | 0.868 | 0.117 | 0.540 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 0.800 | 0.828 | 6 |
| quantile | 0.774 | 0.828 | 7 |
| kde | 0.815 | 0.786 | 5 |
| expert | 0.719 | 0.920 | 9 |
| opt | 0.933 | 0.609 | 1 |
| opt_c6c7 | 0.905 | 0.792 | 2 |
| opt_expert | 0.870 | 0.741 | 3 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 2 | 0.000 | 0.583 | 1.000 | b*C*d*E*f+b*C*D*F+b*C*D*e+B*c*d*E+a*C*d*e*F+a*b*d*e*F+A*D*f+A*c*e*f+A*C*E*f+A*C*D*E+A*b*C*F+A*B*c*e<->G |
| quantile | 6 | 0.000 | 0.583 | 1.000 | b*C*E*f+b*C*D+B*c*d*F+B*c*d*E+a*C*D*e*F+a*b*d*e*F+A*c*e*f+A*c*d*f+A*C*D*E*f+A*b*D+A*b*C*F+A*B*c*E*F<->G |
| kde | 2 | 0.000 | 0.750 | 1.000 | b*C*d*E*f+b*C*D*F+b*C*D*e+B*c*d*F+a*b*d*e*F+a*B*c*d*E+A*c*e*f+A*C*D*E+A*b*D*f+A*b*D*e+A*b*C*F+A*B*c*E*F<->G |
| expert | 10 | 0.000 | 0.400 | 1.000 | c*d*E*f+b*D*e*f+a*c*D*E*F+a*b*C*e+a*b*C*d*f+a*B*c*d*F+A*c*f+A*C*D*e+A*b*e*F+A*b*C*D+A*B*d*E*f+A*B*c*E<->G |
| opt | 3 | 0.000 | 0.810 | 0.667 | b*C*d*e*F+A*D*E*f+A*c*E*f+A*b*E*f+A*b*D*f+A*b*D*E+A*b*C*F<->G |
| opt_c6c7 | 1 | 0.000 | 0.750 | 1.000 | a*b*C*D*e+a*B*c*d*F+A*D*f+A*D*E+A*b*c*e*f+A*b*c*D+A*b*C*d*e*F+A*B*c*E<->G |
| opt_expert | 1 | 0.000 | 0.625 | 1.000 | b*C*D*e*f+a*B*c*d*F+A*D*E+A*c*D*F+A*C*E*f+A*b*c*e*f+A*b*C*F+A*B*c*E<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*d*E*f+b*C*D*F+b*C*D*e+B*c*d*E+a*d*e*F+A*E*f+A*D*f+A*D*E+A*c+A*b<->G |
| quantile | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*F+b*C*f+b*C*e+B*c*d*E+a*C*D*F+A*f+A*c+A*b<->G |
| kde | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*F+b*e*F+b*C*d*E*f+b*C*D*F+b*C*D*e+B*c*E*f+A*D*E+A*c+A*b*F<->G |
| expert | 2 | 0.000 | 0.100 | 0.333 | 0.000 | 1.000 | c*E*F+c*d*E+b*D*e*f+b*C*f+b*C*e+a*c*d*F+A*E+A*D+A*c*f+A*b<->G |
| opt | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | b*C*e*F+A*D*f+A*c*E*f+A*b*E<->G |
| opt_c6c7 | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*F+b*C*D+A*E*f+A*D*f+A*D*E+A*b<->G |
| opt_expert | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*d*F+b*C*e+A*E*f+A*D*E+A*c*F+A*b<->G |

