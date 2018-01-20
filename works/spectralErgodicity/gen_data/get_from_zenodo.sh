#
# This is a shell script assuming you have wget, unzip and mv installed.
# 
# Run this with source get_from_zenodo.sh
#
# Clean up
rm -rf 2017a_ergodicRandomMatrix_data_notebook.zip gen_data ergodicity_random_matrix_17a.ipynb
# Clean get copy
ZEN="https://zenodo.org/record/822411/files/2017a_ergodicRandomMatrix_data_notebook.zip"
wget $ZEN
unzip 2017a_ergodicRandomMatrix_data_notebook.zip
mv gen_data/*obj .
rm -rf 2017a_ergodicRandomMatrix_data_notebook.zip gen_data ergodicity_random_matrix_17a.ipynb
