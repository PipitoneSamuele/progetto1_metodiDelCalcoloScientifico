import numpy

#https://atozmath.com/example/CONM/GaussEli.aspx?q=GS2&q1=E1

def gauss_seidel(A, b, x, tol) :
    p = getTriangolarInf(A)
    r = b - (A @ x)
    y = forwardSubstitution(p, b)
    x = 1
    return x

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