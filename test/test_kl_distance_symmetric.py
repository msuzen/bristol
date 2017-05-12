import unittest
from bristol.ensembles import Circular
from bristol.spectral import Ergodicity
import numpy as np

class test_kl_distance_symmetric(unittest.TestCase):

      epsilon = 1e-9

      def test_kl_distance_symmetric_01(self):
          ergo     = Ergodicity()
          np.random.seed(1235)
          Nk       = np.random.random(100)
          Nk_minus = np.random.random(100)
          kl       = ergo.kl_distance_symmetric(Nk,Nk_minus)
          self.assertTrue(kl-91.808228136131163 < self.epsilon)
