from scipy.io import mmread
import utility.Constants as constants
import methods.Jacobi as ja
import methods.Gauss_Seidel as gs
import methods.Gradiente as grad
import methods.Gradiente_coniugato as grad_conj
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
sol_jacobi = jacobi_solution = ja.jacobi(a, b, x_test, constants.TOL[3])
sol_gauss = gauss_solution = gs.gauss_seidel(a, b, x_test, constants.TOL[3])
#grad.gradiente(a, b, x_test, constants.TOL[0])
#grad_conj.gradiente_coniugato(a, b, x_test, constants.TOL[0])

# calcolo degli errori relativi, numero iterazioni e tempo di calcolo TODO
if(sol_jacobi != None) :
    print("relative error for Jacobi: ", op.calculateRelativeError(sol_jacobi, x_soluzione))
else :
    print("No solution found from Jacobi iterations")
if(sol_gauss != None) :
    print("relative error for Gauss_Seidel: ", op.calculateRelativeError(sol_gauss, x_soluzione))
else :
    print("No solution found from Gauss iterations")