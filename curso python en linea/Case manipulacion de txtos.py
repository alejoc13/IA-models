"""Los f strings son un tipo de texto al cual se le puede dar formato a través de una serie de instrucciones"""
""" los caracteres despue de lso dos puntos pueden ser:
f: flotante
d:decimal
c:caracter (codifica ascii  )
s:convierte a string"""
print(f'{3.141596:.3f}') #Dentro de {} se ponen las variables a mostrar seguid o de: para dar el formato deseado 
print(f'{150:d}')
print(f'{66:c}')
print(f'{"este curso esta de ":s}{100}')
"""Los formatos de texto cumplen con un standar determinado que permite modificar varios parametros al mismo tiempo:
f'{var:<n1.n2f}' donde
var: es lo que se piensa mostrar
<: determina hacia donde se va a alinear el valor a mostrar que puede ser cualqueira de lso siguientes simbolos
   <(alinear a la izquierda),>(alinear a la derecha),^(centrar)
n1: es el valor que define cuantos espacios va a ocupar el caracter a mostrar
.n2: define al fantidad de decimales a mostrar(Si el formato es decimal
f: que pude ser reemplazdo por cualqueira de lso valores de formato que se vieron en el apartado anteiror"""
print('#--------')
print(f'[{"Daniel":<20}]')
print(f'[{"Daniel":^20}]')
print(f'[{"Daniel":>20}]')
print('#--------')
"""Al trabajar con número el operardor , antes del formato obliga a python a mostrar separadores recordando que el . se utiliza 
para definir la cantidad de decimales que se presentarán al mostrar en pantalla"""
print(f'{6224511444:,d}')
print(f'{6224511444.4434:,.3f}') #si se usa el indicadoe , y se va a afirmar el nmero de deciamles se pone primero la ,
print('#--------')
print(f'{11483.528:10,.2f}\n{-4581.4413:10,.2f}')

