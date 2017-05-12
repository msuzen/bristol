import unittest
from bristol.ensembles import Circular

class test_unit_anti(unittest.TestCase):

      epsilon = 1e-9

      def test_unit_anti1(self):
           ce  = Circular()
           z_l = ce.unit_anti() 
           z_u = ce.unit_anti(adir='upper')
           self.assertTrue((z_l[1,0] + z_l[0,1]) < self.epsilon)
           self.assertTrue((z_l[1,0] + 1.0) < self.epsilon)
           self.assertTrue((z_u[0,1] + z_u[0,1]) < self.epsilon)
           self.assertTrue((z_u[0,1] + 1.0) < self.epsilon)

      def test_unit_anti2(self):
           N   = 4
           ce  = Circular()
           z_l = ce.unit_anti(N)
           z_u = ce.unit_anti(N, adir='upper')
           self.assertTrue(z_l[3,].sum()+3.0 < self.epsilon)
           self.assertTrue(z_u[3,].sum()-3.0 < self.epsilon)
