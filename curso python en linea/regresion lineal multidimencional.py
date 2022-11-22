from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

california = fetch_california_housing()
# print(california.DESCR)
print(california.data.shape)
print(california.target.shape)
print(california.feature_names)
pd.set_option("precision",4)
pd.set_option("max_column",9)
pd.set_option("display.width",None)
california_df = pd.DataFrame(california.data,columns=california.feature_names)
california_df["value"] = pd.Series(california.target)#pegar lso preciso de las casas a el dataframe creado con pandas
print(california_df.head(5))
print("#------------------")
muestradd = california_df.sample(frac=0.1,random_state=1)#genera un muestre de la poblacion inicial

sns.set(font_scale = 2)
sns.set_style("whitegrid")
for feature in california.feature_names:
    pl.figure(figsize=(16,9))
    sns.scatterplot(data = muestradd,x=feature,y="value",hue = "value",legend=False)
# pl.show()

print("arreglo para el modelo de machine learning")

x_train,x_test,y_train,y_test = train_test_split(california.data,california.target,random_state=11)
reglin = LinearRegression()
reglin.fit(x_train,y_train)
for i,name in enumerate(california.feature_names):
    print(f'{name:>10}:{reglin.coef_[i]}')
print(f"valor standar de una casa:{reglin.intercept_}")

prediccion =  reglin.predict(x_test)
esperados = y_test

df = pd.DataFrame()
df['esperados'] = pd.Series(esperados)
df['prediccion'] = pd.Series(prediccion)

figure = pl.figure(figsize=(9,9))
sns.scatterplot(data = df,x='esperados',y='prediccion',hue="prediccion",palette="cool",legend=False)
pl.show()
print("meticas:")
print("r2: ",metrics.r2_score(esperados,prediccion))
print("error medio:",metrics.mean_squared_error(esperados,prediccion))