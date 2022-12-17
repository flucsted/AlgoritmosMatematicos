from pickle import FALSE, TRUE 
from turtle import color
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

tamagraf=int(input("Ingrese la cantidad de nodos que componen al grafo: "))

#Creación del grafo completo
G=nx.Graph()
val1=[]
val2=[]
for i in range(1,tamagraf,1):
    G.add_node(i)
#Creación de las aristas con su respectivo peso
for j in range(1,tamagraf,1):
    for k in range(j,tamagraf,1):
        valed=float(input("Ingrese la distancia del nodo "+str(j)+" al nodo "+str(k+1)+": "))
        val1.append(valed)
        if(valed!=0):
            G.add_edge(j,k+1,dis=valed)
#Reorganizar val1 en una matriz con los pesos de cada camino posible (incluso cuando i=j)
conta1=0
for a in range(1,tamagraf+1,1):
    for b in range(1,tamagraf+1,1):
        if((b==a) or (b<a)):
            val2.append(0)
        elif(b>a):
            val2.append(val1[conta1])
            conta1+=1           
list=np.array(val2).reshape(tamagraf,tamagraf)

print(list)
listver=[]
listpes=[]
max=0
for c in range(1,tamagraf+1,1):
    for d in range(1,tamagraf+1,1):
        if(max<list[c-1,d-1]):
            max=list[c-1,d-1]

conta1=0
contarep=0
listarb=[]
listarbrep=[]
while conta1<tamagraf-1:
    node1=0
    node2=0
    min=max
    for e in range(1,tamagraf+1,1):
        for f in range(1,tamagraf+1,1):
            if (list[e-1,f-1]!=0):
                if(min>list[e-1,f-1] and conta1==0):
                    min=list[e-1,f-1]
                    node1=e
                    node2=f
                elif(min>list[e-1,f-1] and conta1!=0):
                    c=0
                    cont=0
                    while c<conta1*2:
                        if(vecarb[c]==e and vecarb[c+1]==f):
                            cont+=1
                        c+=2
                    if(cont<1):
                        if((e in vecrep)==False or (f in vecrep)==False):
                            min=list[e-1,f-1]
                            node1=e
                            node2=f
                        elif((e in vecrep)==True and (f in vecrep)==True): #Verificamos si ambos valores ya estan conectados en un mismo arbol
                            listTemp1=[]
                            listTemp2=[]
                            cont1=0 #Contador del while
                            cont2=0 #Contador del indice del vector Temp1
                            cont6=0 #Contador del indice del vector Temp2
                            cont4=0 #Contador del ciclo para Temp1
                            cont5=0 #Conatdor del ciclo para Temp2
                            while cont1<1:
                                cont3=0 #Contador de actividad en Temp1
                                cont7=0 #Contador de actividad en Temp2
                                for a in range(0,conta1*2,2): #Temp1 (e)
                                    if (cont4==0):  #Agregamos primero al valor conectado a "e"
                                        if(vecarb[a]==e):
                                            listTemp1.append(vecarb[a+1])
                                            cont3+=1
                                        elif(vecarb[a+1]==e):
                                            listTemp1.append(vecarb[a])
                                            cont3+=1
                                    elif (cont4>0): #Agregamos a la lista al siguiente valor conectado en el arbol a partir de "e"
                                        if(vecarb[a]==vecTemp1[cont2-1] and (vecarb[a+1] in listTemp1)==False and (vecarb[a+1]!=e)):
                                            listTemp1.append(vecarb[a+1])
                                            cont3+=1
                                        elif(vecarb[a+1]==vecTemp1[cont2-1] and (vecarb[a] in listTemp1)==False and (vecarb[a]!=e)):
                                            listTemp1.append(vecarb[a])
                                            cont3+=1
                                for b in range(0,conta1*2,2): #Temp2 (f)
                                    if (cont5==0): #Agregamos primero al valor conectado a "f"
                                        if(vecarb[b]==f):
                                            listTemp2.append(vecarb[b+1])
                                            cont7+=1
                                        elif(vecarb[b+1]==f):
                                            listTemp2.append(vecarb[b])
                                            cont7+=1
                                    elif (cont5>0): #Agregamos a la lista al siguiente valor conectado en el arbol a partir de "f"
                                        if(vecarb[b]==vecTemp2[cont6-1] and (vecarb[b+1] in listTemp2)==False and (vecarb[b+1]!=f)):
                                            listTemp2.append(vecarb[b+1])
                                            cont7+=1
                                        elif(vecarb[b+1]==vecTemp2[cont6-1] and (vecarb[b] in listTemp2)==False and (vecarb[b]!=f)):
                                            listTemp2.append(vecarb[b])
                                            cont7+=1
                                if(cont3>0 and cont7>0):
                                    cont4+=1
                                    cont6+=1
                                    cont2+=1
                                    cont5+=1
                                elif(cont3>0):
                                    cont2+=1
                                    cont4+=1
                                elif(cont7>0):
                                    cont6+=1
                                    cont5+=1
                                elif(cont3==0 and cont7==0):
                                    cont1+=1
                                vecTemp1=np.array(listTemp1)
                                vecTemp2=np.array(listTemp2)

                            contador=0
                            lisvec1=np.ndarray.tolist(vecTemp1)
                            lonvec=len(lisvec1) #Verificamos la longitud de vecTemp1
                            lisvec2=np.ndarray.tolist(vecTemp2)
                            # Barremos por todo vecTemp1 para verificar si alguno de sus elementos esta en vecTemp2,
                            # si resulta que si hay algun elemento de vecTemp1 en vecTemp2 concluiremos que si estan conectados
                            # y el programa se lo saltara y continuara la busqueda
                            for b in range(0,lonvec,2): 
                                if(vecTemp1[b] in lisvec2):
                                    contador+=1
                            if(contador==0):
                                min=list[e-1,f-1]
                                node1=e
                                node2=f
                            else:
                                continue
    if(conta1!=0):
        #if((node1 in vecarb)==True and (node2 in vecarb)==True)==False:
        listarb.append(node1)
        listarb.append(node2)
        listpes.append(min)
        vecarb=np.array(listarb)
        vecpes=np.array(listpes)
        conta1+=1
        #elif((node1 in vecarb)==True and (node2 in vecarb)==True):
        #    listarb.append(node1)
        #    listarb.append(node2)
        #    listpes.append(min)
        #    vecarb=np.array(listarb)
        #    vecpes=np.array(listpes)
        #    conta1+=1
    elif(conta1==0):
        listarb.append(node1)
        listarb.append(node2)
        listpes.append(min)
        vecarb=np.array(listarb) #Se agrega la ruta a una lista que registrara el estado actual del arbol
        vecpes=np.array(listpes)
        vecrep=[] 
        vecesp=[]
        conta1+=1
    #Verificación de arbol
    conta=0
    templist=[]
    Listarb=np.ndarray.tolist(vecarb)
    while conta<tamagraf: #Vemos el numero de veces que aparece un nodo en el arbol y lo guardamos si aparece minimo 2 veces
        contarb=Listarb.count(conta+1)
        if(contarb==2 or contarb>2):
            templist.append(conta+1)
        conta+=1
    c=0
    while c<conta1*2: #Verificamos cuales son los valores "pareja" de aquellos valores que sabemos que aparecen almenos 1 vez en vecarb
        if((vecarb[c] in templist)==True and (vecarb[c+1] in vecrep)==False):
            listarbrep.append(vecarb[c+1])
            contarep+=1
        if((vecarb[c+1] in templist)==True and (vecarb[c] in vecrep)==False):
            listarbrep.append(vecarb[c])
            contarep+=1    
        c+=2
    vecrep=np.array(listarbrep)

print(vecpes)
print(vecarb)
print(vecrep)

#Creación del grafo mínimo
F=nx.Graph()
for i in range(1,tamagraf,1):
    F.add_node(i)
#Creación de las aristas con su respectivo peso
j=0
for k in range(1,(tamagraf*2)-1,2):
    F.add_edge(vecarb[k-1],vecarb[k],dist=vecpes[j])
    j+=1

pos=nx.circular_layout(G) #Por default "planar_layout" tiene dim=2
nx.draw_networkx(G,pos)
labels=nx.get_edge_attributes(G, 'dis')
nx.draw_networkx_edge_labels(G,pos,labels)
plt.title("Grafo completo")
plt.show()

pos1=nx.circular_layout(F) #Por default "planar_layout" tiene dim=2
nx.draw_networkx(F,pos1)
labels1=nx.get_edge_attributes(F, 'dist')
nx.draw_networkx_edge_labels(F,pos1,labels1)
plt.title("Grafo mínimo")
plt.show()
