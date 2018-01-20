# Ergodicity in Random Matrices

Author: M. Suzen

Last Up Date: January 2018
 
Reproducing results from `arXiv:1704.08303` 

## Notebooks
* `01_generating_circular_ensembles_notes.ipynb` : Notes on how to generate circular ensembles.
* `02_ergodicity_random_matrix.ipynb` :  Computing "decay function", approach to spectral ergodicity.

## Requirements  
As in `02_ergodicity_random_matrix.ipynb`

### Software

As in `02_ergodicity_random_matrix.ipynb`

For this sheet `Bristol 0.2.0` is needed with Python 2.7, due to datasets.

### Data files: Generated Circular Ensembles

As in `02_ergodicity_random_matrix.ipynb`

The following data files should be available

* `./data_cue.obj` : CUE data
* `./data_coe.obj` : COE data
* `./data_cse.obj` : CSE data

These can be either generated or a copy can be downloaded from zenodo.

#### Get from zenodo
As in `02_ergodicity_random_matrix.ipynb`

Via script under the same directory as this notebook at `get_data/get_from_zenodo.sh`. Apply the following under `gen_data`:

`source get_from_zenodo.sh`

#### Generate the data locally (Takes couple of hours! depending on the number of cores.)
As in `02_ergodicity_random_matrix.ipynb`

To generate the data run `data_gen.py` under `gen_data`.

### Dataset dictionary
As in `02_ergodicity_random_matrix.ipynb`

Each dataset is a dictionary;

* The following keys, `['N1024', 'N64', 'N256', 'N512', 'N128', 'N768']`, representing different matrix size in the first

* Each matrix size keys contains an other dictionary with the following keys:
    * `local_seeds` : seeds used in different cores, integer array of size number of cores used (4 here).
    * `matrix_size` : integer, in
    * `number_of_matrices` : number of matrices used, M
    * `c_eigen`: set of eigenvalues from M=40 different realization of matrices.

