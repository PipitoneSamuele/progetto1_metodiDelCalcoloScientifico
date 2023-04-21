import numpy
import utility.Constants as constants
import utility.Matrix_operations as mo

#TODO: ripulisci codice
#TODO: sposta funzioni nell'utility se servono
#TODO: 

def gauss_seidel(A, b, x, tol) :
    for i in range(constants.MAX_ITERATIONS_TEST) :
        p = getTriangolarInf(A)
        r = b - (A @ x)
        y = forwardSubstitution(p, r)
        x = x + y
        print(x)
        if(mo.checkCurrentSolution(A, x, b, tol)) :
            return x
    return None

def getTriangolarInf(A) :
    B = numpy.matrix.copy(A) #TODO: controlla se si può
    for i in range(len(B)) :
        for j in range(len(B[0])) :
            if(i < j) :
                B[i][j] = 0
    return B

def getTriangolarSup(A) :
    B = numpy.matrix.copy(A) #TODO: controlla se si può
    for i in range(len(B)) :
        for j in range(len(B[0])) :
            if(i >= j) :
                B[i][j] = 0
    return B

def forwardSubstitution(A, b) :
    x = []
    if(A[0][0] == 0) :
        return ValueError
    x.append(b[0]/A[0][0])
    for i in range(1, len(A)) :
        if(A[i][i] == 0) :
            ValueError
        x.append((b[i]-(A[i][:i] @ x[:i]))/A[i][i])
    return numpy.array(x)