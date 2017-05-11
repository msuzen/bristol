import unittest
from bristol.ensembles import Circular
import numpy as np

class test_unit_symplectic(unittest.TestCase):

      epsilon = 1e-9

      def test_unit_symplectic1(self):
           N   = 4
           ce  = Circular()
           u_l = ce.unit_symplectic(N) 
           u_u = ce.unit_symplectic(N, adir='upper')
           r_l = u_l[1,0] + u_l[3,2] + u_l[5,4] + u_l[7,6] + 4.0
           r_u = u_l[1,0] + u_l[3,2] + u_l[5,4] + u_l[7,6] - 4.0
           self.assertTrue(r_l < self.epsilon)
           self.assertTrue(r_u < self.epsilon)

      def test_unit_symplectic2(self):
           N   = 3 
           ce  = Circular()
           u_l = ce.unit_symplectic(N) 
           u_u = ce.unit_symplectic(N, adir='upper')
           self.assertTrue(np.sum(u_l+u_u) < self.epsilon)
