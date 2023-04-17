from scipy.io import mmread
import utility.Constants as constants

a = mmread("progetto1_metodiDelCalcoloScientifico\\resources\data\spa1.mtx")

# x: vettore della soluzione esatta inizializzato a tutti 1
x = [1] * len(a.A) 

# b: vettore della soluzione del sistema
b = a * x 

# tol: lista delle tolleranze con il quale testare i vari metodi
tol = constants.TOL

# calcolo delle soluzioni approssimate TODO

# calcolo degli errori relativi, numero iterazioni e tempo di calcolo TODO

print(x)
print(b)