import numpy 

# Partire da vettore nullo e arrestarsi se la k-esima iterata
# soddisfa ||Ax^k-b||/||b|| < tol.
# Inoltre numero massimo di iterazioni maxIter (> 20000), altrimenti printiamo che non converge a soluzione
    # NB: @ è un operatore che serve per la moltiplicazione matriciale
def jacobi(A, b, x, tol) :
        for i in range(25) :
            D = getDiagonalMatrix(A)
            Dm = invertedDiagonalMatrix(D)
            R = getZeroDiagMatrix(A)
            T = Dm @ R
            C = Dm @ b
            x = (T @ x) + C
            if(checkError(A, x, b, tol)) :
                print("iterazione ", i, " ha trovato la soluzione: ", x)
                return x
        return None #se ritorna none vuol dire che non converge
       
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