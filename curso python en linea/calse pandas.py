import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler

df_train = pd.read_csv('train.csv')
print(df_train.head(20))  #El comando head permite extraer una parte de la tabla 
print(df_train.shape) #Da el tamaño total del dataframe
print(df_train["Id"]) #De esta manera se obtiene una colujmna especifica (DEbe conocerse su nombre)
print(df_train[['Id','SalePrice']]) # De esta manera se obtienen multiples columnas al tiempo 
print(df_train['SalePrice'].mean()) #Operadores estadisticos por ejemplo media
print(df_train.describe()) #Descripcion estadistica de todo el dataframe