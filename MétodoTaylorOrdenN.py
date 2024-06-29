import numpy as np
from sympy import exp,factorial
from matplotlib.pyplot import plot, show, legend
from sympy import Symbol, Derivative, Function


y=Function('y') #Variable función 
t=Symbol('t') #Variable simbolo 
dy="t*exp(3*t)-2*y(t)" #Ingresar y' del P.V.I. considerando a la variable función dependiente de la variable simbolo -----
N=2 #Ingresar el número de aproximaciones deseadas -----
y1=0 #Ingresar el valor del P.V.I. de t inicial -----
inter=np.array([0,1]) #Ingresar el intevalo de t -----
h=(inter[1]-inter[0])/N 
n=2 #Orden del método de Taylor -----

#Función dedicada al método de Euler (Método de Taylor de primer orden) empleado
def Euler(ti,wi):
    res=0
    fn=Derivative(dy,t).doit()
    for a in range(0,n,1):
        if a==0:
            fm=eval(dy).subs(y(t),wi) 
            fm=fm.subs(t,ti)
        else:
            fm=fn.subs(Derivative(y(t),t),dy)
            fn=Derivative(fm,t).doit()
            fm=fm.subs(y(t),wi).evalf()
            fm=fm.subs(t,ti).evalf()
        res+=fm*((h**a)/factorial(a+1))
    return(res)

aprox=np.zeros((N+1,2)) #Definimos la matriz de relación entre t y las aproximaciones
aprox[0,1]=y1 
aprox[0,0]=inter[0]

for b in range(1,N+1,1):
    aprox[b,0]=aprox[b-1,0]+h
    aprox[b,1]=aprox[b-1,1]+h*Euler(aprox[b-1,0],aprox[b-1,1])

print(np.array(["t","y"],dtype=str))
print(aprox)

plot(aprox[:,0],aprox[:,1])
legend(['y aproximado'])
show()

