import pandas as pd 
"""A diferencia de numpy no se apega al indice inicializado 0 y es personalizable, tambien permite utilizar arreglos no
homogeneas permitiendo datos vacios, texto y tiempo"""
"""pandas ofrece los metodos de cserie spar aarreglos unidimencionales que no pueden ser manipulados por numpy por no 
ser homogeneos, la salida de una serie tiene un indice y los datos que se le agreguen, ademas recordemos que esos indices 
son suceptibles de ser personalizados en caso de ser neesario o desearse hacelro"""
tiempo_web = pd.Series([160,256,98,108])
print(tiempo_web)
ejemplo=pd.Series(3.1416,range(5)) #crea una serie de 5 elementos dodne todos son 3.1416
print(ejemplo)
"""Para acceder a los ele,emts de una serie se realzia el mismo procedimietno qeu apra un arreglo numpy o una lista"""
print(tiempo_web[2])
"""Esta liberria cuenta con un el mismo compendio de estadisticas descriptivas que numpy ya que esta construida sobre numpy"""
print(tiempo_web.mean())
print(tiempo_web.describe())
print('#-------')
"""La personalización de lso indices se realiza:"""
tiempo_web = pd.Series([160,256,98,108], index = ['Laura','Daniel','Alberto','Eva'])
print(tiempo_web)
#ahora se accede a la informacion como utilizando diccionarios, es decir el indice es basicamente una clave pero no se pierde la posibilidad  ingresar con los indices nuemricos a pesar de la modificación
print(tiempo_web['Laura'])
print(tiempo_web.Laura)
