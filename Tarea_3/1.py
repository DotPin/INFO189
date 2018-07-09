#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

# Valores por defecto van aqui

largo = 3  # numero de elementos

# arreglo y otras constantes
D = [0.02, 0.005, 0.0035]  # Arreglo de variables D

L = [1.3, 8, 2.5]  # Arreglo de L

while True:
    temp = raw_input("Si/No editar variables: ")
    if temp not in ('si','Si','no','No'):
        print("Escriba una respuesta valida: ")
        continue
    if (temp == 'si' or temp =='Si'):
        while True:
            try:
                largo = int(raw_input("Ingrese numero de elementos: "))
            except ValueError:
                print("Ingrese un numero valido, positivo mayor que 2.")
                continue
            if not largo > 2:
                print("Ingrese un numero valido, positivo mayor que 2.")
                continue
            if largo >= 2:
                break
        D = []
        counter = 1
        for i in range(0,largo):
            while True:
                try:
                    temp = float(raw_input("Ingrese valor "+str(counter)+" de D: "))
                except ValueError:
                    print("Ingrese un numero valido, positivo.")
                    continue
                if not temp > 0:
                    print("Ingrese un numero valido, positivo.")
                    continue
                else:
                    counter = counter + 1
                    D.append(temp)
                    break
        L = []
        counter = 1
        for i in range(0,largo):
            while True:
                try:
                    temp = float(raw_input("Ingrese valor "+str(counter)+" de L: "))
                except ValueError:
                    print("Ingrese un numero valido, positivo.")
                    continue
                if not temp > 0:
                    print("Ingrese un numero valido, positivo.")
                    continue
                else:
                    counter = counter + 1
                    L.append(temp)
                    break
        break
    if (temp =='no' or temp =='No'):
        break

I = [[0 for x in xrange(2)] for x in xrange(2)]  # Arreglo elementos

F = [0 for x in xrange(largo+1)]  # arreglo vector F


Q = 1  # valor temperatura ambiente


# condiciones de borde
#I[0] = 20
#I[3] = -15

M = []  # vector multidimensional

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

