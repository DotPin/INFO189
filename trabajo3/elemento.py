#!/usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np





#condiciones térmicas
kx = 0.3
area = (7.5*7.5)/2
Tf1 = 150   #interior
Tf2 = 10    #exterior
h1 = 2      #interior
h2 = 0.3    #exterior

#matrices borde elementoCuadrado
mij= np.array([[2,1,0,0],[1,2,0,0],[0,0,0,0],[0,0,0,0]])
mjk= np.array([[0,0,0,0],[0,2,1,0],[0,1,2,0],[0,0,0,0]])
mkm= np.array([[0,0,0,0],[0,0,0,0],[0,0,2,1],[0,0,1,2]])
mmi= np.array([[2,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,2]])

#matrices borde elementoTriangular
tij= np.array([[2,1,0],[1,2,0],[0,0,0]])
tjk= np.array([[0,0,0],[0,2,1],[0,1,2]])
tki= np.array([[2,0,1],[0,0,0],[1,0,2]])

#matrices factores elementoCuadrado
nx = np.array([[2, -1, -1, 1],[-2, 2, 1, -1],[-1, 1, 2, -2],[1, -1, -2, 2]])
ny = np.array([[2, 1, -1, -2],[1, 2, -2, -1],[-1, -2, 2, 1],[-2, -1, 1, 2]])

#ingreso coordenadas e5 y e6 triangulares superior e inferior
t5 = np.array([[0,0],[0.2,0],[0,0.2]])
t6 = np.array([[0.2,0],[0.2,0.2],[0,0.2]])


#matrices factores para triangulo e5 y e6 respectivamente
trX1=[]
trY1=[]

trX2=[]
trY2=[]

#calculo factores triangulo
def elementoTriangular(b):
    tb = []
    tbb = []
    tc = []
    tcc = []
    bi = b[1][1] - b[2][1]
    bj = b[2][1] - b[0][1]
    bk = b[0][1] - b[1][1]
    
    ci = b[2][0] - b[1][0]
    cj = b[0][0] - b[2][0]
    ck = b[1][0] - b[0][0]
    
    tb.append([bi*bi,bi*bj,bi*bk])
    tb.append([bj*bi,bj*bj,bj*bk])
    tb.append([bk*bi,bk*bj,bk*bk])
    tbb = np.array(tb)
    
    
    tc.append([ci*ci,ci*cj,ci*ck])
    tc.append([cj*ci,cj*cj,cj*ck])
    tc.append([ck*ci,ck*cj,ck*ck])
    tcc = np.array(tc)
    return tbb,tcc

[trX1, trY1] = elementoTriangular(t5)
[trX2, trY2] = elementoTriangular(t6)


#matrices de conduccion x elemento
kd9 = ((0.08*nx) + ((2/9)*ny))
e9 = np.array([3,4,9,8])

kd10 = ((0.08*nx) + ((2/9)*ny))
e10 = np.array([4,5,10,9])

kd11 = ((0.08*nx) + ((2/9)*ny))
e11 = np.array([8,9,14,13])

kd12 = ((0.08*nx) + ((2/9)*ny))
e12 = np.array([9,10,15,14])

kd13 = ((14/45*nx) + ((2/35)*ny))
e13 = np.array([11,12,17,16])

kd14 = ((14/45*nx) + ((2/35)*ny))
e14 = np.array([12,13,18,17])

kd15 = ((14/45*nx) + ((2/35)*ny))
e15 = np.array([16,17,20,19])

kd16 = ((14/45*nx) + ((2/35)*ny))
e16 = np.array([17,18,21,20])

kd5 = (kx/(area*0.2))*(trX1+trY1)
e5 = np.array([4,6,10])

kd6 = (kx/(area*0.2))*(trX2+trY2)
e6 = np.array([6,11,10])


#matrices de conductividad x elemento
kc9 = ((h2*12.5)/6)*mij
kc10 = ((h2*12.5)/6)*mij

kc13 = ((h2*17.5)/6)*mmi
kc15 = ((h2*17.5)/6)*mmi


#vectores de termicidad x elemento
f1 = ((20*30*0.1)/2)*np.array([1,0,0,1])
f2 = 90*np.array([0,1,1,0])
f3 = 90*np.array([0,1,0,0])
f4 = ((20*50*0.1)/2)*np.array([0,0,1,1])

f5 = ((20*50*0.2)/2)*np.array([1,0,1])
f6 = ((20*30*0.2)/2)*np.array([0,1,1])


#Matriz ensamble de elementos K
MT = np.zeros((12,12))

#Matriz k general
for i in range(0,len(kd5)):#fila
    for j in range(0,len(kd5)):#columna
         MT[e5[i]-1][e5[j]-1]+=kd5[i][j]+kc5[i][j]
         MT[e6[i]-1][e6[j]-1]+=kd6[i][j]+kc6[i][j]    

for i in range(0, len(kd1)):#fila
    for j in range(0, len(kd1)):#columna
        MT[e1[i]-1][e1[j]-1]+=kd1[i][j]+kc1[i][j]
        MT[e2[i]-1][e2[j]-1]+=kd2[i][j]
        MT[e3[i]-1][e3[j]-1]+=kd3[i][j]
        MT[e4[i]-1][e4[j]-1]+=kd4[i][j]+kc4[i][j]

def matrizEndamble():
    print("\n\n***************MAtriz Ensamble************\n")
    for i in range(len(MT)):
        for i in range(len(MT)):
            print MT[i][j],
            print "\t",
        print "\n"
    print("***************FIN Matriz Ensamble************\n\n")
    
F = np.zeros(12)        
#Vector de termincidad F
for i in range(0,len(e5)):
    F[e5[i]-1]+=f5[i]
    F[e6[i]-1]+=f6[i]
for i in range(0,len(e1)):
    F[e1[i]-1]+=f1[i]
    F[e2[i]-1]+=f2[i]
    F[e3[i]-1]+=f3[i]
    F[e4[i]-1]+=f4[i]

for i in range(0,12):#borrar filas,valores conocidos, temperatura interna chimenea
        MT[2][i]=0
        MT[5][i]=0
        MT[6][i]=0
MT[2][2]=1
MT[5][5]=1
MT[6][6]=1      

matrizEndamble()
c = np.linalg.solve(MT, F)
for i in range(len(MT)):
    print("Solución del sistema variable FI({0}) = {1}").format(i+1,c[i])