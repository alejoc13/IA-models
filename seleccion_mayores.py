def MayordeTres(a,b,c):
    vec = [a,b,c]
    resultado = a
    for i in vec:

        if i>resultado:
            resultado=i
    return resultado
 
a = -1
b = 10
c = 3

resultado =MayordeTres(a,b,c)
print(resultado)



