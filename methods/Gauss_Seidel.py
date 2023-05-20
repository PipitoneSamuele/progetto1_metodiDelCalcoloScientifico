import utility.Constants as constants
import utility.Matrix_operations as mo
import scipy.sparse as sparse

#TODO: ripulisci codice
#TODO: sposta funzioni nell'utility se servono

def gauss_seidel(a, b, x, tol) :
    for i in range(constants.MAX_ITERATIONS_TEST) :
        L = sparse.tril(a, 0)
        U = sparse.triu(a, 1)
        L = sparse.linalg.inv(L.tocsc())
        T = -L @ U
        C = L @ b.transpose()
        x = T@x.transpose() + C
        if(mo.checkSparseSolution(a, x.transpose(), b, tol)) :
            print("iterazione ", i+1, " ha trovato la soluzione: ", x)
            return x
    return None #se ritorna none vuol dire che non converge