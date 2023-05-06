#Classe usata per testare funzioni in altre classi o funzionalità che stiamo sviluppando

import utility.Matrix_operations as mo
import methods.Jacobi as jacobi
import methods.Gauss_Seidel as gs
import methods.Gradiente as grad
import numpy
import utility.Constants as constants
import scipy.sparse as sparse

#A = numpy.array([[2.0, 1.0], [1.0, 2.0]])

#b = numpy.array([8.0, 1.0])
#x = numpy.array([0.0, 0.0])

A = sparse.coo_matrix([[2.0, 1.0], [1.0, 2.0]])
b = sparse.coo_array([8.0, 1.0])
x = sparse.coo_array([0.0, 0.0])

jacobi.jacobi(A, b, x, constants.TOL_TEST)