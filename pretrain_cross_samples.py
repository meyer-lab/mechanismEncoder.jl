"""
Pretraining of population + individual parameters based on per sample
pretraining
"""

import sys
import os

import pandas as pd
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import fides
import petab.visualize
import amici.petab_objective

from pypesto.optimize import FidesOptimizer

from mEncoder.autoencoder import MechanisticAutoEncoder
from mEncoder.pretraining import (
    generate_cross_sample_pretraining_problem, pretrain,
    store_and_plot_pretraining
)
from mEncoder.plotting import plot_cross_samples
from mEncoder import MODEL_FEATURE_PREFIX, apply_objective_settings

MODEL = sys.argv[1]
DATA = sys.argv[2]
SAMPLES = sys.argv[3]
INIT = sys.argv[4]
N_HIDDEN = int(sys.argv[5])
JOB = int(sys.argv[6])

mae = MechanisticAutoEncoder(N_HIDDEN, (
    os.path.join('data', f'{DATA}__{MODEL}__measurements.tsv'),
    os.path.join('data', f'{DATA}__{MODEL}__conditions.tsv'),
    os.path.join('data', f'{DATA}__{MODEL}__observables.tsv'),
), MODEL, SAMPLES.split('.'), par_modulation_scale=0.5)

problem = generate_cross_sample_pretraining_problem(mae)
pretraindir = 'pretraining'
pretrained_samples = {}

prefix = f'{mae.pathway_name}__{mae.data_name}'
output_prefix = f'{prefix}__{SAMPLES}__pca__{N_HIDDEN}__{JOB}'

if INIT == 'pca':
    for sample in SAMPLES.split('.'):
        df = pd.read_csv(
            os.path.join(pretraindir, f'{prefix}__{sample}.csv'), index_col=[0]
        )
        pretrained_samples[sample] = df[[
            col for col in df.columns
            if not col.startswith(MODEL_FEATURE_PREFIX)
        ]]

    def startpoints(**kwargs):
        """
        Custom startpoint routine for cross sample pretraining. This function
        uses the results computed for the completely unconstrained problem
        where the model is just fitted to each individual sample. For each
        sample, a random local optimization result is picked. Then
        shared population parameters are computed as mean over all samples and
        sample specific input parameter are computed by substracting this mean
        from the local solution.
        """
        n_starts = kwargs['n_starts']
        lb = kwargs['lb']

        dim = lb.size
        xs = np.empty((n_starts, dim))

        for istart in range(n_starts):
            # use parameter values from random start for each sample
            par_combo = pd.concat([
                pretraining[
                    pretraining.index == np.random.randint(len(pretraining))
                ]
                for pretraining in pretrained_samples.values()
            ])
            par_combo.index = SAMPLES.split('.')
            means = par_combo.mean()
            par_combo -= means
            inputs = [
                '__'.join(x.split('__')[:-1]).replace(MODEL_FEATURE_PREFIX, '')
                for x in mae.petab_importer.petab_problem.parameter_df.index
                if x.startswith(MODEL_FEATURE_PREFIX)
                and x.endswith(par_combo.index[0])
            ]
            w = la.lstsq(mae.data_pca, par_combo[inputs].values)[0].flatten()
            # compute INPUT parameters as as difference to mean
            for ix, xname in enumerate(
                    problem.get_reduced_vector(np.asarray(problem.x_names),
                                               problem.x_free_indices)
            ):
                if xname.startswith('inflate') and xname.endswith('weight'):
                    xs[istart, ix] = w[int(xname.split('_')[1])]
                else:
                    xs[istart, ix] = means[xname.replace('_obs', '')]

        return xs


apply_objective_settings(problem)

optimizer = FidesOptimizer(
    hessian_update=fides.HybridUpdate(),
    options={
        fides.Options.FATOL: 1e-6,
        fides.Options.XTOL: 1e-8,
        fides.Options.MAXTIME: 3600 * 10,
        fides.Options.MAXITER: 1,
        fides.Options.SUBSPACE_DIM: fides.SubSpaceDim.TWO,
    }
)
np.random.seed(JOB)
result = pretrain(problem, startpoints, 1, optimizer)
store_and_plot_pretraining(result, pretraindir, output_prefix)

importer = mae.petab_importer
model = importer.create_model()
solver = importer.create_solver()
edatas = importer.create_edatas()

x = problem.get_reduced_vector(result.optimize_result.list[0]['x'],
                               problem.x_free_indices)
simulation = problem.objective(x, return_dict=True)

# Convert the simulation to PEtab format.
simulation_df = amici.petab_objective.rdatas_to_simulation_df(
    simulation['rdatas'],
    model=model,
    measurement_df=importer.petab_problem.measurement_df,
)

# Plot with PEtab
plot_cross_samples(importer.petab_problem.measurement_df,
                   simulation_df,
                   'pretraining',
                   output_prefix)
