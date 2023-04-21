#Classe usata per testare funzioni in altre classi o funzionalità che stiamo sviluppando

import utility.Matrix_operations as mo
import methods.Jacobi as jacobi
import methods.Gauss_Seidel as gs
import numpy
import utility.Constants as constants

A = numpy.array([[2.0, 0.0, 0.0], [1.0, 2.0, 0.0], [1.0, 1.0, 2.0]])

b = numpy.array([2.0, -1.0, 0.0])
x = numpy.array([1.0, 1.0, 1.0])

B = numpy.array([[1,1,1], [1,1,1], [1,1,1]])

#jacobi.jacobi(A, b, x, 1)

#print("inf \n", gs.getTriangolarInf(B))
#print("sup \n", gs.getTriangolarSup(B))
gs.gauss_seidel(A, b, x, 1)

#jacobi.jacobi(A, b, x, constants.TOL_TEST)