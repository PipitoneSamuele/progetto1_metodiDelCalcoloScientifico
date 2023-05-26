from scipy.io import mmread
import utility.Constants as constants
import methods.Jacobi as jacobi
import methods.Gauss_Seidel as gauss
import methods.Gradiente as grad
import scipy.sparse as sparse
import utility.Matrix_operations as op

a = mmread("resources/data/spa1.mtx")

# x_soluzione: vettore della soluzione esatta inizializzato a tutti 1
x_soluzione = sparse.coo_array([1.0] * len(a.A))
x_test = sparse.coo_array([0.0] * len(a.A))

# b: vettore della soluzione del sistema
b = a @ x_soluzione.transpose()

# tol: lista delle tolleranze con il quale testare i vari metodi
tol = constants.TOL

# calcolo delle soluzioni approssimate TODO
#jacobi_solution = jacobi.jacobi(a, b, x_test, constants.TOL[0]) #ci mette tante iterazioni
gauss_solution = gauss.gauss_seidel(a, b, x_test, constants.TOL[0])

#grad.gradiente(a, b, x, constants.TOL_TEST)
# calcolo degli errori relativi, numero iterazioni e tempo di calcolo TODO
#print("relative error: ", op.calculateRelativeError(jacobi_solution, x_soluzione))