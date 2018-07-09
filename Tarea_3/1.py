#!/usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np


largo = 3   #numero de elementos



I = [[0.0 for x in xrange(2)] for x in xrange(2)] #Arreglo elementos

F = [0.0 for x in xrange(largo+1)]      #arreglo vector F

#arreglo y otras constantes
D = [0.0 for x in xrange(largo)]   #Arreglo de variables D

L = [0.0 for x in xrange(largo)]   #Arreglo de L

Q = 1.0   #valor temperatura ambiente

for i in range(largo):
    D[i] = float(input("Ingrese un numero para D: "))
    L[i] = float(input("Ingrese un numero para L: "))

#condiciones de borde
#I[0] = 20
#I[3] = -15

M=[]    #vector multidimensional

#creación multimatrices
for k in range(largo):
    for i in range(2):
        for j in range(2):
            I[i][j] = D[k]/L[k]
    M.append(I)


def armaMatriz(A):#Funcion para armar la matriz global, usando las 3 matrices
    #generadas a partir de los 3 elementos
    MatrizComp = [[0.0 for x in xrange(len(A)+1)] for x in xrange(len(A)+1)]
    for i in range(0,len(A)):
        for j in range(0,2):
            for k in range(0,2):
                MatrizComp[i+j][i+k] = MatrizComp[i+j][i+k] + A[i][j][k]
    return MatrizComp

F[0]=(Q*L[0])/2

for j in range(largo):
    F[j+1] = F[j] + (Q*L[j])/2

F[len(F)-1] = (Q*L[j])/2
    
gb = []
gb = armaMatriz(M)

print(gb)
print(F)


c = np.linalg.solve(gb, F)    #entrega resultado de vector x

print(c)

