import numpy

def isCholeskyDecomposable(a) :
    try:
        ch = numpy.linalg.cholesky(a)
        return True
    except numpy.linalg.LinAlgError as e:
        if e.args[0] == 'Matrix is not positive definite' :
            return False
        else :
            raise e