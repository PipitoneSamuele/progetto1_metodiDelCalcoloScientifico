import utility.Matrix_operations as op
import utility.Constants as const
import os

def relativeErrorCheck(mySolution, solution, cod_number) :
    """
    Controlla l'errore relativo della soluzione trovata dai metodi confrontandola con la soluzione corretta 
    passata in input

    param mySolution: Vettore soluzione trovato dal metodo
    param solution: Vettore soluzione del sistema lineare
    param cod_number: Numero che indica quale metodo è stato utilizzato
    """
    if(const.JACOBI[0] == cod_number) : 
        name = const.JACOBI[1]
    if(const.GAUSS_SEIDEL[0] == cod_number) : 
        name = const.GAUSS_SEIDEL[1]
    if(const.GRADIENTE[0] == cod_number) : 
        name = const.GRADIENTE[1]
    if(const.GRADIENTE_CONIUGATO[0] == cod_number) : 
        name = const.GRADIENTE_CONIUGATO[1]
    
    if(mySolution != None) :
        print("Relative error for " + name + ": ", op.calculateRelativeError(mySolution, solution))
    else :
        print("No solution found from " + name + " iterations")

def showFiles() :
    """
    Metodo usato per stampare i files presenti sotto la cartella data

    return: Il nome del file scelto dall'utente
    """
    files = [f for f in os.listdir("resources/data") if os.path.isfile(os.path.join("resources/data", f))]

    for file in files :
        file = file[:len(file)-4]
        print(file)
    return input("Inserisci il nome del file da prendere in input: ")

def showTollerance() :
    """
    Metodo usato per stampare e scegliere le tolleranze 

    return: La tolleranza scelta dall'utente
    """
    i = 1
    for tol in const.TOL :
        print(i, ")", tol)
        i += 1
    choice = int(input("Seleziona la tolleranza con un numero: "))
    return const.TOL[choice-1]