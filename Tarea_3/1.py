#!/usr/bin/python
# -*- coding: utf-8 -*- 

from sympy import *


largo = 4

I = ["" for x in xrange(largo)] #Arreglo de incognitas

#arreglo y otras constantes
D = ["" for x in xrange(largo-1)]   #Arreglo de variables D

L = ["" for x in xrange(largo-1)]   #Arreglo de L

Q = 1



#condiciones de borde
I[0] = 20
I[3] = -15

#llenado vector
in_ind=0
for i in range(1,(largo-1)):
    sn = "T"+str(in_nd)
    sy = symbols(nd)
    I[i] = "T"+str(in_nd)    
    in_ind += 1

def armaMatriz(A):#Funcion para armar la matriz global, usando las 3 matrices
    #generadas a partir de los 3 elementos
    MatrizComp = zeros((len(A)+1),(len(A)+1))
    for i in range(0,len(A)):
        for j in range(0,2):
            for k in range(0,2):
                MatrizComp[i+j][i+k] = MatrizComp[i+j][i+k] + A[i][j][k]
    return MatrizComp
