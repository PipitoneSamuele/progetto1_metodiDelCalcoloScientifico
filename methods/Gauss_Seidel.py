import utility.Constants as constants
import utility.Matrix_operations as mo
import scipy.sparse as sparse

def gauss_seidel(a, b, x, tol) :
    """
    Metodo iterativo per la risoluzione di sistemi lineari

    param a: Matrice dei coefficienti del sistema lineare
    param b: Vettore dei termini noti
    param x: Vettore dei coefficienti delle incognite
    param tol: Numero razionale, idealmente piccolo, che indica quando il metodo si deve arrestare
    """
    for i in range(constants.MAX_ITERATIONS) :
        r = b - (a @ x.transpose())
        l = sparse.tril(a, 0)
        y = sparse.linalg.spsolve_triangular(l.tocsr(), r.toarray())
        y = sparse.coo_array(y)
        x = x + y.transpose()
        if(mo.checkSparseSolutionResidual(r, b, tol)) :
            print("iterazione ", i+1, "del metodo Gauss_Seidel, ha trovato la soluzione:\n", x, "\n")
            return x
    return None