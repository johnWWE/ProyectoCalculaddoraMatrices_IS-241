def sumaMatrices():
    print("\n\tSuma de dos Matrices")
    Fila = "Fila" ; Columna = "Columna"
    print("\nPara la primera Matriz")
    Filax = Pedir_ValidarDatoEntero(Fila) ; Columnax = Pedir_ValidarDatoEntero(Columna)
    print("\nPara la segunda Matriz")
    Filay = Pedir_ValidarDatoEntero(Fila) ; Columnay = Pedir_ValidarDatoEntero(Columna)
    if Columnax == Columnay and Filax == Filay:
        print("Llenando primera Matriz...")
        MatrizA=IngresarElementoMatriz(Filax,Columnax) ; Matriz1 = np.array(MatrizA)
        print("Llenando segunda Matriz...")
        MatrizB=IngresarElementoMatriz(Filay,Columnay) ; Matriz2 = np.array(MatrizB)
        Suma =[]
        for i in range (Filax):
            Suma.append( [0] * Columnax)
            for j in range(Columnax):
                Suma[i][j] += MatrizA[i][j] + MatrizB[i][j]

        resultado = np.array(Suma)
        print("\n\tMatriz A\n", Matriz1)
        print("\n\tMatriz B\n", Matriz2)
        print("\nLa suma de las matrices es:")
        print(resultado)
    else:
        print("Recuerde la suma entre dos matrices debe ser de la misma dimension de filas y columnas")
#RESTA DE MATRICES
def restaMatrices():
    print("\n\tSuma de dos Matrices")
    Fila = "Fila" ; Columna = "Columna"
    print("\nPara la primera Matriz")
    Filax = Pedir_ValidarDatoEntero(Fila) ; Columnax = Pedir_ValidarDatoEntero(Columna)
    print("\nPara la segunda Matriz")
    Filay = Pedir_ValidarDatoEntero(Fila) ; Columnay = Pedir_ValidarDatoEntero(Columna)
    if Columnax == Columnay and Filax == Filay:
        print("Llenando primera Matriz...")
        MatrizA=IngresarElementoMatriz(Filax,Columnax) ; Matriz1 = np.array(MatrizA)
        print("Llenando segunda Matriz...")
        MatrizB=IngresarElementoMatriz(Filay,Columnay) ; Matriz2 = np.array(MatrizB)
        Resta =[]
        for i in range (Filax):
            Resta.append( [0] * Columnax)
            for j in range(Columnax):
                Resta[i][j] += MatrizA[i][j] - MatrizB[i][j]

        resultado = np.array(Resta)
        print("\n\tMatriz A\n", Matriz1)
        print("\n\tMatriz B\n", Matriz2)
        print("\nLa resta de las matrices es:")
        print(resultado)
    else:
        print("Recuerde la resta entre dos matrices debe ser de la misma dimension de filas y columnas")