from pysb import Model, Observable

from mEncoder.mechanistic_model import (
    add_monomer_synth_deg, generate_pathway, add_activation,
    add_observables, add_inhibitor, add_gf_bolus
)

model = Model('EGFR_MAPK_AKT_STAT')

rtkfs = ['EGF']

# EGFR
for rtkf_name in rtkfs:
    add_monomer_synth_deg(rtkf_name)
    add_gf_bolus(model, rtkf_name, [rtkf_name])


erbb_cascade = [
    ('EGFR',  {'Y1173': ['EGF']}),
    ('ERBB2', {'Y1248': ['EGF']}),
]
generate_pathway(model, erbb_cascade)

active_rtks = ['EGFR__Y1173_p', 'ERBB2__Y1248_p']
stat_rtks = ['EGFR__Y1173_p', 'ERBB2__Y1248_p']

# MAPK
for ras_name in ['HRAS', 'KRAS', 'NRAS']:
    add_monomer_synth_deg(ras_name, nsites=['N'])
    add_activation(
        model, ras_name, 'N', 'nucleotide_exchange',
        active_rtks
    )

mapk_cascade = [
    ('RAF1',  {'S338':      ['KRAS__N_gtp', 'HRAS__N_gtp', 'NRAS__N_gtp']}),
    ('BRAF',  {'S445':      ['KRAS__N_gtp', 'HRAS__N_gtp', 'NRAS__N_gtp']}),
    ('ARAF',  {'S299':      ['KRAS__N_gtp', 'HRAS__N_gtp', 'NRAS__N_gtp']}),
    ('MAP2K1',   {'S218_S222': ['RAF1__S338_p', 'BRAF__S445_p',
                                'ARAF__S299_p']}),
    ('MAP2K2',   {'S222_S226': ['RAF1__S338_p', 'BRAF__S445_p',
                                'ARAF__S299_p']}),
    ('MAPK1',  {'T185_Y187': ['MAP2K1__S218_p__S222_p',
                              'MAP2K2__S222_p__S226_p']}),
    ('MAPK3',  {'T202_Y204': ['MAP2K1__S218_p__S222_p',
                              'MAP2K2__S222_p__S226_p']}),
]
generate_pathway(model, mapk_cascade)
active_erk = ['MAPK1__T185_p__Y187_p', 'MAPK3__T202_p__Y204_p']
# MTOR

add_monomer_synth_deg('MTOR', asites=['C'],
                      asite_states=['c1', 'c2'])

# AKT
akt_cascade = [
    ('PIK3CA', {'pip2':      ['KRAS__N_gtp', 'HRAS__N_gtp', 'NRAS__N_gtp'] +
                              active_rtks}),
    ('PDPK1',  {'S241':      ['PIK3CA__pip2_p']}),
    ('AKT1',   {'T308':      ['PDPK1__S241_p'],
                'S473':      ['MTOR__C_c2']}),
    ('AKT2',   {'T309':      ['PDPK1__S241_p'],
                'S473':      ['MTOR__C_c2']}),
    ('AKT3',   {'T305':      ['PDPK1__S241_p'],
                'S473':      ['MTOR__C_c2']}),
]
generate_pathway(model, akt_cascade)
active_akt = ['AKT1__T308_p__S473_p', 'AKT2__T309_p__S473_p',
              'AKT3__T305_p__S473_p']

add_activation(
    model, 'MTOR', 'C', 'activation',
    active_akt,
    [],
    site_states=['c1', 'c2']
)

# S6
s6_cascade = [
    ('RPS6KB1', {'S412': ['MTOR__C_c1']}),
    ('RPS6KA1', {'S380': active_erk}),
    ('RPS6',    {'S235_S236': ['RPS6KA1__S380_p', 'RPS6KB1__S412_p']}),
]
generate_pathway(model, s6_cascade)

# GSK
gsk_cascade = [
    ('GSK3B', {'S9': ['AKT1__T308_p__S473_p', 'RPS6KA1__S380_p',
                      'RPS6KB1__S412_p']})
]
generate_pathway(model, gsk_cascade)

# STAT
stat_cascade = [
    ('STAT1', {'Y727': active_erk}),
    ('STAT3', {'Y705': stat_rtks}),
    ('STAT5A', {'Y694': stat_rtks}),
]
generate_pathway(model, stat_cascade)


mtor_cascade = [
    ('EIF4EBP1', {'T37_T46': ['MTOR__C_c1', 'MAPK1__T185_p__Y187_p']}),
]
generate_pathway(model, mtor_cascade)

Observable('AKT_S473',
           model.monomers['AKT1'](S473='p') +
           model.monomers['AKT2'](S473='p') +
           model.monomers['AKT3'](S473='p'))

Observable('AKT_T308',
           model.monomers['AKT1'](T308='p') +
           model.monomers['AKT2'](T309='p') +
           model.monomers['AKT3'](T305='p'))

Observable('ERK_T202_Y204',
           model.monomers['MAPK1'](T185='p', Y187='p') +
           model.monomers['MAPK3'](T202='p', Y204='p'))

Observable('MEK_S221',
           model.monomers['MAP2K1'](S222='p') +
           model.monomers['MAP2K2'](S226='p'))

add_inhibitor(model, 'iEGFR', ['EGFR'])
add_inhibitor(model, 'iMEK', ['MAP2K1', 'MAP2K2'])
add_inhibitor(model, 'iPI3K', ['PIK3CA'])
#add_inhibitor(model, 'iPKC', ['MAP2K1', 'MAP2K2'])

add_observables(model)
