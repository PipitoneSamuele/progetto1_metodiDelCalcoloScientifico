import numpy as np
import utility.Constants as constants

#matrice A deve essere simmetrica e definita positiva

def gradiente(A, b, x, tol) :
    #if check_simmetric(A) and check_def_pos(A):
    for i in range(constants.MAX_ITERATIONS_TEST) :
        r = b - (A @ x)
        print(A @ x)
        y = A @ r
        num_alpha = np.transpose(r) @ r
        den_alpha = np.transpose(r) @ y
        print(num_alpha)
        print(den_alpha)
        alpha = num_alpha/den_alpha
        x = x + (alpha * r)
    return x
    #else:
        #return 0

def check_simmetric(A):
    if np.array_equal(A, np.transpose(A)):
        return True
    else:
        return False

def check_def_pos(A):
    return np.all(np.linalg.eigvals(A) > 0)