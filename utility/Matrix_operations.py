import numpy
import scipy.sparse.linalg as linalg

def isDiagonalAllNonZero(A) :
    """
    Controlla se gli elementi diagonali della matrice A in input sono tutti diversi da zero

    param a: Matrice da controllare
    """
    diagonal = numpy.diagonal(A)
    for x in diagonal :
        if(x == 0) :
            return False
    return True

def checkSparseSolution(A, x, b, tol) : 
    """ 
    Metodo usato per verificare la precisione della x corrente

    param a: Matrice dei coefficienti del sistema lineare
    param b: Vettore dei termini noti
    param x: Vettore dei coefficienti delle incognite
    param tol: Numero razionale, idealmente piccolo, che indica quando il metodo si deve arrestare
    """
    residuo = A.dot(x.transpose()) - b
    value = linalg.norm(residuo) / (linalg.norm(b))
    if(value < tol) :
         return True
    else :
         return False
    
def checkSparseSolutionResidual(residuo, b, tol) :
    """ 
    Metodo usato per verificare la precisione della x corrente, passando il residuo
    calcolato nel metodo risparmiamo operazioni macchina

    param a: Matrice dei coefficienti del sistema lineare
    param b: Vettore dei termini noti
    param x: Vettore dei coefficienti delle incognite
    param tol: Numero razionale, idealmente piccolo, che indica quando il metodo si deve arrestare
    """
    value = linalg.norm(residuo) / (linalg.norm(b))
    #print("tollerance check: ", value)
    if(value < tol) :
         return True
    else :
         return False

def calculateRelativeError(x_approx, x_solution) :
    """
    Metodo che riporta la distanza numerica tra la soluzione approssimata e la soluzione reale

    param x_approx: Vettore soluzione trovato dei metodi
    param x_solution: Vettore soluzione del sistema lineare
    """
    return linalg.norm(x_approx - x_solution) / linalg.norm(x_solution)