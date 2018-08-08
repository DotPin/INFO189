#!/usr/bin/python
# -*- coding: utf-8 -*- 
import numpy as np

w = [[0 for x in xrange(10)] for x in xrange(10)]

c=[]

def matrizEnsamble():
    print("\n\n***************MAtriz Ensamble************\n")
    print "\t",
    for k in range(len(w)):
        print k+1,
        print "\t",
    print "\n"
    for i in range(len(w)):
        print i+1,
        print "\t",
        for j in range(len(w)):
            print np.round(w[i][j],1),
            print "\t",
        print("\n")
    print("***************FIN Matriz Ensamble************\n\n")

with open("sol.txt","r") as a:

    for x in a:
        c.append(float(x))
    a.close()


ind = 0
for i in range(0,3):
    for j in range(0,5):
        w[i][j] = c[ind]
        ind+=1
        print ind
matrizEnsamble()
ind = ind-1
#for i in range(3,6):
    #for j in range(0,3):
        #w[i][j] = c[ind]
        #ind+=1
        #print ind
