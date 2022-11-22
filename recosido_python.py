import numpy as np
from matplotlib import pyplot as pl
#Función para generalizar que se va a optimizar 

def f(x):
    y = -x*np.sin(abs(x))
    return y

#--------------------------------------------

#Implmentación de recocido similado
print('Implementando Modelo de recocido simulado espere un momento')
k = 0 # contador del ciclo while
Niter = 3000 #numero de iteraciones
u = 30.0 #limite superior
l = -5.0 #limiter inferior
Ti = 8.0; #Temperatura inicial
Tfin = 0.00001 #temperatura final
x =  np.random.randint(u) #primer numero aleatorio para el analisis del sistema RS
E_old = f(x)    #energia del punto seleccionado
beta = (Ti-Tfin)/Niter #Factor de enfriamiento
fitness = []

print('Minimizando la función espere un momento')
while k<Niter:
    T = Ti - k*beta; # cambio en la temperatura
    
    #procedimiento para generar un punto nuevo
    valido = 0 # variable de control
    while valido == 0: #ciclo para garantizar qeu el punto nuevo esté dentro del rango adecuado 
        xn = x + np.random.choice([-1,1])*T*1.4 #random.choice es para garantizar que pueda analizarce tanto en la derecha como en la izquierda del punto x
        if xn>= l and xn<=u:
            valido = 1
        E_new = f(xn)  #energia del punto nuevo
    if E_new < E_old: #cambio inmediato si se representa una mejora
        x = xn
        E_old = f(xn)
    else:           #Cambio por probabilidad
        delta_f = E_old-E_new
        r = np.random.rand()
        pa = np.exp(delta_f/T) #probabilidad de aceptación
        if pa>r:
            x = xn  
            E_old = f(xn)    
    fitness.append(E_old)
    k=k+1    
#------
#información en consola
print('El minimo encontrado por el sistema es:')
print('x: '+ str(x))
print('y: '+ str(E_old))

#------
#esta parte es para generar el grafico
print('Generando graficos...Espere un momento')
x1 = np.linspace(l,u,10000)
y = f(x1)
a = pl.figure(1)
pl.plot(x1,y,label='función optimizada')
pl.plot(x,E_old,marker='*',label='solución encontrada')
pl.legend(loc='upper left')
pl.grid()
pl.show()
a = pl.figure(2)
pl.plot(fitness)
pl.grid()
pl.show()
