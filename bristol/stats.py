"""
   
     Statistics Helper Methods

"""


class histogram:

    def __init__(self):
       print("histogram")    

    def h_freedman_diaconis(self, x):
        """

          Find optimal bin size for histogram of x vector.
          

          param:
          x    numpy array

          output:
          h    return estimated bin size in freedman_diaconis

          Example:
          x = np.random.random(100)
          h_freedman_diaconis(x)

        """
        q75, q25 = np.percentile(x,[75,25])
        iqr      = q75 - q25
        n3       = np.power(len(x),-1.0/3.0)
        return(2*iqr*n3)
