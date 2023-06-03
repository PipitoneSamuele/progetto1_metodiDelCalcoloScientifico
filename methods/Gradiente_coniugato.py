import utility.Constants as constants
import utility.Matrix_operations as mo

def gradiente_coniugato(A, b, x, tol, d=None) :
    """Input: A (matrice), b (vettore), x (vettore), d(vettore), tol (numero)
    Risolve il sistema Ax = b tramite il metodo del gradiente coniugato.
    Permette un massimo di 20000 iterazioni di esso, oppure quando si raggiunge una tolleranza pari a tol.
    Output: x: vettore dei risultati.
    """
    x = x.transpose()
    if d == None:
        d = b - A @ x # se d non è specificata allora d = r
    for i in range(constants.MAX_ITERATIONS) :
        r = b - A @ x
        y = A @ d
        z = A @ r
        num_alpha = d.transpose().dot(r)
        den_alpha = d.transpose().dot(y)
        alpha = num_alpha[0,0] / den_alpha[0,0]
        x = x + alpha * d
        r = b - A @ x
        w = A @ r
        num_beta = d.transpose().dot(w)
        den_beta = d.transpose().dot(y)
        beta = num_beta[0,0] / den_beta[0,0]
        d = r - beta * d
        if(mo.checkSparseSolution(A, x.transpose(), b, tol)) :
                print("iterazione ", i+1, " ha trovato soluzione")
                return x
    return None #se ritorna none vuol dire che non converge