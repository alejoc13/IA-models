"""Los diccionarios son un tipo de arreglo que consta de una clave y una información, dicha clave es inmujtagle 
durante la itneracion, pero el valor si puede ser modificado."""
edadusuario = {'laura':28,'Daniel':31,'Alberto':27,'Rogelio':65} # Los diccionarios se crean utilizando {}
for usuario,edad in edadusuario.items(): #.items es un metodo de diccionarios par aaceder a todo su contenido facilmente y las dos variable sdel for fucnionar para trabajar dos varaibles al tiempo
    print(f'el usuario {usuario} tiene {edad} años cumplidos')

"""Probando dobel variable en el for con zip  """
print('#----------------')
nombres = ['a','b','c']
numeros = [1,2,3]
for nom,num in zip(nombres,numeros): #se hace un zip entre las dos listas relacionadas y se recorren juntas (si no se necesita acceder al indice)
    print(nom,num)

print("#----------------")
edadusuario['eva'] = 29 #al no existir la clave, la agrega y guara la informacion qeu se le asigne
edadusuario['laura'] = 50 #Como la clave existe reemplaza la información qeu contenga
"""Los diccionarios permiten eliminar inforamción a partir del metodo del """
del(edadusuario['Daniel']) #elimina la clave y la informacion 
print(edadusuario)
print('#--------')
"""El metodo .get permite extraer información de las claves y no genera error en caso de no existir la clave ingresada"""
edadusuario.get('pepe','No se encuentra la clave')
print('eva' in edadusuario) #esta es la forma de consultar si la clave existe 

print('#--------')
"""El metodo .values en lso diccionarios sirve para acceder unicamente a los valores mas no a las claves"""
for i in edadusuario.values():
    print(i,end=', ')    

"""el metodo .keys se utiliza para acceder unicamente a las calves del diccionaro"""
for nombre in edadusuario.keys():
    print(nombre)

"""Si se utiliza el metodo list con un diccionario convierte (clave,valor)  en una tupla y se genera un lsita de tuplas"""
print(list(edadusuario.items()))

"""Python permite la comparacion de diccionarios, al punto qeu si dos diccionarios tienen las mismas llaves y elementos 
pero se encuentran en iun orden distinto, se detectarra de igual forma que son iguales."""

asistentes_dia1={'Ramírez':'Laura','Cortés': 'Daniel','Pérez':'Alberto'}

asistentes_dia2={'García':'Rogelio','Ramírez': 'Laura','Pérez':'Alberto'}

asistentes_dia3={'Pérez':'Alberto','Cortés': 'Daniel','Ramírez':'Laura'}
print(asistentes_dia1 == asistentes_dia2)
print(asistentes_dia1 == asistentes_dia3)
print('#-----------')
"""Los diccionariso tambein permite rtrabajo a partir de la comprension de diccionarios en el ejemplo vemos la creacion de un 
diccionario donde al llave es el número y el valor el cuadrado de ese numero"""

salida = {i:i**2 for i in range(4,11)}
for clave,valor in salida.items():
    print(f'el valor es {clave} y su cuadrado es {valor}')