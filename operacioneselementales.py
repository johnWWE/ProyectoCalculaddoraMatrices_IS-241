
def operacionesElementales(self,A,n,m):
        while True:
            print(f'\nOPERACIONES ELEMENTALES\n')
            print(" a) Por filas \n b) Por columnas \n c) Salir")
            operacion=input("Ingrese la operacion a realizar: ").lower() 
            if (operacion=="a"):
                while True:
                    print("\n================================")
                    print(" [1] Intercambiar filas \n [2] Multiplicar fila por un escalar \n [3] Obtener fila por medio de suma y multiplicación \n [4]Volver")
                    opc=int(input("\nIngrese valor: "))
                    if opc==1:
                        print('\n Matriz inicial\n')
                        print(np.matrix(A))
                        f1 = int(input('\nIngresar la fila 1 a intercambiar: '))
                        f2 = int(input('Ingresar la fila 2 a intercambiar: \n'))
                        for i in range(0,n):
                            aux = A[f1-1][i]
                            A[f1-1][i]=A[f2-1][i]
                            A[f2-1][i]=aux
                        for i in range (0, 1):
                            for j in range (0,m):
                                lista = []
                                lista.append (A[j])
                                print(lista)
                        print()
                    elif  opc==2:
                        print('\n Matriz inicial\n')
                        print(np.matrix(A))
                        f = int(input('\nIngresar fila: '))
                        numero = int(input('Valor del escalar: \n'))
                        for i in range(n):
                            aux = A[f-1][i]
                            A[f-1][i]=A[f-1][i]*numero
                        print(np.matrix(A))
                    elif opc == 3:
                        print('\n Matriz inicial\n')
                        print(np.matrix(A))
                        f1 = int(input('\nIngresar fila 1: '))
                        f2 = int(input('Ingresar fila 2: '))
                        numero = int(input('Valor del multiplicador: \n'))
                        for i in range(0,n):
                            aux = A[f1-1][i]
                            A[f1-1][i]=A[f1-1][i]*numero + A[f2-1][i]
                        print(np.matrix(A))
                    elif opc==4:
                        break
            elif (operacion=="b"):
                while True:
                    print("\n================================")
                    print(" [1] Intercambiar columnas \n [2] Multiplicar columna por un escalar \n [3] Obtener columna por medio de suma y multiplicación \n [4]Volver")
                    opc=int(input("\nIngrese valor: "))
                    if opc==1:
                        print('\n Matriz inicial\n')
                        print(np.matrix(A))
                        c1 = int(input('\nIngresar la columna 1 a intercambiar: '))
                        c2 = int(input('Ingresar la columna 2 a intercambiar: \n'))
                        print()
                        for j in range(0,m):
                            aux = A[j][c1-1]
                            A[j][c1-1]=A[j][c2-1]
                            A[j][c2-1]=aux
                        for j in range (0, 1):
                            for i in range(0, n):
                                lista = []
                                lista.append (A[i])
                                print(lista)
                        print()
                    elif  opc==2:
                        print('\n Matriz inicial\n')
                        print(np.matrix(A))
                        c = int(input('\nIngresar columna: '))
                        numero = int(input('Valor del multiplicador: \n'))
                        for j in range(0,m):
                            aux = A[j][c-1]
                            A[j][c-1]=A[j][c-1] * numero
                        print (np.matrix(A))
                    elif opc == 3:
                        print('\n Matriz inicial\n')
                        print(np.matrix(A))
                        c1 = int(input('\nIngresar columna 1: '))
                        c2 = int(input('Ingresar columna 2: '))
                        n = int(input('Valor del multiplicador: \n'))
                        for j in range(0,m):
                            aux = A[c1-1][i]
                            A[c1-1][i]=A[c1-1][i]*numero + A[c2-1][i]
                        print(np.matrix(A))
                    elif opc==4:
                        break
            else:
                break