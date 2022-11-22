import sklearn
from sklearn.datasets import load_digits
import matplotlib.pyplot as pl
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
import seaborn as sns
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
digits = load_digits() #PAquete de los numeros para evaluar los numeros
print(digits.DESCR) # da una descriocuon del dataset
print(digits.target[::100]) #muestra un lagbel de que es cada imagen o por lo meno suna arte de ellos 
print(digits.data.shape)
print(digits.target.shape)
print("#-------")
figure,axes = pl.subplots(nrows=4,ncols=6,figsize=(6,4))
for item in zip(axes.ravel(),digits.images,digits.target):
    axes,image,target =item
    axes.imshow(image,cmap=pl.cm.gray_r)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)
pl.tight_layout()
pl.show()

"""Se debe respetar el orden de la siguiente liena"""
x_train,x_test,y_train,y_test = train_test_split(digits.data,digits.target,random_state=11)
print("Tamaño de la poblacion de entrenamiento")
print(x_train.shape)
print("Tamaño de la poblacion de testeo")
print(y_train.shape)

"""Modelo de clasificador kn"""
knn = KNeighborsClassifier() #objeto del clasificador
knn.fit(X = x_train,y = y_train)

predict = knn.predict(X=x_test)
esperado = y_test
equivocados = [item for item in zip(predict,esperado) if item[0]!=item[1]]
print("Lista de las predicciones equivocadas")
print(equivocados)
print("#-------")
print("Valoraciones del modelo")
print(f"{knn.score(x_test,y_test):.2%}")
print("#---------")
"""EL uso de la matriz de confucion"""
conf = confusion_matrix(y_true=esperado,y_pred=predict)
print(conf)
"""EL reporte de clasificacion muestra el pocettaje de cada prediccion"""
nombres = [str(digits) for digits in digits.target_names]
print(classification_report(esperado,predict,target_names=nombres))
df_conf = pd.DataFrame(conf,index=range(10),columns=range(10))
axes = sns.heatmap(df_conf,annot = True,cmap="nipy_spectral_r")#matriz de confucion en forma de mapa de calor
pl.show()

kfold = KFold(n_splits=10,shuffle=True) #Permite aumentar la cantida de datos de forma relativa
puntuacion =  cross_val_score(estimator = knn,X = digits.data,y=digits.target,cv=kfold)

"""Pribando distintos modelos para un mismo dataset, esto es importatnte ya que no en todos loscasos se sabe que modelov a a catuar
de una mejor maenra sobre el probelama, pro tanto realizar todos estos modelos ayuda a solventar la decison al probarlos"""
estimadores =  {"knn":knn,"SVC":SVC(gamma="scale"),"GaussianNB":GaussianNB()}
for nombre,objeto in estimadores.items():
    kfold = KFold(n_splits=10,random_state=11,shuffle=True)
    puntuacion = cross_val_score(estimator=objeto,X=digits.data,y=digits.target,cv=kfold)
    print(f"nombre estimador:{nombre},puntuacion primedio:{puntuacion.mean():.2%}+std:{puntuacion.std():.2%}")
print("#------------------------")
for k in range(1,20,1):
    kfold = KFold(n_splits=10,random_state=11,shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=k) #modifica la cantida de potenciales vecionas para hacer estimaciones.
    puntuacion = cross_val_score(estimator = knn,X=digits.data,y=digits.target)
    print(f"k:{k},puntuacion primedio:{puntuacion.mean():.2%}+std:{puntuacion.std():.2%}")
