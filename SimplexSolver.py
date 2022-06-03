from socket import if_indextoname
from numpy.lib.function_base import append
from sympy import Symbol
import sympy
import math
import cmath            
import numpy as np
from sympy.simplify.simplify import simplify

#Ingresar datos originales
tam1=int(input("Ingrese el numero de variables de la forma estandar de MPL: "))
tam2=int(input("Ingrese el numero de restricciones de la forma estandar de MPL: "))

val1=(list(map(float,input("Ingrese los valores de las entradas de la matriz tecnologica yendo fila por fila y separando con un espacio cada valor: ").split())))
MatT=np.array(val1).reshape(tam2,tam1)

val2=(list(map(float,input("Ingrese los valores de las entradas del vector de recursos b por orden de filas y separando con un espacio: ").split())))
Vecb=np.array(val2).reshape(tam2,1)

val3=(list(map(float,input("Ingrese los valores de los coeficientes de cada variable de la función objetivo separados por espacio: ").split())))
Vecc=np.array(val3).reshape(1,tam1)

valb=(list(map(float,input("Ingrese el numero de las columnas de la matriz tecnologica que se tomaran como base inicial en orden (separelas por espacio): ").split())))
base=np.array(valb).reshape(1,tam2)

#Creacion de la base inicial
B=np.zeros(tam2*tam2).reshape(tam2,tam2)
cB=np.zeros(tam2).reshape(1,tam2)

#Columna
for a in range(1,tam2+1,1):
    cB[0,a-1]=Vecc[0,int(base[0,a-1])-1]
    #Fila
    for c in range(1,tam2+1,1):
        valor=base[0,a-1]
        B[c-1,a-1]=MatT[c-1,int(valor)-1]



#Imprimir Datos Originales
print("Matriz Tecnológica:")
print(MatT)
print("Vector de recursos:")
print(Vecb)
print("Vector de coeficientes de la funcion objetivo:")
print(Vecc)

#Iteraciones
conta=1
d=0
while d<conta:
    print("Iteración #"+str(d)+":")
    print("Base ("+str(d)+"):")
    print(B)
    print("Coeficientes de las variables basicas("+str(d)+"):")
    print(cB)
    IB=np.linalg.inv(B)
    print("Matriz inversa("+str(d)+"):")
    print(IB)
    Tab=np.dot(IB,MatT)
    print("Tabla("+str(d)+"):")
    print(Tab)
    xBo=np.zeros(tam2).reshape(tam2,1)
    xBo=np.dot(IB,Vecb)
    print("Vector X_B"+str(d)+":")
    print(xBo)
    SBF=np.zeros(tam1).reshape(1,tam1)
    #Columna
    for e in range(1,tam2+1,1):
        SBF[0,int(base[0,e-1])-1]=xBo[e-1,0]
    print("Vector de valores para variables basicas actuales("+str(d)+"):")
    print(SBF)
        
    Zmax=np.dot(cB,xBo)
    print("El valor optimo en la iteracion ("+str(d)+") es: "+ str(Zmax))
        
    z0=np.zeros(tam1).reshape(1,tam1)
    z0=np.dot(cB,Tab)
    print("Vector z("+str(d)+"):")
    print(z0)
    print(Vecc)

    #zres=z0-Vecc
    zres=np.zeros(tam1).reshape(1,tam1)
    for x in range(1,tam1+1,1):
        if (abs(z0[0,x-1]-int(z0[0,x-1])))<0.0000001 or (abs(Vecc[0,x-1]-int(Vecc[0,x-1])))<0.0000001:
            zres[0,x-1]=round(z0[0,x-1])-round(Vecc[0,x-1])
        else:
            zres[0,x-1]=z0[0,x-1]-Vecc[0,x-1]
    print("El vector (z-c)("+str(d)+") resultante es:")
    print(zres)
    minv=0
    ent=0
    for f in range(1,tam1+1,1):
        valact=zres[0,f-1]
        if valact<minv:
            minv=valact
            ent=f
    print(ent)
    if minv>=0:
        print("Se ha encontrado el valor óptimo")
        d+=1    
    elif minv<0:
        minc=0
        cont=0
        ento=0
        pes=0
        for g in range(1,tam2+1,1):
            for h in range(1,tam1+1,1):
                if h==ent and (Tab[g-1,h-1]!=0):
                    valor=(xBo[g-1,0])/(Tab[g-1,h-1])
                    print(valor)
                    if (valor>0) and (cont==0):
                        if minc==0:
                            minc=valor
                            pes=g-1
                        elif valor<minc:
                            minc=valor
                            pes=g-1
                    elif valor==0:
                        cont+=1
                        if cont==0:
                            base[0,g-1]=ent
            if g+1==tam2+1:
                base[0,pes]=ent
        if (cont==0) or (cont==1):
            print(base)
            #Nueva base
            for i in range(1,tam2+1,1):
                cB[0,i-1]=Vecc[0,int(base[0,i-1])-1]
                for j in range(1,tam2+1,1):
                    valor=base[0,i-1]
                    B[j-1,i-1]=MatT[j-1,int(valor)-1]
            conta+=1
            d+=1
            vali1=(int(input("Ingrese 0 o 1:")))
            if vali1==0:
                break
            elif vali1==1:
                continue
        elif cont>1:
            print("El MPL contiene un caso de degeneración")
            d+=1