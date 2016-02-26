# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

rna= open('rma.txt','r')
splitrna = rna.readlines()                          
b = []

for line in splitrna[1:] :       
    temp = []
    items = line.split("\t")                  #construct input matrix
    for item in items[1:]:
        temp.append(float(item))
        b.append(temp)
        
import numpy as np                           # prepare output
cor4=open('cor4.txt','w')    
   
for i in b :
   tempcor = []
   for j in b:
       if i == j:                           # calculate coefficient
           tempcor.append([None])
       else:
           tempcor.append(np.corrcoef(i,j)[0,1])
   print >>cor4, (str(tempcor))
   print >>cor4, '\n'