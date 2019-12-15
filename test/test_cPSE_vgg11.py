import unittest
import numpy as np
from bristol import cPSE
import torchvision.models as models

class test_cPSE(unittest.TestCase):

      epsilon = 1e-9

      def test_dlayer_vgg11_01(self):
          netname = 'vgg11'
          pmodel = getattr(models, netname)(pretrained=True)
          A_t = cPSE.get_layer_matrix_set(pmodel)
          eset = cPSE.get_eigenvals_layer_matrix_set(A_t[0])
          eset_per = cPSE.eigenvals_set_to_periodic(eset)
          d_layers = cPSE.d_layers_pse(eset_per)
          delta0 = d_layers[0] - 620.8614145333568
          delta5 = d_layers[5] - 0.4511635231637898
          print("delta0=",delta0)
          print("delta5=",delta5)
          self.assertTrue(delta0 < self.epsilon)
          self.assertTrue(delta5 < self.epsilon)
