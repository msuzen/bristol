# Bristol

[![Build Status](https://travis-ci.org/msuzen/bristol.svg?branch=master)](https://travis-ci.org/msuzen/bristol) 
[![Coverage Status](https://coveralls.io/repos/github/msuzen/bristol/badge.svg?branch=master)](https://coveralls.io/github/msuzen/bristol?branch=master) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.579642.svg)](https://doi.org/10.5281/zenodo.579642)
[![PyPI version](https://img.shields.io/pypi/v/bristol.svg?maxAge=2591000)](https://pypi.org/project/bristol/)
[![Downloads](http://pepy.tech/badge/bristol)](https://pepy.tech/project/bristol)
[![Downloads](https://pepy.tech/badge/bristol/month)](https://pepy.tech/project/bristol)

Parallel Random Matrix tools.

Bristol implements techniques developed by Mezzadri with parallel processing capabilities and a data model for further processing for generating random matrices. Circular module provides methods to generate matrices from Circular Unitary Ensemble (CUE), Circular Ortogonal Ensemble (COE) and Circular Symplectic Ensemble (CSE). Additional spectral analysis utilities are also implemented, such as computation of spectral density and spectral ergodicity.

## Features

* Generation of Circular Ensembles: CUE, COE and CSE.
* Random matrices: Reproducibility both in serial and parallel processing.
* Eigenvalue Spectra, spectral densitiy.
* Kullbach-Leibler divergence and spectral ergodicity measure functionality.

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

* Basics of circular ensembles [ipynb](https://github.com/msuzen/bristol/blob/master/works/spectralErgodicity/01_generating_circular_ensembles_notes.ipynb). 

* Computing spectral ergodicity for generated matrices [ipynb](https://github.com/msuzen/bristol/blob/master/works/spectralErgodicity/01_generating_circular_ensembles_notes.ipynb). This is to reproduce the main figure from [arXiv:1704.08693](https://arxiv.org/abs/1704.08303).
 

## Contact

* Please create an issue for any type of questions or contact `msuzen`.

## References

* Berry, M V & Pragya Shukla 2013, Hearing random matrices and random waves, New. J. Phys. 15 013026 (11pp) [berry456](https://michaelberryphysics.files.wordpress.com/2013/06/berry456.zip)

* Spectral Ergodicity in Deep Learning Architectures via Surrogate Random Matrices, Mehmet Süzen, Cornelius Weber, Joan J. Cerdà, [arXiv:1704.08693](https://arxiv.org/abs/1704.08303)

## Citation

If you use the ideas from this package please do cite as follows 

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
