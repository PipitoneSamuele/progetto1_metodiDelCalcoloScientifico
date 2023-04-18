import numpy

#controlla se gli elementi diagonali della matrice A in input sono tutti diversi da zero
def isDiagonalAllNonZero(A) :
    diagonal = numpy.diagonal(A)
    for x in diagonal :
        if(x == 0) :
            return False
    return True

#TODO: metodo per calcolare l'errore relativo (e = x - x^k)
def rel_error(e) :
    return 0