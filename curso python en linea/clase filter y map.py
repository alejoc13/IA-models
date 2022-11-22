"""El comando filter como indica su nombre lrealiza el filtrado de una lista de datos a partir de una función determinada
es decir realiza sobre una lista de datos una operación que se le indique"""

def espar(i):
    return i%2 == 0

lista=[-3,5,8,4,1,-6,7,10]
print(list(filter(espar,lista))) #el comando  filter debe ir acomapado pro el comando list o no funciona.

"""En caso de requerir funciones muy sencillas es recomendable utilizar funciones lambda, esto evita el crear una cantidad
de funciones sencillas que se llaman repeditdamente"""
print("-------")
print(list(filter(lambda i:i%2==0,lista)))

"""La función map aplica una operación sobre una lista de elementos, nuvamente se da como argumentos la función(o la función lambda
que se requiere aplica y la lsita a modificar"""

print("---")
lista = [-3, 5, 8, 4, 1, -6, 7, 10]
print(list(map(lambda x:x**3,lista))) #tambien requiere la función lista para funcionar correctamente
