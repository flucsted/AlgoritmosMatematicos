import numpy as np
from math import factorial
import sympy as sp
import matplotlib.pyplot as plt

x=sp.Symbol('x')
m=20 #Entero m>=3 del numero de puntos ------
N=2 #Entero N>=1 del numero de tiempos ------
alpha=0.98058044 #Constante ------
l=1.5 #Punto final (recordar h=l/m) u(0,t)=u(l,t)=0 ------
T=1 #Tiempo maximo (recordar k=T/N) ------
f=sp.sin((sp.pi*x)/l) #Función u(x,0) dada ------
nrep=1 #Número de repeticiones del metodo (Recuerda editar los plots para las gráficas generadas) ------
hh=T/nrep

def eccal(T):
    #Paso 1
    h=l/m
    k=T/N
    lamb=((alpha**2)*k)/h**2

    #Paso 2
    vecin=np.zeros(m-1)
    for i in range(1,m,1):
        vecin[i-1]=f.subs(x,i*h).evalf()

    #Paso 3
    lvec=np.zeros(m-1)
    uvec=np.zeros(m-2)
    lvec[0]=1+2*lamb
    uvec[0]=(-lamb)/lvec[0]

    #Paso 4
    for i in range(2,m-1,1):
        lvec[i-1]=1+2*lamb+lamb*uvec[i-2]
        uvec[i-1]=(-lamb)/lvec[i-1]
    
    #Paso 5
    lvec[m-2]=1+2*lamb+lamb*uvec[m-3]
    
    #Paso 6 (pasos 7-11)
    zvec=np.zeros(m-1)
    for j in range(1,N+1,1):
        t=j*k
        zvec[0]=vecin[0]/lvec[0]
        for i in range(2,m,1):
            zvec[i-1]=(vecin[i-1]+lamb*zvec[i-2])/lvec[i-1]
            if i==m-1:
                vecin[i-1]=zvec[i-1]
        for i in range(m-2,0,-1):
            vecin[i-1]=zvec[i-1]-uvec[i-1]*vecin[i]
            
    #Paso 12
    aprox=np.zeros([m-1,2])
    for i in range(1,m,1):
        aprox[i-1,0]=(i-1)*h
        aprox[i-1,1]=vecin[i-1]
    return aprox

aprox=np.zeros([m-1,2,nrep])
for i in range(0,nrep,1):
    TT=i*hh
    aprox[:,:,i]=eccal(TT)

for i in range(0,nrep,1):
    print(np.array(['x','wi'+str(N)],dtype=str))
    print(aprox[:,:,i])

plt.plot(aprox[:,0,0],aprox[:,1,0])
plt.legend(['y/T1 aproximado'])
plt.show()    