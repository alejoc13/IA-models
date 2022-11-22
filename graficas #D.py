from cmath import cos
from pylab import arange,cos,sqrt,meshgrid,figure,cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = plt.axes(projection='3d')
X =  arange(-4,4,0.25)
Y =  arange(-4,4,0.25)
X,Y = meshgrid(X,Y)
R = sqrt(X**2+Y**2)
Z = cos(R)
ax.plot_surface(X,Y,Z,cmap=cm.cool)

plt.show()

