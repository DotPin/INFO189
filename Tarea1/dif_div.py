#!/usr/bin/python
# -*- coding: utf-8 -*-

#Para la ejecución de éste código es necesario tener instalado python v2.7 o superior
#Se necesita ademas tener instalada la paquetería python-sympy
#Desde linux la instalación de la paquetería simbóloca se realiza---> $sudo apt-get install python-sympy


from sympy import *
import numpy as np




#Supuesto:
#Para realizar la ejecución del código asumiremos una EDO del tipo Ax'' + Bx' + Cx = f(t), en una sola dimensión.



##############################Carga de Parámetros#####################################

#Funcion que depende de "t"

def f_t(t):		#módulo de "función" f(t) de ecuación diferencial
  d = -(t*t)            #función dependiente de parámetro "t", cambiar cual sea dependiente del mismo parámetro
  return d

x_0 = float(input("Ingrese el valor de X(0)= "))
x_1 = float(input("Ingrese el valor de X(1)= "))

def ddx(x_a,x,x_p,dx):
    rst = (x_a-2*x+x_p)/(dx*dx)
    return rst
    
def d_x(x_a,x_p,dx):
    rst = (x_a-x_p)/(2*dx)
    return rst
    
#Ingreso valor de constantes de la EDO

print("Se resolverá una edo del tipo Ax'' + Bx' + C = f(t), para la cual se necesitará ingresar los parámetros A,B y c")
print("La funcion f(t)=sin(t) ")

A = float(input("Ingrese el Valor 'A' de la EDO: "))
B = float(input("Ingrese el Valor 'B' de la EDO: "))
C = float(input("Ingrese el Valor 'C' de la EDO: "))

#Para efectos de la diferencia dividida se solicitará "dx"

print("Se solicitará ingreso de dx para el desarrollo de la Diferencia dividida")
print("El dx debe estar en un intervalo 0<dx=<1")
dx = float(input("Ingrese el dx: "))
while (dx<=0 or dx>1):
    print("El dx debe estar en un intervalo 0 < dx =< 1")
    dx = float(input("Ingrese el dx: "))
    

#Se establece rango y se crea vector de coeficientes polinomiales

largo = int(round(1/dx))+1

prl = ["" for x in xrange(largo)]	#genera vector de valores para mallado


prl[0] = x_0
prl[largo-1] = x_1

in_nd = 0
for i in range(1,largo-1):		#relleno con las variables "symbolic" a nodos equisdistantes
    nd = "T"+str(in_nd)                 
    sy = symbols(nd)
    prl[i] = sy
    in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda del mallado


w = ["" for x in range(largo-2)]		#Vector para guardar las ecuaciones lineales
stp = np.arange(x_0,x_1,dx)

in_nd = 0
for i in range(1,largo-1):      #genera los polinomios de las diferencias finitas por nodos
    w[in_nd] = A*ddx(prl[i-1],prl[i],prl[i+1],dx) + B*d_x(prl[i-1],prl[i+1],dx) + C - f_t(stp[i]) 
    in_nd += 1
    
print "\n\n"+"*"*100
print "Polinomios generados mediante diferencia finita central\n\n\n"
for i in range(len(w)):
  print w[i]

with (open("polinomios.txt",'w')) as a:		#exporta los polinomios en archivo de texto
  for i in w:
    a.write(str(i)+"\n")
