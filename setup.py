from setuptools import setup

fp = open('./bristol/version.py')
exec(fp.read())

with open('README.md') as f:
    long_description = f.read()

setup(
      name='bristol',
      version=__version__,
      description="Parallel random matrix tools and random matrix theory deep learning applications. Generate matrices from Circular Unitary Ensemble (CUE), Circular Ortogonal Ensemble (COE) and Circular Symplectic Ensemble (CSE). Additional spectral analysis utilities are also implemented, such as computation of spectral density and spectral ergodicity for complexity of deep learning architectures.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/msuzen/bristol",
      author='M.Suzen',
      author_email='suzen@acm.org',
      license= 'GPL-3',
      packages=['bristol'],
      install_requires=[
                        'numpy >= 1.11', 
                        'torch >= 1.3.0', 
                        'torchvision >= 0.4.1a0+d94043a'
                       ],
      test_suite="test",
      zip_safe=False
     )
