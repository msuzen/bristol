"""

     cPSE related functionality
     


"""


import numpy as np
import sys
import bristol
from bristol.spectral import Ergodicity
import json
from itertools import cycle

ergo = Ergodicity()

import torchvision
import torchvision.models as models
import torch

def get_layer_matrix_set(pmodel):
    """
    
    Return layer matrix set of a given pre-trained model 
    
    Input
    
    pmodel : pytorch torchvision pre-trained model
    
    Returns:
    
    A tuple (A_set, A_set_N, A_set_types)
        A_set       : A list of 2D np-array, weight matrices
        A_set_N     : Shape of NxN matrices. 
        A_set_types : Layer type, pytorch object type that is
                      extracted as 2D weight matrix.
    
    """
    A_set = []
    A_set_N = []
    A_set_types = []
    for x in pmodel.modules():
        type_mod = str(type(x))  # module/method name
        if "torch.nn.modules" in type_mod:
            try:
                layer_weights = torch.Tensor(x.weight)
                shape_layer = list(layer_weights.shape)
                len_shape = len(shape_layer)
                if len_shape >= 2:
                    N = shape_layer[0]
                    M = np.prod(shape_layer[1:])
                    if N > 1 and M > 1:
                        X = layer_weights
                        Ap = np.array(X.reshape(N, M).detach().numpy())
                        A = np.matmul(Ap, np.transpose(Ap))
                        A_set.append(A)
                        A_set_N.append(A.shape)
                        A_set_types.append(type_mod)
            except:
                pass
    return (A_set, A_set_N, A_set_types)


def get_eigenvals_layer_matrix_set(A_set):
    """
    
    Compute eigenvalues of given set of matrices
    
    Input: 
    
    A_set : list of 2D ndarrays, square real 
    
    Output
    eigenvals_set : List of list of eigenvalues
    
    
    """
    eigenvals_set = []
    for A in A_set:
        eigen_values = np.linalg.eigvals(np.matmul(A, np.transpose(A)))
        eigenvals_set.append(eigen_values)
    return eigenvals_set

def list2plist(lst, upper_bound):
    """
    
    Given list lst ans upper_bound.
    Return period_lst, cycle. 
    
    """
    pool = cycle(lst)
    c = 1
    lst_period = []
    for item in pool:
        c = c + 1
        if isinstance(item, np.complex64):
            item = item.real  # catch for numerical small-unstable numbers
        lst_period.append(abs(item))
        if c > upper_bound:
            break
    return lst_period


def eigenvals_set_to_periodic(layer_eigens):
    """
    
    Layer matrix set eigenvalues to periodic set
    
    """
    upper_bound = np.max([len(e) for e in layer_eigens])
    eset_period = [list2plist(e, upper_bound) for e in layer_eigens]
    return eset_period

def d_layers_pse(eset_per):
    """
    
    Progression of D_layers given periodic set

    Ex:
    from bristol import cPSE
    netname = 'vgg11'
    pmodel = getattr(models, netname)(pretrained=True)
    print(type(pmodel))
    A_t = cPSE.get_layer_matrix_set(pmodel)
    eset = cPSE.get_eigenvals_layer_matrix_set(A_t[0])
    eset_per = cPSE.eigenvals_set_to_periodic(eset)
    d_layers = cPSE.d_layers_pse(eset_per)
    
    """
    nlayers = len(eset_per) - 1  # minus 1 for the last layer
    print(nlayers)
    N = len(eset_per[0])
    D_layer = []
    for l in np.arange(1, nlayers):
        eigen_l = np.ravel(np.array(eset_per[0:l]))
        l1 = l + 1
        eigen_l1 = np.ravel(np.array(eset_per[0:l1]))
        omega_l = ergo.thirumalai_mountain(eigen_l, l, N)
        omega_l1 = ergo.thirumalai_mountain(eigen_l1, l1, N)
        dl = ergo.kl_distance_symmetric(omega_l, omega_l1)
        D_layer.append(dl)
    return D_layer


def cpse_measure(pmodel):
    """
    Given torch model object pmodel return 
    pse on layers and mean log pse Cascading PSE
    (d_layers, cpse) : d_layers vector and real number cpse
     
    netname = 'vgg11'
    pmodel = getattr(models, netname)(pretrained=True)
    (d_layers, cpse) = cPSE.cpse(pmodel)
     
    """
    A_t = get_layer_matrix_set(pmodel)
    eset = get_eigenvals_layer_matrix_set(A_t[0])
    eset_per = eigenvals_set_to_periodic(eset)
    d_layers = d_layers_pse(eset_per)
    return d_layers, np.mean(np.log10(d_layers))


