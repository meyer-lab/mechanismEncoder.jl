# exported from PySB model 'EGFR_MAPK_AKT_STAT'

from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, MultiState, Tag, ANY, WILD

Model()

Monomer('EGF', ['inh'])
Monomer('EGF_ext')
Monomer('EGFR', ['Y1173', 'inh'], {'Y1173': ['u', 'p']})
Monomer('ERBB2', ['Y1248', 'inh'], {'Y1248': ['u', 'p']})
Monomer('MAP2K1', ['S218', 'S222', 'inh'], {'S218': ['u', 'p'], 'S222': ['u', 'p']})
Monomer('MAP2K2', ['S226', 'S222', 'inh'], {'S226': ['u', 'p'], 'S222': ['u', 'p']})
Monomer('MAPK1', ['Y187', 'T185', 'inh'], {'Y187': ['u', 'p'], 'T185': ['u', 'p']})
Monomer('MAPK3', ['Y204', 'T202', 'inh'], {'Y204': ['u', 'p'], 'T202': ['u', 'p']})
Monomer('MTOR', ['C', 'inh'], {'C': ['c1', 'c2']})
Monomer('PIK3CA', ['pip2', 'inh'], {'pip2': ['u', 'p']})
Monomer('PDPK1', ['S241', 'inh'], {'S241': ['u', 'p']})
Monomer('AKT1', ['T308', 'S473', 'inh'], {'T308': ['u', 'p'], 'S473': ['u', 'p']})
Monomer('AKT2', ['S473', 'T309', 'inh'], {'S473': ['u', 'p'], 'T309': ['u', 'p']})
Monomer('AKT3', ['S473', 'T305', 'inh'], {'S473': ['u', 'p'], 'T305': ['u', 'p']})
Monomer('RPS6KB1', ['S412', 'inh'], {'S412': ['u', 'p']})
Monomer('RPS6KA1', ['S380', 'inh'], {'S380': ['u', 'p']})
Monomer('RPS6', ['S235', 'S236', 'inh'], {'S235': ['u', 'p'], 'S236': ['u', 'p']})
Monomer('GSK3B', ['S9', 'inh'], {'S9': ['u', 'p']})
Monomer('STAT1', ['Y727', 'inh'], {'Y727': ['u', 'p']})
Monomer('STAT3', ['Y705', 'inh'], {'Y705': ['u', 'p']})
Monomer('STAT5A', ['Y694', 'inh'], {'Y694': ['u', 'p']})
Monomer('EIF4EBP1', ['T37', 'T46', 'inh'], {'T37': ['u', 'p'], 'T46': ['u', 'p']})

Parameter('EGF_eq', 100.0)
Parameter('INPUT_EGF_eq', 0.0)
Parameter('EGF_0', 0.0)
Parameter('EGF_EGF_koff', 0.1)
Parameter('EGF_EGF_kd', 1.0)
Parameter('EGFR_eq', 100.0)
Parameter('INPUT_EGFR_eq', 0.0)
Parameter('EGFR_dephosphorylation_Y1173_base_kcat', 1.0)
Parameter('INPUT_EGFR_dephosphorylation_Y1173_base_kcat', 0.0)
Parameter('ERBB2_eq', 100.0)
Parameter('INPUT_ERBB2_eq', 0.0)
Parameter('ERBB2_dephosphorylation_Y1248_base_kcat', 1.0)
Parameter('INPUT_ERBB2_dephosphorylation_Y1248_base_kcat', 0.0)
Parameter('EGFR_phosphorylation_Y1173_Y1173_EGF_kcat', 1.0)
Parameter('INPUT_EGFR_phosphorylation_Y1173_Y1173_EGF_kcat', 0.0)
Parameter('ERBB2_phosphorylation_Y1248_Y1248_EGF_kcat', 1.0)
Parameter('INPUT_ERBB2_phosphorylation_Y1248_Y1248_EGF_kcat', 0.0)
Parameter('MAP2K1_eq', 100.0)
Parameter('INPUT_MAP2K1_eq', 0.0)
Parameter('MAP2K1_dephosphorylation_S218_base_kcat', 1.0)
Parameter('INPUT_MAP2K1_dephosphorylation_S218_base_kcat', 0.0)
Parameter('MAP2K1_dephosphorylation_S222_base_kcat', 1.0)
Parameter('INPUT_MAP2K1_dephosphorylation_S222_base_kcat', 0.0)
Parameter('MAP2K2_eq', 100.0)
Parameter('INPUT_MAP2K2_eq', 0.0)
Parameter('MAP2K2_dephosphorylation_S226_base_kcat', 1.0)
Parameter('INPUT_MAP2K2_dephosphorylation_S226_base_kcat', 0.0)
Parameter('MAP2K2_dephosphorylation_S222_base_kcat', 1.0)
Parameter('INPUT_MAP2K2_dephosphorylation_S222_base_kcat', 0.0)
Parameter('MAPK1_eq', 100.0)
Parameter('INPUT_MAPK1_eq', 0.0)
Parameter('MAPK1_dephosphorylation_Y187_base_kcat', 1.0)
Parameter('INPUT_MAPK1_dephosphorylation_Y187_base_kcat', 0.0)
Parameter('MAPK1_dephosphorylation_T185_base_kcat', 1.0)
Parameter('INPUT_MAPK1_dephosphorylation_T185_base_kcat', 0.0)
Parameter('MAPK3_eq', 100.0)
Parameter('INPUT_MAPK3_eq', 0.0)
Parameter('MAPK3_dephosphorylation_Y204_base_kcat', 1.0)
Parameter('INPUT_MAPK3_dephosphorylation_Y204_base_kcat', 0.0)
Parameter('MAPK3_dephosphorylation_T202_base_kcat', 1.0)
Parameter('INPUT_MAPK3_dephosphorylation_T202_base_kcat', 0.0)
Parameter('MAP2K1_phosphorylation_S218_S222_S218_S222_EGFR__Y1173_p_kcat', 1.0)
Parameter('INPUT_MAP2K1_phosphorylation_S218_S222_S218_S222_EGFR__Y1173_p_kcat', 0.0)
Parameter('MAP2K1_phosphorylation_S218_S222_S218_S222_ERBB2__Y1248_p_kcat', 1.0)
Parameter('INPUT_MAP2K1_phosphorylation_S218_S222_S218_S222_ERBB2__Y1248_p_kcat', 0.0)
Parameter('MAP2K2_phosphorylation_S222_S226_S222_S226_EGFR__Y1173_p_kcat', 1.0)
Parameter('INPUT_MAP2K2_phosphorylation_S222_S226_S222_S226_EGFR__Y1173_p_kcat', 0.0)
Parameter('MAP2K2_phosphorylation_S222_S226_S222_S226_ERBB2__Y1248_p_kcat', 1.0)
Parameter('INPUT_MAP2K2_phosphorylation_S222_S226_S222_S226_ERBB2__Y1248_p_kcat', 0.0)
Parameter('MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K1__S218_p__S222_p_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K1__S218_p__S222_p_kcat', 0.0)
Parameter('MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K2__S222_p__S226_p_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K2__S222_p__S226_p_kcat', 0.0)
Parameter('MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K1__S218_p__S222_p_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K1__S218_p__S222_p_kcat', 0.0)
Parameter('MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K2__S222_p__S226_p_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K2__S222_p__S226_p_kcat', 0.0)
Parameter('MTOR_eq', 100.0)
Parameter('INPUT_MTOR_eq', 0.0)
Parameter('MTOR_deactivation_C_base_kcat', 1.0)
Parameter('INPUT_MTOR_deactivation_C_base_kcat', 0.0)
Parameter('PIK3CA_eq', 100.0)
Parameter('INPUT_PIK3CA_eq', 0.0)
Parameter('PIK3CA_dephosphorylation_pip2_base_kcat', 1.0)
Parameter('INPUT_PIK3CA_dephosphorylation_pip2_base_kcat', 0.0)
Parameter('PDPK1_eq', 100.0)
Parameter('INPUT_PDPK1_eq', 0.0)
Parameter('PDPK1_dephosphorylation_S241_base_kcat', 1.0)
Parameter('INPUT_PDPK1_dephosphorylation_S241_base_kcat', 0.0)
Parameter('AKT1_eq', 100.0)
Parameter('INPUT_AKT1_eq', 0.0)
Parameter('AKT1_dephosphorylation_T308_base_kcat', 1.0)
Parameter('INPUT_AKT1_dephosphorylation_T308_base_kcat', 0.0)
Parameter('AKT1_dephosphorylation_S473_base_kcat', 1.0)
Parameter('INPUT_AKT1_dephosphorylation_S473_base_kcat', 0.0)
Parameter('AKT2_eq', 100.0)
Parameter('INPUT_AKT2_eq', 0.0)
Parameter('AKT2_dephosphorylation_S473_base_kcat', 1.0)
Parameter('INPUT_AKT2_dephosphorylation_S473_base_kcat', 0.0)
Parameter('AKT2_dephosphorylation_T309_base_kcat', 1.0)
Parameter('INPUT_AKT2_dephosphorylation_T309_base_kcat', 0.0)
Parameter('AKT3_eq', 100.0)
Parameter('INPUT_AKT3_eq', 0.0)
Parameter('AKT3_dephosphorylation_S473_base_kcat', 1.0)
Parameter('INPUT_AKT3_dephosphorylation_S473_base_kcat', 0.0)
Parameter('AKT3_dephosphorylation_T305_base_kcat', 1.0)
Parameter('INPUT_AKT3_dephosphorylation_T305_base_kcat', 0.0)
Parameter('PIK3CA_phosphorylation_pip2_pip2_EGFR__Y1173_p_kcat', 1.0)
Parameter('INPUT_PIK3CA_phosphorylation_pip2_pip2_EGFR__Y1173_p_kcat', 0.0)
Parameter('PIK3CA_phosphorylation_pip2_pip2_ERBB2__Y1248_p_kcat', 1.0)
Parameter('INPUT_PIK3CA_phosphorylation_pip2_pip2_ERBB2__Y1248_p_kcat', 0.0)
Parameter('PDPK1_phosphorylation_S241_S241_PIK3CA__pip2_p_kcat', 1.0)
Parameter('INPUT_PDPK1_phosphorylation_S241_S241_PIK3CA__pip2_p_kcat', 0.0)
Parameter('AKT1_phosphorylation_T308_T308_PDPK1__S241_p_kcat', 1.0)
Parameter('INPUT_AKT1_phosphorylation_T308_T308_PDPK1__S241_p_kcat', 0.0)
Parameter('AKT1_phosphorylation_S473_S473_MTOR__C_c2_kcat', 1.0)
Parameter('INPUT_AKT1_phosphorylation_S473_S473_MTOR__C_c2_kcat', 0.0)
Parameter('AKT2_phosphorylation_T309_T309_PDPK1__S241_p_kcat', 1.0)
Parameter('INPUT_AKT2_phosphorylation_T309_T309_PDPK1__S241_p_kcat', 0.0)
Parameter('AKT2_phosphorylation_S473_S473_MTOR__C_c2_kcat', 1.0)
Parameter('INPUT_AKT2_phosphorylation_S473_S473_MTOR__C_c2_kcat', 0.0)
Parameter('AKT3_phosphorylation_T305_T305_PDPK1__S241_p_kcat', 1.0)
Parameter('INPUT_AKT3_phosphorylation_T305_T305_PDPK1__S241_p_kcat', 0.0)
Parameter('AKT3_phosphorylation_S473_S473_MTOR__C_c2_kcat', 1.0)
Parameter('INPUT_AKT3_phosphorylation_S473_S473_MTOR__C_c2_kcat', 0.0)
Parameter('MTOR_gtp_exchange_C_AKT1__T308_p__S473_p_kcat', 1.0)
Parameter('INPUT_MTOR_gtp_exchange_C_AKT1__T308_p__S473_p_kcat', 0.0)
Parameter('MTOR_gtp_exchange_C_AKT2__T309_p__S473_p_kcat', 1.0)
Parameter('INPUT_MTOR_gtp_exchange_C_AKT2__T309_p__S473_p_kcat', 0.0)
Parameter('MTOR_gtp_exchange_C_AKT3__T305_p__S473_p_kcat', 1.0)
Parameter('INPUT_MTOR_gtp_exchange_C_AKT3__T305_p__S473_p_kcat', 0.0)
Parameter('RPS6KB1_eq', 100.0)
Parameter('INPUT_RPS6KB1_eq', 0.0)
Parameter('RPS6KB1_dephosphorylation_S412_base_kcat', 1.0)
Parameter('INPUT_RPS6KB1_dephosphorylation_S412_base_kcat', 0.0)
Parameter('RPS6KA1_eq', 100.0)
Parameter('INPUT_RPS6KA1_eq', 0.0)
Parameter('RPS6KA1_dephosphorylation_S380_base_kcat', 1.0)
Parameter('INPUT_RPS6KA1_dephosphorylation_S380_base_kcat', 0.0)
Parameter('RPS6_eq', 100.0)
Parameter('INPUT_RPS6_eq', 0.0)
Parameter('RPS6_dephosphorylation_S235_base_kcat', 1.0)
Parameter('INPUT_RPS6_dephosphorylation_S235_base_kcat', 0.0)
Parameter('RPS6_dephosphorylation_S236_base_kcat', 1.0)
Parameter('INPUT_RPS6_dephosphorylation_S236_base_kcat', 0.0)
Parameter('RPS6KB1_phosphorylation_S412_S412_MTOR__C_c1_kcat', 1.0)
Parameter('INPUT_RPS6KB1_phosphorylation_S412_S412_MTOR__C_c1_kcat', 0.0)
Parameter('RPS6KA1_phosphorylation_S380_S380_MAPK1__T185_p__Y187_p_kcat', 1.0)
Parameter('INPUT_RPS6KA1_phosphorylation_S380_S380_MAPK1__T185_p__Y187_p_kcat', 0.0)
Parameter('RPS6KA1_phosphorylation_S380_S380_MAPK3__T202_p__Y204_p_kcat', 1.0)
Parameter('INPUT_RPS6KA1_phosphorylation_S380_S380_MAPK3__T202_p__Y204_p_kcat', 0.0)
Parameter('RPS6_phosphorylation_S235_S236_S235_S236_RPS6KA1__S380_p_kcat', 1.0)
Parameter('INPUT_RPS6_phosphorylation_S235_S236_S235_S236_RPS6KA1__S380_p_kcat', 0.0)
Parameter('RPS6_phosphorylation_S235_S236_S235_S236_RPS6KB1__S412_p_kcat', 1.0)
Parameter('INPUT_RPS6_phosphorylation_S235_S236_S235_S236_RPS6KB1__S412_p_kcat', 0.0)
Parameter('GSK3B_eq', 100.0)
Parameter('INPUT_GSK3B_eq', 0.0)
Parameter('GSK3B_dephosphorylation_S9_base_kcat', 1.0)
Parameter('INPUT_GSK3B_dephosphorylation_S9_base_kcat', 0.0)
Parameter('GSK3B_phosphorylation_S9_S9_AKT1__T308_p__S473_p_kcat', 1.0)
Parameter('INPUT_GSK3B_phosphorylation_S9_S9_AKT1__T308_p__S473_p_kcat', 0.0)
Parameter('GSK3B_phosphorylation_S9_S9_RPS6KA1__S380_p_kcat', 1.0)
Parameter('INPUT_GSK3B_phosphorylation_S9_S9_RPS6KA1__S380_p_kcat', 0.0)
Parameter('GSK3B_phosphorylation_S9_S9_RPS6KB1__S412_p_kcat', 1.0)
Parameter('INPUT_GSK3B_phosphorylation_S9_S9_RPS6KB1__S412_p_kcat', 0.0)
Parameter('STAT1_eq', 100.0)
Parameter('INPUT_STAT1_eq', 0.0)
Parameter('STAT1_dephosphorylation_Y727_base_kcat', 1.0)
Parameter('INPUT_STAT1_dephosphorylation_Y727_base_kcat', 0.0)
Parameter('STAT3_eq', 100.0)
Parameter('INPUT_STAT3_eq', 0.0)
Parameter('STAT3_dephosphorylation_Y705_base_kcat', 1.0)
Parameter('INPUT_STAT3_dephosphorylation_Y705_base_kcat', 0.0)
Parameter('STAT5A_eq', 100.0)
Parameter('INPUT_STAT5A_eq', 0.0)
Parameter('STAT5A_dephosphorylation_Y694_base_kcat', 1.0)
Parameter('INPUT_STAT5A_dephosphorylation_Y694_base_kcat', 0.0)
Parameter('STAT1_phosphorylation_Y727_Y727_MAPK1__T185_p__Y187_p_kcat', 1.0)
Parameter('INPUT_STAT1_phosphorylation_Y727_Y727_MAPK1__T185_p__Y187_p_kcat', 0.0)
Parameter('STAT1_phosphorylation_Y727_Y727_MAPK3__T202_p__Y204_p_kcat', 1.0)
Parameter('INPUT_STAT1_phosphorylation_Y727_Y727_MAPK3__T202_p__Y204_p_kcat', 0.0)
Parameter('STAT3_phosphorylation_Y705_Y705_EGFR__Y1173_p_kcat', 1.0)
Parameter('INPUT_STAT3_phosphorylation_Y705_Y705_EGFR__Y1173_p_kcat', 0.0)
Parameter('STAT3_phosphorylation_Y705_Y705_ERBB2__Y1248_p_kcat', 1.0)
Parameter('INPUT_STAT3_phosphorylation_Y705_Y705_ERBB2__Y1248_p_kcat', 0.0)
Parameter('STAT5A_phosphorylation_Y694_Y694_EGFR__Y1173_p_kcat', 1.0)
Parameter('INPUT_STAT5A_phosphorylation_Y694_Y694_EGFR__Y1173_p_kcat', 0.0)
Parameter('STAT5A_phosphorylation_Y694_Y694_ERBB2__Y1248_p_kcat', 1.0)
Parameter('INPUT_STAT5A_phosphorylation_Y694_Y694_ERBB2__Y1248_p_kcat', 0.0)
Parameter('EIF4EBP1_eq', 100.0)
Parameter('INPUT_EIF4EBP1_eq', 0.0)
Parameter('EIF4EBP1_dephosphorylation_T37_base_kcat', 1.0)
Parameter('INPUT_EIF4EBP1_dephosphorylation_T37_base_kcat', 0.0)
Parameter('EIF4EBP1_dephosphorylation_T46_base_kcat', 1.0)
Parameter('INPUT_EIF4EBP1_dephosphorylation_T46_base_kcat', 0.0)
Parameter('EIF4EBP1_phosphorylation_T37_T46_T37_T46_MTOR__C_c1_kcat', 1.0)
Parameter('INPUT_EIF4EBP1_phosphorylation_T37_T46_T37_T46_MTOR__C_c1_kcat', 0.0)
Parameter('EIF4EBP1_phosphorylation_T37_T46_T37_T46_MAPK1__T185_p__Y187_p_kcat', 1.0)
Parameter('INPUT_EIF4EBP1_phosphorylation_T37_T46_T37_T46_MAPK1__T185_p__Y187_p_kcat', 0.0)
Parameter('iEGFR_0', 0.0)
Parameter('iEGFR_kd', 0.0)
Parameter('iMEK_0', 0.0)
Parameter('iMEK_kd', 0.0)
Parameter('iPI3K_0', 0.0)
Parameter('iPI3K_kd', 0.0)

Expression('EGF_init', EGF_eq*INPUT_EGF_eq)
Expression('EGF_EGF_kon', EGF_EGF_kd*EGF_EGF_koff)
Expression('EGFR_init', EGFR_eq*INPUT_EGFR_eq)
Expression('EGFR_dephosphorylation_Y1173_base_rate', EGFR_dephosphorylation_Y1173_base_kcat*INPUT_EGFR_dephosphorylation_Y1173_base_kcat)
Expression('ERBB2_init', ERBB2_eq*INPUT_ERBB2_eq)
Expression('ERBB2_dephosphorylation_Y1248_base_rate', ERBB2_dephosphorylation_Y1248_base_kcat*INPUT_ERBB2_dephosphorylation_Y1248_base_kcat)
Expression('MAP2K1_init', INPUT_MAP2K1_eq*MAP2K1_eq)
Expression('MAP2K1_dephosphorylation_S218_base_rate', INPUT_MAP2K1_dephosphorylation_S218_base_kcat*MAP2K1_dephosphorylation_S218_base_kcat)
Expression('MAP2K1_dephosphorylation_S222_base_rate', INPUT_MAP2K1_dephosphorylation_S222_base_kcat*MAP2K1_dephosphorylation_S222_base_kcat)
Expression('MAP2K2_init', INPUT_MAP2K2_eq*MAP2K2_eq)
Expression('MAP2K2_dephosphorylation_S226_base_rate', INPUT_MAP2K2_dephosphorylation_S226_base_kcat*MAP2K2_dephosphorylation_S226_base_kcat)
Expression('MAP2K2_dephosphorylation_S222_base_rate', INPUT_MAP2K2_dephosphorylation_S222_base_kcat*MAP2K2_dephosphorylation_S222_base_kcat)
Expression('MAPK1_init', INPUT_MAPK1_eq*MAPK1_eq)
Expression('MAPK1_dephosphorylation_Y187_base_rate', INPUT_MAPK1_dephosphorylation_Y187_base_kcat*MAPK1_dephosphorylation_Y187_base_kcat)
Expression('MAPK1_dephosphorylation_T185_base_rate', INPUT_MAPK1_dephosphorylation_T185_base_kcat*MAPK1_dephosphorylation_T185_base_kcat)
Expression('MAPK3_init', INPUT_MAPK3_eq*MAPK3_eq)
Expression('MAPK3_dephosphorylation_Y204_base_rate', INPUT_MAPK3_dephosphorylation_Y204_base_kcat*MAPK3_dephosphorylation_Y204_base_kcat)
Expression('MAPK3_dephosphorylation_T202_base_rate', INPUT_MAPK3_dephosphorylation_T202_base_kcat*MAPK3_dephosphorylation_T202_base_kcat)
Expression('MTOR_init', INPUT_MTOR_eq*MTOR_eq)
Expression('MTOR_deactivation_C_base_rate', INPUT_MTOR_deactivation_C_base_kcat*MTOR_deactivation_C_base_kcat)
Expression('PIK3CA_init', INPUT_PIK3CA_eq*PIK3CA_eq)
Expression('PIK3CA_dephosphorylation_pip2_base_rate', INPUT_PIK3CA_dephosphorylation_pip2_base_kcat*PIK3CA_dephosphorylation_pip2_base_kcat)
Expression('PDPK1_init', INPUT_PDPK1_eq*PDPK1_eq)
Expression('PDPK1_dephosphorylation_S241_base_rate', INPUT_PDPK1_dephosphorylation_S241_base_kcat*PDPK1_dephosphorylation_S241_base_kcat)
Expression('AKT1_init', AKT1_eq*INPUT_AKT1_eq)
Expression('AKT1_dephosphorylation_T308_base_rate', AKT1_dephosphorylation_T308_base_kcat*INPUT_AKT1_dephosphorylation_T308_base_kcat)
Expression('AKT1_dephosphorylation_S473_base_rate', AKT1_dephosphorylation_S473_base_kcat*INPUT_AKT1_dephosphorylation_S473_base_kcat)
Expression('AKT2_init', AKT2_eq*INPUT_AKT2_eq)
Expression('AKT2_dephosphorylation_S473_base_rate', AKT2_dephosphorylation_S473_base_kcat*INPUT_AKT2_dephosphorylation_S473_base_kcat)
Expression('AKT2_dephosphorylation_T309_base_rate', AKT2_dephosphorylation_T309_base_kcat*INPUT_AKT2_dephosphorylation_T309_base_kcat)
Expression('AKT3_init', AKT3_eq*INPUT_AKT3_eq)
Expression('AKT3_dephosphorylation_S473_base_rate', AKT3_dephosphorylation_S473_base_kcat*INPUT_AKT3_dephosphorylation_S473_base_kcat)
Expression('AKT3_dephosphorylation_T305_base_rate', AKT3_dephosphorylation_T305_base_kcat*INPUT_AKT3_dephosphorylation_T305_base_kcat)
Expression('RPS6KB1_init', INPUT_RPS6KB1_eq*RPS6KB1_eq)
Expression('RPS6KB1_dephosphorylation_S412_base_rate', INPUT_RPS6KB1_dephosphorylation_S412_base_kcat*RPS6KB1_dephosphorylation_S412_base_kcat)
Expression('RPS6KA1_init', INPUT_RPS6KA1_eq*RPS6KA1_eq)
Expression('RPS6KA1_dephosphorylation_S380_base_rate', INPUT_RPS6KA1_dephosphorylation_S380_base_kcat*RPS6KA1_dephosphorylation_S380_base_kcat)
Expression('RPS6_init', INPUT_RPS6_eq*RPS6_eq)
Expression('RPS6_dephosphorylation_S235_base_rate', INPUT_RPS6_dephosphorylation_S235_base_kcat*RPS6_dephosphorylation_S235_base_kcat)
Expression('RPS6_dephosphorylation_S236_base_rate', INPUT_RPS6_dephosphorylation_S236_base_kcat*RPS6_dephosphorylation_S236_base_kcat)
Expression('GSK3B_init', GSK3B_eq*INPUT_GSK3B_eq)
Expression('GSK3B_dephosphorylation_S9_base_rate', GSK3B_dephosphorylation_S9_base_kcat*INPUT_GSK3B_dephosphorylation_S9_base_kcat)
Expression('STAT1_init', INPUT_STAT1_eq*STAT1_eq)
Expression('STAT1_dephosphorylation_Y727_base_rate', INPUT_STAT1_dephosphorylation_Y727_base_kcat*STAT1_dephosphorylation_Y727_base_kcat)
Expression('STAT3_init', INPUT_STAT3_eq*STAT3_eq)
Expression('STAT3_dephosphorylation_Y705_base_rate', INPUT_STAT3_dephosphorylation_Y705_base_kcat*STAT3_dephosphorylation_Y705_base_kcat)
Expression('STAT5A_init', INPUT_STAT5A_eq*STAT5A_eq)
Expression('STAT5A_dephosphorylation_Y694_base_rate', INPUT_STAT5A_dephosphorylation_Y694_base_kcat*STAT5A_dephosphorylation_Y694_base_kcat)
Expression('EIF4EBP1_init', EIF4EBP1_eq*INPUT_EIF4EBP1_eq)
Expression('EIF4EBP1_dephosphorylation_T37_base_rate', EIF4EBP1_dephosphorylation_T37_base_kcat*INPUT_EIF4EBP1_dephosphorylation_T37_base_kcat)
Expression('EIF4EBP1_dephosphorylation_T46_base_rate', EIF4EBP1_dephosphorylation_T46_base_kcat*INPUT_EIF4EBP1_dephosphorylation_T46_base_kcat)

Observable('EGF_obs', EGF(inh=None))
Observable('EGFR__Y1173_p_obs', EGFR(Y1173='p', inh=None))
Observable('ERBB2__Y1248_p_obs', ERBB2(Y1248='p', inh=None))
Observable('MAP2K1__S218_p__S222_p_obs', MAP2K1(S218='p', S222='p', inh=None))
Observable('MAP2K2__S222_p__S226_p_obs', MAP2K2(S226='p', S222='p', inh=None))
Observable('PIK3CA__pip2_p_obs', PIK3CA(pip2='p', inh=None))
Observable('PDPK1__S241_p_obs', PDPK1(S241='p', inh=None))
Observable('MTOR__C_c2_obs', MTOR(C='c2', inh=None))
Observable('AKT1__T308_p__S473_p_obs', AKT1(T308='p', S473='p', inh=None))
Observable('AKT2__T309_p__S473_p_obs', AKT2(S473='p', T309='p', inh=None))
Observable('AKT3__T305_p__S473_p_obs', AKT3(S473='p', T305='p', inh=None))
Observable('MTOR__C_c1_obs', MTOR(C='c1', inh=None))
Observable('MAPK1__T185_p__Y187_p_obs', MAPK1(Y187='p', T185='p', inh=None))
Observable('MAPK3__T202_p__Y204_p_obs', MAPK3(Y204='p', T202='p', inh=None))
Observable('RPS6KA1__S380_p_obs', RPS6KA1(S380='p', inh=None))
Observable('RPS6KB1__S412_p_obs', RPS6KB1(S412='p', inh=None))
Observable('AKT_S473', AKT1(S473='p') + AKT2(S473='p') + AKT3(S473='p'))
Observable('AKT_T308', AKT1(T308='p') + AKT2(T309='p') + AKT3(T305='p'))
Observable('ERK_T202_Y204', MAPK1(Y187='p', T185='p') + MAPK3(Y204='p', T202='p'))
Observable('MEK_S221', MAP2K1(S222='p') + MAP2K2(S226='p'))
Observable('target_EGFR', EGFR())
Observable('target_MAP2K1', MAP2K1())
Observable('target_MAP2K2', MAP2K2())
Observable('target_PIK3CA', PIK3CA())
Observable('tEGF', EGF())
Observable('tEGF_ext', EGF_ext())
Observable('tEGFR', EGFR())
Observable('pEGFR_Y1173', EGFR(Y1173='p'))
Observable('tERBB2', ERBB2())
Observable('pERBB2_Y1248', ERBB2(Y1248='p'))
Observable('tMAP2K1', MAP2K1())
Observable('pMAP2K1_S218', MAP2K1(S218='p'))
Observable('pMAP2K1_S222', MAP2K1(S222='p'))
Observable('pMAP2K1_S218_S222', MAP2K1(S218='p', S222='p'))
Observable('tMAP2K2', MAP2K2())
Observable('pMAP2K2_S226', MAP2K2(S226='p'))
Observable('pMAP2K2_S222', MAP2K2(S222='p'))
Observable('pMAP2K2_S222_S226', MAP2K2(S226='p', S222='p'))
Observable('tMAPK1', MAPK1())
Observable('pMAPK1_Y187', MAPK1(Y187='p'))
Observable('pMAPK1_T185', MAPK1(T185='p'))
Observable('pMAPK1_T185_Y187', MAPK1(Y187='p', T185='p'))
Observable('tMAPK3', MAPK3())
Observable('pMAPK3_Y204', MAPK3(Y204='p'))
Observable('pMAPK3_T202', MAPK3(T202='p'))
Observable('pMAPK3_T202_Y204', MAPK3(Y204='p', T202='p'))
Observable('tMTOR', MTOR())
Observable('tPIK3CA', PIK3CA())
Observable('tPDPK1', PDPK1())
Observable('pPDPK1_S241', PDPK1(S241='p'))
Observable('tAKT1', AKT1())
Observable('pAKT1_T308', AKT1(T308='p'))
Observable('pAKT1_S473', AKT1(S473='p'))
Observable('pAKT1_S473_T308', AKT1(T308='p', S473='p'))
Observable('tAKT2', AKT2())
Observable('pAKT2_S473', AKT2(S473='p'))
Observable('pAKT2_T309', AKT2(T309='p'))
Observable('pAKT2_S473_T309', AKT2(S473='p', T309='p'))
Observable('tAKT3', AKT3())
Observable('pAKT3_S473', AKT3(S473='p'))
Observable('pAKT3_T305', AKT3(T305='p'))
Observable('pAKT3_S473_T305', AKT3(S473='p', T305='p'))
Observable('tRPS6KB1', RPS6KB1())
Observable('pRPS6KB1_S412', RPS6KB1(S412='p'))
Observable('tRPS6KA1', RPS6KA1())
Observable('pRPS6KA1_S380', RPS6KA1(S380='p'))
Observable('tRPS6', RPS6())
Observable('pRPS6_S235', RPS6(S235='p'))
Observable('pRPS6_S236', RPS6(S236='p'))
Observable('pRPS6_S235_S236', RPS6(S235='p', S236='p'))
Observable('tGSK3B', GSK3B())
Observable('pGSK3B_S9', GSK3B(S9='p'))
Observable('tSTAT1', STAT1())
Observable('pSTAT1_Y727', STAT1(Y727='p'))
Observable('tSTAT3', STAT3())
Observable('pSTAT3_Y705', STAT3(Y705='p'))
Observable('tSTAT5A', STAT5A())
Observable('pSTAT5A_Y694', STAT5A(Y694='p'))
Observable('tEIF4EBP1', EIF4EBP1())
Observable('pEIF4EBP1_T37', EIF4EBP1(T37='p'))
Observable('pEIF4EBP1_T46', EIF4EBP1(T46='p'))
Observable('pEIF4EBP1_T37_T46', EIF4EBP1(T37='p', T46='p'))

Expression('inh_PIK3CA', target_PIK3CA/iPI3K_kd)
Expression('inh_MAP2K1', target_MAP2K1/iMEK_kd)
Expression('inh_MAP2K2', target_MAP2K2/iMEK_kd)
Expression('inh_EGFR', target_EGFR/iEGFR_kd)
Expression('EGFR_phosphorylation_Y1173_Y1173_EGF_rate', EGF_obs*EGFR_phosphorylation_Y1173_Y1173_EGF_kcat*INPUT_EGFR_phosphorylation_Y1173_Y1173_EGF_kcat)
Expression('ERBB2_phosphorylation_Y1248_Y1248_EGF_rate', EGF_obs*ERBB2_phosphorylation_Y1248_Y1248_EGF_kcat*INPUT_ERBB2_phosphorylation_Y1248_Y1248_EGF_kcat)
Expression('MAP2K1_phosphorylation_S218_S222_S218_S222_EGFR__Y1173_p_rate', EGFR__Y1173_p_obs*INPUT_MAP2K1_phosphorylation_S218_S222_S218_S222_EGFR__Y1173_p_kcat*MAP2K1_phosphorylation_S218_S222_S218_S222_EGFR__Y1173_p_kcat/(inh_EGFR*iEGFR_0 + 1))
Expression('MAP2K1_phosphorylation_S218_S222_S218_S222_ERBB2__Y1248_p_rate', ERBB2__Y1248_p_obs*INPUT_MAP2K1_phosphorylation_S218_S222_S218_S222_ERBB2__Y1248_p_kcat*MAP2K1_phosphorylation_S218_S222_S218_S222_ERBB2__Y1248_p_kcat)
Expression('MAP2K2_phosphorylation_S222_S226_S222_S226_EGFR__Y1173_p_rate', EGFR__Y1173_p_obs*INPUT_MAP2K2_phosphorylation_S222_S226_S222_S226_EGFR__Y1173_p_kcat*MAP2K2_phosphorylation_S222_S226_S222_S226_EGFR__Y1173_p_kcat/(inh_EGFR*iEGFR_0 + 1))
Expression('MAP2K2_phosphorylation_S222_S226_S222_S226_ERBB2__Y1248_p_rate', ERBB2__Y1248_p_obs*INPUT_MAP2K2_phosphorylation_S222_S226_S222_S226_ERBB2__Y1248_p_kcat*MAP2K2_phosphorylation_S222_S226_S222_S226_ERBB2__Y1248_p_kcat)
Expression('MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K1__S218_p__S222_p_rate', MAP2K1__S218_p__S222_p_obs*INPUT_MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K1__S218_p__S222_p_kcat*MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K1__S218_p__S222_p_kcat/(inh_MAP2K1*iMEK_0 + 1))
Expression('MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K2__S222_p__S226_p_rate', MAP2K2__S222_p__S226_p_obs*INPUT_MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K2__S222_p__S226_p_kcat*MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K2__S222_p__S226_p_kcat/(inh_MAP2K2*iMEK_0 + 1))
Expression('MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K1__S218_p__S222_p_rate', MAP2K1__S218_p__S222_p_obs*INPUT_MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K1__S218_p__S222_p_kcat*MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K1__S218_p__S222_p_kcat/(inh_MAP2K1*iMEK_0 + 1))
Expression('MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K2__S222_p__S226_p_rate', MAP2K2__S222_p__S226_p_obs*INPUT_MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K2__S222_p__S226_p_kcat*MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K2__S222_p__S226_p_kcat/(inh_MAP2K2*iMEK_0 + 1))
Expression('PIK3CA_phosphorylation_pip2_pip2_EGFR__Y1173_p_rate', EGFR__Y1173_p_obs*INPUT_PIK3CA_phosphorylation_pip2_pip2_EGFR__Y1173_p_kcat*PIK3CA_phosphorylation_pip2_pip2_EGFR__Y1173_p_kcat/(inh_EGFR*iEGFR_0 + 1))
Expression('PIK3CA_phosphorylation_pip2_pip2_ERBB2__Y1248_p_rate', ERBB2__Y1248_p_obs*INPUT_PIK3CA_phosphorylation_pip2_pip2_ERBB2__Y1248_p_kcat*PIK3CA_phosphorylation_pip2_pip2_ERBB2__Y1248_p_kcat)
Expression('PDPK1_phosphorylation_S241_S241_PIK3CA__pip2_p_rate', PIK3CA__pip2_p_obs*INPUT_PDPK1_phosphorylation_S241_S241_PIK3CA__pip2_p_kcat*PDPK1_phosphorylation_S241_S241_PIK3CA__pip2_p_kcat/(inh_PIK3CA*iPI3K_0 + 1))
Expression('AKT1_phosphorylation_T308_T308_PDPK1__S241_p_rate', PDPK1__S241_p_obs*AKT1_phosphorylation_T308_T308_PDPK1__S241_p_kcat*INPUT_AKT1_phosphorylation_T308_T308_PDPK1__S241_p_kcat)
Expression('AKT1_phosphorylation_S473_S473_MTOR__C_c2_rate', MTOR__C_c2_obs*AKT1_phosphorylation_S473_S473_MTOR__C_c2_kcat*INPUT_AKT1_phosphorylation_S473_S473_MTOR__C_c2_kcat)
Expression('AKT2_phosphorylation_T309_T309_PDPK1__S241_p_rate', PDPK1__S241_p_obs*AKT2_phosphorylation_T309_T309_PDPK1__S241_p_kcat*INPUT_AKT2_phosphorylation_T309_T309_PDPK1__S241_p_kcat)
Expression('AKT2_phosphorylation_S473_S473_MTOR__C_c2_rate', MTOR__C_c2_obs*AKT2_phosphorylation_S473_S473_MTOR__C_c2_kcat*INPUT_AKT2_phosphorylation_S473_S473_MTOR__C_c2_kcat)
Expression('AKT3_phosphorylation_T305_T305_PDPK1__S241_p_rate', PDPK1__S241_p_obs*AKT3_phosphorylation_T305_T305_PDPK1__S241_p_kcat*INPUT_AKT3_phosphorylation_T305_T305_PDPK1__S241_p_kcat)
Expression('AKT3_phosphorylation_S473_S473_MTOR__C_c2_rate', MTOR__C_c2_obs*AKT3_phosphorylation_S473_S473_MTOR__C_c2_kcat*INPUT_AKT3_phosphorylation_S473_S473_MTOR__C_c2_kcat)
Expression('MTOR_gtp_exchange_C_AKT1__T308_p__S473_p_rate', AKT1__T308_p__S473_p_obs*INPUT_MTOR_gtp_exchange_C_AKT1__T308_p__S473_p_kcat*MTOR_gtp_exchange_C_AKT1__T308_p__S473_p_kcat)
Expression('MTOR_gtp_exchange_C_AKT2__T309_p__S473_p_rate', AKT2__T309_p__S473_p_obs*INPUT_MTOR_gtp_exchange_C_AKT2__T309_p__S473_p_kcat*MTOR_gtp_exchange_C_AKT2__T309_p__S473_p_kcat)
Expression('MTOR_gtp_exchange_C_AKT3__T305_p__S473_p_rate', AKT3__T305_p__S473_p_obs*INPUT_MTOR_gtp_exchange_C_AKT3__T305_p__S473_p_kcat*MTOR_gtp_exchange_C_AKT3__T305_p__S473_p_kcat)
Expression('RPS6KB1_phosphorylation_S412_S412_MTOR__C_c1_rate', MTOR__C_c1_obs*INPUT_RPS6KB1_phosphorylation_S412_S412_MTOR__C_c1_kcat*RPS6KB1_phosphorylation_S412_S412_MTOR__C_c1_kcat)
Expression('RPS6KA1_phosphorylation_S380_S380_MAPK1__T185_p__Y187_p_rate', MAPK1__T185_p__Y187_p_obs*INPUT_RPS6KA1_phosphorylation_S380_S380_MAPK1__T185_p__Y187_p_kcat*RPS6KA1_phosphorylation_S380_S380_MAPK1__T185_p__Y187_p_kcat)
Expression('RPS6KA1_phosphorylation_S380_S380_MAPK3__T202_p__Y204_p_rate', MAPK3__T202_p__Y204_p_obs*INPUT_RPS6KA1_phosphorylation_S380_S380_MAPK3__T202_p__Y204_p_kcat*RPS6KA1_phosphorylation_S380_S380_MAPK3__T202_p__Y204_p_kcat)
Expression('RPS6_phosphorylation_S235_S236_S235_S236_RPS6KA1__S380_p_rate', RPS6KA1__S380_p_obs*INPUT_RPS6_phosphorylation_S235_S236_S235_S236_RPS6KA1__S380_p_kcat*RPS6_phosphorylation_S235_S236_S235_S236_RPS6KA1__S380_p_kcat)
Expression('RPS6_phosphorylation_S235_S236_S235_S236_RPS6KB1__S412_p_rate', RPS6KB1__S412_p_obs*INPUT_RPS6_phosphorylation_S235_S236_S235_S236_RPS6KB1__S412_p_kcat*RPS6_phosphorylation_S235_S236_S235_S236_RPS6KB1__S412_p_kcat)
Expression('GSK3B_phosphorylation_S9_S9_AKT1__T308_p__S473_p_rate', AKT1__T308_p__S473_p_obs*GSK3B_phosphorylation_S9_S9_AKT1__T308_p__S473_p_kcat*INPUT_GSK3B_phosphorylation_S9_S9_AKT1__T308_p__S473_p_kcat)
Expression('GSK3B_phosphorylation_S9_S9_RPS6KA1__S380_p_rate', RPS6KA1__S380_p_obs*GSK3B_phosphorylation_S9_S9_RPS6KA1__S380_p_kcat*INPUT_GSK3B_phosphorylation_S9_S9_RPS6KA1__S380_p_kcat)
Expression('GSK3B_phosphorylation_S9_S9_RPS6KB1__S412_p_rate', RPS6KB1__S412_p_obs*GSK3B_phosphorylation_S9_S9_RPS6KB1__S412_p_kcat*INPUT_GSK3B_phosphorylation_S9_S9_RPS6KB1__S412_p_kcat)
Expression('STAT1_phosphorylation_Y727_Y727_MAPK1__T185_p__Y187_p_rate', MAPK1__T185_p__Y187_p_obs*INPUT_STAT1_phosphorylation_Y727_Y727_MAPK1__T185_p__Y187_p_kcat*STAT1_phosphorylation_Y727_Y727_MAPK1__T185_p__Y187_p_kcat)
Expression('STAT1_phosphorylation_Y727_Y727_MAPK3__T202_p__Y204_p_rate', MAPK3__T202_p__Y204_p_obs*INPUT_STAT1_phosphorylation_Y727_Y727_MAPK3__T202_p__Y204_p_kcat*STAT1_phosphorylation_Y727_Y727_MAPK3__T202_p__Y204_p_kcat)
Expression('STAT3_phosphorylation_Y705_Y705_EGFR__Y1173_p_rate', EGFR__Y1173_p_obs*INPUT_STAT3_phosphorylation_Y705_Y705_EGFR__Y1173_p_kcat*STAT3_phosphorylation_Y705_Y705_EGFR__Y1173_p_kcat/(inh_EGFR*iEGFR_0 + 1))
Expression('STAT3_phosphorylation_Y705_Y705_ERBB2__Y1248_p_rate', ERBB2__Y1248_p_obs*INPUT_STAT3_phosphorylation_Y705_Y705_ERBB2__Y1248_p_kcat*STAT3_phosphorylation_Y705_Y705_ERBB2__Y1248_p_kcat)
Expression('STAT5A_phosphorylation_Y694_Y694_EGFR__Y1173_p_rate', EGFR__Y1173_p_obs*INPUT_STAT5A_phosphorylation_Y694_Y694_EGFR__Y1173_p_kcat*STAT5A_phosphorylation_Y694_Y694_EGFR__Y1173_p_kcat/(inh_EGFR*iEGFR_0 + 1))
Expression('STAT5A_phosphorylation_Y694_Y694_ERBB2__Y1248_p_rate', ERBB2__Y1248_p_obs*INPUT_STAT5A_phosphorylation_Y694_Y694_ERBB2__Y1248_p_kcat*STAT5A_phosphorylation_Y694_Y694_ERBB2__Y1248_p_kcat)
Expression('EIF4EBP1_phosphorylation_T37_T46_T37_T46_MTOR__C_c1_rate', MTOR__C_c1_obs*EIF4EBP1_phosphorylation_T37_T46_T37_T46_MTOR__C_c1_kcat*INPUT_EIF4EBP1_phosphorylation_T37_T46_T37_T46_MTOR__C_c1_kcat)
Expression('EIF4EBP1_phosphorylation_T37_T46_T37_T46_MAPK1__T185_p__Y187_p_rate', MAPK1__T185_p__Y187_p_obs*EIF4EBP1_phosphorylation_T37_T46_T37_T46_MAPK1__T185_p__Y187_p_kcat*INPUT_EIF4EBP1_phosphorylation_T37_T46_T37_T46_MAPK1__T185_p__Y187_p_kcat)

Rule('EGF_ext_to_EGF', EGF_ext() | EGF(inh=None), EGF_EGF_kon, EGF_EGF_koff)
Rule('EGFR_Y1173_base', EGFR(Y1173='p') >> EGFR(Y1173='u'), EGFR_dephosphorylation_Y1173_base_rate)
Rule('ERBB2_Y1248_base', ERBB2(Y1248='p') >> ERBB2(Y1248='u'), ERBB2_dephosphorylation_Y1248_base_rate)
Rule('EGFR_phosphorylation_Y1173_Y1173_EGF', EGFR(Y1173='u') >> EGFR(Y1173='p'), EGFR_phosphorylation_Y1173_Y1173_EGF_rate)
Rule('ERBB2_phosphorylation_Y1248_Y1248_EGF', ERBB2(Y1248='u') >> ERBB2(Y1248='p'), ERBB2_phosphorylation_Y1248_Y1248_EGF_rate)
Rule('MAP2K1_S218_base', MAP2K1(S218='p') >> MAP2K1(S218='u'), MAP2K1_dephosphorylation_S218_base_rate)
Rule('MAP2K1_S222_base', MAP2K1(S222='p') >> MAP2K1(S222='u'), MAP2K1_dephosphorylation_S222_base_rate)
Rule('MAP2K2_S226_base', MAP2K2(S226='p') >> MAP2K2(S226='u'), MAP2K2_dephosphorylation_S226_base_rate)
Rule('MAP2K2_S222_base', MAP2K2(S222='p') >> MAP2K2(S222='u'), MAP2K2_dephosphorylation_S222_base_rate)
Rule('MAPK1_Y187_base', MAPK1(Y187='p') >> MAPK1(Y187='u'), MAPK1_dephosphorylation_Y187_base_rate)
Rule('MAPK1_T185_base', MAPK1(T185='p') >> MAPK1(T185='u'), MAPK1_dephosphorylation_T185_base_rate)
Rule('MAPK3_Y204_base', MAPK3(Y204='p') >> MAPK3(Y204='u'), MAPK3_dephosphorylation_Y204_base_rate)
Rule('MAPK3_T202_base', MAPK3(T202='p') >> MAPK3(T202='u'), MAPK3_dephosphorylation_T202_base_rate)
Rule('MAP2K1_phosphorylation_S218_S222_S218_S222_EGFR__Y1173_p', MAP2K1(S218='u', S222='u') >> MAP2K1(S218='p', S222='p'), MAP2K1_phosphorylation_S218_S222_S218_S222_EGFR__Y1173_p_rate)
Rule('MAP2K1_phosphorylation_S218_S222_S218_S222_ERBB2__Y1248_p', MAP2K1(S218='u', S222='u') >> MAP2K1(S218='p', S222='p'), MAP2K1_phosphorylation_S218_S222_S218_S222_ERBB2__Y1248_p_rate)
Rule('MAP2K2_phosphorylation_S222_S226_S222_S226_EGFR__Y1173_p', MAP2K2(S226='u', S222='u') >> MAP2K2(S226='p', S222='p'), MAP2K2_phosphorylation_S222_S226_S222_S226_EGFR__Y1173_p_rate)
Rule('MAP2K2_phosphorylation_S222_S226_S222_S226_ERBB2__Y1248_p', MAP2K2(S226='u', S222='u') >> MAP2K2(S226='p', S222='p'), MAP2K2_phosphorylation_S222_S226_S222_S226_ERBB2__Y1248_p_rate)
Rule('MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K1__S218_p__S222_p', MAPK1(Y187='u', T185='u') >> MAPK1(Y187='p', T185='p'), MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K1__S218_p__S222_p_rate)
Rule('MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K2__S222_p__S226_p', MAPK1(Y187='u', T185='u') >> MAPK1(Y187='p', T185='p'), MAPK1_phosphorylation_T185_Y187_T185_Y187_MAP2K2__S222_p__S226_p_rate)
Rule('MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K1__S218_p__S222_p', MAPK3(Y204='u', T202='u') >> MAPK3(Y204='p', T202='p'), MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K1__S218_p__S222_p_rate)
Rule('MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K2__S222_p__S226_p', MAPK3(Y204='u', T202='u') >> MAPK3(Y204='p', T202='p'), MAPK3_phosphorylation_T202_Y204_T202_Y204_MAP2K2__S222_p__S226_p_rate)
Rule('MTOR_C_base', MTOR(C='c2') >> MTOR(C='c1'), MTOR_deactivation_C_base_rate)
Rule('PIK3CA_pip2_base', PIK3CA(pip2='p') >> PIK3CA(pip2='u'), PIK3CA_dephosphorylation_pip2_base_rate)
Rule('PDPK1_S241_base', PDPK1(S241='p') >> PDPK1(S241='u'), PDPK1_dephosphorylation_S241_base_rate)
Rule('AKT1_T308_base', AKT1(T308='p') >> AKT1(T308='u'), AKT1_dephosphorylation_T308_base_rate)
Rule('AKT1_S473_base', AKT1(S473='p') >> AKT1(S473='u'), AKT1_dephosphorylation_S473_base_rate)
Rule('AKT2_S473_base', AKT2(S473='p') >> AKT2(S473='u'), AKT2_dephosphorylation_S473_base_rate)
Rule('AKT2_T309_base', AKT2(T309='p') >> AKT2(T309='u'), AKT2_dephosphorylation_T309_base_rate)
Rule('AKT3_S473_base', AKT3(S473='p') >> AKT3(S473='u'), AKT3_dephosphorylation_S473_base_rate)
Rule('AKT3_T305_base', AKT3(T305='p') >> AKT3(T305='u'), AKT3_dephosphorylation_T305_base_rate)
Rule('PIK3CA_phosphorylation_pip2_pip2_EGFR__Y1173_p', PIK3CA(pip2='u') >> PIK3CA(pip2='p'), PIK3CA_phosphorylation_pip2_pip2_EGFR__Y1173_p_rate)
Rule('PIK3CA_phosphorylation_pip2_pip2_ERBB2__Y1248_p', PIK3CA(pip2='u') >> PIK3CA(pip2='p'), PIK3CA_phosphorylation_pip2_pip2_ERBB2__Y1248_p_rate)
Rule('PDPK1_phosphorylation_S241_S241_PIK3CA__pip2_p', PDPK1(S241='u') >> PDPK1(S241='p'), PDPK1_phosphorylation_S241_S241_PIK3CA__pip2_p_rate)
Rule('AKT1_phosphorylation_T308_T308_PDPK1__S241_p', AKT1(T308='u') >> AKT1(T308='p'), AKT1_phosphorylation_T308_T308_PDPK1__S241_p_rate)
Rule('AKT1_phosphorylation_S473_S473_MTOR__C_c2', AKT1(S473='u') >> AKT1(S473='p'), AKT1_phosphorylation_S473_S473_MTOR__C_c2_rate)
Rule('AKT2_phosphorylation_T309_T309_PDPK1__S241_p', AKT2(T309='u') >> AKT2(T309='p'), AKT2_phosphorylation_T309_T309_PDPK1__S241_p_rate)
Rule('AKT2_phosphorylation_S473_S473_MTOR__C_c2', AKT2(S473='u') >> AKT2(S473='p'), AKT2_phosphorylation_S473_S473_MTOR__C_c2_rate)
Rule('AKT3_phosphorylation_T305_T305_PDPK1__S241_p', AKT3(T305='u') >> AKT3(T305='p'), AKT3_phosphorylation_T305_T305_PDPK1__S241_p_rate)
Rule('AKT3_phosphorylation_S473_S473_MTOR__C_c2', AKT3(S473='u') >> AKT3(S473='p'), AKT3_phosphorylation_S473_S473_MTOR__C_c2_rate)
Rule('MTOR_gtp_exchange_C_AKT1__T308_p__S473_p', MTOR(C='c1') >> MTOR(C='c2'), MTOR_gtp_exchange_C_AKT1__T308_p__S473_p_rate)
Rule('MTOR_gtp_exchange_C_AKT2__T309_p__S473_p', MTOR(C='c1') >> MTOR(C='c2'), MTOR_gtp_exchange_C_AKT2__T309_p__S473_p_rate)
Rule('MTOR_gtp_exchange_C_AKT3__T305_p__S473_p', MTOR(C='c1') >> MTOR(C='c2'), MTOR_gtp_exchange_C_AKT3__T305_p__S473_p_rate)
Rule('RPS6KB1_S412_base', RPS6KB1(S412='p') >> RPS6KB1(S412='u'), RPS6KB1_dephosphorylation_S412_base_rate)
Rule('RPS6KA1_S380_base', RPS6KA1(S380='p') >> RPS6KA1(S380='u'), RPS6KA1_dephosphorylation_S380_base_rate)
Rule('RPS6_S235_base', RPS6(S235='p') >> RPS6(S235='u'), RPS6_dephosphorylation_S235_base_rate)
Rule('RPS6_S236_base', RPS6(S236='p') >> RPS6(S236='u'), RPS6_dephosphorylation_S236_base_rate)
Rule('RPS6KB1_phosphorylation_S412_S412_MTOR__C_c1', RPS6KB1(S412='u') >> RPS6KB1(S412='p'), RPS6KB1_phosphorylation_S412_S412_MTOR__C_c1_rate)
Rule('RPS6KA1_phosphorylation_S380_S380_MAPK1__T185_p__Y187_p', RPS6KA1(S380='u') >> RPS6KA1(S380='p'), RPS6KA1_phosphorylation_S380_S380_MAPK1__T185_p__Y187_p_rate)
Rule('RPS6KA1_phosphorylation_S380_S380_MAPK3__T202_p__Y204_p', RPS6KA1(S380='u') >> RPS6KA1(S380='p'), RPS6KA1_phosphorylation_S380_S380_MAPK3__T202_p__Y204_p_rate)
Rule('RPS6_phosphorylation_S235_S236_S235_S236_RPS6KA1__S380_p', RPS6(S235='u', S236='u') >> RPS6(S235='p', S236='p'), RPS6_phosphorylation_S235_S236_S235_S236_RPS6KA1__S380_p_rate)
Rule('RPS6_phosphorylation_S235_S236_S235_S236_RPS6KB1__S412_p', RPS6(S235='u', S236='u') >> RPS6(S235='p', S236='p'), RPS6_phosphorylation_S235_S236_S235_S236_RPS6KB1__S412_p_rate)
Rule('GSK3B_S9_base', GSK3B(S9='p') >> GSK3B(S9='u'), GSK3B_dephosphorylation_S9_base_rate)
Rule('GSK3B_phosphorylation_S9_S9_AKT1__T308_p__S473_p', GSK3B(S9='u') >> GSK3B(S9='p'), GSK3B_phosphorylation_S9_S9_AKT1__T308_p__S473_p_rate)
Rule('GSK3B_phosphorylation_S9_S9_RPS6KA1__S380_p', GSK3B(S9='u') >> GSK3B(S9='p'), GSK3B_phosphorylation_S9_S9_RPS6KA1__S380_p_rate)
Rule('GSK3B_phosphorylation_S9_S9_RPS6KB1__S412_p', GSK3B(S9='u') >> GSK3B(S9='p'), GSK3B_phosphorylation_S9_S9_RPS6KB1__S412_p_rate)
Rule('STAT1_Y727_base', STAT1(Y727='p') >> STAT1(Y727='u'), STAT1_dephosphorylation_Y727_base_rate)
Rule('STAT3_Y705_base', STAT3(Y705='p') >> STAT3(Y705='u'), STAT3_dephosphorylation_Y705_base_rate)
Rule('STAT5A_Y694_base', STAT5A(Y694='p') >> STAT5A(Y694='u'), STAT5A_dephosphorylation_Y694_base_rate)
Rule('STAT1_phosphorylation_Y727_Y727_MAPK1__T185_p__Y187_p', STAT1(Y727='u') >> STAT1(Y727='p'), STAT1_phosphorylation_Y727_Y727_MAPK1__T185_p__Y187_p_rate)
Rule('STAT1_phosphorylation_Y727_Y727_MAPK3__T202_p__Y204_p', STAT1(Y727='u') >> STAT1(Y727='p'), STAT1_phosphorylation_Y727_Y727_MAPK3__T202_p__Y204_p_rate)
Rule('STAT3_phosphorylation_Y705_Y705_EGFR__Y1173_p', STAT3(Y705='u') >> STAT3(Y705='p'), STAT3_phosphorylation_Y705_Y705_EGFR__Y1173_p_rate)
Rule('STAT3_phosphorylation_Y705_Y705_ERBB2__Y1248_p', STAT3(Y705='u') >> STAT3(Y705='p'), STAT3_phosphorylation_Y705_Y705_ERBB2__Y1248_p_rate)
Rule('STAT5A_phosphorylation_Y694_Y694_EGFR__Y1173_p', STAT5A(Y694='u') >> STAT5A(Y694='p'), STAT5A_phosphorylation_Y694_Y694_EGFR__Y1173_p_rate)
Rule('STAT5A_phosphorylation_Y694_Y694_ERBB2__Y1248_p', STAT5A(Y694='u') >> STAT5A(Y694='p'), STAT5A_phosphorylation_Y694_Y694_ERBB2__Y1248_p_rate)
Rule('EIF4EBP1_T37_base', EIF4EBP1(T37='p') >> EIF4EBP1(T37='u'), EIF4EBP1_dephosphorylation_T37_base_rate)
Rule('EIF4EBP1_T46_base', EIF4EBP1(T46='p') >> EIF4EBP1(T46='u'), EIF4EBP1_dephosphorylation_T46_base_rate)
Rule('EIF4EBP1_phosphorylation_T37_T46_T37_T46_MTOR__C_c1', EIF4EBP1(T37='u', T46='u') >> EIF4EBP1(T37='p', T46='p'), EIF4EBP1_phosphorylation_T37_T46_T37_T46_MTOR__C_c1_rate)
Rule('EIF4EBP1_phosphorylation_T37_T46_T37_T46_MAPK1__T185_p__Y187_p', EIF4EBP1(T37='u', T46='u') >> EIF4EBP1(T37='p', T46='p'), EIF4EBP1_phosphorylation_T37_T46_T37_T46_MAPK1__T185_p__Y187_p_rate)

Initial(EGF(inh=None), EGF_init)
Initial(EGF_ext(), EGF_0, fixed=True)
Initial(EGFR(Y1173='u', inh=None), EGFR_init)
Initial(ERBB2(Y1248='u', inh=None), ERBB2_init)
Initial(MAP2K1(S218='u', S222='u', inh=None), MAP2K1_init)
Initial(MAP2K2(S226='u', S222='u', inh=None), MAP2K2_init)
Initial(MAPK1(Y187='u', T185='u', inh=None), MAPK1_init)
Initial(MAPK3(Y204='u', T202='u', inh=None), MAPK3_init)
Initial(MTOR(C='c1', inh=None), MTOR_init)
Initial(PIK3CA(pip2='u', inh=None), PIK3CA_init)
Initial(PDPK1(S241='u', inh=None), PDPK1_init)
Initial(AKT1(T308='u', S473='u', inh=None), AKT1_init)
Initial(AKT2(S473='u', T309='u', inh=None), AKT2_init)
Initial(AKT3(S473='u', T305='u', inh=None), AKT3_init)
Initial(RPS6KB1(S412='u', inh=None), RPS6KB1_init)
Initial(RPS6KA1(S380='u', inh=None), RPS6KA1_init)
Initial(RPS6(S235='u', S236='u', inh=None), RPS6_init)
Initial(GSK3B(S9='u', inh=None), GSK3B_init)
Initial(STAT1(Y727='u', inh=None), STAT1_init)
Initial(STAT3(Y705='u', inh=None), STAT3_init)
Initial(STAT5A(Y694='u', inh=None), STAT5A_init)
Initial(EIF4EBP1(T37='u', T46='u', inh=None), EIF4EBP1_init)

