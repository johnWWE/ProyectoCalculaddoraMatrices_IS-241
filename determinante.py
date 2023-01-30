import numpy as np
#a=[[1,2,3,4,5],[1,4,12,31,5],[1,2,4,7,6],[1,9,8,7,0],[10,11,12,13,16]]
#def calculatorDeterminantMatrix(matriz):
#    determinante = np.linalg.det(matriz)
#    return determinante
#print(calculatorDeterminantMatrix(a)) 
matriz=[]
respuesta=[]
def mat(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz
def llenar(n):
    matriz=mat(n)
    for x in range(n):
        for y in range(n):
            matriz[x][y] = float(input(f"Valor de la fila {x+1} y columna {y+1}: "))
        respuesta.append(float(input("Valor de la constante de la ecuacion "+str(x+1)+" = " )))

def gjordan(n):
    for z in range(n-1,0,-1):
        for x in range (z):
            if (matriz[z][z]!=0):
                p =matriz[x][z]/matriz[z][z]
                matriz[x][z]=matriz[x][z]-(matriz[z][z]* p)
                respuesta[x]=respuesta[x]-(respuesta[z]*p)
def gaussJordan(n):
    for z in range(n-1,0,-1):
        for x in range(z):
            if (matriz[z][z] !=0 ):
                p= matriz[x][z]/matriz[z][z]
                matriz[x][z]=matriz[x][z]-(matriz[z][z]*p)
                respuesta[x]=respuesta[x] - (respuesta[z]*p)
def deter(n):
    det=1
    for x in range(n):
        det =matriz[x][x]*det
    print("\nEl valor de la determinante de la matriz es =",det)
#Programa   
n=int(input("Tamaño  de la matriz: "))
llenar(n)
gjordan(n)
gaussJordan(n)
deter(n)


