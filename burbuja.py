#Ordenamiento por metodo de la burbuja


def MenoraMayor(a):
    for i in range(1,len(a)):
        for j in range(len(a)-i):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

def MayoraMenor(a):
    for i in range(1,len(a)):
        for j in range(len(a)-i):
            if a[j]<a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

a = [2,5,5,9,74]
b = MenoraMayor(a)
print(b)
c= MayoraMenor(a)
print(c)

     
    