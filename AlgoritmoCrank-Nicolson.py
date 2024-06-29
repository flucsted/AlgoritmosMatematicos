import numpy as np
from math import factorial
import sympy as sp
import matplotlib.pyplot as plt

x=sp.Symbol('x')
m=4 #Entero m>=3 del numero de puntos ------
N=2 #Entero N>=1 del numero de tiempos ------
alpha=1 #Constante ------
l=2 #Punto final (recordar h=l/m) u(0,t)=u(l,t)=0 ------
T=0.1 #Tiempo maximo (recordar k=T/N) ------
f=sp.sin((sp.pi*x)/2) #Función u(x,0) dada ------
nrep=1 #Número de repeticiones del metodo (Recuerda editar los plots para las gráficas generadas) ------
hh=T/nrep

def Nicolson(T):
    aprox=np.zeros([m,2])
    #Paso 1
    h=l/m
    k=T/N
    lamb=(alpha**2*k)/h**2
    aprox[m-1,1]=0

    #Paso 2
    for i in range(0,m-1,1):
        aprox[i,1]=f.subs(x,(i+1)*h).evalf()
    
    #Paso 3
    lvec=np.zeros(m)
    uvec=np.zeros(m)

    lvec[0]=1+lamb
    uvec[0]=(-lamb)/(2*lvec[0])

    #Paso 4
    for i in range(1,m-2,1):
        lvec[i]=1+lamb+(lamb*uvec[i-1]/2)
        uvec[i]=-lamb/(2*lvec[i])
    
    #Paso 5
    lvec[m-2]=1+lamb+(lamb*uvec[m-3]/2)

    zvec=np.zeros(m-1)
    #Paso 6 (pasos 7-11)
    for j in range(1,N+1,1):
        t=j*k
        zvec[0]=((1-lamb)*aprox[0,1]+(lamb/2)*aprox[1,1])/lvec[0]

        for i in range(2,m,1):
            zvec[i-1]=((1-lamb)*aprox[i-1,1]+(lamb/2)*(aprox[i,1]+aprox[i-2,1]+zvec[i-2]))/lvec[i-1]
        
        aprox[m-2,1]=zvec[m-2]

        for i in range(m-2,0,-1):
            aprox[i-1,1]=zvec[i-1]-uvec[i-1]*aprox[i,1]
    
    #Paso 12
    for i in range(1,m,1):
        aprox[i-1,0]=(i-1)*h
    return(aprox)

aprox=np.zeros([m,2,nrep])
for i in range(0,nrep,1):
    TT=i*hh
    aprox[:,:,i]=Nicolson(TT)

for i in range(0,nrep,1):
    print(np.array(['x','wi'+str(N)],dtype=str))
    print(aprox[:,:,i])

plt.plot(aprox[0:m-1,0,0],aprox[0:m-1,1,0])
plt.legend(['y/T1 aproximado'])
plt.show()