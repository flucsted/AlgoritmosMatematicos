import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import timeit

start=timeit.timeit() #Tiempo inicial de ejecución

t,y=sp.symbols('t y')
limit=np.array([0,2]) # Límites de aproximación en t ------
dy=y-t**2+1# Función del PVI ------
y1=0.5 # Valor inicial en el t inicial ------
#N=10 # Número de aproximaciones deseadas dentro del intervalo de t -------
TOL=0.00001 # Tolerancia ------
hmin=0.01 # Minimum step size ------
hmax=0.25 # Maximum step size ------

#Paso 1
tt=limit[0]
w=y1
h=hmax
FLAG=1

aprox=np.zeros([1,3])
aprox[0,0]=tt
aprox[0,1]=w
aprox[0,2]=h

#Paso 2 (pasos 3-11)
while FLAG==1:
    K1=h*dy.subs(t,tt).subs(y,w).evalf()
    K2=h*dy.subs(t,tt+(1/4)*h).subs(y,w+(1/4)*K1).evalf()
    K3=h*dy.subs(t,tt+(3/8)*h).subs(y,w+(3/32)*K1+(9/32)*K2).evalf()
    K4=h*dy.subs(t,tt+(12/13)*h).subs(y,w+(1932/2197)*K1-(7200/2197)*K2+(7296/2197)*K3).evalf()
    K5=h*dy.subs(t,tt+h).subs(y,w+(439/216)*K1-(8)*K2+(3680/513)*K3-(845/4104)*K4).evalf()
    K6=h*dy.subs(t,tt+(1/2)*h).subs(y,w-(8/27)*K1+(2)*K2-(3544/2565)*K3+(1859/4104)*K4-(11/40)*K5).evalf()

    R=(1/h)*np.abs((1/360)*K1-(128/4275)*K3-(2197/75240)*K4+(1/50)*K5+(2/55)*K6)

    if R<TOL or R==TOL:
        tt+=h
        w+=(25/216)*K1+(1408/2565)*K3+(2197/4104)*K4-(1/5)*K5
        aprox=np.insert(aprox,aprox.shape[0],np.array([tt,w,h]),0)
    
    delta=0.84*sp.Pow(TOL/R,1/4)
    if delta<0.1 or delta==0.1:
        h=0.1*h
    elif delta>4 or delta==4:
        h=4*h
    else:
        h=delta*h
    
    if h>hmax:
        h=hmax
    
    if tt>limit[1] or tt==limit[1]:
        FLAG=0
    elif tt+h>limit[1]:
        h=limit[1]-tt
    elif h<hmin:
        FLAG=0
    
print(np.array(['t','w','h'],dtype=str))
print(aprox)

plt.plot(aprox[:,0],aprox[:,1])
plt.legend(['y aproximado'])
plt.show()

end=timeit.timeit() #Tiempo final de ejecución
print("El tiempo de ejecución fue de "+str(end-start)+" segundos.") #Impresión de tiempo de ejecución en segundos