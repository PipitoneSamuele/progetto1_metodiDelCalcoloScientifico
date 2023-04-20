import numpy

#controlla se gli elementi diagonali della matrice A in input sono tutti diversi da zero
def isDiagonalAllNonZero(A) :
    diagonal = numpy.diagonal(A)
    for x in diagonal :
        if(x == 0) :
            return False
    return True

#TODO: metodo per calcolare l'errore relativo (e = x - x^k)
def relError(e) :
    return 0

#TODO: ritorna true se nella diagonale è presente il valore maggiore della matrice in termini assoluti
#Serve per dimostrarne la convergenza prima di applicare il metodo risolutivo d Jacobi
def isDiagonallyDominant(A) :
    return False