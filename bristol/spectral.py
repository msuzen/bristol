"""
   
     Ergodicity Module:
      

     Author: M. Suzen

"""
import numpy as np

class ergodicity:

    def __init__(self):
        print("histogram")    

    def spectral_density(
                         c_eigen, 
                         ensemble_size, 
                         N, 
                         delta_rad=0.2
                        ):
        """
             
           Compute spectral density
    
           Author: M.Suzen
    
           Given set of eigenvalues e_i, compute histogram of 
           Angle(e_i) from -Pi to Pi at a given spacing.
    
           Input
           c_eigen        set of eigenvalues as an np array.
           ensemble_size  number of ensembles used, this is used to 
                          scale the resulting spectrum.
           delta_rad      spacing to use in getting the density, 
                          defaults to 0.2 radians.
    
           Output
           A density in two dimensional numpy array, with bin centres in the 
           first column and the density in the second column.
    
          Example: 
            import numpy as np
            from bristol.ensembles import circular
            ce            = circular()
            mseed         = 2963416
            # 5, 10x10 matrices from CUE
            N             = 10
            ensemble_size = 5
            e_cue         = ce._n_eigen_circular(
                                                 seed=mseed, 
                                                 N=N,
                                                 size=ensemble_size,
                                                 ensemble='CUE', 
                                                 set_seed=True
                                                )    
            c_eigen  = e_cue['c_eigen']
            from bristol.spectral import ergodicity
            ergo     = ergodicity()
            sdensity = ergo.spectral_density(c_eigen, ensemble_size, N)
    
        """
        import numpy as np
        b_ks         = np.arange(-np.pi,np.pi, delta_rad) # bin edges
        b_ks_centres = b_ks[1:]-delta_rad/2.0# bin centres
        rho_ensemble = np.histogram(np.angle(c_eigen), bins=b_ks)
        return(np.column_stack((b_ks_centres, rho_ensemble[0]/float(ensemble_size))))



