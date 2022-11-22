import statistics as sta
calificaciones= [68, 90, 80, 100, 80, 75, 85, 95, 70, 70]

"""Las medidas de tendencia central son aquellas que describen un grupo de datos a travé de un unico valor.
Estas medidas describen los puntos de conglomeracion de un grupo de datos y son las siguientes:"""
print(sta.mean(calificaciones)) #media 
print(sta.median(calificaciones)) #mediana
print(sta.mode(calificaciones)) #moda
"""Las medidas de disperción hacen referencia a como estan variando los datos y los rangos en qeu estos se encuentran, dentro de
estas medidas encontramos:"""

sta.stdev(calificaciones) #deviacion estandar muestral
sta.pstdev(calificaciones) #desviacion estandar pobalcional

sta.pvariance(calificaciones) #varianza poblacional 
sta.variance(calificaciones)#varianza muestral
