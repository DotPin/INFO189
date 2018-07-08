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

def armaMatriz(A,B,C):#Funcion para armar la matriz global, usando las 3 matrices
    #generadas a partir de los 3 elementos
    MatrizComp = zeros(4,4) #Creo una matriz simbolica de 4X4 dado que hay 4 nodos.
    counter = 0
    MatrizComp = añadeMatriz(MatrizComp,A,counter)
    counter = 1
    MatrizComp = añadeMatriz(MatrizComp,B,counter)
    counter = 2 
    MatrizComp = añadeMatriz(MatrizComp,C,counter)
    print MatrizComp
    return MatrizComp

def añadeMatriz(A,B,C):
    for (i=0; i < 2; i++):
        for (j=0;j<2; j++):
            A[i+C][j+C] = A[i+C][j+C] + B[i][j]
    return A