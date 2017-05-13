from setuptools import setup

fp = open('./bristol/version.py')
exec(fp.read())

setup(
      name='bristol',
      version=__version__,
      description="Bristol: A Python Package for Random Matrix Ensembles: Application of Random Matrix Theory (RMT) appear in different fields of research. Generation of random matrices numerically is an essential part of this practice. While, matrices should be generated in a numerically stable way and should represent correct matrix ensemble. Bristol implements techniques developed by Mezzadri that addresses these concerns in a Python module with parallel processing capabilities and a data model for further processing.  Circular module provides methods to generate matrices from Circular Unitary Ensemble (CUE), Circular Ortogonal Ensemble (COE) and Circular Symplectic Ensemble (CSE). Additional spectral analysis utilities are also implemented, such as computation of spectral density and spectral ergodicity."
      url="https://github.com/msuzen/bristol",
      author='M.Suzen, C.Garbers',
      author_email='suzen@acm.org',
      license= 'GPL-3',
      packages=['bristol'],
      install_requires=['numpy >= 1.11', 'future >= 0.16.0'],
      test_suite="test",
      zip_safe=False
     )
