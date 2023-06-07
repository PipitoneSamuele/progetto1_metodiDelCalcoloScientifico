from scipy.io import mmread
import scipy.sparse as sparse
import sys, time
from utility import IOUtility as io, Constants as constants, Matrix_checks as check
from methods import Jacobi as ja, Gauss_Seidel as gs, Gradiente as grad, Gradiente_coniugato as grad_conj

matrixString = io.showFiles()

a = mmread("resources/data/" + matrixString + ".mtx")

t0 = time.time()

a_dense = a.toarray()
if(not check.isCholeskyDecomposable(a_dense)) :
    sys.exit("Matrix is not symmetric positive")

tol = io.showTollerance()

t_check = time.time()

x_solution = sparse.coo_array([1.0] * len(a.A))
x_approx = sparse.coo_array([0.0] * len(a.A))

b = a @ x_solution.transpose()

sol_jacobi = ja.jacobi(a, b, x_approx, tol)
t_jacobi = time.time()
print("Tempo di Jacobi: ", t_jacobi - t_check)

sol_gauss = gs.gauss_seidel(a, b, x_approx, tol)
t_gauss = time.time()
print("Tempo di Gauss Seidel: ", t_gauss - t_jacobi)

sol_gradient = grad.gradiente(a, b, x_approx, tol)
t_gradient = time.time()
print("Tempo del Gradiente : ", t_gradient - t_gauss)

sol_conj_gradient = grad_conj.gradiente_coniugato(a, b, x_approx, tol)
t_conj_gradient = time.time()
print("Tempo di Gradiente coniugato: ", t_conj_gradient - t_gradient)

io.relativeErrorCheck(sol_jacobi, x_solution, 1)
io.relativeErrorCheck(sol_gauss, x_solution, 2)
io.relativeErrorCheck(sol_gradient.transpose(), x_solution, 3)
io.relativeErrorCheck(sol_conj_gradient.transpose(), x_solution, 4)