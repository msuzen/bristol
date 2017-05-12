import unittest
from bristol.ensembles import Circular
import numpy as np

class test_gen_cse(unittest.TestCase):

      epsilon = 1e-9

      def test_gen_cse_01(self):
          N     = 8
          ce    = Circular()
          mseed = 2963416
          Hcse0 = ce.gen_cse(8, seed=mseed, set_seed=True)
          Hcse1 = ce.gen_cse(8, seed=mseed, set_seed=True)
          n0    = float(np.imag(Hcse0[0,:].sum()))-0.001106565421140888
          n1    = float(np.real(Hcse1[6,:].sum()))-0.021065228262225025
          self.assertTrue(n0 < self.epsilon)
          self.assertTrue(n1 < self.epsilon)

      def test_gen_cse_02(self):
          N      = 8
          ce     = Circular()
          mseed  = 2963416
          Hcse0  = ce.gen_cse(8, seed=mseed, set_seed=True, adir="upper")
          Hcse1  = ce.gen_cse(8, seed=mseed, set_seed=True, adir="upper")
          n0     = float(np.imag(Hcse0[0,:].sum()))-0.001106565421140888
          n1     = float(np.real(Hcse1[6,:].sum()))-0.021065228262225025
          self.assertTrue(n0 < self.epsilon)
          self.assertTrue(n1 < self.epsilon)
