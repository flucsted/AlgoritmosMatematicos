import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t,y=sp.symbols('t y')
limit=np.array([1,2]) # Límites de aproximación en t ------
dy=1+(y/t) # Función del PVI ------
y1=2 # Valor inicial en el t inicial ------
N=5 # Número de aproximaciones deseadas dentro del intervalo de t (recordar h=(b-a)/N ) -------

#Paso 1
aprox=np.zeros([N+1,2])
h=(limit[1]-limit[0])/N
aprox[0,0]=limit[0]
aprox[0,1]=y1

#Paso 2 (pasos 3-5)
for i in range(1,4,1):
    K1=h*dy.subs(t,aprox[i-1,0]).subs(y,aprox[i-1,1]).evalf()
    K2=h*dy.subs(t,aprox[i-1,0]+(h/2)).subs(y,aprox[i-1,1]+(K1/2)).evalf()
    K3=h*dy.subs(t,aprox[i-1,0]+(h/2)).subs(y,aprox[i-1,1]+(K2/2)).evalf()
    K4=h*dy.subs(t,aprox[i-1,0]+h).subs(y,aprox[i-1,1]+K3).evalf()

    aprox[i,0]=limit[0]+i*h
    aprox[i,1]=aprox[i-1,1]+(K1+2*K2+2*K3+K4)/6

#Paso 6 (pasos 7-10)
for i in range(4,N+1,1):
    aprox[i,0]=limit[0]+i*h
    w=aprox[i-1,1]+h*(55*dy.subs(t,aprox[i-1,0]).subs(y,aprox[i-1,1]).evalf()-59*dy.subs(t,aprox[i-2,0]).subs(y,aprox[i-2,1]).evalf()+37*dy.subs(t,aprox[i-3,0]).subs(y,aprox[i-3,1]).evalf()-9*dy.subs(t,aprox[i-4,0]).subs(y,aprox[i-4,1]).evalf())/24 
    w=aprox[i-1,1]+h*(9*dy.subs(t,aprox[i,0]).subs(y,w)+19*dy.subs(t,aprox[i-1,0]).subs(y,aprox[i-1,1]).evalf()-5*dy.subs(t,aprox[i-2,0]).subs(y,aprox[i-2,1]).evalf()+dy.subs(t,aprox[i-3,0]).subs(y,aprox[i-3,1]).evalf())/24

    aprox[i,1]=w

print(np.array(['t','w'],dtype=str))
print(aprox)

plt.plot(aprox[:,0],aprox[:,1])
plt.legend(['y aproximado'])
plt.show()    
