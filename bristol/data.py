"""
   
     Data Generation Module
     

"""
import numpy as np
from bristol.ensembles import Circular

class Generate: 

      def __init_(self):
          pass

      def spectra_ce(
                     range_N=[64, 128],
                     cSize=5,
                     nchunks=2,
                     seeds=[997123, 1091645],
                     ensemble='all',
                     parallel=False,
                    ):
          """

          Generate eigenvalues of matrices of different size
          drawn from a circular ensemble.


           params:
           range_N   set of Size of the rectangular matrix, NxN.
           cSize     Number of random matrices to generate in a chunk.
           nchunks   number of cSize chunks.
           ensemble  One of the circular ensemble 
                     'CUE', 'COE', 'CSE', defaults to 'all'
           seeds     List of integer to use in random seed 
                     in every chunk.
           parallel  Run in multicore, number of cores as nchunks, 
                     defaults to False

          output:
          Dictionary of dictionaries. 
          * Highest level keys for ensemble `CUE`, `COE` or `CSE`.
          * Then, dictionary with keys describing size, such as 'N16. 
          * Values will be an another dictionary
            with keys `local_seed` integers for seeds 
            used in the chunk, `c_eigen` 
            numpy array of eigenvalues, `N` matrix size, 
            `M` number of matrices used to generate `c_eigen`. Note
            that `c_eigen` will be length NxM.
 
            Example:

          """
          ce      = Circular()
          data_ce = {
                     'CUE':{},
                     'COE':{},
                     'CSE':{}
                    }
          for N in range_N: 
              if(ensemble in ['CUE','all']):
                e_dict = ce.eigen_circular_ensemble(
                                                    N=N,
                                                    cSize=cSize,
                                                    nchunks=nchunks,
                                                    ensemble='CUE',
                                                    seeds=seeds,
                                                    parallel=parallel
                                                   )
                data_ce['CUE']['N'+str(N)] = e_dict
              if(ensemble in ['COE','all']):
                e_dict = ce.eigen_circular_ensemble(
                                                    N=N,
                                                    cSize=cSize,
                                                    nchunks=nchunks,
                                                    ensemble='COE',
                                                    seeds=seeds,
                                                    parallel=parallel
                                                   )
                data_ce['COE']['N'+str(N)] = e_dict
              if(ensemble in ['CSE','all']):
                e_dict = ce.eigen_circular_ensemble(
                                                    N=N,
                                                    cSize=cSize,
                                                    nchunks=nchunks,
                                                    ensemble='CSE',
                                                    seeds=seeds,
                                                    parallel=parallel
                                                   )
                data_ce['COE']['N'+str(N)] = e_dict
          return data_ce
