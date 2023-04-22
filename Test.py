#Classe usata per testare funzioni in altre classi o funzionalità che stiamo sviluppando

import utility.Matrix_operations as mo
import methods.Jacobi as jacobi
import methods.Gauss_Seidel as gs
import methods.Gradiente as grad
import numpy
import utility.Constants as constants

A = numpy.array([[2.0, 1.0], [1.0, 2.0]])

b = numpy.array([8.0, 1.0])
x = numpy.array([0.0, 0.0])

#jacobi.jacobi(A, b, x, 1)

#print("inf \n", gs.getTriangolarInf(B))
#print("sup \n", gs.getTriangolarSup(B))
#gs.gauss_seidel(A, b, x, constants.TOL_TEST)

#jacobi.jacobi(A, b, x, constants.TOL_TEST)

print("Risultato: ", grad.gradiente(A, b, x, constants.TOL_TEST))