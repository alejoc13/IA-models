#algorimo de la burbuja para adivinar numeros( entre 0-100)
import random
lower = 0
upper = 100
decidir = "n"
while decidir == "n":
    numeroResultado =  random.randrange(lower,upper)
    decidir = input(f"Tu numero es {numeroResultado} (s/n): ")
    if decidir == "n":
        pista = input("El número es mayor o menor(h/l): ")
        if pista == "h":
            lower = numeroResultado+1
        if pista =="l":
            upper  = numeroResultado