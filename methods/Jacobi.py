import utility.Constants as constants
import utility.Matrix_operations as matrix_operations

# Partire da vettore nullo e arrestarsi se la k-esima iterata
# soddisfa ||Ax^k-b||/||b|| < tol.
# Inoltre numero massimo di iterazioni maxIter (> 20000), altrimenti printiamo che non converge a soluzione
def jacobi(A, b, x, tol) :

    # Scrivere la matrice matrix come A = M - N, dove M è una matrice invertibile (con determinante non nullo)
    # allora la soluzione x di Ax = b risovle anche 
        # Mx = Nx+b
        # x = M^-1 (Nx+b)
    # x^(k+1) = M^-1 (Nx^k + b), se converge ad un vettore x allora Ax = b
        # Video yt scrive: x^(k+1) = 1/aii * (bi - sommatoria(aij*xj^k))
    # Errore: misurabile con e^k = x^k - x Ovvero e^k = (M^-1 * N)^k * e^0
    # Tips: 
    #   diagonale non deve avere valori nulli, in tal caso si potrebbe permutare A

    k = 1
    while(k <= constants.MAX_ITERATIONS) :
        k += 1
    return None # Se ritorna None vuol dire che abbiamo superato il numero massimo di iterazioni consentite