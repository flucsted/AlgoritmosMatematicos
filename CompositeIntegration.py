import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


#Composite Simpson's Rule (regla de Simpson Cumpuesta)
def SimpGen():
    lim=np.array([0,1]) # Cambiar puntos finales a y b ------
    n=4  # Cambiar entero n (par) de la regla de simpson a utilizar con n>=2 ------
    x=sp.symbols('x') # Definir la variable
    f=sp.sin(x) # Definir la funcion ------
    #Paso 1
    h=(lim[1]-lim[0])/n
    #Paso 2
    XI0=f.subs(x,lim[0]).evalf()+f.subs(x,lim[1]).evalf() # f(a)+f(b) cambiar funciones valuadas ------
    XI1=0
    XI2=0
    #Paso 3
    for i in range(1,n,1):
        #Paso 4
        X=lim[0]+i*h
        #Paso 5
        if i%2==0:
            XI2+=f.subs(x,X).evalf() # f(X) cambiar según funcion valuada ------
        else:
            XI1+=f.subs(x,X).evalf() # f(X) cambiar según funcion valuada ------
    XI=h*(XI0+2*XI2+4*XI1)/3
    return(XI)

print(SimpGen())

