"""
   
     Generating Circular Ensembles


"""

import numpy as np
import multiprocessing as mp
from builtins import map
from functools import partial

def _n_eigen_circular2(seed, N, size, ensemble='CUE',
                       adir='lower', set_seed=False):
        """
        This is a wrapper for _n_eigen_circular, so `seed` comes
        as first argument.
        

        """
        ce = Circular()
        return(ce._n_eigen_circular(N, size, ensemble=ensemble,
                     adir='lower', set_seed=set_seed, seed=seed))


class Circular:

    def __init__(self):
       pass

    def unit_anti(self, N=2, adir='lower'):
        """
        
        Generate antisymmetric unit matrix of size NxN.
        
        
        params:
        N      Size of rectangular NxN ndarray, defaults to 2.
        adir  Direction of Antisymmetry, 'upper' or 'lower' 
          triangular,  defaults to 'lower'.
        
        output:
        z      Antisymmetric unit matrix, NxN ndarray
        
        Example:
        from bristol.ensembles import Circular
        ce = Circular()
        z = ce.unit_anti()         # Generates 2x2, lower anti-symmetric.
        z = ce.unit_anti(adir='upper')  # upper anti-symmetric
        
        """
        z = np.ones([N, N])
        if adir == 'upper':
            upper_ix = np.triu_indices(N)
            z[upper_ix] = -1*z[upper_ix]
            np.fill_diagonal(z, 0)
        if adir == 'lower':
            lower_ix = np.tril_indices(N)
            z[lower_ix]= -1*z[lower_ix]
            np.fill_diagonal(z, 0)
        return z

    def unit_symplectic(self, N, adir='lower'):
        """
        
        Generate unit symplectic matrix 2Nx2N.
        
        
        params:
        N      Base size of rectangular array 2Nx2N ndarray.
        adir  Direction of Antisymmetry, 'upper' or 'lower' triangular,  defaults to 'lower'.
        
        output:
        2Nx2N unit symplectic matrix
        
        Example:
        from bristol.ensembles import Circular
        ce = Circular()
        z  = ce.unit_symplectic(4)         # Generates 8x8 unit symplectic, upper anti-symmetric.
        z  = ce.unit_symplectic(4,adir='upper')  # upper anti-symmetric
        
        """
        z = self.unit_anti(2, adir=adir)
        return np.kron(np.eye(N), z).astype(int)

    def gen_cue(self, N, set_seed=False, seed=42391):
        """
        
        Generate random matrix Circular Unitary Ensemble (CUE)

        Review/reporter: C. Garbers
        
        params:
        N          Size of rectangular array NxN.
        set_seed  Option to pass seed, defaults to False, no seed set.
        seed      If set_seed is set, seed value will be used, defaults to 42391.

        output:
        NxN matrix in  Circular Unitary Ensemble (CUE)
       
        References:
        * M V Berry and Pragya Shukla, New Journal of Physics 15 (2013) 013026 

        Example:
         
        from bristol.ensembles import Circular
        ce     = Circular()
        mseed  = 2963416
        Hcue0  = ce.gen_cue(8, seed=mseed, set_seed=True)
        Hcue1  = ce.gen_cue(8, seed=mseed, set_seed=True)    
        n0     = float(np.imag(Hcue0[0,:].sum()))
        n1     = float(np.real(Hcue1[6,:].sum()))
        n0, n1

                   
        """
        if set_seed:
            np.random.seed(seed)
        f_uni   = lambda n: list(np.random.uniform(0, np.pi *2, n))
        G       = list(map(lambda theta: np.cos(theta)+np.sin(theta)*1j, f_uni(N)))
        A       = np.random.random((N, N))
        B       = np.random.random((N, N))
        H       = 0.5 * (A+B*1j+np.transpose(A)-np.transpose(B)*1j)
        E, U    = np.linalg.eig(H)
        Hcue    = G * U
        return Hcue

    def gen_coe(self, N, set_seed=False, seed=42391):
       """

        Generate random matrix Circular Orthogonal Ensemble (COE)


        params:
        N          Size of rectangular array NxN.
        set_seed  Option to pass seed, defaults to False, no seed set.
        seed      If set_seed is set, seed value will be used, defaults to 42391.

        output:
        NxN matrix in  Circular Orthogonal Ensemble (COE)

        References:
        * M V Berry and Pragya Shukla, New Journal of Physics 15 (2013) 013026

        Example:


        from bristol.ensembles import Circular
        ce     = Circular()
        mseed  = 2963416
        Hcoe0  = ce.gen_coe(8, seed=mseed, set_seed=True)
        Hcoe1  = ce.gen_coe(8, seed=mseed, set_seed=True)
        n0     = float(np.imag(Hcoe0[0,:].sum()))
        n1     = float(np.real(Hcoe1[6,:].sum()))
        n0, n1

       """
       Hcue = self.gen_cue(N,set_seed,seed)
       return Hcue.transpose()*Hcue

    def gen_cse(self, N, set_seed=False, seed=42391, adir='lower'):
       """

        Generate random matrix Circular Symplectic Ensemble (CSE)


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

        from bristol.ensembles import Circular
        ce     = Circular()
        mseed  = 2963416
        Hcse0  = ce.gen_cse(8, seed=mseed, set_seed=True)
        Hcse1  = ce.gen_cse(8, seed=mseed, set_seed=True)
        n0     = float(np.imag(Hcse0[0,:].sum()))
        n1     = float(np.real(Hcse1[6,:].sum()))
        n0, n1

        mseed  = 2963416
        Hcse0  = ce.gen_cse(8, seed=mseed, set_seed=True, adir="upper")
        Hcse1  = ce.gen_cse(8, seed=mseed, set_seed=True, adir="upper")
        n0     = float(np.imag(Hcse0[0,:].sum()))
        n1     = float(np.real(Hcse1[6,:].sum()))
        n0, n1

       """
       Z    = self.unit_symplectic(N, adir=adir)
       Hcue = self.gen_cue(2*N,set_seed,seed)
       return (Z*Hcue.transpose()*Z)*Hcue

    def eigen_circular(self, N, ensemble='CUE', set_seed=False,
                       seed=42391, adir='lower'):
        """

           Generate eigenvalues of a matrix that is a realization from circular 
           random matrix ensemble.
          

           params:
           N     Size of the square random matrix, NxN.
           ensemble  One of the Circular ensemble 'CUE', 'COE', 'CSE'
           set_seed  Option to pass seed, defaults to False, no seed set.
           seed     If set_seed is set, seed value will be used, defaults to 42391.
           adir     Direction of Antisymmetry, 'upper' or 'lower' triangular,  defaults to 'lower'.
           
           output:
           e  eigenvalues as numpy array
         

           Example:
           from bristol.ensembles import Circular
           ce      = Circular()
           mseed   = 2963416    
           e_cue   = ce.eigen_circular(5,  ensemble='CUE', set_seed=True, seed=mseed)
           e_coe   = ce.eigen_circular(10, ensemble='COE', set_seed=True, seed=mseed)
           e_cse   = ce.eigen_circular(15, ensemble='COE', set_seed=True, seed=mseed)
           n_cue   = np.imag(e_cue).sum()
           n_coe   = np.imag(e_coe).sum()
           n_cse   = np.imag(e_cse).sum() 

        """
        if(not ensemble in ['CUE', 'COE', 'CSE']):
            raise Exception("Circular ensemble of \
                     CUE, COE or CSE must \
                     be selected.")
        if ensemble == 'CUE':
            H     = self.gen_cue(N,seed=seed,set_seed=set_seed)
        elif ensemble == 'COE':
            H     = self.gen_coe(N,seed=seed,set_seed=set_seed)
        elif ensemble == 'CSE':
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
        N          Size of the rectangular matrix, NxN.
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
        np.random.seed(local_seed[0])
        if set_seed:
           np.random.seed(seed)
           local_seed = seed
        c_eigen = np.array([self.eigen_circular(N, ensemble=ensemble, set_seed=set_seed,
                                   seed=local_seed, adir=adir) for i in range(size)])
        return {'local_seed':local_seed, 'c_eigen':c_eigen}


    def eigen_circular_ensemble(self, N, cSize=100, nchunks=4,
                                ensemble='CUE', adir='lower',
                                seeds=list(), parallel=True):
        """
         
        Compute eigenvalues of given circular ensemble, in parallel or serial.
        

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
        same random seed:
        
        from bristol.ensembles import Circular
        ce        = Circular()
        mseed     = [123,125,124,122]       
        rr_serial = ce.eigen_circular_ensemble(
                                               10, 
                                               cSize=4, 
                                               nchunks=4, 
                                               seeds=mseed, 
                                               parallel=False
                                              )
        rr_paralel = ce.eigen_circular_ensemble(
                                                10, 
                                                cSize=4, 
                                                nchunks=4, 
                                                seeds=mseed, 
                                                parallel=True
                                               )
        all(rr_serial['c_eigen'] == rr_paralel['c_eigen']) 


        """
        if len(seeds) != nchunks:
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
        if parallel:
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
          return {'local_seeds':local_seeds, 'c_eigen':c_eigen,
              'matrix_size':N, 'number_of_matrices':nchunks*cSize}

