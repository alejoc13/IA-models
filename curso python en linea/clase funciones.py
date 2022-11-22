"""Las funciones puede darceles un valor inicial para evitar qeu el programa se caiga si no pnen lso valores solicitados"""
def raizcuad(num=1):
    resultado = num**(1/2)
    return resultado

print(raizcuad())
"""Tambien es posibel dar un número indefinido de parametros"""
def promedioCalif(*calif): #(*var genera qeu se puedan recivir n cantidad de parametros)
    return sum(calif)/len(calif)

print(promedioCalif(3,2,4,5,5,4.3))

def multiParam(*var): #(*var) se convierte en una lsita y se itera como tal
    resultado = 1
    for i in var:
        resultado*=i
    return resultado
print(multiParam(1,2,3,4))


"""Existen varaibles de alcance local y alcane global donde una se usa solo en la funcion o fragmento de codigo dodne se declara y
la otra funciona en forma generalziada del codigo respectivamente"""
aproxPi = 3.1416 # en este caso esta actua como variable global por no estar dentro de una funcion 

def areaCircle(radio):
    return aproxPi*radio*radio

print(areaCircle(5))
"""Las variable loscasles no pueden ser modificadas dentro de las funciones, sakvo qeu se guarde el return en la varaible global"""