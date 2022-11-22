edad = [65,26,28,36,18]
"""En los dos casos sigueintes se acepta que las lsitas originales sean modificadas y por tanto se pierda el orden 
original en el ual es entregada la inforamción"""
edad.sort() #ordenar de menor a mayor 
print(edad)
edad.sort(reverse=True) #ordenar de mayor a menor
print(edad)
"""Los metodos sigueintes permiten retornar una nueva lista con el orden que se solicite pero sin modificar la original"""
print("---------------")
edad = [65,26,28,36,18]
edadordenada = sorted(edad)
print(edadordenada)
edadordenada = sorted(edad,reverse=True)
print(edad)
print("-----------------")
"""El metodo insert permite agregar un nuevo elemento a un a lista sin borrar el qeu se enc uentra en el lugar esepcificado,
es decir todos los demas cambian una posicion para insertar el nuevo """
vegetales = ['espinaca','apio']
vegetales.insert(0,"lechuga")
print(vegetales)

vegetales.insert(1,"tomate")
print(vegetales)

