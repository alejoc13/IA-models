"""Seaborn es una libreria construida a partir de matplotlib, la idea de usar seaborn es reducir la cantidad de comandos 
que se necesitan para construir una gráfica.

En el primer ejemplo se constgruirá una grafica de barras en la cual se tienen los datos de la simualción del lanzamiento de miles 
de dados"""
import matplotlib.pyplot as pl
import seaborn as sns
import numpy as np 
import random 

tirosdados = [random.randrange(1,7) for i in range(60000)]
valores, frecuencias = np.unique(tirosdados,return_counts = True) #la función unique devuelve los valores obtenidos y activar el counts hace qeu retornes una nueva variable que cuenta cada valor unico
for i in range(len(valores)): #muestra del correcto funcionamiento de np.unique()
    print(f"valor: {valores[i]}, frecuencias:{frecuencias[i]}")
print("#------")
"""Preparar una gráfica con sns tiene varias ventajas, veamos:"""
titulo = f"Resultados de tirar los dados {len(tirosdados)} veces" #definir un titulo de eta maenra permite que sea dinamico, cambia si los valores cambian 
sns.set_style("whitegrid") #este comando permite definir como será el fondo de la grafica
axes = sns.barplot(x=valores,y=frecuencias,palette = "bright")#define un grafico d ebarros y su paleta de colores
axes.set_title(titulo) # Genera el titulo de la grafica
axes.set_xlabel("valores") # Genera titulo del eje x
axes.set_ylabel("frecuencia") #genera titulo del eje y
axes = sns.barplot(x=valores,y=frecuencias,palette = "bright")
axes.set_ylim(top = max(frecuencias)*1.10) #genera un espacio en la parte superior de la grafica, alejando las barras del techo para mejora estetica
for bar,frecuencias in zip(axes.patches,frecuencias):
    text_x = bar.get_x()+bar.get_width()/2.0
    text_y = bar.get_height()
    text = f"{frecuencias:,}\n{frecuencias/len(tirosdados):.3%}"
    axes.text(text_x,text_y,text,fontsize = 11, ha = "center",va="bottom")
pl.show()
