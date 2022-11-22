import numpy as np
import pandas as pd

reg_peso = {'Vanesa':[68,67,66,65],'Kevin':[89,89,90,88],'Fernanda':[59,60,60,62],'Patricia':[70,68,67,65]}

peso = pd.DataFrame(reg_peso) #Convierte un diccionario en un dataframe
print(peso)
#personalización de los indices del dataframe
peso.index = ['Mes 1','Mes 2','Mes 3','Mes 4']
print(peso)
print(peso['Fernanda'])
print(peso.Patricia)
"""El trabajo de seleccionar filas"""

print('#--------')
print(peso.loc['Mes 1']) #Para acceder utilizando los nombres
print('#----------') 
print([peso.iloc[1]])
"""Para seleccionar multiples filas y toda su información """
print('#--------')
print(peso.loc['Mes 1':'Mes 3'])
"para una busqueda de grupos especificos de meses"
print('#------')
print(peso.loc[['Mes 1','Mes 3']])
"""Para los meses especificos de personas especificas"""
print('#------')
print(peso.loc['Mes 2':'Mes 3',['Vanesa','Patricia']]) #busqueda de personas especificas y meses especificos(filas especificas y columans especificas)
print('#------')
"""Se pueden realziar filtros de la información """
print(peso[peso>=70])
print(peso[(peso>=65) & (peso<80)])
print('#------')
"para acceder a celdas especificas del dataframe"
print(peso.at['Mes 3','Patricia'])
"""Para modificar los valores de una celda en epecifico"""
peso.at['Mes 4','Kevin'] = 85
print(peso)
print('#------')
print(peso.describe())#estadisticas
"la precision de la etaditica descriptiva puede se rmodificada"
pd.set_option('precision',1)
print(peso.describe())
print('#------')
print(peso.T) #transponer los dataframe
print('#------')
print(peso.T.describe()) #Estadisticas de la matriz transpuestas 

"""tAMBEIN ES POSIBLE AHCE ORDENAMIENTOS DE LOS DATAFRAMES"""
print(peso.sort_index(ascending = False))#para hacer el ordenamiento sobre lso indices
print(peso.sort_index(axis =1))#reordena desde las columnas
print('#------')
"""Y también se vale ordenar los valores según una fila o columna especifica. El siguiente código ordena de forma 
descendente los datos del DataFrame con respecto a los valores del Mes 1."""
print(peso.loc['Mes 1'].sort_values(ascending = False))#para ordenar la tabla en funcion de lso datos especificados 
