from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
import matplotlib.pyplot as pl
tsne = TSNE(n_components=2,random_state=11)
digits = load_digits()
datos_reducidos =  tsne.fit_transform(digits.data)
dots = pl.scatter(datos_reducidos[:,0],datos_reducidos[:,1],c="black")
dots2 = pl.scatter(datos_reducidos[:,0],datos_reducidos[:,1],c=digits.target, cmap=pl.get_cmap("nipy_spectral_r",10))
colorbar = pl.colorbar(dots2)
pl.show()       