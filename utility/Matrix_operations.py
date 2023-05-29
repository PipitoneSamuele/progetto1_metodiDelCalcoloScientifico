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
    """
    Metodo che riporta la distanza numerica tra la soluzione approssimata e la soluzione reale

    param x_approx: Vettore soluzione trovato dei metodi
    param x_solution: Vettore soluzione del sistema lineare
    """
    return linalg.norm(x_approx - x_solution) / linalg.norm(x_solution)

def forward_substitution(l, b) :
    """
    Metodo utilizzato per la risoluzione di sistemi con matrice triangolare inferiore

    param l: Matrice triangolare inferiore
    param b: Vettore di termini noti
    """
    l = sparse.coo_matrix(l).tocsr().todense()
    b = b.toarray()
    n = l.shape[0]
    x = [0.0] * n
    x[0] = b[0,0] / l[0,0]

    for i in range(1, n) :
        sumJ = 0.0
        for j in range(n) : 
            sumJ += l[i,j] * x[j]
        x[i] = (b[i, 0] - sumJ) / l[i,i]
    return sparse.coo_array(x)
      