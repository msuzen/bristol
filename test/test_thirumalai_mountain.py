import unittest
from bristol.ensembles import Circular
from bristol.spectral import Ergodicity
import numpy as np

class test_thirumalai_mountain(unittest.TestCase):

      epsilon = 1e-9

      def test_test_thirumalai_mountain_01(self):
          ce            = Circular()
          mseed         = 2963416
          # 5, 10x10 matrices from CUE
          N             = 10
          cSize         = 2
          nchunks       = 5
          ensemble_size = cSize*nchunks
          eseeds        = [978712, 34687, 43124, 67831, 1234]
          e_cue         = ce.eigen_circular_ensemble(
                                                     N=N,
                                                     ensemble='CUE', 
                                                     seeds=eseeds,
                                                     cSize=cSize,
                                                     nchunks=nchunks
                                                    )    
          c_eigen_ensemble = e_cue['c_eigen']
          ergo     = Ergodicity()
          tm       = ergo.thirumalai_mountain(
                                              c_eigen_ensemble, 
                                              ensemble_size, 
                                              N
                                             )
          self.assertTrue(tm.shape == (31,))
          self.assertTrue(tm[6:11].sum()-0.104 < self.epsilon)
