from random import random
import numpy as np 

"""La libreria numpy es la base de mjuchas otras librerias como scipy, esta especializada en arreglos y es neesario hacer la
instalación de la misma ya que no viene dentro de los paquetes princiaples de python. Esta librería crea objetos de distintos
tipos que se manejan de formas distintas com veremos a lo largo de este script"""

a = np.array([1,2,3,4,5,6]) #asi se crea un arreglo numerico en numpy
b = np.array([[1,2],[3,4],[5,6],[7,8]]) #arreglos multidimencionales 
print(f'El arreglo unidimensional:\n{a}')
print('#---------')
print(f'El arreglo multidimencional: {b}')
"""La construccion de arreglso de tipo numpy tambien soportan el manejo de comprension de listas"""

impares = np.array([i for i in range(1,31) if i%2!=0])
print('#--------')
print(f'El arreglo constuido a partir de comprension de listas:\n{impares}')

"""Los arreglos tipo numpy tienen algunos atribustos muy utiles que permiten determinar caracteristicas de los areglos que
se estan utilizando a lo largo de la ejecucion de los programas:"""
print('#-----------')
enteros = np.array([[9,10,11,12],[8,7,6,5]])
flotantes=np.array([[9**(1/2),10**(1/2),3.33,],[10/3,3.4,3.03]])
#El metodo dtype ofrece inforamcion del tipo de elementos contenido en el arreglo
print(enteros.dtype)
print(flotantes.dtype)
print('#-----------')
print(f'el arreglo es de {enteros.ndim} dimensiones')#ofrece el las dimenciones por las que esta compuesto el arreglo
print('#-----------')
print(f'el arreglo en sus dimensiones tiene los tamaños: {enteros.shape}')
print('#-----------')
"""El metodo .size devuelve la cantidad total de elementos que posee el arreglo mientras el .itemsize regresa cuantos 
separados por coma tiene el arrelgo ( size es la suma los elementos de cada fila en arreglos multidimensionales"""
print(f'El arreglo posee un total de {enteros.size} elementos')
print(f'El arreglo posee un total de {enteros.itemsize} elementos')
print('#-------------')
for fila in flotantes: # es posible iterar vectores numpy
    for columna in fila:
        print(columna,end=', ')

print('#-------')
"""se utiliza el arreglo impares construido con comprension de listas determinar la forma del arreglo y la cantidad de
dimensiones del mismo """
print(impares.ndim)
print(impares.shape)
print('#-----------')
"""la funcion arange nos permite trabajar con arreglos de la misma forma que range lo hace con las listas"""
print(np.arange(8)) # fucniona igual a 'range')
print(np.arange(12,2,-3)) #dando saltos y tambien aplica los indices negatios 
print(np.linspace(0.0,1.0,5)) #linspace(inicio,final,cantidadElementos)
print(np.arange(21,1,-1).reshape(4,5)) #permite darle un formato tipo matriz al arreglo .reshape
"""debe tenerse en cuenta que al usar reshape la cantidad de elementos concuerde con el numero de elementos a utilizar 
o el arreglo no funcionara"""
print(np.arange(0,10000).reshape(5,2000)) #no se mostrará toda la informacion por su tamaño
print('#---------')
"""Los arregle pueden operarse entre si, de diversas maneras como si fueran variables sencillas """

lista1 = np.arange(2,18,3)
lista2 = np.linspace(-2,20,6)

print(lista2-lista1)
print(lista2/lista1)
print(lista2 == lista1) #las comparaciones se hacen elemento a elemento

"""Los arreglos en numpy estan hecho apra ser validos a aplicar operadores de asignación"""
print(lista2)
lista2**=2
print(lista2)
print('#-----------')
"""Numpy presenta su propio catalogo de calculso estadisticos de forma que si se tiene numpy no es del todo necesario importar
otras librerias  (salvo que sea mas eficiente ya lo descubriré luego)"""
ventas=np.array( [[554,606,710,851],[1244,898,416,1763],[841,655,1105,1067]])
print(ventas.mean())
print(ventas.std())
print(ventas.max())
print(ventas.min())
print(ventas.var())
"""El agregado de numpy a este tipo de calculso es que tambien pemite el realizar el procedimiento de analisis estadistico
por filas y pro columnas"""
print('#---------')
print(ventas.mean(axis=0)) #Promedio de cada una de las columnas
print(ventas.mean(axis =1)) #Promedio de cada una de las filas
print('#-------------')
"""La indexación en numpy se realiza como se ve a continuación"""
ventas=np.array ([[ 554, 606, 710, 851],
 [1244, 898, 416, 1763],
 [ 841, 655, 1105, 1067]])
print(ventas[0,1])
print('#--------')
print(ventas[:,0]) #Columnas completas 
print(ventas[0,:])#filas completas
print(ventas[:,[0,2]]) #traer multiples columas o filas y el inverso completo
print('#--------')
"""EL metodo reshape crea una copia pero no modifica el arreglo original, caso contrario al metodo resize que si cambia 
permanentemente el arreglo sobre el que se aplica"""
ventas = np.array([[ 500, 600, 550, 800], [1200, 800, 400,1000]])
print(ventas)
ventas.resize(1,8)
print(ventas)
ventas = np.array([[ 500, 600, 550, 800], [1200, 800, 400,1000]])
print(ventas.T) #este metodo transpone las matrices

