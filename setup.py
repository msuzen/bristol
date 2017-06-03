from setuptools import setup

fp = open('./bristol/version.py')
exec(fp.read())

setup(
      name='bristol',
      version=__version__,
      description="Bristol implements techniques developed by Mezzadri with parallel processing capabilities and a data model for further processing for generating random matrices. Circular module provides methods to generate matrices from Circular Unitary Ensemble (CUE), Circular Ortogonal Ensemble (COE) and Circular Symplectic Ensemble (CSE). Additional spectral analysis utilities are also implemented, such as computation of spectral density and spectral ergodicity.",
      url="https://github.com/msuzen/bristol",
      author='M.Suzen',
      author_email='suzen@acm.org',
      license= 'GPL-3',
      packages=['bristol'],
      install_requires=['numpy >= 1.11', 'future >= 0.16.0'],
      test_suite="test",
      zip_safe=False
     )
