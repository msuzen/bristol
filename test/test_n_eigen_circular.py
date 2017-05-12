#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:11:15 2017

@author: msuzen

%load_ext autoreload
%autoreload 2

"""

import unittest
from bristol.ensembles import Circular
import numpy as np

class test_n_eigen_circular(unittest.TestCase):

      epsilon = 1e-9

      def test_n_eigen_circular_01(self):
          mseed   = 2963416
          ce      = Circular()
          e_cue   = ce._n_eigen_circular(
                                         seed=mseed, 
                                         N=5,
                                         size=1,
                                         ensemble='CUE', 
                                         set_seed=True
                                        )  
          e_coe   = ce._n_eigen_circular(
                                         seed=mseed, 
                                         N=10,
                                         size=1,
                                         ensemble='COE', 
                                         set_seed=True
                                        )   
          e_cse   = ce._n_eigen_circular(
                                         seed=mseed, 
                                         N=15,
                                         size=1,
                                         ensemble='CSE', 
                                         set_seed=True
                                        )   
          n_cue   = np.imag(e_cue['c_eigen']).sum()
          n_coe   = np.imag(e_coe['c_eigen']).sum()
          n_cse   = np.imag(e_cse['c_eigen']).sum()
          self.assertTrue(n_cue-0.70246404091524939 < self.epsilon)
          self.assertTrue(n_coe-0.02388152067472389 < self.epsilon)
          self.assertTrue(np.abs(n_cse)< self.epsilon)
          
          
      def test_n_eigen_circular_02(self):
          mseed   = 2963416
          ce      = Circular()
          e_cue   = ce._n_eigen_circular(
                                         seed=mseed, 
                                         N=5,
                                         size=3,
                                         ensemble='CUE', 
                                         set_seed=True
                                        )
          e_coe   = ce._n_eigen_circular(
                                         seed=mseed, 
                                         N=10,
                                         size=3,
                                         ensemble='COE', 
                                         set_seed=True
                                        )   
          e_cse   = ce._n_eigen_circular(
                                         seed=mseed, 
                                         N=15,
                                         size=3,
                                         ensemble='CSE', 
                                         set_seed=True
                                        )   
          n_cue   = np.imag(e_cue['c_eigen']).sum()
          n_coe   = np.imag(e_coe['c_eigen']).sum()
          n_cse   = np.imag(e_cse['c_eigen']).sum()
          self.assertTrue(n_cue+2.1073921227457482 < self.epsilon)
          self.assertTrue(n_coe-0.0716445620241715 < self.epsilon)
          self.assertTrue(np.abs(n_cse) < self.epsilon)   
