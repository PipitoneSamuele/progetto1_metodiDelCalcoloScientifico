import utility.Constants as constants
import utility.Matrix_operations as mo
import scipy.sparse as sparse

#TODO: ripulisci codice
#TODO: sposta funzioni nell'utility se servono
#TODO: efficienza da rivedere, capisci come non fare l'inversa

def gauss_seidel(a, b, x, tol) :
    for i in range(constants.MAX_ITERATIONS_TEST) :
        r = b - (a @ x.transpose())
        L = sparse.tril(a, 0)
        y = mo.forward_substitution(L, r)
        x = x + y
        if(mo.checkSparseSolution(a, x, b, tol)) :
            print("iterazione ", i+1, " ha trovato la soluzione: ", x)
            return x
    return None #se ritorna none vuol dire che non converge