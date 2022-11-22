"""Reto con Karen"""
def mayor(a,b):
    solve = a 
    if b>a:
        solve = b
    return solve

def max_de_tres(a,b,c):
    comp =  [a,b,c]
    solve =  comp[0]
    for i in comp:
        if i> solve:
            solve = i
    return solve

def longitud_sitema(a):
    cont = 0
    for i in a:
        cont +=1
    return cont

def esVocal(a):
    a = a.upper()
    if a == "A" or a== "E" or a =="I" or a=="O" or a == "U":
        return True
    else:
        return False

def sumar(a):
    suma = 0 
    for i in a:
        suma+=i
    return suma 

def multiplicar(a):
    mult = 1
    for i in a:
        mult *=i
    return mult

def inversa(a):
    salida = ""
    for i in range(-1,-len(a)-1,-1):
        salida = salida + a[i]
    return salida
        
def es_palindromo(a):
    b = inversa(a)
    if a == b:
        return True
    else:
        return False

def superposicion(a,b):
    cont = 0
    for i in a:
        for j in b:
            if i == j:
                cont +=1
    if cont != 0:
        return True
    else:
        return False 

def generar_n_caracteres(n,crt):
    crt = str(crt)
    return n*crt

def histograma(a):
    for i in a:
        print("*"*i)

def max_in_list(a):
    solve = a[0]
    for i in a:
        if i>solve:
            solve=i
    return solve

def mas_larga(a):
    solve = ""
    for i in a:
        if len(i)>len(solve):
            solve = i
    return solve 

def filtrar_palabras(a,n):
    list  = [word for word in a if len(word)>n]
    return list

def cantidad_mayusculas(a):
    cont = 0
    for letter in a:
        if letter.isupper():
            cont +=1
    return cont

def contar_vocales(a):
    vocales ={}
    for i in a:
        if esVocal(i):
            i=i.lower()
            if i in list(vocales):
                vocales[i]+=1
            else:
                vocales[i]=1
    return vocales

def convertirBinario(a):
    decimal = 0 
    for i in range(-1,-len(a)-1,-1):
        decimal += (2**(abs(i)-1))*a[i]
    return(decimal)
