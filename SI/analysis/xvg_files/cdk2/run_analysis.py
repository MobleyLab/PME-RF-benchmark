import sys, os
from pmx.workflow import pmxworkflow, \
workflow1_parameterize_ligands, \
workflow2_make_perturbations, \
workflow3_solvate, \
workflow4_write_scripts, \
workflow5_submit_simulations, \
workflow6_check_simulations, \
workflow7_analyse
pwf = pmxworkflow.pmxvariables(target='cdk2',
                              forcefield='openff-1.0.0.offxml',
                              path='./RF_GPU/',
                              replicates=[1,2,3],
                              verbose=True)

workflow7_analyse.analyzeSimulations(pwf)

