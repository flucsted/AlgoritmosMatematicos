import numpy as np
import random as rd
from numpy import size 

tamtab=6#int(input("Ingrese el número de reinas a acomodar: "))
cansol=3#int(input("Ingrese la cantidad de tableros que desea tener como soluciones iniciales: "))
Numit=200000    
Nvar=3 #Numero de variables de decision
HMCR=rd.uniform(0,1) #Tasa de aceptación de la memoria armonica
PAR=rd.uniform(0,1) #Tasa de ajuste de tono

class Complementos:
    def OneMax(HMS):
        HMSTemp=np.transpose(HMS)
        Fx=np.sum(HMSTemp,axis=0)
        return Fx

    def CamArm(sim,coord,newHMS,HMS):
        Fx=Complementos.OneMax(HMS)

        coordx=np.where(Fx==np.amax(Fx))
        coordi=coordx[0].tolist()
        cord=np.array(coordi)
        cordn=rd.randint(0,size(cord)-1)
        
        matrizcand=sim[coord,:,:] #Tomamos la matriz que va a ser modificada y la guardamos
        multmatrizcand=sim
        
        newHMS=np.array(newHMS) #Posible nuevo ajuste de armonia
        actHMS=np.array(HMS[cordn]) #Armonia seleccionada para cambiarse
        conta=0 
        while conta<250:
            #Acciones en caso de que la fila/columna/diagonal posea la mayor diferencia
            random=rd.uniform(0,1)
            if random<=0.5: #Movimiento por fila
                randf=rd.randint(0,tamtab-1)
                vectemp=matrizcand[randf,:]
                randd=rd.uniform(0,1)
                if randd<=0.5: #Desplazamiento a la izquierda
                    vectemp=np.roll(vectemp,-1)
                    matrizcand[randf,:]=vectemp
                else: #Desplazamiento a la derecha
                    vectemp=np.roll(vectemp,1)
                    matrizcand[randf,:]=vectemp
            else: #Movimiento por columna
                randc=rd.randint(0,tamtab-1)
                vectemp=matrizcand[:,randc]
                randd=rd.uniform(0,1)
                if randd<=0.5: #Desplazamiento hacia arriba
                    vectemp=np.roll(vectemp,-1)
                    matrizcand[:,randc]=vectemp
                else: #Desplazamiento hacia abajo
                    vectemp=np.roll(vectemp,1)
                    matrizcand[:,randc]=vectemp
            multmatrizcand[cordn,:,:]=matrizcand
            ArmTemp=BusquedaArmonica.MemArm(multmatrizcand)
            actHMS=ArmTemp[cordn,:]
            actHMSsum1=Complementos.OneMax(actHMS) #Comprobamos el fitness general de está nueva armonia
            actHMSsum=Complementos.OneMax(actHMSsum1)
            if np.array_equal(actHMS,newHMS) or actHMSsum==0: #Termina el ciclo en caso de que se llegue a la armonia solicitada o si se encuentra directamente la solución
                break
            conta+=1
        return matrizcand

class BusquedaArmonica:
    #Generamos la armononia inicial
    def GenDArm():
        #Generamos cansol matrices de tamaño tamtab*tamtab llenas de ceros
        matrizcero = np.zeros(shape=(cansol,tamtab,tamtab),dtype=int) #(shape=(n. matrices,n. filas, n. columnas)) (#matriz, #fila, #columnna)
        #Introduciremos las reinas en matrices "desechables" por filas que nos permitiran verificar los resultados por iteración
        matrizcand=matrizcero 
        for b in range(0,cansol,1): #Paso entre matrices
            for c in range(0,tamtab,1): #Paso entre filas
                temprand=rd.randint(0,tamtab-1)
                matrizcand[b,c,temprand]=1
        return matrizcand

    #Evaluador del HMS actual
    def MemArm(sim): 
        HMS=[]
        #Hacemos el conteo de reinas por fila y columna, y registramos un aumento en caso de que exista alguna fila/columna con almenos 2 reinas
        for a in range(0,cansol,1): #Matriz
            contemp1=contemp2=contemp3=0 ############
            for b in range(0,tamtab,1): #Fila/Columna
                fila=sim[a,b,:]
                fila=fila.tolist()
                conteo1=fila.count(1) #Conteo fila
                columna=[columna[b] for columna in sim[a]]
                conteo2=columna.count(1) #Conteo columna
                if(conteo1==2 or conteo1>2):
                    contemp1+=1
                if(conteo2==2 or conteo2>2):
                    contemp2+=1
            for c in range(-tamtab+1,tamtab,1): #Diagonales
                simdia=np.diag(sim[a],k=c) 
                siminvdia=np.fliplr(sim[a])
                siminvdia=np.diag(siminvdia,k=c)
                simdia=simdia.tolist() #Lista de la diagonal principal 
                siminvdia=siminvdia.tolist() #Lista de la diagonal secundaria
                conteo1=simdia.count(1) #Conteo en la diagonal principal 
                conteo2=siminvdia.count(1) #Conteo en la diagonal secundaria
                
                if(conteo1==2 or conteo1>2):
                    contemp3+=1
                if(conteo2==2 or conteo2>2):
                    contemp3+=1
            HMS.append(contemp1)
            HMS.append(contemp2)
            HMS.append(contemp3)
        HMS=np.array(HMS).reshape(cansol,3)
        return HMS
    
    #Verificamos el ancho de banda actual
    def AnchoDeBanda(HMS): 
        BW=[] #Inicializamos la lista de anchos de banda
        HMSFil=np.array(HMS[:,0]).reshape(1,cansol) #Extraemos los valores del HMS actual por cada variable de decision
        HMSCol=np.array(HMS[:,1]).reshape(1,cansol)
        HMSDia=np.array(HMS[:,2]).reshape(1,cansol)
        BW.append(np.std(HMSFil)) #Desviacion estandar por filas
        BW.append(np.std(HMSCol)) #Desviacion estandar por columnas
        BW.append(np.std(HMSDia)) #Desviacion estandar por diagonales
        BW=np.array(BW)
        return BW

    def BusArm(HMS,BW):
        confirm=False
        conta=0
        newHMS=[]
        while conta<Nvar:
            if(rd.uniform(0,1)<HMCR):
                indice=rd.randint(1,cansol) #Se elige algún elemento de la armonia actual
                if(rd.uniform(0,1)<PAR):
                    newHMSi=HMS[indice-1,conta]+round(BW[conta]*(rd.uniform(0,1)))
                else:
                    newHMSi=HMS[indice-1,conta]
            else:
                if(conta<2):
                    newHMSi=rd.randint(0,round(tamtab/2))
                else:
                    newHMSi=rd.randint(0,tamtab)
            newHMS.append(newHMSi)
            conta+=1
        newHMS=np.array(newHMS)
        FxHMS=Complementos.OneMax(HMS)
        Fxnew=Complementos.OneMax(newHMS)
        MaxHMS=np.amax(FxHMS)
        Maxnew=np.amax(Fxnew)
        if(Maxnew<MaxHMS):
            coord=np.where(FxHMS==np.amax(FxHMS)) #Array que posee cual es la matriz candidata considerada para cambiarse
            coordi=coord[0].tolist()
            cord=np.array(coordi) 
            coordenada=cord[0] #Tomamos el primer valor de la lista del/de candidato/s a modificar 
            newarm=Complementos.CamArm(sim,coordenada,newHMS,HMS) #Se lleva a cabo el proceso de cambio de la matriz candidata 
            simaux=sim
            simaux[coordenada,:,:]=newarm
            HMSTemp=BusquedaArmonica.MemArm(simaux)
            HMSTempNew=HMSTemp[coordenada,:]
            newarmsum=Complementos.OneMax(HMSTempNew)
            if np.array_equal(HMSTempNew,newHMS) or newarmsum==0:
                for a in range(0,Nvar,1):
                    HMS[coordenada,a]=newHMS[a] #Se cambia la memoria armonica actual en caso de que se haya confirmado que esta es posible
                sim[coordenada,:,:]=newarm #Se lleva a cabo el ajuste armonico en la matriz de cambio 
                confirm=True
        return confirm

###############################################################################################################################################
#Aplicación del algoritmo
sim=BusquedaArmonica.GenDArm() #Generamos las soluciones iniciales
HMS=BusquedaArmonica.MemArm(sim) #Memoria armonica actual
attempt=1
while attempt<Numit:
    bool=False
    BW=BusquedaArmonica.AnchoDeBanda(HMS) #Ancho de banda actual
    BusArm=BusquedaArmonica.BusArm(HMS,BW) #Busqueda armonica dada la HMS actual
    print(attempt)
    if BusArm==True:
        Fx=Complementos.OneMax(HMS) #Aplicacion del One Max sobre la HMS actualizada
        for a in range(0,cansol,1):
            if Fx[a]==0:
                bool=True
                break
    if bool==True:
        break
    attempt+=1
print("Las soluciones resultantes fueron: ")
print(sim)
print("Con un fitness de:")
print(HMS)