import utility.Constants as constants
import utility.Matrix_operations as mo

def gradiente(A, b, x, tol) :
    """Input: A (matrice), b (vettore), x (vettore), tol (numero)
    Risolve il sistema Ax = b tramite il metodo del gradiente.
    Permette un massimo di 20000 iterazioni di esso, oppure quando si raggiunge una tolleranza pari a tol.
    Output: x: vettore dei risultati.
    """
    x = x.transpose()
    for i in range(constants.MAX_ITERATIONS) :
        r = b - A @ x
        y = A @ r
        num_alpha = r.transpose().dot(r)
        den_alpha = r.transpose().dot(y)
        alpha = num_alpha[0,0] / den_alpha[0,0]
        x = x + alpha * r
        if(mo.checkSparseSolution(A, x.transpose(), b, tol)) :
                print("iterazione ", i+1, " ha trovato soluzione")
                return x
    return None #se ritorna none vuol dire che non converge