import numpy

#controlla se gli elementi diagonali della matrice A in input sono tutti diversi da zero
def isDiagonalAllNonZero(A) :
    diagonal = numpy.diagonal(A)
    for x in diagonal :
        if(x == 0) :
            return False
    return True