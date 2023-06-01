import numpy

def isCholeskyDecomposable(a) :
    """
    Metodo utilizzato per controllare se la matrice passata in input sia simmetrica e positiva

    input a: La matrice da controllare

    return True se simmetrica e positiva, False altrimenti
    """
    try:
        ch = numpy.linalg.cholesky(a)
        return True
    except numpy.linalg.LinAlgError as e:
        if e.args[0] == 'Matrix is not positive definite' :
            return False
        else :
            raise e