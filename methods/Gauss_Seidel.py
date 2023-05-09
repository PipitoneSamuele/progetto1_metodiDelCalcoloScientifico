import utility.Constants as constants
import utility.Matrix_operations as mo
import scipy.sparse as sparse

#TODO: ripulisci codice
#TODO: sposta funzioni nell'utility se servono

def gauss_seidel(a, b, x, tol) :
    for i in range(constants.MAX_ITERATIONS_TEST) :
        p = sparse.tril(a, 0)
        r = b.transpose() - (a @ x.transpose())
        y = forwardSubstitution(p, r)
        x = x + y.transpose()
        if(mo.checkSparseSolution(a, x, b, tol)) :
            print("iterazione ", i, " ha trovato la soluzione: ", x)
            return x
    return None

#inefficiente O(n^2)
def forwardSubstitution(a, b) :
    a = a.todense()
    b = b.todense()
    x = [0] * len(b) 

    for i in range(len(b)):
        x[i] = b[i]
        for j in range(0, i) :
            x[i] -= a[i, j] * x[j]
        x[i] /= a[i, i]
    return sparse.coo_array(x)