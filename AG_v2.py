import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def funcion_prueba(x):
    res = np.sqrt(x[0]**2 + x[1]**2)
    return res

#Genera los valores qeu barren todo el dominio 
random.seed(0)
x = np.linspace(-100, 100, 1000)
y = np.linspace(-100, 100, 1000)

#Evalua todos los valores de las varaibles
x_ax, y_ax = np.meshgrid(x,y)
vals = np.c_[x_ax.ravel(),y_ax.ravel()]
fx = np.reshape([funcion_prueba(val) for val in vals],(1000,1000))
ax = plt.axes(projection='3d')
#fig = plt.figure()
ax.plot_surface(x_ax,y_ax,fx,cmap=cm.coolwarm)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
plt.show()

