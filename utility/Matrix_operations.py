import numpy
import scipy.sparse.linalg as linalg
import scipy.sparse as sparse

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
    residuo = A.dot(x.transpose()) - b
    value = linalg.norm(residuo) / (linalg.norm(b))
    print("tollerance check: ", value)
    if(value < tol) :
         return True
    else :
         return False

#TODO: ritorna true se nella diagonale è presente il valore maggiore della matrice in termini assoluti
#Serve per dimostrarne la convergenza prima di applicare il metodo risolutivo d Jacobi
def isDiagonallyDominant(A) :
    return False

def calculateRelativeError(x_approx, x_solution) :
    return linalg.norm(x_approx - x_solution) / linalg.norm(x_solution)

#funziona
def forward_substitution(L, b) :
    L = sparse.coo_matrix(L).tocsr().todense()
    b = b.toarray()[0]
    n = L.shape[0]
    x = [0.0] * n
    x[0] = b[0] / L[0,0]

    for i in range(1, n) :
        sumJ = 0.0
        for j in range(n) : 
            sumJ += L[i,j] * x[j]
        x[i] = (b[i] - sumJ) / L[i,i]
    return x
      