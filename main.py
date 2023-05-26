from scipy.io import mmread
import utility.Constants as constants
import methods.Jacobi as jacobi
import methods.Gradiente as grad
import scipy.sparse as sparse

a = mmread("resources/data/spa1.mtx")

# x: vettore della soluzione esatta inizializzato a tutti 1
x_vera = sparse.coo_array([1.0] * len(a.A))
x_test = sparse.coo_array([0.0] * len(a.A))

# b: vettore della soluzione del sistema
# TODO: controlla che il b ottenuto sia corretto
#b = a @ x.transpose()
b = a @ x_vera.transpose()

# tol: lista delle tolleranze con il quale testare i vari metodi
tol = constants.TOL

# calcolo delle soluzioni approssimate TODO
jacobi.jacobi(a, b, x_test, constants.TOL[3])

#grad.gradiente(a, b, x, constants.TOL_TEST)
# calcolo degli errori relativi, numero iterazioni e tempo di calcolo TODO
