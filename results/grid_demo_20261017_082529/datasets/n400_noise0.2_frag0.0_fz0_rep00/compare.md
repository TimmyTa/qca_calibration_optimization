# n400_noise0.2_frag0.0_fz0_rep00

- data: n=400, noise=0.2, frag=0.0, fuzzvalues=`seq(0, 0.2, 0.01)`, seed=33000
- true model: `D*f*c+A*C*E<->G`  (irrelevant: B)
- OUT rule (same for every mode): n >= 5, incl >= 0.800, PRI >= 0.500

## Calibration

| mode | S | feasible | cons | cov | n_positive_rows | membership_mae | same_side_0.5 | crossover_err_pct | crisp |
|---|---|---|---|---|---|---|---|---|---|
| oracle | 0.575 | True | 0.820 | 0.539 | 12 | 0.000 | 1.000 | 0.000 | 0.795 |
| quantile | 0.745 | False | 0.000 | 0.000 | 0 | 0.108 | 0.985 | 0.022 | 0.590 |
| kde | 0.505 | False | 0.000 | 0.000 | 0 | 0.055 | 1.000 | 0.000 | 0.686 |
| expert | 0.608 | False | 0.837 | 0.451 | 12 | 0.046 | 1.000 | 0.000 | 0.771 |
| opt | 0.535 | False | 0.805 | 0.499 | 13 | 0.060 | 0.984 | 0.024 | 0.840 |
| opt_c6c7 | 0.555 | False | 0.809 | 0.436 | 12 | 0.085 | 0.973 | 0.041 | 0.659 |
| opt_expert | 0.507 | False | 0.807 | 0.434 | 12 | 0.073 | 0.990 | 0.021 | 0.679 |

## Truth-table rows vs truth

| mode | row_precision | row_recall | false_positive_rows |
|---|---|---|---|
| oracle | 1.000 | 0.750 | 0 |
| quantile |  | 0.000 | 0 |
| kde |  | 0.000 | 0 |
| expert | 1.000 | 0.750 | 0 |
| opt | 1.000 | 0.812 | 0 |
| opt_c6c7 | 1.000 | 0.750 | 0 |
| opt_expert | 1.000 | 0.750 | 0 |

## Conservative solution vs truth

| mode | n_cs | cs_correct | cs_term_precision | cs_paths_found_sup | cs_solution |
|---|---|---|---|---|---|
| oracle | 1 | 0.000 | 0.833 | 1.000 | b*c*D*f+a*c*D*f+A*D*E*f+A*b*C*d*E*F+A*B*C*E*f+A*B*C*D*E<->G |
| quantile | 0 |  |  |  | (none) |
| kde | 0 |  |  |  | (none) |
| expert | 1 | 0.000 | 0.833 | 1.000 | b*c*D*f+a*c*D*f+A*D*E*f+A*b*C*d*E*F+A*B*C*E*f+A*B*C*D*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | c*D*E*f+b*c*D*f+a*c*D*f+A*C*d*E*f+A*C*D*E*F+A*b*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | b*c*D*f+a*c*D*f+A*C*d*E*f+A*C*D*E*F+A*b*C*E<->G |
| opt_expert | 1 | 1.000 | 1.000 | 1.000 | c*D*E*f+a*B*c*D*f+A*C*E*f+A*C*D*E+A*b*c*D*f<->G |

## Parsimonious solution vs truth

| mode | n_ps | ps_sub_correct | ps_term_precision_sub | ps_paths_found_sub | ps_exact | ps_irrelevant_in | ps_solution |
|---|---|---|---|---|---|---|---|
| oracle | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D*f+A*C*E<->G |
| quantile | 0 |  |  |  |  |  | (none) |
| kde | 0 |  |  |  |  |  | (none) |
| expert | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D*f+A*C*E<->G |
| opt | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D*f+A*C*E<->G |
| opt_c6c7 | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | c*D*f+A*C*E<->G |
| opt_expert | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | c*D*E*f+C*D*E*F+B*c*D*e+A*c*D*f+A*C*E*f<->G |

