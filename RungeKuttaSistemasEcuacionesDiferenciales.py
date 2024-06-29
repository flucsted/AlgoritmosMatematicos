import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


ndy=2 # (m) Definir el número de ecuaciones existentes del sistema (debe ser igual al número de variables de cada ecuación) ------
t=sp.Symbol('t')
#Definimos todas las variables necesarias para el sistema (tiene que ser la misma cantidad de valores definidas en ndy) ------
u1,u2=sp.symbols('u1 u2')
limit=np.array([0,4]) # Límites de aproximación en t ------
# Ecuaciones del sistema (tiene que ser la misma cantidad de valores definidas en ndy) ------
dy1=3*u1-0.002*u1*u2
dy2=0.0006*u1*u2-0.5*u2
# Valores iniciales en el t inicial (tiene que ser la misma cantidad de valores definidas en ndy) ------
y1=1000
y2=500
N=10 #Número de aproximaciones deseadas ------

#Paso 1
h=(limit[1]-limit[0])/N
tt=limit[0]

#Paso 2
aprox=np.zeros([N+1,ndy+1])
for j in range(1,ndy+1,1): aprox[0,j]= eval("y"+str(j))

aprox[0,0]=tt

#Paso 3 es el paso 2
#Paso 4 (pasos 5-11)
for i in range(1,N+1,1):
    kmat=np.zeros([4,ndy])
    for j in range(1,ndy+1,1):
        f=eval("dy"+str(j))
        for r in range(1,ndy+1,1):
            if r==ndy:
                f=f.subs("u"+str(r),aprox[i-1,r]).evalf()
                f=f.subs(t,tt).evalf()
            else:
                f=f.subs("u"+str(r),aprox[i-1,r]).evalf()
        kmat[0,j-1]=h*f
    for j in range(1,ndy+1,1):
        f=eval("dy"+str(j))
        for r in range(1,ndy+1,1):
            if r==ndy:
                f=f.subs("u"+str(r),aprox[i-1,r]+(1/2)*kmat[0,r-1]).evalf()
                f=f.subs(t,tt+(h/2)).evalf()
            else:
                f=f.subs("u"+str(r),aprox[i-1,r]+(1/2)*kmat[0,r-1]).evalf()
        kmat[1,j-1]=h*f
    for j in range(1,ndy+1,1):
        f=eval("dy"+str(j))
        for r in range(1,ndy+1,1):
            if r==ndy:
                f=f.subs("u"+str(r),aprox[i-1,r]+(1/2)*kmat[1,r-1]).evalf()
                f=f.subs(t,tt+(h/2)).evalf()
            else:
                f=f.subs("u"+str(r),aprox[i-1,r]+(1/2)*kmat[1,r-1]).evalf()
        kmat[2,j-1]=h*f
    for j in range(1,ndy+1,1):
        f=eval("dy"+str(j))
        for r in range(1,ndy+1,1):
            if r==ndy:
                f=f.subs("u"+str(r),aprox[i-1,r]+kmat[2,r-1]).evalf()
                f=f.subs(t,tt+h).evalf()
            else:
                f=f.subs("u"+str(r),aprox[i-1,r]+kmat[2,r-1]).evalf()
        kmat[3,j-1]=h*f
    for j in range(1,ndy+1,1):
        aprox[i,j]=aprox[i-1,j]+(kmat[0,j-1]+2*kmat[1,j-1]+2*kmat[2,j-1]+kmat[3,j-1])/6
    tt=limit[0]+i*h
    aprox[i,0]=tt

print(aprox)

plt.plot(aprox[:,0],aprox[:,1])
plt.plot(aprox[:,0],aprox[:,2])
plt.legend(['y1 aproximado','y2 aproximado'])
plt.show()
