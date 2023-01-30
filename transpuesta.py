def matrizTranspuesta():

    filas_MatrizA=  int(input("Ingrese la cantidad de filas de la matriz A: "))
    columnas_MatrizA=  int(input("Ingrese la cantidad de columnas de la matriz A: "))
    print("La matriz que usted acaba de introdducir es de orden ", filas_MatrizA,"*", columnas_MatrizA)
#creando una matriz
    matrizA  = []
    for i in range(filas_MatrizA):
        matrizA.append([0]* columnas_MatrizA)

#rellenando la matriz A
    for fila in range(filas_MatrizA):
        for columna in range(columnas_MatrizA):
        #usemos excepciones para evitar errores no previstos, es error si el usuaario introduce
        # un dato que no sea numerico
            while True:
                try:
                    matrizA[fila][columna]= float(input(f'Ingrese el valor en la posicion {fila+1},{columna+1}: '))
                    break
                except ValueError:
                    print('Solo es admisible valores numericos, intente de nuevo => ')#mensaje para poer un numero

#mostrando la matrizA
    print('\nMatriz A \n')
    for i in matrizA:
        print(i)

 # otra matriz vacia para aalmacenar la transpuesta
    matrizTranspuesta = []
    for i in range(columnas_MatrizA):
        matrizTranspuesta.append([0]* filas_MatrizA)

    for fila in range(columnas_MatrizA):
            for columna in range(filas_MatrizA):
                matrizTranspuesta[fila][columna] = matrizA[columna][fila] #es transpuesta cuando se cambia las filas por las columnas
#imprimir la matriz transpuesta
    print('\nMatriz Transpuesta de A \n')
    for i in matrizTranspuesta:
        print(i)
matrizTranspuesta()
#sdsdcddd