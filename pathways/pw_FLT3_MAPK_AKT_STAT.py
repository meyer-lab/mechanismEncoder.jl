from mEncoder.mechanistic_model import (
    add_monomer_synth_deg, generate_pathway, add_activation,
    add_observables, add_inhibitor
)

from pysb import Model

model = Model('FLT3_MAPK_AKT_STAT')

# FLT3
for rtkf_name in ['FL']:
    add_monomer_synth_deg(rtkf_name)

rtk_cascade = [
    ('FLT3',  {'Y843': ['FL']}),
    ('ABL2',   {'Y1294': [],
                'Y177': []})
]
generate_pathway(model, rtk_cascade)

# ERK
for ras_name in ['HRAS', 'KRAS', 'NRAS']:
    add_monomer_synth_deg(ras_name, nsites=['N'])
    add_activation(
        model, ras_name, 'N', 'nucleotide_exchange',
        ['FLT3__Y843_p', 'ABL2__Y177_p']
    )

mapk_cascade = [
    ('RAF1',   {'S338':      ['KRAS__N_gtp', 'HRAS__N_gtp', 'NRAS__N_gtp'],
                'S29_S289_S296_S301_S642':  ['MAPK1__T185_p__Y187_p',
                                             'MAPK3__T202_p__Y204_p']}),
    ('BRAF',   {'S447':      ['KRAS__N_gtp', 'HRAS__N_gtp', 'NRAS__N_gtp']}),
    ('MAP2K1', {'S218_S222': [
        'RAF1__S29_u__S289_u__S296_u__S301_u__S338_p__S642_u',
        'BRAF__S447_p'
    ]}),
    ('MAP2K2', {'S222_S226': [
        'RAF1__S29_u__S289_u__S296_u__S301_u__S338_p__S642_u',
        'BRAF__S447_p'
    ]}),
    ('MAPK1',  {'T185_Y187': ['MAP2K1__S218_p__S222_p',
                              'MAP2K2__S222_p__S226_p']}),
    ('MAPK3',  {'T202_Y204': ['MAP2K1__S218_p__S222_p',
                              'MAP2K2__S222_p__S226_p']}),
]
generate_pathway(model, mapk_cascade)

# AKT
akt_cascade = [
    ('PIK3CA', {'pip2':      ['KRAS__N_gtp', 'HRAS__N_gtp', 'NRAS__N_gtp',
                              'FLT3__Y843_p']}),
    ('AKT1',   {'T308':      ['PIK3CA__pip2_p']}),
    ('AKT2',   {'T309':      ['PIK3CA__pip2_p']}),
    ('AKT3',   {'T305':      ['PIK3CA__pip2_p']}),
]
generate_pathway(model, akt_cascade)
active_akt = ['AKT1__T308_p', 'AKT2__T309_p',
              'AKT3__T305_p']

gsk_cascade = [
    ('GSK3A', {'S21': active_akt}),
    ('GSK3B', {'S9': active_akt})
]
generate_pathway(model, gsk_cascade)

# STAT
stat_cascade = [
    ('JAK1', {'Y1034_Y1035': ['FLT3__Y843_p', 'ABL2__Y177_p']}),
    ('JAK2', {'Y570_Y1007_Y1008': ['FLT3__Y843_p', 'ABL2__Y177_p']}),
    ('JAK3', {'Y980_Y981':   ['FLT3__Y843_p', 'ABL2__Y177_p']}),
    ('STAT1', {'Y701':  ['JAK1__Y1034_p__Y1035_p',
                         'JAK2__Y1007_p__Y1008_p',
                         'JAK3__Y980_p__Y981_p']}),
    ('STAT3', {'Y705':  ['JAK1__Y1034_p__Y1035_p',
                         'JAK2__Y1007_p__Y1008_p',
                         'JAK3__Y980_p__Y981_p'],
               'T714_T727': active_akt}),
    ('STAT5A', {'Y694': ['JAK1__Y1034_p__Y1035_p',
                         'JAK2__Y1007_p__Y1008_p',
                         'JAK3__Y980_p__Y981_p'],
                'S780': ['MAPK1__T185_p__Y187_p',
                         'MAPK3__T202_p__Y204_p']}),
    ('STAT5B', {'Y699': ['JAK1__Y1034_p__Y1035_p',
                         'JAK2__Y1007_p__Y1008_p',
                         'JAK3__Y980_p__Y981_p']}),
]
generate_pathway(model, stat_cascade)

add_inhibitor(model, 'ruxolitnib', ['JAK1', 'JAK2', 'JAK3'])
add_inhibitor(model, 'trametinib', ['MAP2K1', 'MAP2K2'])
add_inhibitor(model, 'dasatinib', ['ABL2'])

add_observables(model)
