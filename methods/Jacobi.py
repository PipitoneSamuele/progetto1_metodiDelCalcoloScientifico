import scipy.sparse as sparse
import utility.Constants as constants
import utility.Matrix_operations as mo

def jacobi(a, b, x, tol) :
    """
    Metodo iterativo per la risoluzione di sistemi lineari

    param a: Matrice dei coefficienti del sistema lineare
    param b: Vettore dei termini noti
    param x: Vettore dei coefficienti delle incognite
    param tol: Numero razionale, idealmente piccolo, che indica quando il metodo si deve arrestare
    """
    for i in range(constants.MAX_ITERATIONS) :
        d = getInvertedDiagonalMatrix(a)
        x = x.transpose()
        residuo = b - (a @ x) 
        x = x + (d @ residuo)
        x = x.transpose()
        if(mo.checkSparseSolutionResidual(residuo, b, tol)) :
            print("iterazione ", i+1, "del metodo Jacobi, ha trovato la soluzione:\n")
            return x
    return None

def getInvertedDiagonalMatrix(a) :
    """
    Ritorna la matrice con solo la diagonale inversa nella forma 1/Aii

    param a: Matrice di input
    """
    diag = a.diagonal()
    for i in range(len(diag)) :
        diag[i] = 1/diag[i]
    return sparse.diags(diag, 0)