# Bristol

[![Build Status](https://travis-ci.com/msuzen/bristol.svg?branch=master)](https://travis-ci.com/msuzen/bristol) 
[![Coverage Status](https://coveralls.io/repos/github/msuzen/bristol/badge.svg?branch=master)](https://coveralls.io/github/msuzen/bristol?branch=master) 
[![PyPI version](https://img.shields.io/pypi/v/bristol.svg?maxAge=2591000)](https://pypi.org/project/bristol/)
[![Downloads](http://pepy.tech/badge/bristol)](https://pepy.tech/project/bristol)
[![Downloads](https://pepy.tech/badge/bristol/month)](https://pepy.tech/project/bristol)
[![arXiv:1704.08303](http://img.shields.io/badge/arXiv-1704.08303-B31B1B.svg)](https://arxiv.org/abs/1704.08303)
[![Zenodo:Archive:v0.1.8](https://zenodo.org/badge/DOI/10.5281/zenodo.579642.svg)](https://doi.org/10.5281/zenodo.579642)
[![Zenodo:Surrogate Matrices Data](https://zenodo.org/badge/DOI/10.5281/zenodo.822411.svg)](https://doi.org/10.5281/zenodo.822411)
[![arXiv:1911.07831](http://img.shields.io/badge/arXiv-1911.07831-B31B1B.svg)](https://arxiv.org/abs/1911.07831)
[![arXiv:2006.13687](http://img.shields.io/badge/arXiv-2006.13687-B31B1B.svg)](https://arxiv.org/abs/2006.13687)

Parallel random matrix tools and random matrix theory deep learning applications. 
Generate matrices from Circular Unitary Ensemble (CUE), Circular Ortogonal Ensemble (COE) and 
Circular Symplectic Ensemble (CSE). Additional spectral analysis utilities are 
also implemented, such as computation of spectral density and spectral ergodicity 
for complexity of deep learning architectures.

## Features

* Generation of Circular Ensembles: CUE, COE and CSE.
* Random matrices: Reproducibility both in serial and parallel processing.
* Eigenvalue Spectra, spectral densitiy.
* Kullbach-Leibler divergence and spectral ergodicity measure functionality.
* Cascading Periodic Spectral Ergodicity (cPSE)


## Installation

Install with pip from [pypi](https://pypi.python.org/pypi/bristol).

```bash
pip install bristol
```

To use the latest development version

```bash
pip install -upgrade git+https://github.com/msuzen/bristol.git
```

## Documentation
### Complexity of a deep learning model: cPSE

You need to put your model as pretrained model format of PyTorch. An example for vgg, 
and use `cPSE.cpse_measure` function simply:

```
from bristol import cPSE
import torchvision.models as models
netname = 'vgg11'
pmodel = getattr(models, netname)(pretrained=True)
(d_layers, cpse) = cPSE.cpse_measure(pmodel)
```

This would give `cpse` a single number expressing the complexity of your network and `d_layers` evolution of 
`periodic spectral ergodicity` withing layers as a vector, order matters.

### Prototype notebooks 

* Basics of circular ensembles [ipynb](https://github.com/msuzen/bristol/blob/master/works/spectralErgodicity/01_generating_circular_ensembles_notes.ipynb). 

* Computing spectral ergodicity for generated matrices [ipynb](https://github.com/msuzen/bristol/blob/master/works/spectralErgodicity/01_generating_circular_ensembles_notes.ipynb). This is to reproduce the main figure from [arXiv:1704.08693](https://arxiv.org/abs/1704.08303).

* The concept of cascading periodic ergodicity (cPSE) [ipynb](https://github.com/msuzen/bristol/blob/master/works/cPSE/periodic_spectral_ergodicity_dnn.ipynb) This is only to reproduce paper's results from [arXiv:1911.07831](https://arxiv.org/abs/1911.07831).

* Empirical deviations of semicircle law in mixed-matrix ensembles,  <br>
  M. Suezen, 
  [hal-03464130](https://hal.archives-ouvertes.fr/hal-03464130) | [ipynb](https://github.com/msuzen/bristol/blob/master/works/mixedMatrixEnsembles/deviation_semicirclelaw.ipynb) Reproduces the work with the same title.

## Contact

* Please create an issue for any type of questions or contact `msuzen`.

## References

* Berry, M V & Pragya Shukla 2013, Hearing random matrices and random waves, New. J. Phys. 15 013026 (11pp) [berry456](https://michaelberryphysics.files.wordpress.com/2013/06/berry456.zip)

* Spectral Ergodicity in Deep Learning Architectures via Surrogate Random Matrices, Mehmet Süzen, Cornelius Weber, Joan J. Cerdà, [arXiv:1704.08693](https://arxiv.org/abs/1704.08303)

* Periodic Spectral Ergodicity: A Complexity Measure for Deep Neural Networks and Neural Architecture Search, Mehmet Süzen, Cornelius Weber, Joan J. Cerdà, [arXiv:1911.07831](https://arxiv.org/abs/1911.07831)

* Empirical deviations of semicircle law in mixed-matrix ensembles,  <br>
  M. Suezen, 
  [hal-03464130](https://hal.archives-ouvertes.fr/hal-03464130) | [ipynb](https://github.com/msuzen/bristol/blob/master/works/mixedMatrixEnsembles/deviation_semicirclelaw.ipynb) Reproduces the work with the same title.

## Citation

If you use the ideas or tools from this package please do cite our manuscripts.

```
@article{suezen2017a,
    title={Spectral Ergodicity in Deep Learning Architectures via Surrogate Random Matrices},
    author={Mehmet Süzen and Cornelius Weber and Joan J. Cerdà},
    year={2017},
    eprint={1704.08303},
    archivePrefix={arXiv},
    primaryClass={stat.ML}
}
```

```
@article{suezen2019a,
    title={Periodic Spectral Ergodicity: A Complexity Measure for Deep Neural Networks and Neural Architecture Search},
    author={Mehmet Süzen and Cornelius Weber and Joan J. Cerdà},
    year={2019},
    eprint={1911.07831},
    archivePrefix={arXiv},
    primaryClass={stat.ML}
}
```
