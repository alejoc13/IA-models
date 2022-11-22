import random as rd
from matplotlib import pyplot as pl
def crear_individuos(tv):
    return [rd.randrange(1,10) for i in range(tv)]
    
def analizar_sudoku(sudoku):
    error = 0
    #para analizar filas
    for fila in sudoku:
        for i in range(1,10):
            cuenta = fila.count(i)
            if cuenta == 0:
                error+=1
            if cuenta >1:
                error+=cuenta
    #para el analisis de columnas
    for j in range(9):
        columna = [sudoku[i][j] for i in range(9)]
        for valor in range(1,10):
            cuenta =  columna.count(valor)
            if cuenta==0:
                error+=1
            if cuenta>1:
                error+= cuenta
    return error

def generar_tablero(tc,individuo,inicial):
    vc = [i for i in inicial]
    tablero = []
    control = 0
    for i in range(len(vc)):
        if vc[i] == 0:
            vc[i] = individuo[control]
            control+=1
    for i in range(0,len(vc),tc):
        tablero.append(vc[i:i+tc])
        
    return vc,tablero

def clonacion(pob,fit,n,Pc,Np):
    clones = []
    copy_fit = [j for j in fit] #copia de los errores
    copy_fit.sort()
    for i in range(n):
        val = copy_fit[i]
        ind = fit.index(val)
        for j in range(round(Pc*Np)):
            clones.append(pob[ind])
    return clones
    









#inicialización de los valores del sudoku
tc = 9 #tamaño del sudocu
sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
"""
sudoku = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
"""
#----Obtener los valores dados y sus indices para cuidar que nunca se pierdan
inicial = []
indices =   []
for i in sudoku:
    inicial += i
indices = [i for i in range(tc*tc) if inicial[i]!=0]
tv = inicial.count(0) #tamaño del vector para soluciones 
#----Fin de la inicialización del sudoku

#----Inicialización de los parametros de AIS

Np = 400             # Tamaño de la poblacion 
n = 300               # Número de individuos a clonar 
dim = 2              # Dimensión del problema
Nb = 30              # Número de bits por dimención 
maxk = 1000            # Cantidad máxima de iteraciones
Pm = 0.09            # Probabilidad de mutación
Pd = 0.06            # Porcentaje de diversidad
Pc = 0.09            # Porcentaje de clonación 
k = 0                # iteración actual
nc = round(Np*Pc*n)  # Numero total de clones en cada iteración 
nci = int(Np*Pc)     #Cantidad de cloens de cada  individuo
Pr = int(Np-Pd*Np-n) # Cantidad de población remanente/los mejores de cada generación
npd = int(Pd*Np)     #Cantidad de población por diversidad
#----vectores de almacenamiento
fit = []
fitm = []
sol =[]
resulesto = []


#----Crear la población inicial 
pob = [crear_individuos(tv) for i in range(Np)]
#----evaluar la población inicial
for i in range(Np):
    vc,tablero = generar_tablero(tc,pob[i],inicial)
    fit.append(analizar_sudoku(tablero))

#---A partir de este momento entra en el ciclo iterativo
while k<maxk:
    Clones = clonacion(pob,fit,n,Pc,Np)
    #----Hipermutacion
    Cm = []
    for i in Clones:
        aux = []
        for j in range(tv):
            r = rd.random()
            if r<=Pm:
                aux.append(rd.randrange(1,10))
            else:
                aux.append(i[j])
        Cm.append(aux)

    #----Evaluar los clones.
    for i in range(nc):
        vc,tablero = generar_tablero(tc,Cm[i],inicial)
        fitm.append(analizar_sudoku(tablero))
    #----Proceso de reseleccion   
    Cmr = []
    pob1 = []
    
    cPr = 0 #contador de población remanente
    for i in range(0,nc,nci):
        cambio = min(fitm[i:i+nci])
        ind_cambio = fitm.index(cambio)
        aux = Cm[ind_cambio]
        Cmr.append(aux)
        if cPr<Pr:
            pob1.append(Clones[i])
            cPr+=1
    pob2 = []
    pob2 = pob1+Cmr
    for i in range(npd):
        pob2.append(crear_individuos(tv))
    pob = pob2
    for i in range(Np):
        vc,tablero = generar_tablero(tc,pob[i],inicial)
        fit[i]=analizar_sudoku(tablero)
    pob = pob[0:Np]
    aux1 = min(fit)
    sol.append(aux1)
    k+=1





pl.title("Comportamiento Sistemas Inmjunes artificiales")
pl.plot(sol,label='soluciones')
pl.show()

        
