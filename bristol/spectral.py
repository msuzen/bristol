"""
   
     Ergodicity Module:
      

"""

import numpy as np


class Ergodicity:
    def __init__(self):
        pass

    def spectral_density(self, c_eigen, ensemble_size, N, delta_rad=0.2):
        """
             
           Compute spectral density
    
    
           Given set of eigenvalues e_i, compute histogram of 
           Angle(e_i) from -Pi to Pi at a given spacing.
    
           Input
           c_eigen        set of eigenvalues as an np array.
           ensemble_size  number of ensembles used, this is used to 
                          scale the resulting spectrum.
           delta_rad      spacing to use in getting the density, 
                          defaults to 0.2 radians. Used only for complex
    
           Output
           A density in two dimensional numpy array, with bin centres in the 
           first column and the density in the second column.
    
          Example:
              
            import numpy as np
            from bristol.ensembles import Circular
            ce            = Circular()
            mseed         = 2963416
            # 5, 10x10 matrices from CUE
            N             = 10
            ensemble_size = 5
            e_cue         = ce.eigen_circular(
                                              N=N,
                                              ensemble='CUE', 
                                              set_seed=True,
                                              seed=mseed
                                             )    
            from bristol.spectral import Ergodicity
            ergo     = Ergodicity()
            sdensity = ergo.spectral_density(e_cue, ensemble_size, N)
    
        """
        is_C = True
        try:
            sum_c = sum([np.abs(c.imag) for c in c_eigen])
            if (sum_c < 1e-9):
                is_C = False
        except:
            pass
        if (is_C):
            b_ks = np.arange(-np.pi, np.pi, delta_rad)  # bin edges
            b_ks_centres = b_ks[1:] - delta_rad / 2.0  # bin centres
            rho_ensemble = np.histogram(np.angle(c_eigen), bins=b_ks)
            den = np.column_stack(
                (b_ks_centres, rho_ensemble[0] / float(ensemble_size)))
        if (not is_C):
            hist_v, bin_edge = np.histogram(c_eigen)
            bin_centre = bin_edge[:-1] + (bin_edge[1] - bin_edge[0]) / 2.0
            den = np.column_stack((bin_centre, hist_v / float(ensemble_size)))

        return den

    def thirumalai_mountain(self,
                            c_eigen_ensemble,
                            ensemble_size,
                            N,
                            delta_rad=0.2):
        """
         
         Compute TM metric for given set of eigenvalues e_i.
    
    
         Input
          c_eigen_ensemble : set of eigenvalues as a 1D np array
          ensemble_size    : number of ensembles used, this is used to scale the resulting spectrum.
          N                : matrix size used to generate eigenvalues.
          delta_rad        : spacing to use in getting the density, defaults to 0.2 radians.
    
         Output
          Omega, TM metric 1d numpy array.
          
          References:
              Spectral Ergodicity in Deep Learning Architectures 
              via Surrogate Random Matrices, 
              Mehmet Suezen, Cornelius Weber, Joan J. Cerd{`a}, 
              arXiv:1704.08693
          
          Example: 
            # On Ipython
            %load_ext autoreload
            %autoreload 2
         
            import numpy as np
            from bristol.ensembles import Circular
            ce            = Circular()
            mseed         = 2963416
            # 5, 10x10 matrices from CUE
            N             = 10
            cSize         = 2
            nchunks       = 5
            ensemble_size = cSize*nchunks
            eseeds        = [978712, 34687, 43124, 67831, 1234]
            e_cue         = ce.eigen_circular_ensemble(
                                                       N=N,
                                                       ensemble='CUE', 
                                                       seeds=eseeds,
                                                       cSize=cSize,
                                                       nchunks=nchunks
                                                      )    
            c_eigen_ensemble = e_cue['c_eigen']
            from bristol.spectral import Ergodicity
            ergo     = Ergodicity()
            tm       = ergo.thirumalai_mountain(
                                                c_eigen_ensemble, 
                                                ensemble_size, 
                                                N
                                               )
    
        """
        sden_ensemble = self.spectral_density(c_eigen_ensemble, ensemble_size,
                                              N, delta_rad)
        omega = np.zeros(sden_ensemble.shape[0])
        for i in range(ensemble_size):
            ix = np.arange(0, N) + N * i
            sden_spec = self.spectral_density(c_eigen_ensemble[ix], 1, N,
                                              delta_rad)
            omega = np.power(
                (sden_spec[:, 1] - sden_ensemble[:, 1]), 2) + omega
        return omega / ensemble_size / N

    def kl_distance_symmetric(self, Nk, Nk_minus, shift=1e-9):
        """
    
        Compute Kullback-Leibler Divergence in two directions. 
    
    
        Input:
         Nk, Nk_minus     Two 1D numpy arrays 
         shift            Epsilon shift distribution upwards, to avoid for zeros, defaults to 1e-9. 
    
        Output:
          Distance from KL divergence, floating number.
          
        Example:
            # On Ipython
            %load_ext autoreload
            %autoreload 2
            import numpy as np
            from bristol.spectral import Ergodicity
            ergo     = Ergodicity()
            np.random.seed(1235)
            Nk       = np.random.random(100)
            Nk_minus = np.random.random(100)
            ergo.kl_distance_symmetric(Nk,Nk_minus)
    
        """
        KL_k = np.sum(Nk * np.log2((Nk + shift) / (Nk_minus + shift)))
        KL_k_minus = np.sum(Nk_minus * np.log2(
            (Nk_minus + shift) / (Nk + shift)))
        return ((KL_k + KL_k_minus))

    def approach_se(self, Ns, ensemble_size, eigen_data, delta_rad=0.2):
        """
     
         Approach to spectral ergodicity Consecutive 
         
         Parameters
         ----------
         Ns            : Matrix sizes used in a list
         ensemble_size : Number of matrices used
         eigen_data    : Dictionary with key entries from Ns 
                         and values are outputs from 
                         'eigen_circular_ensemble', see example
                         
         References:
         
         Spectral Ergodicity in Deep Learning Architectures 
         via Surrogate Random Matrices, 
         Mehmet Suezen, Cornelius Weber, Joan J. Cerd{`a}, 
         arXiv:1704.08693 
         
         Example:
         
          import numpy as np     
          from bristol.ensembles import Circular
          ce         = Circular()
          mseed      = [123,125,124]       
          Ns         = [5, 10, 15]
          cSize      = 2
          nChunks    = 3
          eigen_data5 = ce.eigen_circular_ensemble(
                                                   Ns[0], 
                                                   cSize=cSize, 
                                                   nchunks=nChunks, 
                                                   seeds=mseed, 
                                                   parallel=False
                                                  )
         eigen_data10 = ce.eigen_circular_ensemble(
                                                   Ns[1], 
                                                   cSize=cSize, 
                                                   nchunks=nChunks, 
                                                   seeds=mseed, 
                                                   parallel=False
                                                  )
         eigen_data15 = ce.eigen_circular_ensemble(
                                                   Ns[2], 
                                                   cSize=cSize, 
                                                   nchunks=nChunks, 
                                                   seeds=mseed, 
                                                   parallel=False
                                                  )
         ensemble_size = cSize*nChunks 
         eigen_data = {
                       "N5":eigen_data5, 
                       "N10":eigen_data10,
                       "N15":eigen_data15
                      }
         from bristol.spectral import Ergodicity
         ergo = Ergodicity()
         Dse  = ergo.approach_se(
                                 Ns=Ns,
                                 ensemble_size=ensemble_size, 
                                 eigen_data=eigen_data 
                                )
        
        """
        Dse = []
        for i in range(1, len(Ns)):
            c_eigen_ensemble = eigen_data["N" + str(Ns[i])]['c_eigen']
            Nk = self.thirumalai_mountain(c_eigen_ensemble, ensemble_size,
                                          Ns[i], delta_rad)
            c_eigen = eigen_data['N' +
                                 str(Ns[i - 1])]['c_eigen']  # All eigenvalues
            Nk_minus = self.thirumalai_mountain(c_eigen, ensemble_size,
                                                Ns[i - 1], delta_rad)
            Dse.append(self.kl_distance_symmetric(Nk, Nk_minus))
        return (Dse)
