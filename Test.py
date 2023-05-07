#Classe usata per testare funzioni in altre classi o funzionalità che stiamo sviluppando

from scipy.io import mmread
import utility.Matrix_operations as mo
import scipy.sparse as sparse
import scipy.sparse.linalg as linalg
import utility.Constants as constants
import methods.Jacobi as jacobi

A = sparse.coo_matrix([[10.0, 1.0, -1.0], [1.0, 15.0, 1.0], [-1.0, 1.0, 20.0]])
b = sparse.coo_array([18.0, -12.0, 17.0])
x = sparse.coo_array([0.0, 0.0, 0.0])

jacobi.jacobi(A, b, x, 0.001)