import unittest
from bristol.ensembles import Circular
from bristol.spectral import Ergodicity
import numpy as np     

class test_spectral_density(unittest.TestCase):

      epsilon = 1e-9

      def test_spectral_density_01(self):
          ce          = Circular()
          mseed       = [123,125,124]       
          Ns          = [5, 10, 15]
          cSize       = 2
          nChunks     = 3
          eigen_data5 = ce.eigen_circular_ensemble(
                                                   Ns[0], 
                                                   cSize=cSize, 
                                                   nchunks=nChunks, 
                                                   seeds=mseed, 
                                                   parallel=False
                                                  )
          eigen_data10 = ce.eigen_circular_ensemble(
                                                    Ns[1], 
                                                    cSize=cSize, 
                                                    nchunks=nChunks, 
                                                    seeds=mseed, 
                                                    parallel=False
                                                   )
          eigen_data15 = ce.eigen_circular_ensemble(
                                                    Ns[2], 
                                                    cSize=cSize, 
                                                    nchunks=nChunks, 
                                                    seeds=mseed, 
                                                    parallel=False
                                                   )
          ensemble_size = cSize*nChunks 
          eigen_data    = {
                           "N5":eigen_data5, 
                           "N10":eigen_data10,
                           "N15":eigen_data15
                          }
          ergo = Ergodicity()
          Dse  = ergo.approach_se(
                                  Ns=Ns,
                                  ensemble_size=ensemble_size,
                                  eigen_data=eigen_data
                                 )
          self.assertTrue(len(Dse) == 2)
          d0 = -12.287133235052062 
          d1 = -8.3998021593200445
          self.assertTrue(Dse[0]+d0 < self.epsilon)
          self.assertTrue(Dse[1]+d1 < self.epsilon)
