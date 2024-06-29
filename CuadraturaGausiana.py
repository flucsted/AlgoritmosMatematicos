import numpy as np
from math import factorial
from sympy import cos, sin, exp, factorial
from matplotlib.pyplot import plot, show, legend
from sympy import Derivative, Function, Abs, pi, integrate, log, symbols

x,t=symbols('x,t') #Definicion de la variable principal y el cambio de variable
f="(x**2)*log(x)" #Definicion de la funcion a integrar ------
fe=f
inter=np.array([1,1.5]) #Define los intervalos a integrar ------
n=3 #Grado de la cuadratura ------
tabla=np.zeros((n,2)) #Creamos la tabla de raices y coeficientes

#Funcion para crear el n-esimo polinomio de Legendre
def LegPol():
    poli=np.poly1d([0])
    N=np.trunc(n/2)
    for m in range(0,int(N)+1,1):
        escal=(((-1)**m)*(factorial(2*n-2*m)))/((2**n)*(factorial(m))*(factorial(n-m))*(factorial(n-2*m)))
        vecaux=np.zeros(n-2*m+1)
        if (0 in vecaux)==True:
           vecaux[0]=1
        else:
            vecaux=np.array([1])
        polaux=np.poly1d(vecaux)
        polaux=polaux*escal
        poli=np.polyadd(poli,polaux)
    return(poli)

#Agregamos las raices a la tabla
for a in range(0,n,1):
    tabla[a,0]=np.roots(LegPol())[a]

#Función para crear los coeficientes ci
def cmaker(i):
    poli=np.poly1d([1])
    for j in range(0,n,1):
        if j!=i:
            escal=tabla[i,0]-tabla[j,0]
            polaux=np.poly1d([1,-tabla[j,0]])
            polaux=polaux/escal
            poli=np.polymul(poli,polaux)
    integ=np.polyint(poli)
    diff=np.polyval(integ,1)-np.polyval(integ,-1)
    return(diff)

#Agregamos los coeficientes a la tabla
for b in range(0,n,1):
    tabla[b,1]=cmaker(b)

#Cuadratura gaussiana para intervalos arbitrarios
f=eval(f).subs(x,(1/2)*((inter[1]-inter[0])*t+inter[0]+inter[1]))

aprox=0
for c in range(0,n,1):
    aprox+=tabla[c,1]*f.subs(t,tabla[c,0]).evalf()

print("La integral de "+str(fe)+" en "+str(inter)+" tiene un valor aproximado de "+str(aprox)+".")