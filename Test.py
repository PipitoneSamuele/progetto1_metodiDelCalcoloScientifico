#Classe usata per testare funzioni in altre classi o funzionalità che stiamo sviluppando

import scipy.sparse as sparse
import methods.Gauss_Seidel as gauss
import methods.Jacobi as jacobi
import methods.Gradiente as grad
import methods.Gradiente_coniugato as grad_con

A = sparse.coo_matrix([[4.0, 1.0, -2.0], [-1.0, 4.0, -1.0], [1.0, -1.0, 4.0]])
b = sparse.coo_array([4.0, 0.0, 4.0])
x = sparse.coo_array([1.0, 1.0, 1.0])



#gauss.gauss_seidel(A, b, x, 0.001)
#jacobi.jacobi(A, b, x, 0.001)

grad.gradiente(A, b, x, 0.001)
#grad_con.gradiente_coniugato(A, b, x, x, 0.001)
