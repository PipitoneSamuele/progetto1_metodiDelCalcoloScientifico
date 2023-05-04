import numpy as np
import utility.Constants as constants

#matrice A deve essere simmetrica e definita positiva

def gradiente(A, b, x, tol) :
    """Input: A (matrice), b (vettore), x (vettore), tol (numero)
    Risolve il sistema Ax = b tramite il metodo del gradiente.
    Permette un massimo di 20000 iterazioni di esso, oppure quando si raggiunge una tolleranza pari a tol.
    Output: x: vettore dei risultati.
    """
    #TODO: aggiungere limite per tol
    for i in range(constants.MAX_ITERATIONS_TEST) :
        r = b - (A @ x)
        y = A @ r
        num_alpha = np.transpose(r) @ r
        den_alpha = np.transpose(r) @ y
        alpha = num_alpha/den_alpha
        x = x + (alpha * r)
    return x

# TODO:  verificare se funziona correttamente
def check_simmetric(A):
    """Input: A (matrice)
    Controlla se la matrice A é simmetrica confrontandola con la sua trasposta.
    Output: True se la matrice é simmetrica, False altrimenti.
    """
    return np.array_equal(A, np.transpose(A))

# TODO:  verificare se funziona correttamente
def check_def_pos(A):
    """Input: A (matrice)
    Controlla se la matrice A é definita positiva controllando se i suoi autovalori sono strettamente maggiori di 0.
    Output: True se la matrice é definita positiva, False altrimenti.
    """
    return np.all(np.linalg.eigvals(A) > 0)