from cmath import pi
import random as rd
import math
from matplotlib import pyplot as pl
import numpy as np
import matplotlib.pyplot as plt
def crearIndividuos(dim,Nb):

    return [rd.randrange(0,2) for i in range(Nb*dim)]
    

def conversor_decimal(u,l,B,Nb):

    B = B[::-1] # invertir el vector para hacer la conversión correctamente.
    num = sum([(2**i)*B[i] for i in range(Nb)])
    den = sum(2**i for i in range(Nb))
    dec =  l + (num/den)*(u-l)

    return dec

def f(x,y):
    return -(y+47)*math.sin(math.sqrt(abs(y+(x/2)+47)))- x*math.sin(math.sqrt(abs(x-(y+47))))
    #return -1/(1+abs(x+(2+1j)*y+1))
    #return   x**2 + y**2
    #return -(math.sin(x)*(math.sin((x**2)/pi)**20)+math.sin(y)*(math.sin((2*(y**2)/pi))**20))
 



# ----Metodo de selección de la Ruleta
def seleccionRuleta(z_pob):
    # se genera el acomulado de las solucones
    E = -sum(z_pob) # El negativo se usa en caso de minimización 
    pi =  [-i/E for i in z_pob ] #se genera la probabilidad  de selección de cada individuo
    qi = []
    qi.append(pi[0])
    for i in range(1,len(pi),1): #probabilidad acomulada de cada solución
        qi.append(sum(pi[0:i+1]))
    r = rd.random() # valor de referencia para seleccionar
    for i in range(len(qi)):
        if qi[i]>r:   #comparacion del valor acomulado con el valor de referencia para seleccionar un padre
            return i
            break
 
#---- Inicialización de parametros del metodo AG
Nb = 40 # por cada dimención, por tanto la cadena total debe contener el doble.
u = 600
l = -600
dim = 2
cantPob = 100
iter = 200
mut = 0.04
pobDecimal = []
x_pob = [0 for i in range(cantPob)]
y_pob = [0 for i in range(cantPob)]
z_pob = [0 for i in range(cantPob)]
x_iter = []
y_iter = []
sol_iter =[]
k_iter = []
sol_prom = []
k = 0

#----Creación de la poblacón inicial y sus soluciones
pob = [crearIndividuos(dim,Nb) for i in range(cantPob)]

while k<iter:
    for i in range(cantPob):
        x_pob[i],y_pob[i] =  conversor_decimal(u,l,pob[i][0:Nb],Nb),conversor_decimal(u,l,pob[i][Nb::],Nb)
        z_pob[i] = f(x_pob[i],y_pob[i])
    #---- Selección de los padres mas aptos de cada generación
    p1 = seleccionRuleta(z_pob)
    p2 = seleccionRuleta(z_pob)
    padre1 = pob[p1]
    padre2 = pob[p2]
    
    #----se inicia la operación de cruce de individuos (Multiples puntos de cruce)
    pc1 = rd.randrange(Nb*2-4)
    pc2 = rd.randrange(pc1,Nb*2)
    
    #----Se generan los hijos necesarios
    h1 = pob[p1][0:pc1]+pob[p2][pc1:pc2]+pob[p1][pc2::]
    h2 = pob[p2][0:pc1]+pob[p1][pc1:pc2]+pob[p2][pc2::]

    #---proceso de mutación 
    for i in range(Nb*2):
        r = rd.random()
        if r> mut:
            h1[i] = rd.randrange(0,2)
        r = rd.random()
        if r> mut:
            h2[i] = rd.randrange(0,2)
    aux  = z_pob.index(max(z_pob))
    pob[aux] = h1 
    aux  = z_pob.index(max(z_pob))
    pob[aux] = h2
    
    z_min = min(z_pob)
    x_min = x_pob[z_pob.index(z_min)]
    y_min = y_pob[z_pob.index(z_min)]
    sol_iter.append(z_min)
    k_iter.append(k)
    x_iter.append(x_min)
    y_iter.append(y_min)
    sol_prom.append(sum(z_pob)/cantPob)
    k+=1

X = np.arange(l,u,0.1)
Y = np.arange(l,u,0.1)
x,y = np.meshgrid(X,Y)

#z = -1/(1+np.abs(x+(0+1j)*y+1))
#z = x**2 +y**2
z= -(y+47)*np.sin(np.sqrt(np.abs(y+(x/2)+47)))- x*np.sin(np.sqrt(np.abs(x-(y+47))))
#z = -(np.sin(x)*(np.sin((x**2)/pi)**20)+np.sin(y)*(np.sin((2*(y**2)/pi))**20))

ax = plt.axes(projection='3d')
ax.plot_surface(x,y,z)
pl.title("Función objetivo")
pl.xlabel("x")
pl.ylabel("y")
plt.show()

a = pl.figure(1)
pl.plot(sol_iter,label='Promedio de las soluciones')
pl.plot(sol_prom)
pl.title("Comportamineto AG")
pl.xlabel("Iteración")
pl.ylabel("f(x,y)")
pl.grid()
pl.show()
print(f"El punto de menor energía se encontró en:\nx:{x_iter[-1]}\ny:{y_iter[-1]}\ncon un valor de\nz:{sol_iter[-1]}")
print(f"El minimo esperado es: {np.min(z)}")