import unittest
from bristol.ensembles import Circular
import numpy as np

class test_gen_coe(unittest.TestCase):

      epsilon = 1e-9

      def test_gen_coe_01(self):
          N     = 8
          ce    = Circular()
          mseed = 2963416
          Hcoe0 = ce.gen_coe(8, seed=mseed, set_seed=True)
          Hcoe1 = ce.gen_coe(8, seed=mseed, set_seed=True)
          n0    =  float(np.imag(Hcoe0[0,:].sum()))-0.17970248404618488
          n1    =  float(np.real(Hcoe1[6,:].sum()))+0.31684016971120316
          self.assertTrue(n0 < self.epsilon)
          self.assertTrue(n1 < self.epsilon)
