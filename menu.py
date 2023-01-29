import numpy as np

def IngresarElementoMatriz(Fila,Columna):
    Matriz = []
    for i in range(Fila):
        Fila_x = []
        for j in range(Columna):
            while True:
                try:
                    Elemento = float(input("Elemento (%d,%d): " %(i,j)))
                except:
                    continue
                break
            Fila_x.append(Elemento)
        Matriz.append(Fila_x)
    return Matriz

def Pedir_ValidarDatoEntero(FilaColumna):
    while True:
        try:
            fila_columna = int(input(f"{FilaColumna}:").lower().replace(" ",""))
        except :
            print("¡¡Digite bien!!")
            continue
        return fila_columna

def ProductoMatrices():
    print("\n\tMultiplicación de dos Matrices")
    Fila = "Fila" ; Columna = "Columna"
    print("\nPara el primer Matriz")
    Filax = Pedir_ValidarDatoEntero(Fila) ; Columnax = Pedir_ValidarDatoEntero(Columna)
    print("\nPara el segundo Matriz")
    Filay = Pedir_ValidarDatoEntero(Fila) ; Columnay = Pedir_ValidarDatoEntero(Columna) 
    if Columnax == Filay:
        print("Llenando primer Matriz...")
        MatrizA=IngresarElementoMatriz(Filax,Columnax) ; Matriz1 = np.array(MatrizA)
        print("Llenando segundo Matriz...")
        MatrizB=IngresarElementoMatriz(Filay,Columnay) ; Matriz2 = np.array(MatrizB)
        Producto =[]
        for i in range (len(MatrizA)):
            Producto.append([0]*len(MatrizB))
            for j in range (len(MatrizB[0])):
                for k in range (len(MatrizB)):
                    Producto[i][j] += MatrizA[i][k]*MatrizB[k][j]
        resultado = np.array(Producto)
        print("\n\tMatriz A\n", Matriz1)
        print("\n\tMatriz B\n", Matriz2)
        print("\nSu Producto de las matrices es:")
        print(resultado)
    else:
        print("Recuerde la multiplicación entre dos matrices debe ser mxn * nxp")

#Menú General
while True:
    #print("\tBIENVENIDO")
    print("\n\tCALCULADORA DE MATRICES")
    print("""
    [P] PRODUCTO 
    [S] SUMA
    [R] RESTA
    [I] INVERSA
    [D] DETERMINANTE
    [0] SALIR """)
    Opcion=input("--->").lower().replace(" ", "")
    listaOpciones=["P", "S", "R","I","D","0","p","s","r","i","d", "PRODUCTO", "SUMA", "RESTA", "INVERSA", "DETERMINANTE",
                   "producto","suma","resta","inversa","determinante"]
    while Opcion in listaOpciones:
        if Opcion =="P" or Opcion=="p" or Opcion=="PRODUCTO" or Opcion=="producto":
            ProductoMatrices()
            break
        elif Opcion=="S" or Opcion=="s" or Opcion=="SUMA" or Opcion=="suma":
            #sumamatrices()
            break
        elif Opcion =="R" or Opcion=="r" or Opcion=="RESTA" or Opcion=="resta":
            #restamatrices()
            break
        elif Opcion=="I" or Opcion=="i" or Opcion=="INVERSA" or Opcion=="inversa":
            #inversamatrices()
            break
        elif Opcion=="D" or Opcion=="d" or Opcion=="DETERMINANTE" or Opcion=="determinante":
            #determinantematrices()
            break
    if Opcion not in listaOpciones:
            print("\n¡¡Digite Opción correcta!!")
            continue
    else:
        if Opcion=="0" or Opcion== "salir" or Opcion == "OPCION":
            break
print("Fin del programa")
