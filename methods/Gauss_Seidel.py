import numpy

#https://atozmath.com/example/CONM/GaussEli.aspx?q=GS2&q1=E1

def gauss_seidel(A, b, x, tol) :
    p = getTriangolarInf(A)
    r = b - (A @ x)
    print("r: ", r)
    y = forwardSubstitution(p, b)
    print("y: ", y)
    x = x + y
    print("x: ", x)
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
    if(A[0][0] == 0) :
        return ValueError
    x = b/A[0][0]
    for i in range(2, len(A)) :
        if(A[i][i] == 0) :
            ValueError
        x = (b[i]-(A[i][i]*x))/A[i][i]
    return x