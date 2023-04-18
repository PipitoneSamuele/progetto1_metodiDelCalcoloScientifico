#Classe usata per testare funzioni in altre classi o funzionalità che stiamo sviluppando

import utility.Matrix_operations as mo
import methods.Jacobi as jacobi
import numpy
import utility.Constants as constants

#NB: se usi la matrice A per entrambi i metodi non funziona, in quanto chiamare un metodo e passare A lo modifica,
#    forse bisogna non ritornarla dal metodo ma creare una nuova matrice e ritornare quella (non nuova tipo A = B -> stesso puntamento a memoria)
A = numpy.array([[1.0, 2.0], [3.0, 4.0]])

b = numpy.array([0.0, 0.0])
x = numpy.array([1.0, 1.0])

print(jacobi.jacobi(A, b, x, constants.TOL_TEST))