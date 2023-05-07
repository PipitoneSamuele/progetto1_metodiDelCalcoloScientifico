import numpy
import scipy.sparse as sparse
import scipy.sparse.linalg as linalg
import utility.Constants as constants

### TODO: controlla efficienza
### TODO: commenta funzioni
### TODO: se possono essere utili queste funzioni da altre parti spostale nell'utility
### TODO: le lettere maiuscole sono costanti

# @ è un operatore che serve per la moltiplicazione matriciale
def jacobi(A, b, x, tol) :
        for i in range(constants.MAX_ITERATIONS_TEST) :
            D = getInvertedDiagonalMatrix(A)
            r = getZeroDiagMatrix(A)
            r = -r
            T = D.dot(r)
            C = D.dot(b.transpose())
            intermedio = T.dot(x.transpose())
            x = intermedio + C
            x = x.transpose()
            if(checkSolution(A, x, b, tol)) :
                print("iterazione ", i, " ha trovato la soluzione: ", x)
                return x
        return None #se ritorna none vuol dire che non converge

def getInvertedDiagonalMatrix(A) :
    diag = A.diagonal()
    for i in range(len(diag)) :
        diag[i] = 1/diag[i]
    return sparse.diags(diag, 0) #NB: questa è una dia_matrix non coo_matrix

#Metodo che ritorna una matrice la cui diagonale sono tutti 0 e gli altri elementi sono invertiti di segno
def getZeroDiagMatrix(A) :
    triu_A = sparse.triu(A, 1)
    tril_A = sparse.tril(A, -1)
    return triu_A + tril_A #coo_matrix

def checkSolution(A, x, b, tol) : 
    residuo = A.dot(x.transpose()) - b.transpose()
    value = linalg.norm(residuo) / (linalg.norm(b))
    print("value", value)
    if(value < tol) :
         return True
    else :
         return False