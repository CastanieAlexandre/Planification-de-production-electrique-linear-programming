# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:51:27 2022

@author: alexandre.castanie
"""
import gurobipy as gp
import numpy as np
import pandas as pd
from IPython.display import display

periode,demande,duree = gp.multidict({'p1':[15000,6], 'p2':[30000,3], 'p3':[25000,6], 'p4':[40000,3],'p5':[27000,6]})

types,Pmax,Pmin,cout,nbmax=gp.multidict({'A':[2000,850,1.5,12],'B':[1750,1250,1.5,11],'C':[4000,1500,2.75,5]})

m=gp.Model()

y=m.addVars(types,periode,lb=0,vtype=gp.GRB.CONTINUOUS)
s=m.addVars(types,periode,lb=0,vtype=gp.GRB.CONTINUOUS)
m.setObjective(gp.quicksum(y[k,p] * duree[p] * cout[k] for k in types for p in periode), gp.GRB.MINIMIZE)

contrainte1=m.addConstrs((y.sum('*',p)==demande[p] for p in periode))
contrainte2=m.addConstrs((y[k,p]+s[k,p]==Pmax[k]*nbmax[k] for k in types for p in periode)) 

m.update()
m.optimize()

pdict={k:[v.x for v in y.select(k,'*')] for k in types}
df=pd.DataFrame(pdict)
display(df)

pdict2={k:[v.x for v in s.select(k,'*')] for k in types}
df2=pd.DataFrame(pdict2)
display(df2)

x1=[i[j] for i in pdict.values() for j in range(len(i))]
x2=[i[j] for i in pdict2.values() for j in range(len(i))]
x=x1+x2

b=[Pmax[t]*nbmax[t] for t in types for p in periode]
for p in periode:
    b.append(demande[p])

b2=np.array(5*[Pmax['A']*nbmax['A']]+5*[Pmax['B']*nbmax['B']]+5*[0]+[demande[p] for p in periode])

A=np.zeros((20,30))
A[0:5,0:5]=np.identity(5)
A[15:20,0:5]=np.identity(5)
A[5:10,5:10]=np.identity(5)
A[15:20,5:10]=np.identity(5)
A[10:15,10:15]=np.identity(5)
A[15:20,10:15]=np.identity(5)
A[0:5,15:20]=np.identity(5)
A[5:10,20:25]=np.identity(5)
A[10:15,25:30]=np.identity(5)

Ab=np.zeros((20,20))
Ab[1,0]=1
Ab[2,1]=1
Ab[3,2]=1
Ab[4,3]=1
Ab[16,0]=1
Ab[17,1]=1
Ab[18,2]=1
Ab[19,3]=1
Ab[5:10,4:9]=np.identity(5)
Ab[15:20,4:9]=np.identity(5)
Ab[0:5,9:14]=np.identity(5)
Ab[5,14]=1
Ab[10:15,15:20]=np.identity(5)

Ab_inv = np.linalg.inv(Ab)
c=np.array(5*[cout['A']]+5*[cout['B']]+5*[cout['C']]+15*[0])
cb=np.array(4*[cout['A']]+5*[cout['B']]+11*[0])

u=cb.dot(Ab_inv)
#copt=c-u.dot(A)

#print(b)
#print(b2)
#print(copt)
#print(u)
#print(A)
#print(x)
#print(Ab_inv.dot(b))