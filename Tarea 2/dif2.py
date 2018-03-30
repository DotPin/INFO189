#!/usr/bin/python
# -*- coding: utf-8 -*-

#Para la ejecución de éste código es necesario tener instalado python v2.7 o superior
#Se necesita ademas tener instalada la paquetería python-sympy
#Desde linux la instalación de la paquetería simbóloca se realiza---> $sudo apt-get install python-sympy
#Para el desarrollo de este código es necesario tener instalada la paquetería "numpy" ---> $sudo apt-get install python-numpy


from sympy import *
#import numpy as np




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

def ddy(y_a,y,y_p,dy):
    rst = (y_a-2*y+y_p)/(dy*dy)
    return rst

def ddz(z_a,z,z_p,dz):
    rst = (z_a-2*z+z_p)/(dz*dz)
    return rst
    
    
def d_x(x_a,x_p,dx):
    rst = (x_a-x_p)/(2*dx)
    return rst

#Para efectos de la diferencia dividida se solicitará "dx"

print("Se solicitara ingreso de dx para el desarrollo de la Diferencia dividida")
print("El dx debe estar en un intervalo 0<dx=<1")
dx = float(input("Ingrese el dx: "))
while (dx<=0 or dx>1):
    print("El dx debe estar en un intervalo 0 < dx =< 1")
    dx = float(input("Ingrese el dx: "))
    

#Se establece rango y se crea vector de coeficientes polinomiales

largo = int(round(x_1/dx))+1

prl = [[["" for x in xrange(largo)] for x in xrange(largo)]	for x in xrange(largo)]#genera vector de valores para mallado

for i in range(0,largo):
    for j in range(0,largo):
        prl[i][j][0] = 0.5
        prl[i][j][largo-1] = 10
print(prl)

in_nd = 0
for i in range(1,largo-1):		#relleno con las variables "symbolic" a nodos equisdistantes
    for j in range(1,largo-1):
        for k in range(1,largo-1):
            nd = "T"+str(in_nd)                 
            sy = symbols(nd)
            prl[i][j][k] = sy
            in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda del mallado
            print(nd)


w = ["" for x in range(largo-2)]		#Vector para guardar las ecuaciones lineales
#stp = np.arange(x_0,x_1,dx)

in_nd = 0
for i in range(1,largo-1):      #genera los polinomios de las diferencias finitas por nodos
    for j in range(1,largo-1):
        for k in range(1,largo-1):
            w[in_nd] = ddx(prl[i-1][j][k],prl[i][j][k],prl[i+1][j][k],dx) + ddy(prl[i][j-1][k],prl[i][j][k],prl[i][j+1][k],dx) + ddz(prl[i][j][k-1],prl[i][j][k],prl[i][j][k+1],dx)
            in_nd += 1
    
print "\n\n"+"*"*100
print "Polinomios generados mediante diferencia finita central\n\n\n"
for i in range(len(w)):
  print w[i]

with (open("polinomios.txt",'w')) as a:		#exporta los polinomios en archivo de texto
  for i in w:
    a.write(str(i)+"\n")
