from itertools import count
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as pl

enoe=pd.read_excel("mu_enoe.xlsx")

tabla1 = pd.pivot_table(enoe,values="ingreso_mensual",index="edad",columns="niv_edu",aggfunc=np.sum)

sexos,conteo = np.unique(enoe["sex"],return_counts=True)
print(tabla1)
sns.set_style("whitegrid")
sns.barplot(x=sexos,y=conteo)
pl.show()
cormat = enoe.corr()
print(cormat)
hm = sns.heatmap(cormat,cbar=True,square=True,annot=True)
pl.show()
sns.scatterplot(x=enoe["anios_esc"],y=enoe["ingreso_mensual"],data=enoe)
pl.show()
print("#----------------")
sns.displot(enoe["anios_esc"])
pl.show()
print(type(tabla1))