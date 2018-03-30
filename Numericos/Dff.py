#!/usr/bin/python
# -*- coding: utf-8 -*-

#Para la ejecución de éste código es necesario tener instalado python v2.7 o superior
#Se necesita ademas tener instalada la paquetería python-sympy
#Desde linux la instalación de la paquetería simbóloca se realiza---> $sudo apt-get install python-sympy
#Para windows es necesario tener instalado la paquetería sympy
#a descargar e instalar desde el siguiente link:https://pypi.python.org/pypi/sympy
#y desde la ventana cmd de windows con la instancia de python ejecutada en la dirección de la carpeta sympy, ejecutar "setup.py install"


from sympy import *
import csv


#Valores deberán ser ingresados manualmente con sus respectivas validaciones.

def rigidez(e,dz,mega):		#constante de rigidez de la placa
  d = (e*(dz*dz*dz))/(12*(1-mega*mega))
  return d



#Sección de declaración de variables mediante ingresos manuales y validados********

#**********************************************************************************


#declaracion de subparticiones, valores de intervalo ]0,1[


particionx = input("Ingrese el valor de la subparticion dx en el rango ]0,1[: ")


while (0>=particionx) or (particionx>=1):
    particionx = input("ERROR, ingrese un valor dentro del intervalo ]0,1[: ")

particiony = input("Ingrese el valor de la subparticion dy en el rango ]0,1[: ")

while (0>=particiony) or (particiony>=1):
    particiony = input("ERROR, ingrese un valor dentro del intervalo ]0,1[: ")

dx = particionx	#subparticion en x
dy = particiony	#subparticion en y



#constantes:
xxx = input("Ingrese el valor de la unidad dimensional [metros]: ")
while (0>=xxx):
    xxx = input("ERROR, ingrese un valor positivo: ")
#xxx = 2		#unidad dimensional [metro]
q = input("Ingrese el valor de q (Deben estar en Pacales(Pa) ): ")
while (0>=q):
    q = input("ERROR, ingrese un valor positivo: ")
#q = 33.6 	#unidad en KPa deben estar en Pa x lo que se multiplica x 1000
z = input("Ingrese el valor del espesor de la placa ]0,1[ :")
while (0>=z):
    z = input("ERROR, ingrese un valor positivo: ")
#z = 0.01	#valor de espezor de placa
omega = input("Ingrese el valor del desplazamiento de la placa flexionada ]0,1[: ")
while (0>=omega) or (omega>=1):
    omega = input("ERROR, ingrese un valor dentro del intervalo ]0,1[: ")
#omega= 0.3	#valor desplazamiento de la placa flexionada"
print "El modulo de Young debe ser expresado en notacion cientifica, se le pedira acontinuacion las siguientes expresiones-> (BASE)*10^(EXPONENTE)"
numero = input("Ingrese la BASE para el modulo de Young (Positiva): ")
while (0>=numero):
    numero = input("ERROR, ingrese un valor positivo: ")

exponente =  input("Ingrese el EXPONENTE para el modulo de Young (Positivo): ")
while (0>=exponente):
    exponente = input("ERROR, ingrese un valor positivo (no sea weon xD): ")

ep = numero*pow(10,exponente)
#ep = 2*pow(10,11)	#modulo de young



#*******************************************Métodos********************************

def mostrar(texto):		#Muestra malla de nodos
  print "\n\n************************{}******************************".format(texto)
  for i in range(0,ancho):		#relleno con las variables "symbolic" a nodos equisdistantes
    for j in range(0,largo):		#por dentro de la superficie
      if prl[i][j] != "":
	print prl[i][j],
	print "\t",
      else:
	print "\t",
	#print "{} \t".format(prl[i][j])
    print "\n"
  print "************************{}******************************\n\n".format(texto)


#calculo de diferencia dividida en X y en Y.

def ddtx(ant,cntt,sig):
  return ((ant-2*cntt+sig)/(dx*dx))

def ddty(ant,cntt,sig):
  return ((ant-2*cntt+sig)/(dy*dy))




#*****************************************Principal**********************************

ancho = int(round(xxx/dy))+1	#valor para matriz de mallado y vector de polinomios
largo = int(round(xxx/dx))+1 	#valor para matriz de mallado y vector de polinomios

prl = [["" for x in xrange(largo)] for x in xrange(ancho)]	#genera matriz de valores para mallado

for i in range(0,largo):	#rellenado condiciones de borde en fila
    prl[0][i] = 0		#rellena con 0 la primera fila
    prl[ancho-1][i] = 0		#rellena con 0 la ultima fla

for i in range(0,ancho):	#rellenado condiciones de borde en columna
    prl[i][0] = 0		#rellena con 0 primera columna
    prl[i][largo-1] = 0		#rellena con 0 la última columna


in_nd = 0
for i in range(1,ancho-1):		#relleno con las variables "symbolic" a nodos equisdistantes
  for j in range(1,largo-1):		#por dentro del area de tipo "T+numero", numero = [0,(largo-2)*(ancho-2)]
    nd = "T"+str(in_nd)
    sy = symbols(nd)
    prl[i][j] = sy
    #print "{}".format(prl[i][j])
    in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda del mallado

mostrar("Modelo de Mallado Nodal")

w = ["" for x in range((largo-2)*(ancho-2))]		#Vector para guardar las ecuaciones lineales

in_nd = 0
for i in range(1,ancho-1):			#genera los polinomios de las diferencias finitas por nodos
  for j in range(1,largo-1):			#mediante el laplaceano, la cual se usa la diferencia finita central
    w[in_nd] = ddtx(prl[i][j+1],prl[i][j],prl[i][j-1]) + ddty(prl[i+1][j],prl[i][j],prl[i-1][j]) + (q*1000)/rigidez(ep,z,omega)
    in_nd += 1

print "\n\n"+"*"*100
print "Polinomios generados mediante diferencia finita central\n\n\n"
for i in range(len(w)):
  print w[i]

with (open("polinomios.txt",'w')) as a:		#exporta los polinomios en archivo de texto
  for i in w:
    a.write(str(i)+"\n")

vv = []
vv.append(ancho)
vv.append(largo)

dataCSV = open("len", "wb")
writer = csv.writer(dataCSV, dialect='excel')
writer.writerows([vv])

