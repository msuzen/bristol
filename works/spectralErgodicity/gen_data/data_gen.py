#
# Spectral Ergodicity in Random Matrices
# (c) 2017
# 
# Author: M.Suzen
# 
# To measure timing
#' http://stackoverflow.com/questions/5849800/tic-toc-functions-analog-in-python
def tic():
    # Homemade version of matlab tic and toc functions
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print "Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds."
    else:
        print "Toc: start time not set"

#
# Generate Data for CUE, COE, CSE
# N= 64, 128, 256, 512, 768, 1024
# M=40
#   N matrix sizes, M number of matrices
#
# Output data files: 
#   data_cue.obj, data_coe.obj and data_cse.obj
#   are dictionaries of dictionary
#   keys are : ['N64', 'N128', 'N256', 'N512', 'N768', 'N1024']
#   values are dictionaries with keys: ['local_seeds', 'matrix_size', 'number_of_matrices', 'c_eigen']
#
import os
import pickle
from bristol.ensembles import Circular
ce = Circular()
# seed for 4 cpu cores (or chunks if not parallel)
seed_v   = [997123,1091645,1352,32718]
data_cue = {}
data_coe = {}
data_cse = {}
range_n  = [64, 128, 256, 512, 768, 1024]
for N in range_n:
    print("cue  N=", N)
    tic()
    data_cue['N'+str(N)] = ce.eigen_circular_ensemble(N,  cSize=10, nchunks=4, seeds=seed_v, ensemble='CUE')
    toc()
    print("coe  N=", N)
    tic()
    data_coe['N'+str(N)] = ce.eigen_circular_ensemble(N,  cSize=10, nchunks=4, seeds=seed_v, ensemble='COE')
    toc()
    print("cse  N=", N)
    tic()
    data_cse['N'+str(N)] = ce.eigen_circular_ensemble(N,  cSize=10, nchunks=4, seeds=seed_v, ensemble='CSE')
    toc()
# Write data files
fp = open('data_cue.obj', 'wb') 
pickle.dump(data_cue, fp)
fp.close()
fp = open('data_coe.obj', 'wb')
pickle.dump(data_coe, fp)
fp.close()
fp = open('data_cse.obj', 'wb') 
pickle.dump(data_cse, fp)
fp.close()
