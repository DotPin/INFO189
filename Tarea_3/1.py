#!/usr/bin/python
# -*- coding: utf-8 -*-

from sympy import *

# Valores por defecto van aqui

largo = 3  # numero de elementos

# arreglo y otras constantes
D = [0.02, 0.005, 0.0035]  # Arreglo de variables D

L = [1.3, 8, 2.5]  # Arreglo de L

FronteraA = 20
FronteraB = -15

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
        while True:
            try:
                temp = float(raw_input("Ingrese primer valor de frontera: "))
            except ValueError:
                print("Ingrese un numero valido.")
                continue
            FronteraA = temp
            break
        while True:
            try:
                temp = float(raw_input("Ingrese segundo valor de frontera: "))
            except ValueError:
                print("Ingrese un numero valido.")
                continue
            FronteraB = temp
            break
        break
    if (temp =='no' or temp =='No'):
        break

I = [[0.0 for x in xrange(2)] for x in xrange(2)]  # Arreglo elementos

F = [0.0 for x in xrange(largo+1)]  # arreglo vector F

V = [0.0 for x in xrange(largo+1)]  # vector incognitas

W = [0.0 for x in xrange(largo+1)] #Vector polinomico

Q = 0  # valor temperatura ambiente

M = []  # vector multidimensional

gb = [] # Matriz ensamble



#genera vector de incógnitas nodales, para solución final
def init_v():
    in_nd=0
    for k in range(largo+1):
        nd = "T"+str(in_nd)                 
        V[k] = Symbol(nd)
        in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda del mallado
        

#creación multimatrices, permite apilar las submatrices de cada elemento
def elementos():
    for k in range(largo):
        for i in range(2):
            for j in range(2):
                if(i==j):
                    I[i][j] = D[k]/L[k]
                else:
                    I[i][j] = -(D[k]/L[k])
        M.append(I)


#Funcion para armar la matriz global, usando las 3 matrices
#generadas a partir de los 3 elementos
def armaMatriz(A):
    MatrizComp = [[0.0 for x in xrange(len(A)+1)] for x in xrange(len(A)+1)]
    for i in range(0,len(A)):
        for j in range(0,2):
            for k in range(0,2):
                MatrizComp[i+j][i+k] = MatrizComp[i+j][i+k] + A[i][j][k]
    return MatrizComp

#función de constantes lineales para el sistema lineal
def fun_f():
    F[0]=(Q*L[0])/2
    for j in range(1,largo-1):
        F[j+1] = F[j] + (Q*L[j])/2

    F[len(F)-1] = (Q*L[j])/2
  
#genero polinomios de la multiplicacion Matriz(A)*Vector(X), con A, matriz de emsamble, y X vector de incógnitas
def polinomios():
    for i in range(largo+1):
        for j in range(largo+1):
            W[i] = gb[i][j]*V[j] + W[i]


#Solución del sistema lineal mediante sustitución progresiva, "Regla de Cramer"
def solucion():
    cp = [x for x in V]
    sol = solve(W[0].subs(V[0],20))
    V[0] = FronteraA
    V[1] = sol[0]+F[1]
    print(V[0])
    print(W)
    for i in range(1,largo-1):
        sol = solve(W[i].subs(cp[i-1],V[i-1]).subs(cp[i],V[i]).subs(cp[i+1],V[i+1]))
        V[i+1]= sol[0]+F[i+2]
    V[largo]=FronteraB
    print(V)

init_v()
elementos()
gb = armaMatriz(M)
fun_f()
poliniomios()
solucion()



