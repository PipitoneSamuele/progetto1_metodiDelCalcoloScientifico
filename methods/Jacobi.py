import numpy
import utility.Constants as constants

### TODO: controlla efficienza
### TODO: commenta funzioni
### TODO: se possono essere utili queste funzioni da altre parti spostale nell'utility
### TODO: le lettere maiuscole sono costanti

# @ è un operatore che serve per la moltiplicazione matriciale
def jacobi(A, b, x, tol) :
        for i in range(constants.MAX_ITERATIONS_TEST) :
            D = getInvertedDiagonalMatrix(A)
            R = getZeroDiagMatrix(A)
            x = ((D @ R) @ x) + (D @ b)
            print("x: ", x)
            if(checkCurrentSolution(A, x, b, tol)) :
                print("iterazione ", i, " ha trovato la soluzione: ", x)
                return x
        return None #se ritorna none vuol dire che non converge
       
def getInvertedDiagonalMatrix(A) :
    B = numpy.matrix.copy(A) #TODO: controlla se si può
    for i in range(len(B)) :
        for j in range(len(B[0])) :
            if(i != j) :
                B[i][j] = 0
            else :
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

def checkCurrentSolution(A, x, b, tol) :
    if(numpy.divide(numpy.linalg.norm((A@x) - b), numpy.linalg.norm(b)) < tol) :
        return True
    else :
        return False