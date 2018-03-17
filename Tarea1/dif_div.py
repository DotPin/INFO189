#!/usr/bin/python
# -*- coding: utf-8 -*-

#Para la ejecución de éste código es necesario tener instalado python v2.7 o superior
#Se necesita ademas tener instalada la paquetería python-sympy
#Desde linux la instalación de la paquetería simbóloca se realiza---> $sudo apt-get install python-sympy


from sympy import *



#Supuesto:
#Para realizar la ejecución del código asumiremos una EDO del tipo Ax'' + Bx' + Cx = f(t), en una sola dimensión.



##############################Carga de Parámetros#####################################

#Funcion que depende de "t"

def f_t(t):		#módulo de "función" f(t) de ecuación diferencial
  d = sin(t)            #función dependiente de parámetro "t", cambiar cual sea dependiente del mismo parámetro
  return d


#ingreso del intervalo a producir aproximación

inicio  = input("ingrese valor inicio intervalo (inicio >=0) : ")
while (inicio<0):
    print("ERROR, debe ingresar valor inicio>=0")
    inicio  = input("ingrese valor inico intervalo (inicio >=0) : ")

fin     = input("ingrese valor final intervalo (final>inicio) : ")
while (fin<inicio):
    print("ERROR, valor fin debe ser mayor al inicial")
    fin     = input("ingrese valor final intervalo (final>inicio) : ")
    
#Ingreso valor de constantes de la EDO

print("Se resolverá una edo del tipo Ax'' + Bx' + Cx = f(t), para la cual se necesitará ingresar los parámetros A,B y c")

A = input("Ingrese el Valor 'A' de la EDO")
B = input("Ingrese el Valor 'B' de la EDO")
C = input("Ingrese el Valor 'C' de la EDO")

#Para efectos de la diferencia dividida se solicitará "dx"

print("Se solicitará ingreso de dx para el desarrollo de la Diferencia dividida")
print("El dx debe estar en un intervalo 0<dx=<1")
dx = input("Ingrese el dx: ") 
while (dx<=0 or dx>1):
    print("El dx debe estar en un intervalo 0 < dx =< 1")
    dx = input("Ingrese el dx: ") 
    
#Se establece rango y se crea vector de coeficientes polinomiales

largo = int(round(fin/dx))+1

prl = ["" for x in xrange(largo)]	#genera vector de valores para mallado


#prl[0] = condicion inicial

