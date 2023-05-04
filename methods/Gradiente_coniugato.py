import numpy as np
import utility.Constants as constants

#matrice A deve essere simmetrica e definita positiva

def gradiente_coniugato(A, b, x, d, tol) :
    """Input: A (matrice), b (vettore), x (vettore), d(vettore), tol (numero)
    Risolve il sistema Ax = b tramite il metodo del gradiente coniugato.
    Permette un massimo di 20000 iterazioni di esso, oppure quando si raggiunge una tolleranza pari a tol.
    Output: x: vettore dei risultati.
    """
    #TODO: aggiungere limite per tol
    for i in range(constants.MAX_ITERATIONS_TEST) :
        r = b - (A @ x)
        y = A @ d
        z = A @ r
        alpha = (d * r) / (d * y)
        x = x + (alpha * d)
        r = b - A @ x
        w = A @ r
        beta = (d * w) / (d * y)
        d = r - beta * d
    return x