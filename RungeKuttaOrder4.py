import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t,y=sp.symbols('t y')
limit=np.array([0,1]) # Límites de aproximación en t ------
dy=t*sp.exp(3*t)-2*y # Función del PVI ------
y1=0 # Valor inicial en el t inicial ------
N=2 # Número de aproximaciones deseadas dentro del intervalo de t -------

#Paso 1
h=(limit[1]-limit[0])/N
tt=limit[0]
w=y1

aprox=np.zeros([N+1,2])
aprox[0,0]=tt
aprox[0,1]=w

#Paso 2 (pasos 3-5)
for i in range(1,N+1,1):
    K1=h*dy.subs(t,tt).subs(y,w).evalf()
    K2=h*dy.subs(t,tt+h/2).subs(y,w+K1/2).evalf()
    K3=h*dy.subs(t,tt+h/2).subs(y,w+K2/2).evalf()
    K4=h*dy.subs(t,tt+h).subs(y,w+K3).evalf()

    w=w+(K1+2*K2+2*K3+K4)/6
    tt=limit[0]+i*h
    aprox[i,0]=tt
    aprox[i,1]=w

print(np.array(['t','w'],dtype=str))
print(aprox)

plt.plot(aprox[:,0],aprox[:,1])
plt.legend(['y aproximado'])
plt.show()