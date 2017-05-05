import unittest
from bristol.ensembles import circular
import numpy as np

class test_gen_cue(unittest.TestCase):

      epsilon = 1e-9

      def test_gen_cue_01(self):
           N     = 8
           ce    = circular()
           mseed = 2963416
           Hcue0 = ce.gen_cue(8, seed=mseed, set_seed=True)
           Hcue1 = ce.gen_cue(8, seed=mseed, set_seed=True)    
           n0    =  float(np.imag(Hcue0[0,:].sum()))+0.8937685305710769
           n1    =  float(np.real(Hcue1[6,:].sum()))-0.1639869102814931
           self.assertTrue(n0 < self.epsilon)
           self.assertTrue(n1 < self.epsilon)
