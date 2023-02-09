import numpy as np
import sys
class Matriz:
    def __init__(self,nfilas,ncolumnas):
        self.nfilas = nfilas
        self.ncolumnas = ncolumnas
        self.matriz=[]
        self.matrizMxN=False
        self.matriz_cuadrada=False
        self.operacion=""
    def optenerDatos(self):
        for i in range(0,self.nfilas):
            self.matriz.append([])
            for j in range(0,self.ncolumnas):
                while True:
                    try:
                        valor=int(input(f"Ingrese elemento de la matrix en la posicion {(i+1,j+1)}--> "))
                        break
                    except ValueError as e:
                        print("Ingesaste un caracter no válido vuelve a ingresar los valores. Error de tipo: {0}".format(e))

                self.matriz[i].append(valor)
        return self.matriz   
    def pedirDatos(dato):
            valor=-1
            while valor<0:
                try:
                    valor=int(input(dato))
                    if valor<0:
                        print("Los datos deben ser positivos.")
                except:
                    print("Ingresó un caracter no válido.")
            return valor
    def verificarMatriz(self):
        if self.nfilas==self.ncolumnas:
            self.matriz_cuadrada=True
            return self.matriz_cuadrada
    def MostrarMatriz(self):
      
        for i in range(self.nfilas): 
            print("[",end="")
            for j in range(self.ncolumnas):
                print(self.matriz[i][j],end="")
            print("]")
        print() 

def inversaM(self):
        self.MostrarMatriz()
        if self.verificarMatriz():
            return np.linalg.inv(self.matriz)
        else:
            return ("La matriz a ingresar debe ser 'cuadrada'")

