# exported from PySB model 'EGFR_MAPK_AKT_STAT'

from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, MultiState, Tag, ANY, WILD

Model()

Monomer('EGF', ['inh'])
Monomer('EGF_ext')
Monomer('EGFR', ['Y1173', 'inh'], {'Y1173': ['u', 'p']})
Monomer('ERBB2', ['Y1248', 'inh'], {'Y1248': ['u', 'p']})
Monomer('HRAS', ['N', 'inh'], {'N': ['gdp', 'gtp']})
Monomer('KRAS', ['N', 'inh'], {'N': ['gdp', 'gtp']})
Monomer('NRAS', ['N', 'inh'], {'N': ['gdp', 'gtp']})
Monomer('RAF1', ['S338', 'inh'], {'S338': ['u', 'p']})
Monomer('BRAF', ['S445', 'inh'], {'S445': ['u', 'p']})
Monomer('ARAF', ['S299', 'inh'], {'S299': ['u', 'p']})
Monomer('MAP2K1', ['S218', 'S222', 'inh'], {'S218': ['u', 'p'], 'S222': ['u', 'p']})
Monomer('MAP2K2', ['S222', 'S226', 'inh'], {'S222': ['u', 'p'], 'S226': ['u', 'p']})
Monomer('MAPK1', ['T185', 'Y187', 'inh'], {'T185': ['u', 'p'], 'Y187': ['u', 'p']})
Monomer('MAPK3', ['Y204', 'T202', 'inh'], {'Y204': ['u', 'p'], 'T202': ['u', 'p']})
Monomer('iEGFR', ['target'])
Monomer('iMEK', ['target'])

Parameter('EGF_degradation_kdeg', 1.0)
Parameter('EGF_eq', 100.0)
Parameter('INPUT_EGF_eq', 0.0)
Parameter('EGF_0', 0.0)
Parameter('EGF_EGF_koff', 0.1)
Parameter('EGF_EGF_kd', 1.0)
Parameter('EGFR_degradation_kdeg', 1.0)
Parameter('EGFR_eq', 100.0)
Parameter('INPUT_EGFR_eq', 0.0)
Parameter('EGFR_phosphorylation_Y1173_base_kcat', 1.0)
Parameter('EGFR_dephosphorylation_Y1173_base_kcat', 1.0)
Parameter('INPUT_EGFR_phosphorylation_Y1173_base_kcat', 0.0)
Parameter('INPUT_EGFR_dephosphorylation_Y1173_base_kcat', 0.0)
Parameter('ERBB2_degradation_kdeg', 1.0)
Parameter('ERBB2_eq', 100.0)
Parameter('INPUT_ERBB2_eq', 0.0)
Parameter('ERBB2_phosphorylation_Y1248_base_kcat', 1.0)
Parameter('ERBB2_dephosphorylation_Y1248_base_kcat', 1.0)
Parameter('INPUT_ERBB2_phosphorylation_Y1248_base_kcat', 0.0)
Parameter('INPUT_ERBB2_dephosphorylation_Y1248_base_kcat', 0.0)
Parameter('EGFR_phosphorylation_Y1173_EGF_kcat', 1.0)
Parameter('INPUT_EGFR_phosphorylation_Y1173_EGF_kcat', 0.0)
Parameter('ERBB2_phosphorylation_Y1248_EGF_kcat', 1.0)
Parameter('INPUT_ERBB2_phosphorylation_Y1248_EGF_kcat', 0.0)
Parameter('HRAS_degradation_kdeg', 1.0)
Parameter('HRAS_eq', 100.0)
Parameter('INPUT_HRAS_eq', 0.0)
Parameter('HRAS_gtp_exchange_N_base_kcat', 1.0)
Parameter('HRAS_gdp_exchange_N_base_kcat', 1.0)
Parameter('INPUT_HRAS_gtp_exchange_N_base_kcat', 0.0)
Parameter('INPUT_HRAS_gdp_exchange_N_base_kcat', 0.0)
Parameter('HRAS_gtp_exchange_N_EGFR__Y1173_p_kcat', 1.0)
Parameter('INPUT_HRAS_gtp_exchange_N_EGFR__Y1173_p_kcat', 0.0)
Parameter('HRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat', 1.0)
Parameter('INPUT_HRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat', 0.0)
Parameter('KRAS_degradation_kdeg', 1.0)
Parameter('KRAS_eq', 100.0)
Parameter('INPUT_KRAS_eq', 0.0)
Parameter('KRAS_gtp_exchange_N_base_kcat', 1.0)
Parameter('KRAS_gdp_exchange_N_base_kcat', 1.0)
Parameter('INPUT_KRAS_gtp_exchange_N_base_kcat', 0.0)
Parameter('INPUT_KRAS_gdp_exchange_N_base_kcat', 0.0)
Parameter('KRAS_gtp_exchange_N_EGFR__Y1173_p_kcat', 1.0)
Parameter('INPUT_KRAS_gtp_exchange_N_EGFR__Y1173_p_kcat', 0.0)
Parameter('KRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat', 1.0)
Parameter('INPUT_KRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat', 0.0)
Parameter('NRAS_degradation_kdeg', 1.0)
Parameter('NRAS_eq', 100.0)
Parameter('INPUT_NRAS_eq', 0.0)
Parameter('NRAS_gtp_exchange_N_base_kcat', 1.0)
Parameter('NRAS_gdp_exchange_N_base_kcat', 1.0)
Parameter('INPUT_NRAS_gtp_exchange_N_base_kcat', 0.0)
Parameter('INPUT_NRAS_gdp_exchange_N_base_kcat', 0.0)
Parameter('NRAS_gtp_exchange_N_EGFR__Y1173_p_kcat', 1.0)
Parameter('INPUT_NRAS_gtp_exchange_N_EGFR__Y1173_p_kcat', 0.0)
Parameter('NRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat', 1.0)
Parameter('INPUT_NRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat', 0.0)
Parameter('RAF1_degradation_kdeg', 1.0)
Parameter('RAF1_eq', 100.0)
Parameter('INPUT_RAF1_eq', 0.0)
Parameter('RAF1_phosphorylation_S338_base_kcat', 1.0)
Parameter('RAF1_dephosphorylation_S338_base_kcat', 1.0)
Parameter('INPUT_RAF1_phosphorylation_S338_base_kcat', 0.0)
Parameter('INPUT_RAF1_dephosphorylation_S338_base_kcat', 0.0)
Parameter('BRAF_degradation_kdeg', 1.0)
Parameter('BRAF_eq', 100.0)
Parameter('INPUT_BRAF_eq', 0.0)
Parameter('BRAF_phosphorylation_S445_base_kcat', 1.0)
Parameter('BRAF_dephosphorylation_S445_base_kcat', 1.0)
Parameter('INPUT_BRAF_phosphorylation_S445_base_kcat', 0.0)
Parameter('INPUT_BRAF_dephosphorylation_S445_base_kcat', 0.0)
Parameter('ARAF_degradation_kdeg', 1.0)
Parameter('ARAF_eq', 100.0)
Parameter('INPUT_ARAF_eq', 0.0)
Parameter('ARAF_phosphorylation_S299_base_kcat', 1.0)
Parameter('ARAF_dephosphorylation_S299_base_kcat', 1.0)
Parameter('INPUT_ARAF_phosphorylation_S299_base_kcat', 0.0)
Parameter('INPUT_ARAF_dephosphorylation_S299_base_kcat', 0.0)
Parameter('MAP2K1_degradation_kdeg', 1.0)
Parameter('MAP2K1_eq', 100.0)
Parameter('INPUT_MAP2K1_eq', 0.0)
Parameter('MAP2K1_phosphorylation_S218_base_kcat', 1.0)
Parameter('MAP2K1_dephosphorylation_S218_base_kcat', 1.0)
Parameter('INPUT_MAP2K1_phosphorylation_S218_base_kcat', 0.0)
Parameter('INPUT_MAP2K1_dephosphorylation_S218_base_kcat', 0.0)
Parameter('MAP2K1_phosphorylation_S222_base_kcat', 1.0)
Parameter('MAP2K1_dephosphorylation_S222_base_kcat', 1.0)
Parameter('INPUT_MAP2K1_phosphorylation_S222_base_kcat', 0.0)
Parameter('INPUT_MAP2K1_dephosphorylation_S222_base_kcat', 0.0)
Parameter('MAP2K2_degradation_kdeg', 1.0)
Parameter('MAP2K2_eq', 100.0)
Parameter('INPUT_MAP2K2_eq', 0.0)
Parameter('MAP2K2_phosphorylation_S222_base_kcat', 1.0)
Parameter('MAP2K2_dephosphorylation_S222_base_kcat', 1.0)
Parameter('INPUT_MAP2K2_phosphorylation_S222_base_kcat', 0.0)
Parameter('INPUT_MAP2K2_dephosphorylation_S222_base_kcat', 0.0)
Parameter('MAP2K2_phosphorylation_S226_base_kcat', 1.0)
Parameter('MAP2K2_dephosphorylation_S226_base_kcat', 1.0)
Parameter('INPUT_MAP2K2_phosphorylation_S226_base_kcat', 0.0)
Parameter('INPUT_MAP2K2_dephosphorylation_S226_base_kcat', 0.0)
Parameter('MAPK1_degradation_kdeg', 1.0)
Parameter('MAPK1_eq', 100.0)
Parameter('INPUT_MAPK1_eq', 0.0)
Parameter('MAPK1_phosphorylation_T185_base_kcat', 1.0)
Parameter('MAPK1_dephosphorylation_T185_base_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_T185_base_kcat', 0.0)
Parameter('INPUT_MAPK1_dephosphorylation_T185_base_kcat', 0.0)
Parameter('MAPK1_phosphorylation_Y187_base_kcat', 1.0)
Parameter('MAPK1_dephosphorylation_Y187_base_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_Y187_base_kcat', 0.0)
Parameter('INPUT_MAPK1_dephosphorylation_Y187_base_kcat', 0.0)
Parameter('MAPK3_degradation_kdeg', 1.0)
Parameter('MAPK3_eq', 100.0)
Parameter('INPUT_MAPK3_eq', 0.0)
Parameter('MAPK3_phosphorylation_Y204_base_kcat', 1.0)
Parameter('MAPK3_dephosphorylation_Y204_base_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_Y204_base_kcat', 0.0)
Parameter('INPUT_MAPK3_dephosphorylation_Y204_base_kcat', 0.0)
Parameter('MAPK3_phosphorylation_T202_base_kcat', 1.0)
Parameter('MAPK3_dephosphorylation_T202_base_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_T202_base_kcat', 0.0)
Parameter('INPUT_MAPK3_dephosphorylation_T202_base_kcat', 0.0)
Parameter('RAF1_phosphorylation_S338_KRAS__N_gtp_kcat', 1.0)
Parameter('INPUT_RAF1_phosphorylation_S338_KRAS__N_gtp_kcat', 0.0)
Parameter('RAF1_phosphorylation_S338_HRAS__N_gtp_kcat', 1.0)
Parameter('INPUT_RAF1_phosphorylation_S338_HRAS__N_gtp_kcat', 0.0)
Parameter('RAF1_phosphorylation_S338_NRAS__N_gtp_kcat', 1.0)
Parameter('INPUT_RAF1_phosphorylation_S338_NRAS__N_gtp_kcat', 0.0)
Parameter('BRAF_phosphorylation_S445_KRAS__N_gtp_kcat', 1.0)
Parameter('INPUT_BRAF_phosphorylation_S445_KRAS__N_gtp_kcat', 0.0)
Parameter('BRAF_phosphorylation_S445_HRAS__N_gtp_kcat', 1.0)
Parameter('INPUT_BRAF_phosphorylation_S445_HRAS__N_gtp_kcat', 0.0)
Parameter('BRAF_phosphorylation_S445_NRAS__N_gtp_kcat', 1.0)
Parameter('INPUT_BRAF_phosphorylation_S445_NRAS__N_gtp_kcat', 0.0)
Parameter('ARAF_phosphorylation_S299_KRAS__N_gtp_kcat', 1.0)
Parameter('INPUT_ARAF_phosphorylation_S299_KRAS__N_gtp_kcat', 0.0)
Parameter('ARAF_phosphorylation_S299_HRAS__N_gtp_kcat', 1.0)
Parameter('INPUT_ARAF_phosphorylation_S299_HRAS__N_gtp_kcat', 0.0)
Parameter('ARAF_phosphorylation_S299_NRAS__N_gtp_kcat', 1.0)
Parameter('INPUT_ARAF_phosphorylation_S299_NRAS__N_gtp_kcat', 0.0)
Parameter('MAP2K1_phosphorylation_S222_RAF1__S338_p_kcat', 1.0)
Parameter('INPUT_MAP2K1_phosphorylation_S222_RAF1__S338_p_kcat', 0.0)
Parameter('MAP2K1_phosphorylation_S222_BRAF__S445_p_kcat', 1.0)
Parameter('INPUT_MAP2K1_phosphorylation_S222_BRAF__S445_p_kcat', 0.0)
Parameter('MAP2K1_phosphorylation_S222_ARAF__S299_p_kcat', 1.0)
Parameter('INPUT_MAP2K1_phosphorylation_S222_ARAF__S299_p_kcat', 0.0)
Parameter('MAP2K2_phosphorylation_S226_RAF1__S338_p_kcat', 1.0)
Parameter('INPUT_MAP2K2_phosphorylation_S226_RAF1__S338_p_kcat', 0.0)
Parameter('MAP2K2_phosphorylation_S226_BRAF__S445_p_kcat', 1.0)
Parameter('INPUT_MAP2K2_phosphorylation_S226_BRAF__S445_p_kcat', 0.0)
Parameter('MAP2K2_phosphorylation_S226_ARAF__S299_p_kcat', 1.0)
Parameter('INPUT_MAP2K2_phosphorylation_S226_ARAF__S299_p_kcat', 0.0)
Parameter('MAPK1_phosphorylation_Y187_MAP2K1__S218_p__S222_p_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_Y187_MAP2K1__S218_p__S222_p_kcat', 0.0)
Parameter('MAPK1_phosphorylation_Y187_MAP2K2__S222_p__S226_p_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_Y187_MAP2K2__S222_p__S226_p_kcat', 0.0)
Parameter('MAPK3_phosphorylation_Y204_MAP2K1__S218_p__S222_p_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_Y204_MAP2K1__S218_p__S222_p_kcat', 0.0)
Parameter('MAPK3_phosphorylation_Y204_MAP2K2__S222_p__S226_p_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_Y204_MAP2K2__S222_p__S226_p_kcat', 0.0)
Parameter('iEGFR_0', 0.0)
Parameter('iEGFR_EGFR_koff', 0.1)
Parameter('iEGFR_EGFR_kd', 1.0)
Parameter('iMEK_0', 0.0)
Parameter('iMEK_MAP2K1_koff', 0.1)
Parameter('iMEK_MAP2K1_kd', 1.0)
Parameter('iMEK_MAP2K2_koff', 0.1)
Parameter('iMEK_MAP2K2_kd', 1.0)

Expression('EGF_synthesis_ksyn', EGF_degradation_kdeg*EGF_eq)
Expression('EGF_synthesis_rate', EGF_synthesis_ksyn*INPUT_EGF_eq)
Expression('EGF_degradation_rate', EGF_degradation_kdeg)
Expression('EGF_ss', EGF_synthesis_rate/EGF_degradation_rate)
Expression('EGF_EGF_kon', EGF_EGF_kd*EGF_EGF_koff)
Expression('EGFR_synthesis_ksyn', EGFR_degradation_kdeg*EGFR_eq)
Expression('EGFR_synthesis_rate', EGFR_synthesis_ksyn*INPUT_EGFR_eq)
Expression('EGFR_degradation_rate', EGFR_degradation_kdeg)
Expression('EGFR_ss', EGFR_synthesis_rate/EGFR_degradation_rate)
Expression('EGFR_phosphorylation_Y1173_base_rate', EGFR_phosphorylation_Y1173_base_kcat*INPUT_EGFR_phosphorylation_Y1173_base_kcat)
Expression('EGFR_dephosphorylation_Y1173_base_rate', EGFR_dephosphorylation_Y1173_base_kcat*INPUT_EGFR_dephosphorylation_Y1173_base_kcat)
Expression('ERBB2_synthesis_ksyn', ERBB2_degradation_kdeg*ERBB2_eq)
Expression('ERBB2_synthesis_rate', ERBB2_synthesis_ksyn*INPUT_ERBB2_eq)
Expression('ERBB2_degradation_rate', ERBB2_degradation_kdeg)
Expression('ERBB2_ss', ERBB2_synthesis_rate/ERBB2_degradation_rate)
Expression('ERBB2_phosphorylation_Y1248_base_rate', ERBB2_phosphorylation_Y1248_base_kcat*INPUT_ERBB2_phosphorylation_Y1248_base_kcat)
Expression('ERBB2_dephosphorylation_Y1248_base_rate', ERBB2_dephosphorylation_Y1248_base_kcat*INPUT_ERBB2_dephosphorylation_Y1248_base_kcat)
Expression('HRAS_synthesis_ksyn', HRAS_degradation_kdeg*HRAS_eq)
Expression('HRAS_synthesis_rate', HRAS_synthesis_ksyn*INPUT_HRAS_eq)
Expression('HRAS_degradation_rate', HRAS_degradation_kdeg)
Expression('HRAS_ss', HRAS_synthesis_rate/HRAS_degradation_rate)
Expression('HRAS_gtp_exchange_N_base_rate', HRAS_gtp_exchange_N_base_kcat*INPUT_HRAS_gtp_exchange_N_base_kcat)
Expression('HRAS_gdp_exchange_N_base_rate', HRAS_gdp_exchange_N_base_kcat*INPUT_HRAS_gdp_exchange_N_base_kcat)
Expression('KRAS_synthesis_ksyn', KRAS_degradation_kdeg*KRAS_eq)
Expression('KRAS_synthesis_rate', KRAS_synthesis_ksyn*INPUT_KRAS_eq)
Expression('KRAS_degradation_rate', KRAS_degradation_kdeg)
Expression('KRAS_ss', KRAS_synthesis_rate/KRAS_degradation_rate)
Expression('KRAS_gtp_exchange_N_base_rate', INPUT_KRAS_gtp_exchange_N_base_kcat*KRAS_gtp_exchange_N_base_kcat)
Expression('KRAS_gdp_exchange_N_base_rate', INPUT_KRAS_gdp_exchange_N_base_kcat*KRAS_gdp_exchange_N_base_kcat)
Expression('NRAS_synthesis_ksyn', NRAS_degradation_kdeg*NRAS_eq)
Expression('NRAS_synthesis_rate', NRAS_synthesis_ksyn*INPUT_NRAS_eq)
Expression('NRAS_degradation_rate', NRAS_degradation_kdeg)
Expression('NRAS_ss', NRAS_synthesis_rate/NRAS_degradation_rate)
Expression('NRAS_gtp_exchange_N_base_rate', INPUT_NRAS_gtp_exchange_N_base_kcat*NRAS_gtp_exchange_N_base_kcat)
Expression('NRAS_gdp_exchange_N_base_rate', INPUT_NRAS_gdp_exchange_N_base_kcat*NRAS_gdp_exchange_N_base_kcat)
Expression('RAF1_synthesis_ksyn', RAF1_degradation_kdeg*RAF1_eq)
Expression('RAF1_synthesis_rate', RAF1_synthesis_ksyn*INPUT_RAF1_eq)
Expression('RAF1_degradation_rate', RAF1_degradation_kdeg)
Expression('RAF1_ss', RAF1_synthesis_rate/RAF1_degradation_rate)
Expression('RAF1_phosphorylation_S338_base_rate', INPUT_RAF1_phosphorylation_S338_base_kcat*RAF1_phosphorylation_S338_base_kcat)
Expression('RAF1_dephosphorylation_S338_base_rate', INPUT_RAF1_dephosphorylation_S338_base_kcat*RAF1_dephosphorylation_S338_base_kcat)
Expression('BRAF_synthesis_ksyn', BRAF_degradation_kdeg*BRAF_eq)
Expression('BRAF_synthesis_rate', BRAF_synthesis_ksyn*INPUT_BRAF_eq)
Expression('BRAF_degradation_rate', BRAF_degradation_kdeg)
Expression('BRAF_ss', BRAF_synthesis_rate/BRAF_degradation_rate)
Expression('BRAF_phosphorylation_S445_base_rate', BRAF_phosphorylation_S445_base_kcat*INPUT_BRAF_phosphorylation_S445_base_kcat)
Expression('BRAF_dephosphorylation_S445_base_rate', BRAF_dephosphorylation_S445_base_kcat*INPUT_BRAF_dephosphorylation_S445_base_kcat)
Expression('ARAF_synthesis_ksyn', ARAF_degradation_kdeg*ARAF_eq)
Expression('ARAF_synthesis_rate', ARAF_synthesis_ksyn*INPUT_ARAF_eq)
Expression('ARAF_degradation_rate', ARAF_degradation_kdeg)
Expression('ARAF_ss', ARAF_synthesis_rate/ARAF_degradation_rate)
Expression('ARAF_phosphorylation_S299_base_rate', ARAF_phosphorylation_S299_base_kcat*INPUT_ARAF_phosphorylation_S299_base_kcat)
Expression('ARAF_dephosphorylation_S299_base_rate', ARAF_dephosphorylation_S299_base_kcat*INPUT_ARAF_dephosphorylation_S299_base_kcat)
Expression('MAP2K1_synthesis_ksyn', MAP2K1_degradation_kdeg*MAP2K1_eq)
Expression('MAP2K1_synthesis_rate', MAP2K1_synthesis_ksyn*INPUT_MAP2K1_eq)
Expression('MAP2K1_degradation_rate', MAP2K1_degradation_kdeg)
Expression('MAP2K1_ss', MAP2K1_synthesis_rate/MAP2K1_degradation_rate)
Expression('MAP2K1_phosphorylation_S218_base_rate', INPUT_MAP2K1_phosphorylation_S218_base_kcat*MAP2K1_phosphorylation_S218_base_kcat)
Expression('MAP2K1_dephosphorylation_S218_base_rate', INPUT_MAP2K1_dephosphorylation_S218_base_kcat*MAP2K1_dephosphorylation_S218_base_kcat)
Expression('MAP2K1_phosphorylation_S222_base_rate', INPUT_MAP2K1_phosphorylation_S222_base_kcat*MAP2K1_phosphorylation_S222_base_kcat)
Expression('MAP2K1_dephosphorylation_S222_base_rate', INPUT_MAP2K1_dephosphorylation_S222_base_kcat*MAP2K1_dephosphorylation_S222_base_kcat)
Expression('MAP2K2_synthesis_ksyn', MAP2K2_degradation_kdeg*MAP2K2_eq)
Expression('MAP2K2_synthesis_rate', MAP2K2_synthesis_ksyn*INPUT_MAP2K2_eq)
Expression('MAP2K2_degradation_rate', MAP2K2_degradation_kdeg)
Expression('MAP2K2_ss', MAP2K2_synthesis_rate/MAP2K2_degradation_rate)
Expression('MAP2K2_phosphorylation_S222_base_rate', INPUT_MAP2K2_phosphorylation_S222_base_kcat*MAP2K2_phosphorylation_S222_base_kcat)
Expression('MAP2K2_dephosphorylation_S222_base_rate', INPUT_MAP2K2_dephosphorylation_S222_base_kcat*MAP2K2_dephosphorylation_S222_base_kcat)
Expression('MAP2K2_phosphorylation_S226_base_rate', INPUT_MAP2K2_phosphorylation_S226_base_kcat*MAP2K2_phosphorylation_S226_base_kcat)
Expression('MAP2K2_dephosphorylation_S226_base_rate', INPUT_MAP2K2_dephosphorylation_S226_base_kcat*MAP2K2_dephosphorylation_S226_base_kcat)
Expression('MAPK1_synthesis_ksyn', MAPK1_degradation_kdeg*MAPK1_eq)
Expression('MAPK1_synthesis_rate', MAPK1_synthesis_ksyn*INPUT_MAPK1_eq)
Expression('MAPK1_degradation_rate', MAPK1_degradation_kdeg)
Expression('MAPK1_ss', MAPK1_synthesis_rate/MAPK1_degradation_rate)
Expression('MAPK1_phosphorylation_T185_base_rate', INPUT_MAPK1_phosphorylation_T185_base_kcat*MAPK1_phosphorylation_T185_base_kcat)
Expression('MAPK1_dephosphorylation_T185_base_rate', INPUT_MAPK1_dephosphorylation_T185_base_kcat*MAPK1_dephosphorylation_T185_base_kcat)
Expression('MAPK1_phosphorylation_Y187_base_rate', INPUT_MAPK1_phosphorylation_Y187_base_kcat*MAPK1_phosphorylation_Y187_base_kcat)
Expression('MAPK1_dephosphorylation_Y187_base_rate', INPUT_MAPK1_dephosphorylation_Y187_base_kcat*MAPK1_dephosphorylation_Y187_base_kcat)
Expression('MAPK3_synthesis_ksyn', MAPK3_degradation_kdeg*MAPK3_eq)
Expression('MAPK3_synthesis_rate', MAPK3_synthesis_ksyn*INPUT_MAPK3_eq)
Expression('MAPK3_degradation_rate', MAPK3_degradation_kdeg)
Expression('MAPK3_ss', MAPK3_synthesis_rate/MAPK3_degradation_rate)
Expression('MAPK3_phosphorylation_Y204_base_rate', INPUT_MAPK3_phosphorylation_Y204_base_kcat*MAPK3_phosphorylation_Y204_base_kcat)
Expression('MAPK3_dephosphorylation_Y204_base_rate', INPUT_MAPK3_dephosphorylation_Y204_base_kcat*MAPK3_dephosphorylation_Y204_base_kcat)
Expression('MAPK3_phosphorylation_T202_base_rate', INPUT_MAPK3_phosphorylation_T202_base_kcat*MAPK3_phosphorylation_T202_base_kcat)
Expression('MAPK3_dephosphorylation_T202_base_rate', INPUT_MAPK3_dephosphorylation_T202_base_kcat*MAPK3_dephosphorylation_T202_base_kcat)
Expression('iEGFR_EGFR_kon', iEGFR_EGFR_kd*iEGFR_EGFR_koff)
Expression('iMEK_MAP2K1_kon', iMEK_MAP2K1_kd*iMEK_MAP2K1_koff)
Expression('iMEK_MAP2K2_kon', iMEK_MAP2K2_kd*iMEK_MAP2K2_koff)

Observable('EGF_obs', EGF(inh=None))
Observable('EGFR__Y1173_p_obs', EGFR(Y1173='p', inh=None))
Observable('ERBB2__Y1248_p_obs', ERBB2(Y1248='p', inh=None))
Observable('KRAS__N_gtp_obs', KRAS(N='gtp', inh=None))
Observable('HRAS__N_gtp_obs', HRAS(N='gtp', inh=None))
Observable('NRAS__N_gtp_obs', NRAS(N='gtp', inh=None))
Observable('RAF1__S338_p_obs', RAF1(S338='p', inh=None))
Observable('BRAF__S445_p_obs', BRAF(S445='p', inh=None))
Observable('ARAF__S299_p_obs', ARAF(S299='p', inh=None))
Observable('MAP2K1__S218_p__S222_p_obs', MAP2K1(S218='p', S222='p', inh=None))
Observable('MAP2K2__S222_p__S226_p_obs', MAP2K2(S222='p', S226='p', inh=None))
Observable('ERK_T202_Y204', MAPK1(T185='p', Y187='p') + MAPK3(Y204='p', T202='p'))
Observable('MEK_S221', MAP2K1(S222='p') + MAP2K2(S226='p'))
Observable('tEGF', EGF())
Observable('tEGF_ext', EGF_ext())
Observable('tEGFR', EGFR())
Observable('pEGFR_Y1173', EGFR(Y1173='p'))
Observable('tERBB2', ERBB2())
Observable('pERBB2_Y1248', ERBB2(Y1248='p'))
Observable('tHRAS', HRAS())
Observable('tKRAS', KRAS())
Observable('tNRAS', NRAS())
Observable('tRAF1', RAF1())
Observable('pRAF1_S338', RAF1(S338='p'))
Observable('tBRAF', BRAF())
Observable('pBRAF_S445', BRAF(S445='p'))
Observable('tARAF', ARAF())
Observable('pARAF_S299', ARAF(S299='p'))
Observable('tMAP2K1', MAP2K1())
Observable('pMAP2K1_S218', MAP2K1(S218='p'))
Observable('pMAP2K1_S222', MAP2K1(S222='p'))
Observable('pMAP2K1_S218_S222', MAP2K1(S218='p', S222='p'))
Observable('tMAP2K2', MAP2K2())
Observable('pMAP2K2_S222', MAP2K2(S222='p'))
Observable('pMAP2K2_S226', MAP2K2(S226='p'))
Observable('pMAP2K2_S222_S226', MAP2K2(S222='p', S226='p'))
Observable('tMAPK1', MAPK1())
Observable('pMAPK1_T185', MAPK1(T185='p'))
Observable('pMAPK1_Y187', MAPK1(Y187='p'))
Observable('pMAPK1_T185_Y187', MAPK1(T185='p', Y187='p'))
Observable('tMAPK3', MAPK3())
Observable('pMAPK3_Y204', MAPK3(Y204='p'))
Observable('pMAPK3_T202', MAPK3(T202='p'))
Observable('pMAPK3_T202_Y204', MAPK3(Y204='p', T202='p'))
Observable('tiEGFR', iEGFR())
Observable('tiMEK', iMEK())

Expression('EGFR_phosphorylation_Y1173_EGF_rate', EGF_obs*EGFR_phosphorylation_Y1173_EGF_kcat*INPUT_EGFR_phosphorylation_Y1173_EGF_kcat)
Expression('ERBB2_phosphorylation_Y1248_EGF_rate', EGF_obs*ERBB2_phosphorylation_Y1248_EGF_kcat*INPUT_ERBB2_phosphorylation_Y1248_EGF_kcat)
Expression('HRAS_gtp_exchange_N_EGFR__Y1173_p_rate', EGFR__Y1173_p_obs*HRAS_gtp_exchange_N_EGFR__Y1173_p_kcat*INPUT_HRAS_gtp_exchange_N_EGFR__Y1173_p_kcat)
Expression('HRAS_gtp_exchange_N_ERBB2__Y1248_p_rate', ERBB2__Y1248_p_obs*HRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat*INPUT_HRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat)
Expression('KRAS_gtp_exchange_N_EGFR__Y1173_p_rate', EGFR__Y1173_p_obs*INPUT_KRAS_gtp_exchange_N_EGFR__Y1173_p_kcat*KRAS_gtp_exchange_N_EGFR__Y1173_p_kcat)
Expression('KRAS_gtp_exchange_N_ERBB2__Y1248_p_rate', ERBB2__Y1248_p_obs*INPUT_KRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat*KRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat)
Expression('NRAS_gtp_exchange_N_EGFR__Y1173_p_rate', EGFR__Y1173_p_obs*INPUT_NRAS_gtp_exchange_N_EGFR__Y1173_p_kcat*NRAS_gtp_exchange_N_EGFR__Y1173_p_kcat)
Expression('NRAS_gtp_exchange_N_ERBB2__Y1248_p_rate', ERBB2__Y1248_p_obs*INPUT_NRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat*NRAS_gtp_exchange_N_ERBB2__Y1248_p_kcat)
Expression('RAF1_phosphorylation_S338_KRAS__N_gtp_rate', KRAS__N_gtp_obs*INPUT_RAF1_phosphorylation_S338_KRAS__N_gtp_kcat*RAF1_phosphorylation_S338_KRAS__N_gtp_kcat)
Expression('RAF1_phosphorylation_S338_HRAS__N_gtp_rate', HRAS__N_gtp_obs*INPUT_RAF1_phosphorylation_S338_HRAS__N_gtp_kcat*RAF1_phosphorylation_S338_HRAS__N_gtp_kcat)
Expression('RAF1_phosphorylation_S338_NRAS__N_gtp_rate', NRAS__N_gtp_obs*INPUT_RAF1_phosphorylation_S338_NRAS__N_gtp_kcat*RAF1_phosphorylation_S338_NRAS__N_gtp_kcat)
Expression('BRAF_phosphorylation_S445_KRAS__N_gtp_rate', KRAS__N_gtp_obs*BRAF_phosphorylation_S445_KRAS__N_gtp_kcat*INPUT_BRAF_phosphorylation_S445_KRAS__N_gtp_kcat)
Expression('BRAF_phosphorylation_S445_HRAS__N_gtp_rate', HRAS__N_gtp_obs*BRAF_phosphorylation_S445_HRAS__N_gtp_kcat*INPUT_BRAF_phosphorylation_S445_HRAS__N_gtp_kcat)
Expression('BRAF_phosphorylation_S445_NRAS__N_gtp_rate', NRAS__N_gtp_obs*BRAF_phosphorylation_S445_NRAS__N_gtp_kcat*INPUT_BRAF_phosphorylation_S445_NRAS__N_gtp_kcat)
Expression('ARAF_phosphorylation_S299_KRAS__N_gtp_rate', KRAS__N_gtp_obs*ARAF_phosphorylation_S299_KRAS__N_gtp_kcat*INPUT_ARAF_phosphorylation_S299_KRAS__N_gtp_kcat)
Expression('ARAF_phosphorylation_S299_HRAS__N_gtp_rate', HRAS__N_gtp_obs*ARAF_phosphorylation_S299_HRAS__N_gtp_kcat*INPUT_ARAF_phosphorylation_S299_HRAS__N_gtp_kcat)
Expression('ARAF_phosphorylation_S299_NRAS__N_gtp_rate', NRAS__N_gtp_obs*ARAF_phosphorylation_S299_NRAS__N_gtp_kcat*INPUT_ARAF_phosphorylation_S299_NRAS__N_gtp_kcat)
Expression('MAP2K1_phosphorylation_S222_RAF1__S338_p_rate', RAF1__S338_p_obs*INPUT_MAP2K1_phosphorylation_S222_RAF1__S338_p_kcat*MAP2K1_phosphorylation_S222_RAF1__S338_p_kcat)
Expression('MAP2K1_phosphorylation_S222_BRAF__S445_p_rate', BRAF__S445_p_obs*INPUT_MAP2K1_phosphorylation_S222_BRAF__S445_p_kcat*MAP2K1_phosphorylation_S222_BRAF__S445_p_kcat)
Expression('MAP2K1_phosphorylation_S222_ARAF__S299_p_rate', ARAF__S299_p_obs*INPUT_MAP2K1_phosphorylation_S222_ARAF__S299_p_kcat*MAP2K1_phosphorylation_S222_ARAF__S299_p_kcat)
Expression('MAP2K2_phosphorylation_S226_RAF1__S338_p_rate', RAF1__S338_p_obs*INPUT_MAP2K2_phosphorylation_S226_RAF1__S338_p_kcat*MAP2K2_phosphorylation_S226_RAF1__S338_p_kcat)
Expression('MAP2K2_phosphorylation_S226_BRAF__S445_p_rate', BRAF__S445_p_obs*INPUT_MAP2K2_phosphorylation_S226_BRAF__S445_p_kcat*MAP2K2_phosphorylation_S226_BRAF__S445_p_kcat)
Expression('MAP2K2_phosphorylation_S226_ARAF__S299_p_rate', ARAF__S299_p_obs*INPUT_MAP2K2_phosphorylation_S226_ARAF__S299_p_kcat*MAP2K2_phosphorylation_S226_ARAF__S299_p_kcat)
Expression('MAPK1_phosphorylation_Y187_MAP2K1__S218_p__S222_p_rate', MAP2K1__S218_p__S222_p_obs*INPUT_MAPK1_phosphorylation_Y187_MAP2K1__S218_p__S222_p_kcat*MAPK1_phosphorylation_Y187_MAP2K1__S218_p__S222_p_kcat)
Expression('MAPK1_phosphorylation_Y187_MAP2K2__S222_p__S226_p_rate', MAP2K2__S222_p__S226_p_obs*INPUT_MAPK1_phosphorylation_Y187_MAP2K2__S222_p__S226_p_kcat*MAPK1_phosphorylation_Y187_MAP2K2__S222_p__S226_p_kcat)
Expression('MAPK3_phosphorylation_Y204_MAP2K1__S218_p__S222_p_rate', MAP2K1__S218_p__S222_p_obs*INPUT_MAPK3_phosphorylation_Y204_MAP2K1__S218_p__S222_p_kcat*MAPK3_phosphorylation_Y204_MAP2K1__S218_p__S222_p_kcat)
Expression('MAPK3_phosphorylation_Y204_MAP2K2__S222_p__S226_p_rate', MAP2K2__S222_p__S226_p_obs*INPUT_MAPK3_phosphorylation_Y204_MAP2K2__S222_p__S226_p_kcat*MAPK3_phosphorylation_Y204_MAP2K2__S222_p__S226_p_kcat)

Rule('synthesis_EGF', None >> EGF(inh=None), EGF_synthesis_rate)
Rule('degradation_EGF', EGF() >> None, EGF_degradation_rate)
Rule('EGF_ext_to_EGF', EGF_ext() | EGF(inh=None), EGF_EGF_kon, EGF_EGF_koff)
Rule('synthesis_EGFR', None >> EGFR(Y1173='u', inh=None), EGFR_synthesis_rate)
Rule('degradation_EGFR', EGFR() >> None, EGFR_degradation_rate)
Rule('EGFR_Y1173_base', EGFR(Y1173='p') | EGFR(Y1173='u'), EGFR_phosphorylation_Y1173_base_rate, EGFR_dephosphorylation_Y1173_base_rate)
Rule('synthesis_ERBB2', None >> ERBB2(Y1248='u', inh=None), ERBB2_synthesis_rate)
Rule('degradation_ERBB2', ERBB2() >> None, ERBB2_degradation_rate)
Rule('ERBB2_Y1248_base', ERBB2(Y1248='p') | ERBB2(Y1248='u'), ERBB2_phosphorylation_Y1248_base_rate, ERBB2_dephosphorylation_Y1248_base_rate)
Rule('EGFR_phosphorylation_Y1173_EGF', EGFR(Y1173='u') >> EGFR(Y1173='p'), EGFR_phosphorylation_Y1173_EGF_rate)
Rule('ERBB2_phosphorylation_Y1248_EGF', ERBB2(Y1248='u') >> ERBB2(Y1248='p'), ERBB2_phosphorylation_Y1248_EGF_rate)
Rule('synthesis_HRAS', None >> HRAS(N='gdp', inh=None), HRAS_synthesis_rate)
Rule('degradation_HRAS', HRAS() >> None, HRAS_degradation_rate)
Rule('HRAS_N_base', HRAS(N='gtp') | HRAS(N='gdp'), HRAS_gtp_exchange_N_base_rate, HRAS_gdp_exchange_N_base_rate)
Rule('HRAS_gtp_exchange_N_EGFR__Y1173_p', HRAS(N='gdp') >> HRAS(N='gtp'), HRAS_gtp_exchange_N_EGFR__Y1173_p_rate)
Rule('HRAS_gtp_exchange_N_ERBB2__Y1248_p', HRAS(N='gdp') >> HRAS(N='gtp'), HRAS_gtp_exchange_N_ERBB2__Y1248_p_rate)
Rule('synthesis_KRAS', None >> KRAS(N='gdp', inh=None), KRAS_synthesis_rate)
Rule('degradation_KRAS', KRAS() >> None, KRAS_degradation_rate)
Rule('KRAS_N_base', KRAS(N='gtp') | KRAS(N='gdp'), KRAS_gtp_exchange_N_base_rate, KRAS_gdp_exchange_N_base_rate)
Rule('KRAS_gtp_exchange_N_EGFR__Y1173_p', KRAS(N='gdp') >> KRAS(N='gtp'), KRAS_gtp_exchange_N_EGFR__Y1173_p_rate)
Rule('KRAS_gtp_exchange_N_ERBB2__Y1248_p', KRAS(N='gdp') >> KRAS(N='gtp'), KRAS_gtp_exchange_N_ERBB2__Y1248_p_rate)
Rule('synthesis_NRAS', None >> NRAS(N='gdp', inh=None), NRAS_synthesis_rate)
Rule('degradation_NRAS', NRAS() >> None, NRAS_degradation_rate)
Rule('NRAS_N_base', NRAS(N='gtp') | NRAS(N='gdp'), NRAS_gtp_exchange_N_base_rate, NRAS_gdp_exchange_N_base_rate)
Rule('NRAS_gtp_exchange_N_EGFR__Y1173_p', NRAS(N='gdp') >> NRAS(N='gtp'), NRAS_gtp_exchange_N_EGFR__Y1173_p_rate)
Rule('NRAS_gtp_exchange_N_ERBB2__Y1248_p', NRAS(N='gdp') >> NRAS(N='gtp'), NRAS_gtp_exchange_N_ERBB2__Y1248_p_rate)
Rule('synthesis_RAF1', None >> RAF1(S338='u', inh=None), RAF1_synthesis_rate)
Rule('degradation_RAF1', RAF1() >> None, RAF1_degradation_rate)
Rule('RAF1_S338_base', RAF1(S338='p') | RAF1(S338='u'), RAF1_phosphorylation_S338_base_rate, RAF1_dephosphorylation_S338_base_rate)
Rule('synthesis_BRAF', None >> BRAF(S445='u', inh=None), BRAF_synthesis_rate)
Rule('degradation_BRAF', BRAF() >> None, BRAF_degradation_rate)
Rule('BRAF_S445_base', BRAF(S445='p') | BRAF(S445='u'), BRAF_phosphorylation_S445_base_rate, BRAF_dephosphorylation_S445_base_rate)
Rule('synthesis_ARAF', None >> ARAF(S299='u', inh=None), ARAF_synthesis_rate)
Rule('degradation_ARAF', ARAF() >> None, ARAF_degradation_rate)
Rule('ARAF_S299_base', ARAF(S299='p') | ARAF(S299='u'), ARAF_phosphorylation_S299_base_rate, ARAF_dephosphorylation_S299_base_rate)
Rule('synthesis_MAP2K1', None >> MAP2K1(S218='u', S222='u', inh=None), MAP2K1_synthesis_rate)
Rule('degradation_MAP2K1', MAP2K1() >> None, MAP2K1_degradation_rate)
Rule('MAP2K1_S218_base', MAP2K1(S218='p') | MAP2K1(S218='u'), MAP2K1_phosphorylation_S218_base_rate, MAP2K1_dephosphorylation_S218_base_rate)
Rule('MAP2K1_S222_base', MAP2K1(S222='p') | MAP2K1(S222='u'), MAP2K1_phosphorylation_S222_base_rate, MAP2K1_dephosphorylation_S222_base_rate)
Rule('synthesis_MAP2K2', None >> MAP2K2(S222='u', S226='u', inh=None), MAP2K2_synthesis_rate)
Rule('degradation_MAP2K2', MAP2K2() >> None, MAP2K2_degradation_rate)
Rule('MAP2K2_S222_base', MAP2K2(S222='p') | MAP2K2(S222='u'), MAP2K2_phosphorylation_S222_base_rate, MAP2K2_dephosphorylation_S222_base_rate)
Rule('MAP2K2_S226_base', MAP2K2(S226='p') | MAP2K2(S226='u'), MAP2K2_phosphorylation_S226_base_rate, MAP2K2_dephosphorylation_S226_base_rate)
Rule('synthesis_MAPK1', None >> MAPK1(T185='u', Y187='u', inh=None), MAPK1_synthesis_rate)
Rule('degradation_MAPK1', MAPK1() >> None, MAPK1_degradation_rate)
Rule('MAPK1_T185_base', MAPK1(T185='p') | MAPK1(T185='u'), MAPK1_phosphorylation_T185_base_rate, MAPK1_dephosphorylation_T185_base_rate)
Rule('MAPK1_Y187_base', MAPK1(Y187='p') | MAPK1(Y187='u'), MAPK1_phosphorylation_Y187_base_rate, MAPK1_dephosphorylation_Y187_base_rate)
Rule('synthesis_MAPK3', None >> MAPK3(Y204='u', T202='u', inh=None), MAPK3_synthesis_rate)
Rule('degradation_MAPK3', MAPK3() >> None, MAPK3_degradation_rate)
Rule('MAPK3_Y204_base', MAPK3(Y204='p') | MAPK3(Y204='u'), MAPK3_phosphorylation_Y204_base_rate, MAPK3_dephosphorylation_Y204_base_rate)
Rule('MAPK3_T202_base', MAPK3(T202='p') | MAPK3(T202='u'), MAPK3_phosphorylation_T202_base_rate, MAPK3_dephosphorylation_T202_base_rate)
Rule('RAF1_phosphorylation_S338_KRAS__N_gtp', RAF1(S338='u') >> RAF1(S338='p'), RAF1_phosphorylation_S338_KRAS__N_gtp_rate)
Rule('RAF1_phosphorylation_S338_HRAS__N_gtp', RAF1(S338='u') >> RAF1(S338='p'), RAF1_phosphorylation_S338_HRAS__N_gtp_rate)
Rule('RAF1_phosphorylation_S338_NRAS__N_gtp', RAF1(S338='u') >> RAF1(S338='p'), RAF1_phosphorylation_S338_NRAS__N_gtp_rate)
Rule('BRAF_phosphorylation_S445_KRAS__N_gtp', BRAF(S445='u') >> BRAF(S445='p'), BRAF_phosphorylation_S445_KRAS__N_gtp_rate)
Rule('BRAF_phosphorylation_S445_HRAS__N_gtp', BRAF(S445='u') >> BRAF(S445='p'), BRAF_phosphorylation_S445_HRAS__N_gtp_rate)
Rule('BRAF_phosphorylation_S445_NRAS__N_gtp', BRAF(S445='u') >> BRAF(S445='p'), BRAF_phosphorylation_S445_NRAS__N_gtp_rate)
Rule('ARAF_phosphorylation_S299_KRAS__N_gtp', ARAF(S299='u') >> ARAF(S299='p'), ARAF_phosphorylation_S299_KRAS__N_gtp_rate)
Rule('ARAF_phosphorylation_S299_HRAS__N_gtp', ARAF(S299='u') >> ARAF(S299='p'), ARAF_phosphorylation_S299_HRAS__N_gtp_rate)
Rule('ARAF_phosphorylation_S299_NRAS__N_gtp', ARAF(S299='u') >> ARAF(S299='p'), ARAF_phosphorylation_S299_NRAS__N_gtp_rate)
Rule('MAP2K1_phosphorylation_S222_RAF1__S338_p', MAP2K1(S218='u', S222='u') >> MAP2K1(S218='p', S222='p'), MAP2K1_phosphorylation_S222_RAF1__S338_p_rate)
Rule('MAP2K1_phosphorylation_S222_BRAF__S445_p', MAP2K1(S218='u', S222='u') >> MAP2K1(S218='p', S222='p'), MAP2K1_phosphorylation_S222_BRAF__S445_p_rate)
Rule('MAP2K1_phosphorylation_S222_ARAF__S299_p', MAP2K1(S218='u', S222='u') >> MAP2K1(S218='p', S222='p'), MAP2K1_phosphorylation_S222_ARAF__S299_p_rate)
Rule('MAP2K2_phosphorylation_S226_RAF1__S338_p', MAP2K2(S222='u', S226='u') >> MAP2K2(S222='p', S226='p'), MAP2K2_phosphorylation_S226_RAF1__S338_p_rate)
Rule('MAP2K2_phosphorylation_S226_BRAF__S445_p', MAP2K2(S222='u', S226='u') >> MAP2K2(S222='p', S226='p'), MAP2K2_phosphorylation_S226_BRAF__S445_p_rate)
Rule('MAP2K2_phosphorylation_S226_ARAF__S299_p', MAP2K2(S222='u', S226='u') >> MAP2K2(S222='p', S226='p'), MAP2K2_phosphorylation_S226_ARAF__S299_p_rate)
Rule('MAPK1_phosphorylation_Y187_MAP2K1__S218_p__S222_p', MAPK1(T185='u', Y187='u') >> MAPK1(T185='p', Y187='p'), MAPK1_phosphorylation_Y187_MAP2K1__S218_p__S222_p_rate)
Rule('MAPK1_phosphorylation_Y187_MAP2K2__S222_p__S226_p', MAPK1(T185='u', Y187='u') >> MAPK1(T185='p', Y187='p'), MAPK1_phosphorylation_Y187_MAP2K2__S222_p__S226_p_rate)
Rule('MAPK3_phosphorylation_Y204_MAP2K1__S218_p__S222_p', MAPK3(Y204='u', T202='u') >> MAPK3(Y204='p', T202='p'), MAPK3_phosphorylation_Y204_MAP2K1__S218_p__S222_p_rate)
Rule('MAPK3_phosphorylation_Y204_MAP2K2__S222_p__S226_p', MAPK3(Y204='u', T202='u') >> MAPK3(Y204='p', T202='p'), MAPK3_phosphorylation_Y204_MAP2K2__S222_p__S226_p_rate)
Rule('iEGFR_inhibits_EGFR', EGFR(inh=None) + iEGFR(target=None) | EGFR(inh=1) % iEGFR(target=1), iEGFR_EGFR_kon, iEGFR_EGFR_koff)
Rule('iMEK_inhibits_MAP2K1', MAP2K1(inh=None) + iMEK(target=None) | MAP2K1(inh=1) % iMEK(target=1), iMEK_MAP2K1_kon, iMEK_MAP2K1_koff)
Rule('iMEK_inhibits_MAP2K2', MAP2K2(inh=None) + iMEK(target=None) | MAP2K2(inh=1) % iMEK(target=1), iMEK_MAP2K2_kon, iMEK_MAP2K2_koff)

Initial(EGF(inh=None), EGF_ss)
Initial(EGF_ext(), EGF_0, fixed=True)
Initial(EGFR(Y1173='u', inh=None), EGFR_ss)
Initial(ERBB2(Y1248='u', inh=None), ERBB2_ss)
Initial(HRAS(N='gdp', inh=None), HRAS_ss)
Initial(KRAS(N='gdp', inh=None), KRAS_ss)
Initial(NRAS(N='gdp', inh=None), NRAS_ss)
Initial(RAF1(S338='u', inh=None), RAF1_ss)
Initial(BRAF(S445='u', inh=None), BRAF_ss)
Initial(ARAF(S299='u', inh=None), ARAF_ss)
Initial(MAP2K1(S218='u', S222='u', inh=None), MAP2K1_ss)
Initial(MAP2K2(S222='u', S226='u', inh=None), MAP2K2_ss)
Initial(MAPK1(T185='u', Y187='u', inh=None), MAPK1_ss)
Initial(MAPK3(Y204='u', T202='u', inh=None), MAPK3_ss)
Initial(iEGFR(target=None), iEGFR_0, fixed=True)
Initial(iMEK(target=None), iMEK_0, fixed=True)
