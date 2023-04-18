import utility.Constants as constants
import utility.Matrix_operations as matrix_operations
import numpy 

# Partire da vettore nullo e arrestarsi se la k-esima iterata
# soddisfa ||Ax^k-b||/||b|| < tol.
# Inoltre numero massimo di iterazioni maxIter (> 20000), altrimenti printiamo che non converge a soluzione
def jacobi(A, b, x, tol) :
    k = 0
    # Scrivere la matrice matrix come A = M - N, dove M è una matrice invertibile (con determinante non nullo)
    # allora la soluzione x di Ax = b risovle anche 
        # Mx = Nx+b
        # x = M^-1 (Nx+b)
    # x^(k+1) = M^-1 (Nx^k + b), se converge ad un vettore x allora Ax = b
        # Video yt scrive: x^(k+1) = 1/aii * (bi - sommatoria(aij*xj^k))
    # Errore: misurabile con e^k = x^k - x Ovvero e^k = (M^-1 * N)^k * e^0
    # Tips: 
    #   diagonale non deve avere valori nulli, in tal caso si potrebbe permutare A
    # NB: @ è un operatore che serve per la moltiplicazione matriciale
    while(k < constants.MAX_ITERATIONS_TEST) :
        r = (A@x) - b
        x = x + (getDiagMatrix(A) @ r)
        k += 1
        return x
        #if(checkError(A, x, b, tol)) :
        #    return x
    return None #se ritorna none vuol dire che non converge

#Metodo che ritorna una matrice con tutti 0 tranne la diagonale principale, assumo matrice quadrata
def getDiagMatrix(A) :
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            if(i != j) :
                A[i][j] = 0
            else :
                A[i][j] = 1/(A[i][j])
    return A

#Metodo che ritorna una matrice la cui diagonale sono tutti 0 e gli altri elementi sono invertiti di segno
def getZeroDiagMatrix(A) :
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            if(i == j) :
                A[i][j] = 0
            else :
                A[i][j] = -A[i][j]
    return A

def diagonalInvert(A) :
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            if(i == j) :
                A[i][j] = 1/(A[i][j])
    return A

def checkError(A, x, b, tol) :
    if(numpy.divide(numpy.linalg.norm((A@x)-b), numpy.linalg.norm(b)) < tol) : 
        return True
    else :
        return False