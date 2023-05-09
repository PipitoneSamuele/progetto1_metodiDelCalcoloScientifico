import numpy
import scipy.sparse.linalg as linalg

#controlla se gli elementi diagonali della matrice A in input sono tutti diversi da zero
def isDiagonalAllNonZero(A) :
    diagonal = numpy.diagonal(A)
    for x in diagonal :
        if(x == 0) :
            return False
    return True

#TODO: metodo per calcolare l'errore relativo OLD
def checkCurrentSolution(A, x, b, tol) :
    if(numpy.divide(numpy.linalg.norm((A@x) - b), numpy.linalg.norm(b)) < tol) :
        return True
    else :
        return False

#TODO: metodo per calcolare l'errore relativo di matrici sparse
def checkSparseSolution(A, x, b, tol) : 
    residuo = A.dot(x.transpose()) - b.transpose()
    value = linalg.norm(residuo) / (linalg.norm(b))
    print("value", value)
    if(value < tol) :
         return True
    else :
         return False

#TODO: ritorna true se nella diagonale è presente il valore maggiore della matrice in termini assoluti
#Serve per dimostrarne la convergenza prima di applicare il metodo risolutivo d Jacobi
def isDiagonallyDominant(A) :
    return False