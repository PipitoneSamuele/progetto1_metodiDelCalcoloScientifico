import numpy

def gaub_seidel(A, b, x, tol) :
    return False

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