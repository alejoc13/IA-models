from cmath import pi
import random as rd
import math
from matplotlib import pyplot as pl
import numpy as np
import matplotlib.pyplot as plt

def clonacion(z_pob,pob,n,Pc,Np):
    """
    Parameters
    ----------
    z_pob: List
    Description:evaluacion en la función objetivo
    pob: list 
    description: población binaria
    n: int 
    description: cantidad de individuos a clonar
    Pc: int
    description: porcentaje de clonación
    Np: int
    description: Tamaño de la clonación
    retornar: list 
    description: Matriz de clones

    Returns
    ----------
    Clones: list
    description: matriz de clones del sistema
    pob1: list
    description: Pobalción de la generación actual reorganizada
    """
    pob1 = []
    Clones = []
    copy_z = [i for i in z_pob]
    copy_z.sort()
    for i in range(n):
        val = copy_z[i]
        ind = z_pob.index(val)
        for j in range(round(Pc*Np)):
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
    """crea individuos binarios de tamaño dim*Nb donde:
    Nb: Número de bits en por cada dimención 
    dim: Dimenciones en las que esta determinado el problema
    retorna: Una cadena binaria de bits
    """
    return [rd.randrange(0,2) for i in range(Nb*dim)]

def f(x,y):
    """ Esta función es la encargada de evaluar la función objetivo en 
    dos dimenciones"""
    return -(y+47)*math.sin(math.sqrt(abs(y+(x/2)+47)))- x*math.sin(math.sqrt(abs(x-(y+47))))
    #return x**2 + y**2

#Parametros iniciales del sistema 
Np = 100             # Tamaño de la poblacion 
n = 80               # Número de individuos a clonar 
dim = 2              # Dimensión del problema
Nb = 30              # Número de bits por dimención 
maxk = 50            # Cantidad máxima de iteraciones
Pm = 0.04            # Probabilidad de mutación
Pd = 0.05            # Porcentaje de diversidad
Pc = 0.06            # Porcentaje de clonación 
l,u =-600,600        # Limites del espacio de busqueda 
k = 0                # iteración actual
nc = round(Np*Pc*n)  # Numero total de clones en cada iteración 
nci = int(Np*Pc)     #Cantidad de cloens de cada  individuo
Pr = int(Np-Pd*Np-n) # Cantidad de población remanente/los mejores de cada generación
npd = int(Pd*Np)     #Cantidad de población por diversidad

#Para almacenar las soluciones.
x = [1 for i in range(Np)]
y = [1 for i in range(Np)]
z = [1 for i in range(Np)]

#Para la matriz Clonada y mutada
xm = [0 for i in range(nc)]
ym = [0 for i in range(nc)]
zm = [0 for i in range(nc)]

pob = [crearIndividuos(dim,Nb) for i in range(Np)]
sol = []
sol_prom = []
#A partir de aquí se inicia las iteraciones
for i in range(Np):
    x[i],y[i] = conversor_decimal(u,l,pob[i][0:Nb],Nb),conversor_decimal(u,l,pob[i][Nb::],Nb)
    z[i] = f(x[i],y[i])
#Se obtiene la matriz de clonación y la población reorganizada

while k<maxk:
    Clones,pob1 = clonacion(z,pob,n,Pc,Np)
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
        xm[i],ym[i] = conversor_decimal(u,l,Cm[i][0:Nb],Nb),conversor_decimal(u,l,Cm[i][Nb::],Nb)
        zm[i] = f(xm[i],ym[i])
    #proceso de reselección
    Cmr = []
    for i in range(0,nc,nci):
        cambio = min(zm[i:i+nci])
        ind_cambio = zm.index(cambio)
        aux = Cm[ind_cambio]
        Cmr.append(aux)

    pob2 = pob1[0:Pr]+Cmr
    for i in range(npd):
        aux = crearIndividuos(dim,Nb)
        pob2.append(aux)
    pob = pob2
    for i in range(Np):
        x[i],y[i] = conversor_decimal(u,l,pob[i][0:Nb],Nb),conversor_decimal(u,l,pob[i][Nb::],Nb)
        z[i] = f(x[i],y[i])
    
    sol.append(min(z))
    sol_prom.append(sum(z)/Np)
    x_sol = x[z.index(min(z))]
    y_sol = y[z.index(min(z))]


    k+=1

    
print(f"El punto de menor energía es:\nx:{x_sol}\ny:{y_sol}\nz:{sol[-1]}")
a = pl.figure(1)
pl.title("Comportamiento Sistemas Inmjunes artificiales")
pl.plot(sol,label='soluciones')
pl.plot(sol_prom,label='Promedio de las soluciones')

pl.legend(loc='upper right')
pl.xlabel("Iteración", size = 10)
pl.ylabel("f(x,y)", size = 10)
pl.grid()
pl.show()