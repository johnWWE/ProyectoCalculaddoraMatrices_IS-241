#1. Suma, resta, multiplicación de matrices.


import numpy as np

filas    =int(input("Ingrese en números enteros la filas de la matriz: "))
columnas =int(input("Ingrese en números enteros las columnas de la matriz: "))

def crear_matriz(filas,columnas):
    f=-1
    c=-1
    e_fil=[]
    for i in range(0,filas):
        e_col=[]
        f +=1
        for j in range(0,columnas):
            c +=1
            valor = int(input(f"ingrese el valor del componente {i},{j}="))
            e_col.append(valor)
        e_fil.append(e_col)
    return e_fil


matrizA= np.array(crear_matriz(filas, columnas))
matrizB= np.array(crear_matriz(filas, columnas))


suma= matrizA + matrizB
resta=matrizA - matrizB
multiplicacion = matrizA*matrizB

print(f"Suma de matrices: \n{suma} \n\n Resta de matrices : \n{resta} \n\n Multiplicación de matrices: \n{multiplicacion} ")