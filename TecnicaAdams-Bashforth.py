import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

norder=2 # Ingresar el número de pasos del método de Adams-Moulton a emplear ------
t,y=sp.symbols('t y')
limit=np.array([1,2]) # Límites de aproximación en t ------
dy=1+(y/t) # Función del PVI ------
y1=2 # Valor inicial en el t inicial ------
N=5 # Número de aproximaciones deseadas dentro del intervalo de t (recordar h=(b-a)/N )-------
h=(limit[1]-limit[0])/N

#Función para obtener las alpha restantes por medio de Rungen-kutta de orden 4
def Ini(ini):

    b=ini+(norder-1)*h
    limit=np.array([0,b])
    tt=limit[0]
    w=y1

    aprox=np.zeros([N+1,2])
    aprox[0,0]=tt
    aprox[0,1]=w

    for i in range(1,norder,1):
       K1=h*dy.subs(t,tt).subs(y,w).evalf()
       K2=h*dy.subs(t,tt+h/2).subs(y,w+K1/2).evalf()
       K3=h*dy.subs(t,tt+h/2).subs(y,w+K2/2).evalf()
       K4=h*dy.subs(t,tt+h).subs(y,w+K3).evalf()

       w=w+(K1+2*K2+2*K3+K4)/6
       tt=limit[0]+i*h
       aprox[i,0]=tt
       aprox[i,1]=w
    return aprox

aprox=Ini(limit[0])

if norder==2:
    for i in range(1,N,1):
        aprox[i+1,0]=aprox[0,0]+(i+1)*h
        aprox[i+1,1]=aprox[i,1]+(h/2)*(3*dy.subs(t,aprox[i,0]).subs(y,aprox[i,1]).evalf()-dy.subs(t,aprox[i-1,0]).subs(y,aprox[i-1,1]).evalf())
elif norder==3:
    for i in range(2,N,1):
        aprox[i+1,0]=aprox[0,0]+(i+1)*h
        aprox[i+1,1]=aprox[i,1]+(h/12)*(23*dy.subs(t,aprox[i,0]).subs(y,aprox[i,1]).evalf()-16*dy.subs(t,aprox[i-1,0]).subs(y,aprox[i-1,1]).evalf()+5*dy.subs(t,aprox[i-2,0]).subs(y,aprox[i-2,1]).evalf())
elif norder==4:
    for i in range(3,N,1):
        aprox[i+1,0]=aprox[0,0]+(i+1)*h
        aprox[i+1,1]=aprox[i,1]+(h/24)*(55*dy.subs(t,aprox[i,0]).subs(y,aprox[i,1]).evalf()-59*dy.subs(t,aprox[i-1,0]).subs(y,aprox[i-1,1]).evalf()+37*dy.subs(t,aprox[i-2,0]).subs(y,aprox[i-2,1]).evalf()-9*dy.subs(t,aprox[i-3,0]).subs(y,aprox[i-3,1]).evalf())
#elif norder==5:
#    for i in range(4,N,1):
#        aprox[i+1,0]=aprox[0,0]+(i+1)*h
#        aprox[i+1,1]=aprox[i,1]+(h/720)*(1901*dy.subs(t,aprox[i,0]).subs(y,aprox[i,1]).evalf()-2774*dy.subs(t,aprox[i-1,0]).subs(y,aprox[i-1,1]).evalf()+2616*dy.subs(t,aprox[i-2,0]).subs(y,aprox[i-2,1]).evalf()-1274*dy.subs(t,aprox[i-3,0]).subs(y,aprox[i-3,1]).evalf()+251*dy.subs(t,aprox[i-4,0]).subs(y,aprox[i-4,1]).evalf())

print(np.array(['t','w'],dtype=str))

vec=np.zeros(10)
conta=0
for i in range(0,10,1):
    hh=(limit[1]-limit[0])/20
    y=t*sp.log(t)+2*t
    vec[i]=y.subs(t,limit[0]+(i+1)*hh).evalf()
    if i==0 or i==1:
        aprox[i,0]+=1
    if i%2==0 and i>0:
        aprox[conta+1,1]=vec[i]
        conta+=1
        aprox[conta+1,0]+=1
    if i==9:
        aprox[conta+1,1]=vec[i]
    
    

print(aprox)
vec2=np.array([1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2])
plt.plot(aprox[:,0],aprox[:,1])
plt.plot(vec2[:],vec[:])
plt.legend(['y aproximado', 'valor real'])
plt.show()