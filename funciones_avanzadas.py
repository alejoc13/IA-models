import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.pyplot import plot,figure,show,title
X = np.arange(-2,2,0.1)
Y = np.arange(-2,2,0.1)
x,y = np.meshgrid(X,Y)
#z = -(y+47)*np.sin(np.sqrt(abs(y+(x/2)+47)))- x*np.sin(np.sqrt(np.abs(x-(y+47))))
z = -1/(1+np.abs(x+(0+1j)*y+1))
ax = plt.axes(projection='3d')
ax.plot_surface(x,y,z)
plt.show()
print(np.min(z))





        


