import numpy as np
from sympy import Symbol, ln, integrate, exp

x=Symbol('x')
f="exp(-x)" #Función integrada ------
lim=np.array([0,1]) #Límites de integración ------
n=2 #Grado de precisión ------
h=(lim[1]-lim[0])/n

#Función de regla trapezoidal (n=1)
def traprul():
    aprox=0
    val=lim[0]
    for a in range(0,n+1,1):
        if a!=0:
            val+=h
        aprox+=eval(f).subs(x,val)
    aprox=aprox*(h/2)
    return aprox

#Función de regla de Simpson (n=2)
def SimpRule():
    aprox=0
    val=lim[0]
    vect=np.array([1,4,1])
    for a in range(0,n+1,1):
        if a!=0:
            val+=h
        aprox+=vect[a]*eval(f).subs(x,val)
    aprox=aprox*(h/3)
    return aprox

#Función de regla de Simpson 3/8 (n=3)
def Simp38Rule():
    aprox=0
    val=lim[0]
    vect=np.array([1,3,3,1])
    for a in range(0,n+1,1):
        if a!=0:
            val+=h
        aprox+=vect[a]*eval(f).subs(x,val)
    aprox=aprox*(3*h/8)
    return aprox

# n=4
def n4Rule():
    aprox=0
    val=lim[0]
    vect=np.array([7,32,12,32,7])
    for a in range(0,n+1,1):
        if a!=0:
            val+=h
        aprox+=vect[a]*eval(f).subs(x,val)
    aprox=aprox*(2*h/45)
    return aprox

if (n==1):
    print("La integral de "+f+" en "+str(lim)+" es: "+str(traprul()))
elif (n==2):
    print("La integral de "+f+" en "+str(lim)+" es: "+str(SimpRule()))
elif (n==3):
    print("La integral de "+f+" en "+str(lim)+" es: "+str(Simp38Rule()))
elif (n==4):
    print("La integral de "+f+" en "+str(lim)+" es: "+str(n4Rule()))

#num=(integrate(f,(x,1.25,1.5)))-SimpRule()
print(integrate(f))