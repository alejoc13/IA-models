from keras.datasets import mnist
import tensorflow
import matplotlib.pyplot as pl
import seaborn as sns
import numpy as np

(x_train,y_train),(x_test,y_tesy) = mnist.load_data()
indices = np.random.choice(np.arange(len(x_train)),24,replace=False)
figure,axes= pl.subplots(nrows = 4,ncols = 6,figsize=(16,9))
for item in zip(axes.ravel(),x_train[indices],y_train[indices]):
    axes,image,target = item
    axes.imshow(image,cmap="gray_r")
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)
pl.show()
"""A partir de est epunto se va a hacer un mini ejercicio de limpieza de datos"""
xtrain = x_train.reshape(60000,28,28,1)
print(xtrain.shape)
xtest = x_test.reshape(10000,28,28,1)
print(xtest.shape)
"Normalizacion de los datos"
xtrain = xtrain.astype("float32")/255
xtest = xtest.astype("float32")/255
"one hot encoding"
