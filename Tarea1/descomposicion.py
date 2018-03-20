#!/usr/bin/python
# -*- coding: UTF-8 -*-
# validación de tipo de elemento isinstance(valor, tipo) = true/false

#Script que recibe un archivo con "n" polinomios para generar matriz A y vector B del sistema lineal Ax = B
#Este script realiza la descomposicion solo si la variable simbólica nodal del script "valores" es "T"
#este script solo funciona despues de haber hecho funcionar el script valores.py, debido que debe recibir un archivo de texto
#como parámetro para poder funcionar la descomposicion polinomial.


import numpy as np

with open("polinomios.txt","r") as a:
  c=[]
  
  indice = 0
  for x in a:
    c.append(x.split(" "))	
    indice += 1			
  
  mm = [[float(0) for x in xrange(indice)] for x in xrange(indice)]	
  vct = [float(0) for x in xrange(indice)]				
  
  for b in c:
    for d in range(len(b)):
      if b[d].find("*")>0:
	b[d]= b[d].split("*")
      
  def descomponer2(x,y,m):	
    if len(x) < 3:		
      x[0] = float(x[0])*m	
      l = x[1].split("T")	
      l = int(l[1])		
      mm[y][l]= x[0]		
    else:			
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

c = np.linalg.solve(mm, vct)
print("Solución del sistema")
for i in range(len(c)):
    print(c[i])

