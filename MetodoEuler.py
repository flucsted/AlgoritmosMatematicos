import numpy as np
from math import factorial
from sympy import cos, sin, exp
from matplotlib.pyplot import plot, show, legend
from sympy import Symbol, Derivative, Function, Abs, pi

y=Function('y') #Variable función 
t=Symbol('t') #Variable simbolo 
dy="(0.002)*(1-y(t))" #Ingresar la derivada del P.V.I. considerando a la variable función dependiente de la variable simbolo -----
lim=np.array([0,50]) #Intervalo de t ------
N=50 #Número de aproximaciones deseadas ------
y1=0.01 #Valor en el punto inicial ------

#Paso 1
h=(lim[1]-lim[0])/N
t0=lim[0]
w=y1
aprox=np.zeros((N+1,2))
aprox[0,0]=t0
aprox[0,1]=w

print(np.array(["t","y"],dtype=str))

#Paso 2
for i in range(0,N,1):
    temp=eval(dy).subs(y(t),w)
    temp=temp.subs(t,t0).evalf()
    w+=h*temp
    t0=lim[0]+(i+1)*h
    aprox[i+1,0]=t0
    aprox[i+1,1]=w

print(aprox)
plot(aprox[:,0],aprox[:,1])
legend(['y aproximado'])
show()