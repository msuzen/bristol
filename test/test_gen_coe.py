import unittest
from bristol.ensembles import Circular
import numpy as np

class test_gen_coe(unittest.TestCase):

      epsilon = 1e-9

      def test_gen_coe_01(self):
          ce    = Circular()
          mseed = 2963416
          Hcoe0 = ce.gen_coe(8, seed=mseed, set_seed=True)
          Hcoe1 = ce.gen_coe(8, seed=mseed, set_seed=True)
          n0    =  float(np.imag(Hcoe0[0,:].sum()))-0.2712959924904533
          n1    =  float(np.real(Hcoe1[6,:].sum()))+0.4453698237585775
          self.assertTrue(n0 < self.epsilon)
          self.assertTrue(n1 < self.epsilon)
