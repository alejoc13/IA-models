import re
codigo  = "9401354"
print("codigo correcto" if re.fullmatch(codigo,"9400354") else "codigo incorrecto")
print("telefono correcto" if re.fullmatch(r'\d{10}',"3012023164") else "telefono incorrecto") # r strihgn cumpel con dar un criterio de comparacion
print("Bien escrito" if re.fullmatch('[A-Z][a-z]*',"Elvira") else "mal escrito") #comprueba qeu inicia con mayuscual y lo demas es minuscula
"""recordar que dejar el asterisco inplica qeu puede haber uan cantidad indefinida de lelemtons que cumplan con una caracteristica 
mietras quitarlo solo valida que exista 1 elemento cumpliendo la regla solicitada"""
print("sin asterisco:")
print("Bien escrito" if re.fullmatch('[^a-z]',"R") else "mal escrito") #^ lo que ahce es pedir que se excluya el conjunto
print("con asterisco:")
print("Bien escrito" if re.fullmatch('[^a-z]*',"ROGELIO") else "mal escrito")
print('#-----------')
print('Confirmando minusculas')
print("Bien escrito" if re.fullmatch('[A-Z][a-z]+',"Rogelio") else "mal escrito") #+ lo qeu perminte es preguntar si almenos un elemento del conjunto esta presente
print('#-----------')
"""TAmbien es posible solicitar uqe la expresion cumpla con una cantidad determinadad de digitos"""
print("verificando si hay n digitos o mas")
print("Correcto" if re.fullmatch(r'\d{4,}',"9875") else "incorrecto")
print("verificando si hay entre n y m digitos")
print("Correcto" if re.fullmatch(r'\d{4,8}',"987534545") else "incorrecto")
"""Crea y prueba una expresión regular que cuadra con una dirección de calle que consiste de un número con uno o más digitos 
seguido de 2 palabras de una o más caracteres. Por ejemplo 372 Callejón Rojo"""
print('#-----------')
calle = r'\d+ [A-Z][a-z]* [A-Z][a-z]*'
"""\d+  obliga a que se cumpla la existencia de digitos
   Los espacios entre expresiones hacen qeu se garantice cuantas partes debe tener el elemento a analizar
   [A-Z] exige qeu se inicie en Mayuscula 
   [a-z]* pide que todos los siguientes elementos hasta el proximo espacio sean minusculas"""

print("formato de calle correco" if re.fullmatch(calle,"434 Callejon Rojo") else "Formato de calle incorrecto")
"""LA expresioens regulare stambien permiten hacer cabios en cadenas"""
print("#-----------")
"""La funcion se le dan como argumentos:
expresion r'' que se busca reemplazar 
expresion por al cual se va a reemplazar 
la cadena objetivo sobre la que se va a trabajar"""
print("original: 'Salto 1\nSalto 2\nSalto 3'")
print("modificado",re.sub(r'\n',",",'Salto 1\nSalto 2\nSalto 3'))
print("#-----------")
print(re.sub(r'\n',",",'Salto 1\nSalto 2\nSalto 3',count = 1)) #count =n define el numero de reemplazos)

print("#-----------")
print(re.split(r',\s*',"s ,e,p,  a,r,a ,d,o")) # el astirisco le dice que tome todos los espacios hasta que encuentre algo diferente como uno solo
print(re.split(r',\s*',"s,e,p,a,r,a,d,o",maxsplit = 3)) #tambien permite definir el numero de partisiones
print(re.sub(r'\n+',", ","W\nX\n\nY\n\n\nZ")) #el + hace que todos los espacios seguidos sean cortados como uno solo 
print("#-----------")
"""Formas de busqueda con el operador search en el paquete re funcion apara buscar cosas especificas en todo un texto
pudiendole dar parametros especiales que definen algunas caracteristicas"""
busca1 = re.search("texto","este es solo un texto de pruena") #esta es una busqueda que solo da el resultado si se le solicita explicitamente
print(busca1.group() if busca1 else "No se encontro") # esta es la forma correcta de solicitar la salida de .search hy la salida es la palabra buscada si esta en el grupo de lo contrario da un mensaje de error
print("#-----------")
"""el comando flags =re.IGNORECASE permite ignorar la restrccion de python de minusculas y mayusculas"""
busca3 = re.search("Van","Guido Van Rossum",flags =re.IGNORECASE)
print(busca3.group() if busca3 else "no se encontro") 
print("#-----------")
buscador = re.search("^python","Guido Van Rosuum es el creador de python")
print(buscador.group() if buscador else "No se qeu buscaba y no lo encontre")#el caracte ^ permite que se busque el objetivo solo en la inicialización del texto