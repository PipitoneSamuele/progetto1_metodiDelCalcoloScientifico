from scipy.io import mmread
import utility.Constants as constants
import methods.Jacobi as ja
import methods.Gauss_Seidel as gs
import methods.Gradiente as grad
import methods.Gradiente_coniugato as grad_conj
import scipy.sparse as sparse
import utility.Matrix_operations as op
import utility.Matrix_checks as check
import sys
import time
import os

files = [f for f in os.listdir("resources/data") if os.path.isfile(os.path.join("resources/data", f))]

for file in files :
    file = file[:len(file)-4]
    print(file)

matrixString = input("Insert the name of the file containing the input matrix (from the above list): ")

a = mmread("resources/data/" + matrixString + ".mtx")

t0 = time.time()

a_dense = a.toarray()
if(not check.isCholeskyDecomposable(a_dense)) :
    sys.exit("Matrix is not symmetric positive")

t_check = time.time()
print("Check time: ", t_check - t0)

x_solution = sparse.coo_array([1.0] * len(a.A))
x_approx = sparse.coo_array([0.0] * len(a.A))

b = a @ x_solution.transpose()

tol = constants.TOL

# calcolo delle soluzioni approssimate TODO
sol_jacobi = jacobi_solution = ja.jacobi(a, b, x_approx, constants.TOL[0])
t_jacobi = time.time()
print("Jacobi time: ", t_jacobi - t_check)

sol_gauss = gauss_solution = gs.gauss_seidel(a, b, x_approx, constants.TOL[0])
t_gauss = time.time()
print("Gauss Seidel time: ", t_gauss - t_jacobi)

sol_gradient = gradient_solution = grad.gradiente(a, b, x_approx, constants.TOL[0])
t_gradient = time.time()
print("Gradient time: ", t_gradient - t_gauss)

sol_conj_gradient = conj_gradient_solution = grad_conj.gradiente_coniugato(a, b, x_approx, constants.TOL[0])
t_conj_gradient = time.time()
print("Conjugate Gradient time: ", t_conj_gradient - t_gradient)

# calcolo degli errori relativi, numero iterazioni e tempo di calcolo TODO
if(sol_jacobi != None) :
    print("Relative error for Jacobi: ", op.calculateRelativeError(sol_jacobi, x_solution))
else :
    print("No solution found from Jacobi iterations")
if(sol_gauss != None) :
    print("Relative error for Gauss_Seidel: ", op.calculateRelativeError(sol_gauss, x_solution))
else :
    print("No solution found from Gauss iterations")
if(sol_gradient != None) :
    print("Relative error for Gradient: ", op.calculateRelativeError(sol_gradient.transpose(), x_solution))
else :
    print("No solution found from Gradient iterations")
if(sol_conj_gradient != None) :
    print("Relative error for Conjugate Gradient: ", op.calculateRelativeError(sol_conj_gradient.transpose(), x_solution))
else :
    print("No solution found from Conjugate Gradient iterations")