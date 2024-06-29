import numpy as np
from math import factorial
import sympy as sp
from matplotlib.pyplot import plot, show, legend


m=5 #Numero par ------
n=5 #Numero par ------
x,y=sp.symbols('x,y') #Definimos las variables
f=sp.exp(-x**2-y**2) #Función ------
cx=0*x #Limite inferior de la primera integral ------
dx=sp.sqrt(1-x**2) #Limite superior de la primera integral ------
inter1=np.array([0,1]) #Segundo intervalo de integracion ------


#Paso 1
h=(inter1[1]-inter1[0])/n
j1=j2=j3=0

#Paso 2 (Paso 3-8)
for i in range(0,n+1,1):
    r=inter1[0]+i*h #Variable x para Simpson
    if (type(cx)==float) or (type(dx)==float):
        HX=(dx-cx)/m
        k1=(f.subs(x,r).subs(y,cx).evalf())+(f.subs(x,r).subs(y,dx).evalf())
        k2=k3=0
        for j in range(1,m,1):
            z=cx+j*HX #Variable y para Simpson
            Q=f.subs(x,r).subs(y,z).evalf()
            if (j%2==0):
                k2+=Q
            else:
                k3+=Q
    else:
        HX=(dx.subs(x,r).evalf()-cx.subs(x,r).evalf())/m
        k1=(f.subs(x,r).subs(y,cx.subs(x,r).evalf()).evalf())+(f.subs(x,r).subs(y,dx.subs(x,r).evalf()).evalf())
        k2=k3=0
        for j in range(1,m,1):
            z=(cx.subs(x,r).evalf())+j*HX #Variable y para Simpson
            Q=f.subs(x,r).subs(y,z).evalf()
            if (j%2==0):
                k2+=Q
            else:
                k3+=Q
    L=(k1+2*k2+4*k3)*(HX/3)
    if i==0 or i==n:
        j1+=L
    elif i%2==0:
        j2+=L
    else:
        j3+=L

#Paso 9
J=(j1+2*j2+4*j3)*(h/3)

#Paso 10
print("La integral de "+str(f)+" en los intervalos ["+str(cx)+","+str(dx)+"] y ["+str(inter1[0])+","+str(inter1[1])+"] para los ejes y,x respectivamente es: "+str(J))
