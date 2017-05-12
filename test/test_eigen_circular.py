import unittest
from bristol.ensembles import Circular
import numpy as np

class test_eigen_circular(unittest.TestCase):

      epsilon = 1e-9

      def test_eigen_circular_01(self):
          ce      = Circular()
          mseed   = 2963416
          e_cue   = ce.eigen_circular(5,  ensemble='CUE', set_seed=True, seed=mseed)  
          e_coe   = ce.eigen_circular(10, ensemble='COE', set_seed=True, seed=mseed)  
          e_cse   = ce.eigen_circular(15, ensemble='CSE', set_seed=True, seed=mseed)  
          n_cue   = np.imag(e_cue).sum()
          n_coe   = np.imag(e_coe).sum()
          n_cse   = np.imag(e_cse).sum()
          self.assertTrue(n_cue+0.702464040915249 < self.epsilon)
          self.assertTrue(n_coe-0.023881520674723 < self.epsilon)
          self.assertTrue(np.abs(n_cse) < self.epsilon)
