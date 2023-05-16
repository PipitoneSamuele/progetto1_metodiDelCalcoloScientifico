import utility.Constants as constants
import utility.Matrix_operations as mo

def gradiente_coniugato(A, b, x, d, tol) :
    """Input: A (matrice), b (vettore), x (vettore), d(vettore), tol (numero)
    Risolve il sistema Ax = b tramite il metodo del gradiente coniugato.
    Permette un massimo di 20000 iterazioni di esso, oppure quando si raggiunge una tolleranza pari a tol.
    Output: x: vettore dei risultati.
    """
    x = x.transpose()
    b = b.transpose()
    d = d.transpose()
    for i in range(constants.MAX_ITERATIONS_TEST) :
        r = b - A @ x
        y = A @ d
        z = A @ r
        alpha = d.dot(r) / d.dot(y)
        x = x + alpha * d
        r = b - A @ x
        w = A @ r
        beta = d.dot(w) / d.dot(y)
        d = r - beta * d
        if(mo.checkSparseSolution(A, x.transpose(), b.transpose(), tol)) :
                print("iterazione ", i, " ha trovato la soluzione: ", x)
                return x
    return None #se ritorna none vuol dire che non converge