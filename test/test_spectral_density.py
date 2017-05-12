import unittest
from bristol.ensembles import Circular
from bristol.spectral import Ergodicity

class test_spectral_density(unittest.TestCase):

      epsilon = 1e-9

      def test_spectral_density_01(self):
           N        = 10 
           ce       = Circular()
           mseed    = 2963416
           e_cue    = ce.eigen_circular(
                                        N=N,
                                        ensemble='CUE', 
                                        set_seed=True,
                                        seed=mseed
                                       )
           ergo     = Ergodicity()
           sdensity = ergo.spectral_density(e_cue, ensemble_size=1, N=N)
           self.assertTrue(sdensity.shape == (31,2))
           self.assertTrue(sdensity[5:15,1].sum()-4.0 < self.epsilon)
           self.assertTrue(sdensity[15:27,0].sum()-12.700888156922527 < self.epsilon)
