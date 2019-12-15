import unittest
import numpy as np
from bristol import cPSE
import torchvision.models as models

class test_cPSE(unittest.TestCase):

      epsilon = 1e-9

      def test_dlayer_vgg11_01(self):
          netname = 'vgg11'
          pmodel = getattr(models, netname)(pretrained=True)
          d_layers, cpse = cPSE.cpse_measure(pmodel)
          delta0 = d_layers[0] - 620.8614145333568
          delta5 = d_layers[5] - 0.4511635231637898
          delta_c = cpse - 0.03596423728640884
          self.assertTrue(delta0 < self.epsilon)
          self.assertTrue(delta5 < self.epsilon)
          self.assertTrue(delta_c< self.epsilon)
