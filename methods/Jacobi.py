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
        r = -getZeroDiagMatrix(a)
        t = d.dot(r)
        c = d.dot(b)
        intermedio = t.dot(x.transpose())
        x = intermedio + c
        x = x.transpose()
        if(mo.checkSparseSolution(a, x, b, tol)) :
            print("iterazione ", i+1, " ha trovato la soluzione: ", x)
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

def getZeroDiagMatrix(a) :
    """
    Ritorna la matrice con la diagonale posta a 0

    param a: Matrice di input
    """
    triu_A = sparse.triu(a, 1)
    tril_A = sparse.tril(a, -1)
    return triu_A + tril_A 