#---- importar las librerías que se nececitan
import math
import random
import statistics
from matplotlib import pyplot as pl

#definir la función de trabajo
def f(x):
    y = -x*math.sin(abs(x))
    return y

#covnersor de binario a decimal con limites
def conversor_decimal(u,l,B,Nb):

    B = B[::-1] # invertir el vector para hacer la conversión correctamente.
    num = sum([(2**i)*B[i] for i in range(Nb)])
    den = sum(2**i for i in range(Nb))
    dec =  l + (num/den)*(u-l)

    return dec
#------Selección por ruleta
def seleccion(q):
    sel = -1
    r = random.random()
    for i in range(len(q)):
        if q[i] > r:
            sel = i
            break
    return sel

# Calcular probabilidad de aceptación p
def p_function(y_pob):
    ny_pob = []
    for i in range(len(y_pob)):
        aux=-1*y_pob[i]
        ny_pob.append(aux)
    E = sum(ny_pob)
    p = []
    for i in range(len(ny_pob)):
        aux = ny_pob[i]
        aux = aux/E
        p.append(aux)
    return p
#------ Inicialización de los valores predeterminados del modelo.

k = 0 # contador del ciclo while
Niter = 200 #numero de iteraciones
u = 100.0 #limite superior
l = 0.0 #limiter inferior
pi = 100 #tamaño de la población inicial.
Nb = 17 #número de bits de la población.
mut = 0.75
y_prom = [] #para poder guardar como cambia el promedio de la población con las ejecuciones

#Creación de la pobalción inicial

pob = [] #para guardar la pobalción
x_pob = [] #para guardar los valores decimales de la poblacion
y_pob = [] #fitness de la población
y_min = [] #mejor solución a lo largo de las generaciones.

for i in range(pi): 
    B = []   #para guardar los individuos
    for j in range(Nb):
        B.append(random.randint(0,1))
    pob.append(B)
    dec = conversor_decimal(u,l,B,Nb)
    x_pob.append(dec)
    y_pob.append(f(dec))

#------Aquí inicial el ciclo iterativo de lso algoritmos genéticos.
while k<Niter:
    #selección para los padres para los cruces
    p = p_function(y_pob)
    q = []
    for i in range(len(p)):
        q.append(0)
    q[0] = p[0]
    for c in range(1,len(p)):
        q[c] = sum(p[0:c+1])
    sel = seleccion(q)
    p1 = pob[sel]
    sel = seleccion(q)
    p2 = pob[sel]
    # Generar el punto de cruce
    pc = random.randint(2,Nb-2)
    #crear a los hijos
    
    h1 = []
    h2 = []
    h1 = p1[0:pc+1]+p2[pc+1::]
    h2 = p2[0:pc+1]+p1[pc+1::]
    #mutacion
    for i in range(Nb):
        r = random.random()
        if mut>r:
            h1[i] = random.randint(0,1)
        r = random.random()
        if mut>r:
            h2[i] = random.randint(0,1)
    #reemplazo de los dos peores
    re = max(y_pob)
    ind=y_pob.index(re)
    pob[ind] = h1
    re = max(y_pob)
    ind=y_pob.index(re)
    pob[ind] = h2
    #análisis de la poblacion
    for i in range(pi):
        B = pob[i]
        dec = conversor_decimal(u,l,B,Nb)
        x_pob[i]= dec
        y_pob[i] = f(dec)

    #seleccionar el mas apto para presentar solución
    aux = min(y_pob)
    ind = y_pob.index(aux)
    x_sol = x_pob[ind]
    y_sol = y_pob[ind]
    #Datos para graficar la fitness
    aux=statistics.mean(y_pob)
    y_prom.append(aux)
    y_min.append(y_sol)
    k+=1
    if y_prom[-1] == y_sol:
        break

#------ aquí termina el ciclo iterativo del AG y empiza la entrega de información

#------ Sección para entregar información 

#información en consola
print('El minimo encontrado por el sistema es:')
print('x: '+ str(x_sol))
print('y: '+ str(y_sol))

#------
#esta parte es para generar el grafico
print('Generando graficos...Espere un momento')
k = l
x =[]
y=[]
#para generar el vector sin numpy 
while k<u:
    x.append(k)
    y.append(f(k))
    k+=0.0001

#generar gráficos
#------ Graficos función y solución
pl.plot(x,y,label='función optimizada')
pl.plot(x_sol,y_sol,marker='x',label='solución encontrada')
pl.legend(loc='upper left')
pl.xlabel("Variable independiente (x)", size = 10)
pl.ylabel("Función objetivo f(x)", size = 10)
pl.grid()
pl.show()
#------Graficos fitness
a = pl.figure(1)
pl.title("Comportamiento Algoritmos Genéticos")
pl.plot(y_prom,label='Promedio de las soluciones')
pl.plot(y_min,label='Solución escogida')
pl.legend(loc='upper right')
pl.xlabel("Iteración", size = 10)
pl.ylabel("Aptitud", size = 10)
pl.grid()
pl.show()
