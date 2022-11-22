import json
frase =  'El veloz murcielago hindu comia feliz cardillo y kiwi La ciguena tocaba el saxofon detras del palenque de paja'
frase = frase.upper()

letras = {}
for letra in frase:
    if letra in list(letras):
        letras[letra] += 1
    else:
        letras[letra] = 1

cosas = list(letras)
cosas.sort()
for letter in cosas:
    print(letter +': '+ str(letras[letter]))
