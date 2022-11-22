from tkinter import font
from sklearn.datasets import load_iris
from sklearn.manifold import TSNE
import matplotlib.pyplot as pl
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN,AgglomerativeClustering,MeanShift,SpectralClustering
from sklearn.decomposition import PCA
import matplotlib.pyplot as pl
import numpy as np
iris  = load_iris()
print("----------")
print("Identificando el dataset")
# print(iris.DESCR)
# print(iris.data.shape)
# print(iris.target.shape)
# print(iris.target_names)
# print(iris.feature_names)
print("#------------")
print("iniciando el trabajo")
pd.set_option("max_columns",5)
pd.set_option("display.width",None)
irisdf = pd.DataFrame(iris.data,columns = iris.feature_names)
irisdf["especie"]= [iris.target_names[i] for i in iris.target]
print(irisdf.head(10))
print("#--------")
print("Decripcion:")
pd.set_option("precision",2)
print(irisdf.describe())
print("Descripción por solo de cada especie:")
print(irisdf.especie.describe())
print("#------------")
sns.set(font_scale = 1.1)
sns.set_style("whitegrid")
cuadriculas =  sns.pairplot(data=irisdf,vars=irisdf.columns[0:4],hue="especie")
pl.show()
kmeans =KMeans(n_clusters=3,random_state=11)
kmeans.fit(iris.data)
print(kmeans.labels_[100:150])
print("#-----------------------")
print("Utilizando el modelo PDA")
pca = PCA(n_components=2,random_state=11)
pca.fit(iris.data)
iris_pca =  pca.transform(iris.data)
print("Cantidad de componentes relevantes pra el modelo")
print(iris_pca.shape)
print("#--------------")
iris_pcadf = pd.DataFrame(iris_pca,columns =["Componente1","Componente2"])
iris_pcadf["especie"] = irisdf["especie"]

iris_centros  =  pca.transform(kmeans.cluster_centers_)
axes = sns.scatterplot(data=iris_pcadf,x="Componente1",y="Componente2",hue="especie",legend="brief",palette="cool")
dots = pl.scatter(iris_centros[:,0],iris_centros[:,1],s=100,c="k")
pl.show()

estimadores = {"Kmeans":kmeans,"DBSCAN":DBSCAN(),"MeanShift":MeanShift(),"spectarlClostering":SpectralClustering(n_clusters=3),"AglomerativeClustering":AgglomerativeClustering(n_clusters=3)}
print("Comparando modelos")
for nombre,estimador in estimadores.items():
    estimador.fit(iris.data)
    print(f"\n{nombre}:")
    for i in range(0,101,50):
        etiquetas,cuentas = np.unique(estimador.labels_[i:i+50],return_counts = True)
        print(f"{i}-{i-50}:")
        for etiqueta,cuenta in zip(etiquetas,cuentas):
            print(f"etiqueta:{etiqueta},  c={cuenta}")