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

Observable('ERK_T202_Y204',
           model.monomers['MAPK1'](T185='p', Y187='p') +
           model.monomers['MAPK3'](T202='p', Y204='p'))

Observable('MEK_S221',
           model.monomers['MAP2K1'](S222='p') +
           model.monomers['MAP2K2'](S226='p'))

add_inhibitor(model, 'iEGFR', ['EGFR'])
add_inhibitor(model, 'iMEK', ['MAP2K1', 'MAP2K2'])
#add_inhibitor(model, 'iPI3K', ['PIK3CA'])
#add_inhibitor(model, 'iPKC', ['MAP2K1', 'MAP2K2'])

add_observables(model)