#serie de fibonacci
import numpy as np
def fibonacci(n):
    fi = [1,1]
    for i in range(n):
        numero = fi[-1] + fi[-2]
        fi.append(numero)
    return fi
n = 20
fi  = fibonacci(n)
print('Los primetos ',n,'numeros de la serie de fibonacci son:')
print(fi)
##----------ejercicio dos para los medicos
def norma(z): #----Función para calcular la norma de un vector 
    cuadrados  = []
    for i in range(len(z)):
        numero  =  z[i]**2
        cuadrados.append(numero)
    norma = sum(cuadrados)
    norma  = np.sqrt(norma)
    return  norma
def  producto_punto(x,y):   #----Función para calcular el producto punto
    p_punto = 0
    for i in range(len(x)):
        mult = x[i]*y[i]
        p_punto+=mult
    return p_punto
#definir los vectores a trabajar
x = [3,4,5]
y = [-2,-1,6]
#----Calcular las normas
normax = norma(x)
normay = norma(y)
p_punto = producto_punto(x,y)
#----Calcular el coseno del angulo y el angulo como tal
coseno_teta = p_punto/(normax*normay)
angle  = np.arccos(coseno_teta)
print('El angulo obtenido entre los dos vectores proporcionados es de: ',angle)
if angle <90:
    print('El angulo es agudo')
elif angle ==90:
    print('El angulo es recto')
else:
    print('El angulo es obtuso')



    
    
