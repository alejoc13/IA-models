from cmath import pi
import random as rd
import math
from matplotlib import pyplot as pl
import numpy as np
import matplotlib.pyplot as plt

def clonacion(z_pob,pob,n,Pc,Np):
    pob1 = []
    Clones = []
    copy_z = [i for i in z_pob]
    copy_z.sort()
    for i in range(n):
        val = copy_z[i]
        ind = z_pob.index(val)
        for i in range(round(Pc*Np)):
            Clones.append(pob[ind])
    for i in range(Np):
        val = copy_z[i]
        ind = z_pob.index(val)
        pob1.append(pob[ind])
    return Clones,pob1

def conversor_decimal(u,l,B,Nb):
    B = B[::-1] # invertir el vector para hacer la conversión correctamente.
    num = sum([(2**i)*B[i] for i in range(Nb)])
    den = sum(2**i for i in range(Nb))
    return  l + (num/den)*(u-l)
    

def crearIndividuos(dim,Nb):
    return [rd.randrange(0,2) for i in range(Nb*dim)]

def f(x):
    y = -x*math.sin(abs(x))
    return y

#Parametros iniciales del sistema 
Np = 100             # Tamaño de la poblacion 
n = 80               # Número de individuos a clonar 
dim = 1              # Dimensión del problema
Nb = 30             # Número de bits por dimención 
maxk = 50         # Cantidad máxima de iteraciones
Pm = 0.06            # Probabilidad de mutación
Pd = 0.05            # Porcentaje de diversidad
Pc = 0.05           # Porcentaje de clonación 
l,u = 0,100       # Limites del espacio de busqueda 
k = 0                # iteración actual
nc = round(Np*Pc*n)  # Numero total de clones en cada iteración 
nci = int(Np*Pc)    #Cantidad de cloens de cada  individuo
Pr = int(Np-Pd*Np-n) # Cantidad de población remanente/los mejores de cada generación
npd = int(Pd*Np)     #Cantidad de población por diversidad

#Para almacenar las soluciones.
x = [1 for i in range(Np)]
y = [1 for i in range(Np)]


#Para la matriz Clonada y mutada
xm = [0 for i in range(nc)]
ym = [0 for i in range(nc)]


pob = [crearIndividuos(dim,Nb) for i in range(Np)]
sol = []
sol_prom=[]
#A partir de aquí se inicia las iteraciones
for i in range(Np):
    x[i] = conversor_decimal(u,l,pob[i],Nb)
    y[i] = f(x[i])
#Se obtiene la matriz de clonación y la población reorganizada

while k<maxk:
    Clones,pob1 = clonacion(y,pob,n,Pc,Np)
    #Mutación de la matriz de clonación
    Cm = []
    for i in Clones:
        aux=[]
        for j in range(Nb*dim):
            r = rd.random()
            if r<=Pm:
                if i[j] == 1:
                    aux.append(0) 
                else:
                    aux.append(1)
            else:
                aux.append(i[j])
        Cm.append(aux)

    #Analisis de la matirz clonacional mutada
    for i in range(nc):
        xm[i] = conversor_decimal(u,l,Cm[i],Nb)
        ym[i] = f(xm[i])
    #proceso de reselección
    Cmr = []
    for i in range(0,nc,nci):
        cambio = min(ym[i:i+nci])
        ind_cambio = ym.index(cambio)
        aux = Cm[ind_cambio]
        Cmr.append(aux)

    pob2 = pob1[0:Pr]+Cmr
    for i in range(npd):
        aux = crearIndividuos(dim,Nb)
        pob2.append(aux)
    pob = pob2
    for i in range(Np):
        x[i]= conversor_decimal(u,l,pob[i],Nb)
        y[i] = f(x[i])
    
    sol.append(min(y))
    x_sol = x[y.index(min(y))]
    sol_prom.append(sum(y)/Np)

    k+=1

print('Generando graficos...Espere un momento')
k = l
x =[]
y=[]
#para generar el vector sin numpy 
while k<u:
    x.append(k)
    y.append(f(k))
    k+=0.0001

print(f"El punto de menor energía es:\nx:{x_sol}\ny:{f(x_sol)}")
pl.plot(x,y,label='función optimizada')
pl.plot(x_sol,sol[-1],marker='x',label='solución encontrada')
pl.legend(loc='upper left')
pl.xlabel("Variable independiente (x)", size = 10)
pl.ylabel("Función objetivo f(x)", size = 10)
pl.grid()
pl.show()
a = pl.figure(1)
pl.title("Comportamiento Sistemas Inmunes Artificiales")
pl.plot(sol,label="solucion escogida")
pl.plot(sol_prom,label='Promedio de las soluciones')
pl.legend(loc='upper right')
pl.xlabel("Iteración", size = 10)
pl.ylabel("Aptitud", size = 10)
pl.grid()
pl.show()