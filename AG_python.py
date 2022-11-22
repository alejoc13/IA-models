import numpy as np
from matplotlib import pyplot as pl

#------ Función a optimizar 
def f(x):
    y = -x*np.sin(abs(x))
    return y

#------Función conversor bionario a decimal
def conversor_decimal(u,l,B,Nb):
    num = 0
    den = 0
    for i in range(Nb):
        aux = (2^i)*B[i]
        num = num+aux
        aux = aux = 2^i
        den = den+aux
    dec = l+(num/den)*(u-l)
    return dec

#------Selección por ruleta
def seleccion(q):
    sel = -1
    r = np.random.rand()
    for i in range(len(q)):
        if q[i] > r:
            sel = i
            break
    return sel
#------selección peores padres
def sel_peores(q):
    sel = -1
    r = np.random.rand()
    for i in range(len(q)):
        if q[i] < r:
            sel = i
            break
    return(sel)

        
        

#------Inicializción del sistema de AG

Nb = 10     #número de bits.
u  =10      #límite superior.
l = -5      #límite inferior.
tp = 5      #tamaño de la población.
mut = 0.7   #probabilidad de mutación.
c = 1       #probabilidad de cuce.
k = 0       #contador de iteraxiones.
Niter = 1000 #cantidad de iteraciones del sistema.
pob = np.random.randint(2,size=(5,10))  #creación de la población inicial binaria de forma aleatoria.
x_pob = np.zeros(5)   #vector para guardar los valores decimales de la población.
y_pob = np.zeros(5)   #vector para guardar la fitness de cada uno de lso individuos de la población.


while k<Niter:
    for i in range(tp): #conversión a decimal y obtención de la fitness.
        b = pob[i][:]
        dec = conversor_decimal(u,l,b,Nb)
        x_pob[i]= dec
        y_pob[i] = f(dec)
   
    #------Selección de los padres y de lso individuos a reemplazar
    E = np.sum(np.dot(y_pob,-1))
    p = np.dot(y_pob,-1)/E
    q = np.zeros(tp)
    q[0]=p[0]
    for c in range(1,len(p)):
        q[c] = np.sum(p[0:c+1])
    p1 = seleccion(q)
    p2 = seleccion(q)
    re1 = sel_peores(q) #primer individuo a reemplazar (indice)
    re2 = sel_peores(q) # segundo individuo a reemplazar(indice)

    padre1 = pob[p1][:]
    padre2 = pob[p2][:]
    #------Cruce entre los padres seleccionados
    pc = np.random.randint(Nb)
    if pc == 0:
        pc+=1
    if pc == Nb:
        pc-=2

    hijo1=[]
    hijo2 =[]
    hijo1 = np.concatenate([padre1[0:pc], padre2[pc::]])
    hijo2 = np.concatenate([padre2[0:pc], padre1[pc::]])
    h = np.zeros([2,Nb])
    h[0] = hijo1
    h[1] = hijo2
    #------Mutación de los hijos
    for i in range(Nb):
        r = np.random.rand()
        if mut>r:
            hijo1[i] = np.random.randint(2)
        r = np.random.rand()
        if mut > r:
            hijo2[i] = np.random.randint(2)
    #------Evaluacion de los hijos obtenidos
    h[0] = hijo1
    h[1] = hijo2
    hx =np.zeros(2)
    hy = np.zeros(2)
    aux = 0
    for b in h:
        hx[aux] = conversor_decimal(u,l,b,Nb)
        hy[aux] = f(hx[aux])
        aux += 1

    y_pob[re1] = hy[0]
    x_pob[re1] = hx[0]
    y_pob[re2] = hy[1]
    x_pob[re2] = hx[1] 

    k+=1



    
    


        
        

