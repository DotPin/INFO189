#!/usr/bin/python
# -*- coding: utf-8 -*- 

from sympy import *


largo = 3   #numero de elementos

V = [0 for x in xrange(largo+1)]    #vector de nodos

P = [0 for x in xrange(largo+1)]    #vector de polinomios

I = [[0 for x in xrange(2)] for in xrange(2)] #Arreglo elementos

F = [0 for x in xrange(largo)]      #arreglo vector F

#arreglo y otras constantes
D = [0 for x in xrange(largo)]   #Arreglo de variables D

L = [0 for x in xrange(largo)]   #Arreglo de L

Q = 1   #valor temperatura ambiente



#condiciones de borde
#I[0] = 20
#I[3] = -15

M=[]    #vector multidimensional


#creación multimatrices
for k in range(largo-1):
    F[k] = (Q*L[k])/2
    for i in range(2):
        for j in range(2):
            I[i][j] = D[k]/L[k] + D[k]
    M.append(I)


#llenado vector
in_ind=0
for i in range(1,(largo-1)):
    sn = "T"+str(in_nd)
    sy = symbols(nd)
    V[i] = sy    
    in_ind += 1

acm=0
for i in range(largo+1):
    for j in range(largo+1):
        acm = acm + matriz[i][j]*I[j]



def armaMatriz(A):#Funcion para armar la matriz global, usando las 3 matrices
    #generadas a partir de los 3 elementos
    MatrizComp = zeros((len(A)+1),(len(A)+1))
    for i in range(0,len(A)):
        for j in range(0,2):
            for k in range(0,2):
                MatrizComp[i+j][i+k] = MatrizComp[i+j][i+k] + A[i][j][k]
    return MatrizComp
