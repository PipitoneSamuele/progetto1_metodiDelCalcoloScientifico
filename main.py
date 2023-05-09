from scipy.io import mmread
import utility.Constants as constants
import methods.Jacobi as jacobi
import scipy.sparse as sparse

a = mmread("progetto1_metodiDelCalcoloScientifico\\resources\data\spa1.mtx")

# x: vettore della soluzione esatta inizializzato a tutti 1
build = [1] * len(a.A)
x = sparse.coo_array(build)

# b: vettore della soluzione del sistema
# TODO: controlla che il b ottenuto sia corretto
b = a @ x.transpose()

# tol: lista delle tolleranze con il quale testare i vari metodi
tol = constants.TOL

# calcolo delle soluzioni approssimate TODO
jacobi.jacobi(a, b.transpose(), x, constants.TOL_TEST)

# calcolo degli errori relativi, numero iterazioni e tempo di calcolo TODO
print(x)