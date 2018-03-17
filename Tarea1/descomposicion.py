#!/usr/bin/python
# -*- coding: UTF-8 -*-
# validación de tipo de elemento isinstance(valor, tipo) = true/false

#Script que recibe un archivo con "n" polinomios para generar matriz A y vector B del sistema lineal Ax = B
#Este script realiza la descomposicion solo si la variable simbólica nodal del script "valores" es "T"
#este script solo funciona despues de haber hecho funcionar el script valores.py, debido que debe recibir un archivo de texto
#como parámetro para poder funcionar la descomposicion polinomial.


import csv

with open("polinomios.txt","r") as a:
  c=[]
  
  indice = 0
  for x in a:
    c.append(x.split(" "))	#genera una tupla de elementos, con subtuplas de elementos
    indice += 1			#cuenta la cantidad de polinomios.
  
  mm = [[float(0) for x in xrange(indice)] for x in xrange(indice)]	#genera matriz A
  vct = [float(0) for x in xrange(indice)]				#genera vector B
  
  for b in c:
    for d in range(len(b)):
      if b[d].find("*")>0:
	b[d]= b[d].split("*")
      
  def descomponer2(x,y,m):	#funcion de descomposicion de subtuplas para formar matriz Ax = B
    if len(x) < 3:		#revisa que la subtupla sea superior a 2
      x[0] = float(x[0])*m	#elemento es transformado a numérico
      l = x[1].split("T")	#separa variable "T" nodal para buscar coordenada en matriz A
      l = int(l[1])		#convierte numero nodal
      mm[y][l]= x[0]		#guarda numero convertido en matriz A
    else:			#en caso de ser elemento flotante es convertido y guardado en matriz B
      x = float(x)*m		
      vct[y] = x
      
  h = 0
  aux = 1
  for p in c:
    print "fila matriz:{0}".format(h)
    for q in p:
      if q == "-":
	aux = -1
      elif q == "+":
	aux = 1
      print "valor q:",q
      if q>2 and q!="+" and q!="-":
	descomponer2(q,h,aux)
    aux=1
    h+=1
  print mm
  print "*"*20
  print vct
  
dataCSV2 = open("vector_b", "wb")
wr = csv.writer(dataCSV2, dialect='excel')
wr.writerows([vct])


dataCSV = open("matriz_a", "wb")
writer = csv.writer(dataCSV, dialect='excel')
writer.writerows(mm)
      