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
    
class test_eigen_circular_ensemble(unittest.TestCase):

      epsilon = 1e-9

      def test_eigen_circular_ensemble_01(self):
          mseeds  = [2963416, 235124, 786134]
          ce      = Circular()
          e_cue   = ce.eigen_circular_ensemble(
                                               seeds=mseeds,
                                               N=5,
                                               nchunks=3,
                                               ensemble='CUE', 
                                               parallel=False
                                              )  
          e_coe   = ce.eigen_circular_ensemble(
                                               seeds=mseeds, 
                                               N=5,
                                               nchunks=3,
                                               ensemble='COE', 
                                               parallel=False
                                              )    
          e_cse   = ce.eigen_circular_ensemble(
                                               seeds=mseeds, 
                                               N=5,
                                               nchunks=3,
                                               ensemble='CSE', 
                                               parallel=False
                                              )
          e_cse2  = ce.eigen_circular_ensemble(
                                               seeds=mseeds, 
                                               N=5,
                                               nchunks=3,
                                               ensemble='CSE', 
                                               parallel=False,
                                               adir="upper"
                                              )
          n_cue   = np.imag(e_cue['c_eigen']).sum()
          n_coe   = np.imag(e_coe['c_eigen']).sum()
          n_cse   = np.imag(e_cse['c_eigen']).sum()
          n_cse2  = np.imag(e_cse2['c_eigen']).sum()
          self.assertTrue(n_cue-62.284496117511054 < self.epsilon)
          self.assertTrue(n_coe+21.810798433338746 < self.epsilon)
          self.assertTrue(np.abs(n_cse) < self.epsilon)
          self.assertTrue(np.abs(n_cse2) < self.epsilon)
          
          
      def test_eigen_circular_ensemble_02(self):
          mseeds  = [2963416, 235124, 786134]
          ce      = Circular()
          e_cue   = ce.eigen_circular_ensemble(
                                               seeds=mseeds,
                                               N=5,
                                               nchunks=3,
                                               ensemble='CUE', 
                                               parallel=True
                                              )  
          e_coe   = ce.eigen_circular_ensemble(
                                               seeds=mseeds, 
                                               N=5,
                                               nchunks=3,
                                               ensemble='COE', 
                                               parallel=True
                                              )    
          e_cse   = ce.eigen_circular_ensemble(
                                               seeds=mseeds, 
                                               N=5,
                                               nchunks=3,
                                               ensemble='CSE', 
                                               parallel=True
                                              )
          e_cse2  = ce.eigen_circular_ensemble(
                                               seeds=mseeds, 
                                               N=5,
                                               nchunks=3,
                                               ensemble='CSE', 
                                               parallel=True,
                                               adir="upper"
                                              )
          n_cue   = np.imag(e_cue['c_eigen']).sum()
          n_coe   = np.imag(e_coe['c_eigen']).sum()
          n_cse   = np.imag(e_cse['c_eigen']).sum()
          n_cse2  = np.imag(e_cse2['c_eigen']).sum()
          self.assertTrue(n_cue-62.284496117511054 < self.epsilon)
          self.assertTrue(n_coe+21.810798433338746 < self.epsilon)
          self.assertTrue(np.abs(n_cse)  < self.epsilon) 
          self.assertTrue(np.abs(n_cse2) < self.epsilon)
