# exported from PySB model 'FLT3_MAPK_cp'

from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, MultiState, Tag, ANY, WILD

Model()

Monomer('RAF1', ['S497', 'S499', 'S621', 'S296', 'inh'], {'S497': ['u', 'p'], 'S499': ['u', 'p'], 'S621': ['u', 'p'], 'S296': ['u', 'p']})
Monomer('MAPK3', ['Y204', 'inh'], {'Y204': ['u', 'p']})
Monomer('ARAF', ['S257', 'inh'], {'S257': ['u', 'p']})
Monomer('MAPK1', ['T185', 'Y187', 'inh'], {'T185': ['u', 'p'], 'Y187': ['u', 'p']})
Monomer('FLT3', ['inh'])

Parameter('RAF1_eq', 100.0)
Parameter('RAF1_dephosphorylation_S497_base_kcat', 1.0)
Parameter('INPUT_RAF1_dephosphorylation_S497_base_kcat', 0.0)
Parameter('RAF1_dephosphorylation_S499_base_kcat', 1.0)
Parameter('INPUT_RAF1_dephosphorylation_S499_base_kcat', 0.0)
Parameter('RAF1_dephosphorylation_S621_base_kcat', 1.0)
Parameter('INPUT_RAF1_dephosphorylation_S621_base_kcat', 0.0)
Parameter('RAF1_dephosphorylation_S296_base_kcat', 1.0)
Parameter('INPUT_RAF1_dephosphorylation_S296_base_kcat', 0.0)
Parameter('MAPK3_eq', 100.0)
Parameter('MAPK3_dephosphorylation_Y204_base_kcat', 1.0)
Parameter('INPUT_MAPK3_dephosphorylation_Y204_base_kcat', 0.0)
Parameter('ARAF_eq', 100.0)
Parameter('ARAF_dephosphorylation_S257_base_kcat', 1.0)
Parameter('INPUT_ARAF_dephosphorylation_S257_base_kcat', 0.0)
Parameter('MAPK1_eq', 100.0)
Parameter('MAPK1_dephosphorylation_T185_base_kcat', 1.0)
Parameter('INPUT_MAPK1_dephosphorylation_T185_base_kcat', 0.0)
Parameter('MAPK1_dephosphorylation_Y187_base_kcat', 1.0)
Parameter('INPUT_MAPK1_dephosphorylation_Y187_base_kcat', 0.0)
Parameter('MAPK3_phosphorylation_Y204_Y204_RAF1__S621_p_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_Y204_Y204_RAF1__S621_p_kcat', 0.0)
Parameter('MAPK3_phosphorylation_Y204_Y204_RAF1__S497_p_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_Y204_Y204_RAF1__S497_p_kcat', 0.0)
Parameter('MAPK3_phosphorylation_Y204_Y204_RAF1__S296_p_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_Y204_Y204_RAF1__S296_p_kcat', 0.0)
Parameter('MAPK3_phosphorylation_Y204_Y204_ARAF__S257_p_kcat', 1.0)
Parameter('INPUT_MAPK3_phosphorylation_Y204_Y204_ARAF__S257_p_kcat', 0.0)
Parameter('RAF1_phosphorylation_S296_S296_MAPK3__Y204_p_kcat', 1.0)
Parameter('INPUT_RAF1_phosphorylation_S296_S296_MAPK3__Y204_p_kcat', 0.0)
Parameter('MAPK1_phosphorylation_T185_T185_RAF1__S499_p_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_T185_T185_RAF1__S499_p_kcat', 0.0)
Parameter('MAPK1_phosphorylation_T185_T185_ARAF__S257_p_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_T185_T185_ARAF__S257_p_kcat', 0.0)
Parameter('MAPK1_phosphorylation_Y187_Y187_RAF1__S499_p_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_Y187_Y187_RAF1__S499_p_kcat', 0.0)
Parameter('MAPK1_phosphorylation_Y187_Y187_ARAF__S257_p_kcat', 1.0)
Parameter('INPUT_MAPK1_phosphorylation_Y187_Y187_ARAF__S257_p_kcat', 0.0)
Parameter('trametinib_0', 0.0)
Parameter('trametinib_kd', 0.0)
Parameter('FLT3_eq', 100.0)
Parameter('RAF1_phosphorylation_S621_S497_S296_S621_S497_S296_FLT3_kcat', 1.0)
Parameter('INPUT_RAF1_phosphorylation_S621_S497_S296_S621_S497_S296_FLT3_kcat', 0.0)
Parameter('ARAF_phosphorylation_S257_S257_FLT3_kcat', 1.0)
Parameter('INPUT_ARAF_phosphorylation_S257_S257_FLT3_kcat', 0.0)

Expression('RAF1_dephosphorylation_S497_base_rate', INPUT_RAF1_dephosphorylation_S497_base_kcat*RAF1_dephosphorylation_S497_base_kcat)
Expression('RAF1_dephosphorylation_S499_base_rate', INPUT_RAF1_dephosphorylation_S499_base_kcat*RAF1_dephosphorylation_S499_base_kcat)
Expression('RAF1_dephosphorylation_S621_base_rate', INPUT_RAF1_dephosphorylation_S621_base_kcat*RAF1_dephosphorylation_S621_base_kcat)
Expression('RAF1_dephosphorylation_S296_base_rate', INPUT_RAF1_dephosphorylation_S296_base_kcat*RAF1_dephosphorylation_S296_base_kcat)
Expression('MAPK3_dephosphorylation_Y204_base_rate', INPUT_MAPK3_dephosphorylation_Y204_base_kcat*MAPK3_dephosphorylation_Y204_base_kcat)
Expression('ARAF_dephosphorylation_S257_base_rate', ARAF_dephosphorylation_S257_base_kcat*INPUT_ARAF_dephosphorylation_S257_base_kcat)
Expression('MAPK1_dephosphorylation_T185_base_rate', INPUT_MAPK1_dephosphorylation_T185_base_kcat*MAPK1_dephosphorylation_T185_base_kcat)
Expression('MAPK1_dephosphorylation_Y187_base_rate', INPUT_MAPK1_dephosphorylation_Y187_base_kcat*MAPK1_dephosphorylation_Y187_base_kcat)

Observable('RAF1__S621_p_obs', RAF1(S621='p', inh=None))
Observable('RAF1__S497_p_obs', RAF1(S497='p', inh=None))
Observable('RAF1__S296_p_obs', RAF1(S296='p', inh=None))
Observable('ARAF__S257_p_obs', ARAF(S257='p', inh=None))
Observable('MAPK3__Y204_p_obs', MAPK3(Y204='p', inh=None))
Observable('RAF1__S499_p_obs', RAF1(S499='p', inh=None))
Observable('target_ARAF', ARAF())
Observable('target_RAF1', RAF1())
Observable('FLT3_obs', FLT3(inh=None))
Observable('tRAF1', RAF1())
Observable('pRAF1_S497', RAF1(S497='p'))
Observable('pRAF1_S499', RAF1(S499='p'))
Observable('pRAF1_S621', RAF1(S621='p'))
Observable('pRAF1_S296', RAF1(S296='p'))
Observable('pRAF1_S497_S499', RAF1(S497='p', S499='p'))
Observable('pRAF1_S497_S621', RAF1(S497='p', S621='p'))
Observable('pRAF1_S296_S497', RAF1(S497='p', S296='p'))
Observable('pRAF1_S499_S621', RAF1(S499='p', S621='p'))
Observable('pRAF1_S296_S499', RAF1(S499='p', S296='p'))
Observable('pRAF1_S296_S621', RAF1(S621='p', S296='p'))
Observable('pRAF1_S497_S499_S621', RAF1(S497='p', S499='p', S621='p'))
Observable('pRAF1_S296_S497_S499', RAF1(S497='p', S499='p', S296='p'))
Observable('pRAF1_S296_S497_S621', RAF1(S497='p', S621='p', S296='p'))
Observable('pRAF1_S296_S499_S621', RAF1(S499='p', S621='p', S296='p'))
Observable('pRAF1_S296_S497_S499_S621', RAF1(S497='p', S499='p', S621='p', S296='p'))
Observable('tMAPK3', MAPK3())
Observable('pMAPK3_Y204', MAPK3(Y204='p'))
Observable('tARAF', ARAF())
Observable('pARAF_S257', ARAF(S257='p'))
Observable('tMAPK1', MAPK1())
Observable('pMAPK1_T185', MAPK1(T185='p'))
Observable('pMAPK1_Y187', MAPK1(Y187='p'))
Observable('pMAPK1_T185_Y187', MAPK1(T185='p', Y187='p'))
Observable('tFLT3', FLT3())

Expression('MAPK3_phosphorylation_Y204_Y204_RAF1__S621_p_rate', RAF1__S621_p_obs*INPUT_MAPK3_phosphorylation_Y204_Y204_RAF1__S621_p_kcat*MAPK3_phosphorylation_Y204_Y204_RAF1__S621_p_kcat/(inh_RAF1*trametinib_0 + 1))
Expression('MAPK3_phosphorylation_Y204_Y204_RAF1__S497_p_rate', RAF1__S497_p_obs*INPUT_MAPK3_phosphorylation_Y204_Y204_RAF1__S497_p_kcat*MAPK3_phosphorylation_Y204_Y204_RAF1__S497_p_kcat/(inh_RAF1*trametinib_0 + 1))
Expression('MAPK3_phosphorylation_Y204_Y204_RAF1__S296_p_rate', RAF1__S296_p_obs*INPUT_MAPK3_phosphorylation_Y204_Y204_RAF1__S296_p_kcat*MAPK3_phosphorylation_Y204_Y204_RAF1__S296_p_kcat/(inh_RAF1*trametinib_0 + 1))
Expression('MAPK3_phosphorylation_Y204_Y204_ARAF__S257_p_rate', ARAF__S257_p_obs*INPUT_MAPK3_phosphorylation_Y204_Y204_ARAF__S257_p_kcat*MAPK3_phosphorylation_Y204_Y204_ARAF__S257_p_kcat/(inh_ARAF*trametinib_0 + 1))
Expression('RAF1_phosphorylation_S296_S296_MAPK3__Y204_p_rate', MAPK3__Y204_p_obs*INPUT_RAF1_phosphorylation_S296_S296_MAPK3__Y204_p_kcat*RAF1_phosphorylation_S296_S296_MAPK3__Y204_p_kcat)
Expression('MAPK1_phosphorylation_T185_T185_RAF1__S499_p_rate', RAF1__S499_p_obs*INPUT_MAPK1_phosphorylation_T185_T185_RAF1__S499_p_kcat*MAPK1_phosphorylation_T185_T185_RAF1__S499_p_kcat/(inh_RAF1*trametinib_0 + 1))
Expression('MAPK1_phosphorylation_T185_T185_ARAF__S257_p_rate', ARAF__S257_p_obs*INPUT_MAPK1_phosphorylation_T185_T185_ARAF__S257_p_kcat*MAPK1_phosphorylation_T185_T185_ARAF__S257_p_kcat/(inh_ARAF*trametinib_0 + 1))
Expression('MAPK1_phosphorylation_Y187_Y187_RAF1__S499_p_rate', RAF1__S499_p_obs*INPUT_MAPK1_phosphorylation_Y187_Y187_RAF1__S499_p_kcat*MAPK1_phosphorylation_Y187_Y187_RAF1__S499_p_kcat/(inh_RAF1*trametinib_0 + 1))
Expression('MAPK1_phosphorylation_Y187_Y187_ARAF__S257_p_rate', ARAF__S257_p_obs*INPUT_MAPK1_phosphorylation_Y187_Y187_ARAF__S257_p_kcat*MAPK1_phosphorylation_Y187_Y187_ARAF__S257_p_kcat/(inh_ARAF*trametinib_0 + 1))
Expression('inh_ARAF', target_ARAF/trametinib_kd)
Expression('inh_RAF1', target_RAF1/trametinib_kd)
Expression('RAF1_phosphorylation_S621_S497_S296_S621_S497_S296_FLT3_rate', FLT3_obs*INPUT_RAF1_phosphorylation_S621_S497_S296_S621_S497_S296_FLT3_kcat*RAF1_phosphorylation_S621_S497_S296_S621_S497_S296_FLT3_kcat)
Expression('ARAF_phosphorylation_S257_S257_FLT3_rate', FLT3_obs*ARAF_phosphorylation_S257_S257_FLT3_kcat*INPUT_ARAF_phosphorylation_S257_S257_FLT3_kcat)

Rule('RAF1_S497_base', RAF1(S497='p') >> RAF1(S497='u'), RAF1_dephosphorylation_S497_base_rate)
Rule('RAF1_S499_base', RAF1(S499='p') >> RAF1(S499='u'), RAF1_dephosphorylation_S499_base_rate)
Rule('RAF1_S621_base', RAF1(S621='p') >> RAF1(S621='u'), RAF1_dephosphorylation_S621_base_rate)
Rule('RAF1_S296_base', RAF1(S296='p') >> RAF1(S296='u'), RAF1_dephosphorylation_S296_base_rate)
Rule('MAPK3_Y204_base', MAPK3(Y204='p') >> MAPK3(Y204='u'), MAPK3_dephosphorylation_Y204_base_rate)
Rule('ARAF_S257_base', ARAF(S257='p') >> ARAF(S257='u'), ARAF_dephosphorylation_S257_base_rate)
Rule('MAPK1_T185_base', MAPK1(T185='p') >> MAPK1(T185='u'), MAPK1_dephosphorylation_T185_base_rate)
Rule('MAPK1_Y187_base', MAPK1(Y187='p') >> MAPK1(Y187='u'), MAPK1_dephosphorylation_Y187_base_rate)
Rule('MAPK3_phosphorylation_Y204_Y204_RAF1__S621_p', MAPK3(Y204='u') >> MAPK3(Y204='p'), MAPK3_phosphorylation_Y204_Y204_RAF1__S621_p_rate)
Rule('MAPK3_phosphorylation_Y204_Y204_RAF1__S497_p', MAPK3(Y204='u') >> MAPK3(Y204='p'), MAPK3_phosphorylation_Y204_Y204_RAF1__S497_p_rate)
Rule('MAPK3_phosphorylation_Y204_Y204_RAF1__S296_p', MAPK3(Y204='u') >> MAPK3(Y204='p'), MAPK3_phosphorylation_Y204_Y204_RAF1__S296_p_rate)
Rule('MAPK3_phosphorylation_Y204_Y204_ARAF__S257_p', MAPK3(Y204='u') >> MAPK3(Y204='p'), MAPK3_phosphorylation_Y204_Y204_ARAF__S257_p_rate)
Rule('RAF1_phosphorylation_S296_S296_MAPK3__Y204_p', RAF1(S296='u') >> RAF1(S296='p'), RAF1_phosphorylation_S296_S296_MAPK3__Y204_p_rate)
Rule('MAPK1_phosphorylation_T185_T185_RAF1__S499_p', MAPK1(T185='u') >> MAPK1(T185='p'), MAPK1_phosphorylation_T185_T185_RAF1__S499_p_rate)
Rule('MAPK1_phosphorylation_T185_T185_ARAF__S257_p', MAPK1(T185='u') >> MAPK1(T185='p'), MAPK1_phosphorylation_T185_T185_ARAF__S257_p_rate)
Rule('MAPK1_phosphorylation_Y187_Y187_RAF1__S499_p', MAPK1(Y187='u') >> MAPK1(Y187='p'), MAPK1_phosphorylation_Y187_Y187_RAF1__S499_p_rate)
Rule('MAPK1_phosphorylation_Y187_Y187_ARAF__S257_p', MAPK1(Y187='u') >> MAPK1(Y187='p'), MAPK1_phosphorylation_Y187_Y187_ARAF__S257_p_rate)
Rule('RAF1_phosphorylation_S621_S497_S296_S621_S497_S296_FLT3', RAF1(S497='u', S621='u', S296='u') >> RAF1(S497='p', S621='p', S296='p'), RAF1_phosphorylation_S621_S497_S296_S621_S497_S296_FLT3_rate)
Rule('ARAF_phosphorylation_S257_S257_FLT3', ARAF(S257='u') >> ARAF(S257='p'), ARAF_phosphorylation_S257_S257_FLT3_rate)

Initial(RAF1(S497='u', S499='u', S621='u', S296='u', inh=None), RAF1_eq)
Initial(MAPK3(Y204='u', inh=None), MAPK3_eq)
Initial(ARAF(S257='u', inh=None), ARAF_eq)
Initial(MAPK1(T185='u', Y187='u', inh=None), MAPK1_eq)
Initial(FLT3(inh=None), FLT3_eq)

