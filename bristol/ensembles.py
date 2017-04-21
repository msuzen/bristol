"""
   
     Generating Circular Ensembles

     Author: M. Suzen

"""

import numpy as np
import multiprocessing as mp
from builtins import range
from functools import partial

def _n_eigen_circular2(seed, N, size, ensemble='CUE', 
                       adir='lower', set_seed=False):
        """
        This is a wrapper for _n_eigen_circular, so `seed` comes
        as first argument.

        """
        ce = circular()
        return(ce._n_eigen_circular(N, size, ensemble=ensemble, 
                     adir='lower', set_seed=set_seed, seed=seed))

class circular:

    def __init__(self):
        print("")
 
    def unit_anti(self,N=2, adir='lower'):
        """
        
        Generate antisymmetric unit matrix of size NxN.
        
        Author: M.Suzen
        
        params:
        N      Size of rectangular NxN ndarray, defaults to 2.
        adir  Direction of Antisymmetry, 'upper' or 'lower' 
          triangular,  defaults to 'lower'.
        
        output:
        z      Antisymmetric unit matrix, NxN ndarray
        
        Example:
        from bristol.ensembles import circular
        ce = circular()
        z = ce.unit_anti()         # Generates 2x2, lower anti-symmetric.
        z = ce.unit_anti(adir='upper')  # upper anti-symmetric
        
        """
        z = np.ones([N, N])
        if(adir == 'upper'):
           upper_ix = np.triu_indices(N)
           z[upper_ix]= -1*z[upper_ix]
        if(adir == 'lower'):
           lower_ix = np.tril_indices(N)
           z[lower_ix]= -1*z[lower_ix]    
           np.fill_diagonal(z, 0)
        return(z)

    def unit_symplectic(self, N, adir='lower'):
        """
        
        Generate unit symplectic matrix 2Nx2N.
        
        Author: M.Suzen
        
        params:
        N      Base size of rectangular array 2Nx2N ndarray.
        adir  Direction of Antisymmetry, 'upper' or 'lower' triangular,  defaults to 'lower'.
        
        output:
        2Nx2N unit symplectic matrix
        
        Example:
        from bristol.ensembles import circular
        ce = circular()
        z  = ce.unit_symplectic(4)         # Generates 8x8 unit symplectic, upper anti-symmetric.
        z  = ce.unit_symplectic(4,adir='upper')  # upper anti-symmetric
        
        """
        z = self.unit_anti(2, adir=adir)
        return(np.kron(np.eye(N), z).astype(int)) 


    def gen_cue(self, N, set_seed=False, seed=42391):
        """
        
        Generate random matrix Circular Unitary Ensemble (CUE)

        Author: M.Suzen
        
        params:
        N          Size of rectangular array NxN.
        set_seed  Option to pass seed, defaults to False, no seed set.
        seed      If set_seed is set, seed value will be used, defaults to 42391.

        output:
        NxN matrix in  Circular Unitary Ensemble (CUE)
       
        References:
        * M V Berry and Pragya Shukla, New Journal of Physics 15 (2013) 013026 

        Example:
        
        Hcue = gen_cue(10)
        
        """
        if(set_seed):
           np.random.seed(seed)
        f      = lambda n : map(lambda x: np.random.normal(), range(n))
        f_uni = lambda n : map(lambda x: np.random.uniform(2*np.pi), range(n))
        G      = map(lambda theta: np.cos(theta)+np.sin(theta)*1j, f_uni(N))
        A       = np.random.random((N,N))
        B       = np.random.random((N,N))
        H      = 0.5 * (A+B*1j+np.transpose(A)-np.transpose(B)*1j)
        E, U  = np.linalg.eig(H)
        Hcue  = G * U
        return(Hcue)

    def gen_coe(self, N, set_seed=False, seed=42391):
       """
        
        Generate random matrix Circular Orthogonal Ensemble (COE)

        Author: M.Suzen
        
        params:
        N          Size of rectangular array NxN.
        set_seed  Option to pass seed, defaults to False, no seed set.
        seed      If set_seed is set, seed value will be used, defaults to 42391.

        output:
        NxN matrix in  Circular Orthogonal Ensemble (COE)
       
        References:
        * M V Berry and Pragya Shukla, New Journal of Physics 15 (2013) 013026 

        Example:
        
        Hcoe = gen_coe(10)
        
       """
       Hcue = self.gen_cue(N,set_seed,seed)
       return(Hcue.transpose()*Hcue)

    def gen_cse(self, N, set_seed=False, seed=42391, adir='lower'):
       """
        
        Generate random matrix Circular Symplectic Ensemble (CSE)

        Author: M.Suzen
        
        params:
        N          Size of rectangular array NxN.
        set_seed  Option to pass seed, defaults to False, no seed set.
        seed      If set_seed is set, seed value will be used, defaults to 42391.
        adir      Direction of Antisymmetry, 'upper' or 'lower' triangular,  defaults to 'lower'.

        output:
        NxN matrix in  Circular Symlectic Ensemble (CSE)
       
        References:
        * M V Berry and Pragya Shukla, New Journal of Physics 15 (2013) 013026 

        Example:
        
        Hcoe = gen_coe(10)
        
       """
       Z    = self.unit_symplectic(N, adir=adir)
       Hcue = self.gen_cue(2*N,set_seed,seed)
       return((Z*Hcue.transpose()*Z)*Hcue)

    def eigen_circular(self, N, ensemble='CUE', set_seed=False, 
               seed=42391, adir='lower'):
        """

           Generate eigenvalues of a matrix that is a realization from circular 
           random matrix ensemble.
          
           Author: M.Suzen

           params:
           N     Size of the square random matrix, NxN.
           ensemble  One of the Circular ensemble 'CUE', 'COE', 'CSE'
           set_seed  Option to pass seed, defaults to False, no seed set.
           seed     If set_seed is set, seed value will be used, defaults to 42391.
           adir     Direction of Antisymmetry, 'upper' or 'lower' triangular,  defaults to 'lower'.
           
           output:
           e  eigenvalues as numpy array
         

           Example:
           e_cue_5    = eigen(5)           # eigenvalues of 5x5 matrix from CUE 
           e_cse_5    = eigen(5,ensemble='cse') #  eigenvalues of 5x5 matrix from CSE

        """
        if(not ensemble in ['CUE', 'COE', 'CSE']):
            raise Exception("Circular ensemble of \
                     CUE, COE or CSE must \
                     be selected.")
        if(ensemble == 'CUE'):
            H     = self.gen_cue(N,seed=seed,set_seed=set_seed)
        if(ensemble == 'COE'):
            H     = self.gen_coe(N,seed=seed,set_seed=set_seed)
        if(ensemble == 'CSE'):
            H     = self.gen_cse(N,seed=seed,set_seed=set_seed,adir=adir)
        e, u = np.linalg.eig(H)
        return(e)

    def _n_eigen_circular(self, N, size, ensemble='CUE', 
                  adir='lower', set_seed=False, seed=9876):
        """

        Compute eigenvalues of a given circular ensemble, 
        by generating `size` number of matrices. A choice
        of seed is generated if set_seed is False.

        params:
        N           Size of the rectangular matrix, NxN.
        size       Number of random matrices to generate.
        ensemble   One of the circular ensemble 'CUE', 'COE', 'CSE'
        set_seed   Option to pass seed, defaults to False, no seed set.
        seed       If set_seed is set, seed value will be used, defaults to 9876.
        adir       Direction of Antisymmetry, 'upper' or 'lower' triangular,  defaults to 'lower'.

        output:
        Dictionary with keys `local_seed` an integer, and numpy array of eigenvalues
        for each matrix in key `c_eigen`.
       
        Example:
        res = _n_eigen_circular(10, 10) 

        """
        local_seed = np.random.choice(1000000, 1)
        np.random.seed(local_seed)
        if(set_seed):
           np.random.seed(seed)
           local_seed = seed
        c_eigen = np.empty(0)
        for i in range(size):
           e = self.eigen_circular(N, ensemble=ensemble, set_seed=False, seed=42391, adir=adir)
           c_eigen = np.append(c_eigen, e)
        return({'local_seed':local_seed, 'c_eigen':c_eigen})


    def eigen_circular_ensemble(self, N, cSize=100, nchunks=4, 
                    ensemble='CUE', adir='lower', 
                    seeds=list(), parallel=True):
        """
         
        Compute eigenvalues of given circular ensemble, in parallel or serial.
        

        Author: M.Suzen

        params:
        N           Size of the rectangular matrix, NxN.
        cSize      Number of random matrices to generate in a chunk.
        nchunks    number of cSize chunks.
        ensemble   One of the circular ensemble 'CUE', 'COE', 'CSE', defaults to 'CUE'
        adir       Direction of Antisymmetry, 'upper' or 'lower' triangular,  defaults to 'lower'.
        seeds      List of integer to use in random seed in every chunk.
        parallel   Run in multicore, number of cores as nchunks, defaults to True

        output:
        Dictionary with keys `local_seed` an integer, and numpy array of eigenvalues
        for each matrix in key `c_eigen`.

        Example:

        Parallel and serial runs should produce the same result with the
        same random seed
        
        rr_serial = rm.eigen_circular_ensemble(100, cSize=4, nchunks=4, 
                           seeds=[123,125,124,122], 
                           parallel=False)
        rr_paralel = rm.eigen_circular_ensemble(100, cSize=4, nchunks=4, 
                            seeds=[123,125,124,122])
        all(rr_serial['c_eigen'] == rr_paralel['c_eigen']) 


        """
        if(len(seeds) != nchunks):
          raise Exception("Seeds vector must be provided for each chunk")
        if(not parallel):
         local_seeds = []
         c_eigen     = np.empty(0)
         for i in range(nchunks):
             res = {}
             res = self._n_eigen_circular(N=N, size=cSize, ensemble=ensemble, 
                         adir='lower', set_seed=True, 
                         seed=seeds[i])
             local_seeds.append(res['local_seed'])
             c_eigen = np.append(c_eigen, res['c_eigen'])
         return({'local_seeds':local_seeds, 'c_eigen':c_eigen})
        if(parallel):
          wrap_f      = partial(_n_eigen_circular2, N=N, 
                                size=cSize, ensemble=ensemble,
                                adir='lower', set_seed=True) 
          pool        = mp.Pool(processes=nchunks)
          rrp         = pool.map(wrap_f, seeds)
          pool.close()
          pool.join()
          local_seeds = []
          c_eigen      = np.empty(0)
          for j in range(nchunks):
             local_seeds.append(rrp[j]['local_seed'])
             c_eigen = np.append(c_eigen, rrp[j]['c_eigen'])
          return({'local_seeds':local_seeds, 'c_eigen':c_eigen, 
              'matrix_size':N, 'number_of_matrices':nchunks*cSize})

