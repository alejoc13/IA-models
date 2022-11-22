import pandas as pd 
import numpy as np 
res_df = pd.read_excel("Datos Restaurante.xlsx")
precios_df = pd.read_csv("Precios Restaurant.csv")
"""En el mayor de los casos se debe limpiar los datos, por ejeplo en el caso particular del archivo utilizado los valores monetarios 
constan del signo de pesos, entonces a pesar de que excel directamente los reconose como valores numericos operables, pandas 
no permite esto, por lo tanto el paso siguiente es limpiar los datos para poder utilizarlos(punto para excel)"""
"""1. Identificar el simbolo que está dando probelmas en este caso $
   2. Eliminarlo de los datos
   3. TRansformar str a float"""
print("Formato tabla orginal:")
print(precios_df.head(5))
precios_df["Precio"] = precios_df["Precio"].str.replace("$","").astype(float)
precios_df["Costo"] = precios_df["Costo"].str.replace("$","").astype(float)
print("Formato tabla modificada:")
print(precios_df.head(5))
"""A partir de este momento ya es posible realizar operaciones entre lascolumnas de interes, por ejemplo obtener una nueva 
columna que de las gananacias obtenidas por las ventas, Como no existe una columna con este nombre pyton la crea como la ultima
columna al lado izquierdo del dataframe"""
precios_df["Ganancias"] = precios_df["Precio"]-precios_df["Costo"]
print("Dataframe con la columna agregada:")
print(precios_df.head(5))

"""El metodo drop de pandas me permite eliminar una columna de información de forma permantente, especificando su nombre y el eje 
en el que se desea borrar"""
print("#--------")
print("TAbla del restarurnte original:")
print(res_df.head(5))

res_df = res_df.drop("Hora de Cobro",axis = 1) #se elimina la columna hora de cobro

print("#--------")
print("Tabla del restarurnte Modificada:")
print(res_df.head(5))

"""Es posibel filtrar informaciom y crear dataframes nuevos con las caracteristicas que deseemos, por ejemplo el dataframe
precioscarosdf contendra todos los platos que tengan un costo superior a 100"""
print("#----------")
print("Nuevo dataframe filtrando costos:")
precioscarosdf = precios_df[precios_df["Precio"]>100]
print(precioscarosdf.head(20))
"""El siguiente filtro permite crear una nueva columna llamada margen, la cual será alto o bajo segun si la ganancia es 
mayor o menor a 100, pero todo se almacenara como string en una nueva columna de nombre margen."""
precios_df["Margen"] = np.where(precios_df["Ganancias"]>100,"Alto","Bajo") #este pedazo s ehace con numpy
print("#----------")
print("TAbla con la columna Margen")
print(precios_df.head(5))
"""TAmbien es posible cambiar el nombre de las columnas usando comandos propios de pandas, donde pra cambar un no,bre de columna
se procede de la siguiente manera """
print("#--------")
print("La siguiente tabal cambia el nombre Atendió\npor el nombre Mesero:")
res_df = res_df.rename(columns = {"Atendió":"Mesero"})
print(res_df.head(5))
"""Es posible generar nuevos dataframe a partir de juntar dos que tienen elementos en comun, por ejemplo  las tabals de restaurante
y precios restaurante contienen ambos los nombres de lso productos, por tanto es posible juntarlas de manera que se compartan los 
elementos de ambas tablas de manera ordenada sin tener qeu realizarlo a mano"""
restpreciodf = res_df.merge(precios_df, on=["Producto"], how="left")

"""Este metodo debe respetar la nomenvalactura de la linea anterior donde
se debe guardar el nuevo dataframe en una nueva varaible, la primera tabla se escribe sunombre.merge
el priemr argumento es la segunda tabala a trabajar, el valor on = [""] solicita cual será la columna de referencia 
para generar la nueva tabala  y el parametro how = pide la forma en qeu se realizara el agregado de las tablas(por el momento 
solo conozco left) """""
print("#-------")
print("Nueva tabla concatenando a partir de coincdencias las anteriores:\n")
print(restpreciodf.head(5))

"""Existe un metodo para crear una lista de elementos unicos, que tambien cumple como funcion el eliminar los elementos duplicados
esta funcion es bastante sencilal pero requeire de guardar en un alista independietne en cas de no qeurere afectar la integridad
de la tabal sobre la que se esta trabajando"""

meseros = res_df["Mesero"]
meseros = meseros.drop_duplicates()
print("#---------")
print("Se muesta una lsita de toso slso jombres de los meserso:")
print(meseros)

"""PAra generar una tabla tpivot desde pandas se respeta la estructura de a comtinuacion, aggfun se toma de numpy y s eusa 
para definir el tipo de operacion qeu se realziara sobre values, el index sse toma de cateforias"""
ventporcat = pd.pivot_table(restpreciodf,values="Precio",index = "Categoria",aggfunc = np.sum)
print("Tabla pivote 1")
print(ventporcat)
"""ESta seugnda version permite ahcer comparaciones, entre las categorias y una columna seleccionada, index son las filas"""
ventxcatxtipo = pd.pivot_table(restpreciodf,values = "Precio", index = "Categoria", columns = "Tipo_x",aggfunc = np.sum)
print("Tabla pivote 2")
print(ventxcatxtipo)
"""tabla pivote con distintas jerarquias"""

tipoxmesero = pd.pivot_table(restpreciodf,values= "Precio", index = ["Tipo_x","Categoria"],columns = "Mesero",aggfunc = np.sum)
print("Tabalcon jerarquias al mostrar")
print(tipoxmesero)