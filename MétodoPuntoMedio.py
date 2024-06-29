import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t,y=sp.symbols('t y')
limit=np.array([0,1]) # Límites de aproximación en t ------
dy=t*sp.exp(3*t)-2*y # Función del PVI ------
y1=0 # Valor inicial en el t inicial ------
N=2 # Número de aproximaciones deseadas dentro del intervalo de t -------
h=(limit[1]-limit[0])/N

aprox=np.zeros([N+1,2])
aprox[0,0]=limit[0]
aprox[0,1]=y1

for i in range(1,N+1,1):
    aprox[i,0]=limit[0]+i*h
    aprox[i,1]=aprox[i-1,1]+h*dy.subs(t,aprox[i-1,0]+(h/2)).subs(y,aprox[i-1,1]+(h/2)*dy.subs(t,aprox[i-1,0]).subs(y,aprox[i-1,1])).evalf()

print(np.array(['t','w'],dtype=str))
print(aprox)

plt.plot(aprox[:,0],aprox[:,1])
plt.legend(['y aproximado'])
plt.show()
