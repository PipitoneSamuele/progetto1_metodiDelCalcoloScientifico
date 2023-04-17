#Classe usata per testare funzioni in altre classi o funzionalità che stiamo sviluppando

import utility.Matrix_operations as mo
import numpy

A = numpy.matrix([[0, 2], [3, 4]])

print(mo.isDiagonalAllNonZero(A))