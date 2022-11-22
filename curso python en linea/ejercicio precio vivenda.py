import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot     as pl

df_train  = pd.read_csv("train.csv")
sns.distplot(df_train["SalePrice"]) # Grafica de distribución de datos en python 
pl.show()

df_train["SalePrice"].skew() #REtorna la asimetría de una distribución de precios 
"""La asimetria desplazada a la izquierda se considera una asimetria positiva, mientras las
asimetría desplazada a la derecha se considera una asimetría negativa """

df_train["SalePrice"].kurt() #entrega la curtosis de una gráfica
"""La curtosis es una medida estadística que determina el grado de concentración que presentan 
los valores de una variable alrededor de la zona central de la distribución de frecuencias. 
También es conocida como medida de apuntamiento."""

var = 'GrLivArea'
data = pd.concat([df_train["SalePrice"],df_train[var]],axis=1) #construye una tabla mas pequeña con la información a comparar

data.plot.scatter(x=var,y="SalePrice",ylim = (0,800000))
pl.show()

var = "TotalBsmtSF"
data = pd.concat([df_train["SalePrice"],df_train[var]],axis = 1)
data.plot.scatter(x = var,y = "SalePrice",ylim = (0,800000))
pl.show()

"""GRaficas de relaciones categoricas, a partir de este momento las comparacioens dependen 
de variables no numericas que cualifican los precios como por ejemplo qeu tan habitable es la casa 
en categorias de 1 a 10"""
var = "OverallQual"
data = pd.concat([df_train["SalePrice"],df_train[var]],axis=1)
f,ax = pl.subplots(figsize=(8,6))
fig = sns.boxplot(x=var,y="SalePrice",data=data)
fig.axis(ymin = 0,ymax = 800000)
pl.show()


"""Analsiis del precio de venta en relación al año de construcción de la casa """
var = "YearBuilt"
data = pd.concat([df_train["SalePrice"],df_train[var]],axis=1)
f,ax = pl.subplots(figsize=(20,8))
fig = sns.boxplot(x=var,y="SalePrice",data=data)
fig.axis(ymin = 0,ymax = 800000)
pl.xticks(rotation = 90) #Ordena los label del eje x rotados 90 grados para mejor visualización
pl.show()

"""A partir de ete punto se hace uso de las matrices de correlación. Estas matrices muetran todas las correlaciones entre las variables 
y como interactuan entre si."""

cormat = df_train.corr() # Entrega la tabla de correlacion a traves del metodo corr
f,ax = pl.subplots(figsize = (12,9))
sns.heatmap(cormat,vmax=.8,square = True)
pl.show()

"""La reducción de la variable de correlación alas k varaibles mas realcionadas al dato de importancia (precio de vente en este caso)
a través de pandas"""
k = 10 #cantidad de varaibles a analizar
cols = cormat.nlargest(k,"SalePrice")["SalePrice"].index
cm = np.corrcoef(df_train[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm,cbar = True,annot = True, square = True, fmt = ".2f",annot_kws = {"size":10},yticklabels=cols.values, xticklabels=cols.values)
pl.show()

"""Uso de grafico tipo scatter de correlación donde se muestran graficas entre los fatos mas relacionados entre si"""
sns.set() #cofiguracion por defecto si no se poen nada adentro
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt'] #Columanas de interes a graficar
sns.pairplot(df_train[cols],size = 2.5)
pl.show()