import utility.Constants as constants
import utility.Matrix_operations as matrix_operations
import numpy 

# Partire da vettore nullo e arrestarsi se la k-esima iterata
# soddisfa ||Ax^k-b||/||b|| < tol.
# Inoltre numero massimo di iterazioni maxIter (> 20000), altrimenti printiamo che non converge a soluzione
    # NB: @ è un operatore che serve per la moltiplicazione matriciale
def jacobi(A, b, x, tol) :
        for i in range(constants.MAX_ITERATIONS_TEST) :
            D = getDiagonalMatrix(A)
            #print("D: ", D)
            Dm = invertedDiagonalMatrix(D)
            #print("D inverted: ", Dm)
            R = getZeroDiagMatrix(A)
            #print("R", R)
            #print("x before: ", x)
            x = Dm @ (b - (R@x))
            print("x after: ", x)
        """
    k = 0
    while(k < constants.MAX_ITERATIONS_TEST) :
        r = (A@x) - b #NON devi prendere A ma P - N
        x = x + (getInvertedDiagonalMatrix(A) @ r)
        k += 1
        if(checkError(A, x, b, tol)) :
            return x
    return None #se ritorna none vuol dire che non converge
        """

def getDiagonalMatrix(A) :
    B = numpy.matrix.copy(A) #TODO: controlla se si può
    for i in range(len(B)) :
        for j in range(len(B[0])) :
            if(i != j) :
                B[i][j] = 0
    return B

#Metodo che ritorna una matrice con tutti 0 tranne la diagonale principale, assumo matrice quadrata
def invertedDiagonalMatrix(A) :
    B = numpy.matrix.copy(A) #TODO: controlla se si può
    for i in range(len(B)) :
        for j in range(len(B[0])) :
            if(i == j) :
                B[i][j] = 1/(B[i][j])            
    return B

#Metodo che ritorna una matrice la cui diagonale sono tutti 0 e gli altri elementi sono invertiti di segno
def getZeroDiagMatrix(A) :
    B = numpy.matrix.copy(A) #TODO: controlla se si può
    for i in range(len(B)) :
        for j in range(len(B[0])) :
            if(i == j) :
                B[i][j] = 0
            else :
                B[i][j] = -B[i][j]
    return B

def checkError(A, x, b, tol) :
    if(numpy.divide(numpy.linalg.norm((A@x) - b), numpy.linalg.norm(b)) < tol) :
        return True
    else :
        return False