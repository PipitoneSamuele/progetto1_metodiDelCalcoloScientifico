import utility.Constants as constants
import utility.Matrix_operations as mo

def gradiente(A, b, x, tol) :
    """Input: A (matrice), b (vettore), x (vettore), tol (numero)
    Risolve il sistema Ax = b tramite il metodo del gradiente.
    Permette un massimo di 20000 iterazioni di esso, oppure quando si raggiunge una tolleranza pari a tol.
    Output: x: vettore dei risultati.
    """
    #TODO sistemare la divisione num_alpha / den_alpha per valori piccoli
    x = x.transpose()
    b = b.transpose()
    for i in range(constants.MAX_ITERATIONS_TEST) :
        r = b - A @ x
        y = A @ r
        num_alpha = r.transpose().dot(r)
        den_alpha = r.transpose().dot(y)
        alpha = num_alpha[0,0] / den_alpha[0,0]
        print(alpha)
        x = x + alpha * r
        if(mo.checkSparseSolution(A, x.transpose(), b.transpose(), tol)) :
                print("iterazione ", i, " ha trovato la soluzione: ", x)
                return x
    return None #se ritorna none vuol dire che non converge