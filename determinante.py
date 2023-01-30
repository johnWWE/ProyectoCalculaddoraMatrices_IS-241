import numpy as np
a=[[1,2,3,4,5],[1,4,12,31,5],[1,2,4,7,6],[1,9,8,7,0],[10,11,12,13,16]]
def calculatorDeterminantMatrix(matriz):
    determinante = np.linalg.det(matriz)
    return determinante
print(calculatorDeterminantMatrix(a)) 
