from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Word
import nltk.corpus 
texto = 'Y cuando despertó. Todo a su alrededor era luminoso'
blob = TextBlob(texto) #converitr un texto al tipo de variable que puede aplicarsele NLP
print("#----------")
print(blob.sentences)#Rompe en oraciones segun lo qeu entiende el metodo separando por puntos
print(blob.words) #devuelve las palabras unicas en la oracion

"Segundo Ejemplo"
frase2 = TextBlob('I have good discipline to study. In the future I will be a great engineer') #reconoce independeintemente del idioma(parece) pero fincuona muchisimo mejor en ingles
print("#----------")
print("Separacion en palabras unicas del texto")
print(frase2.words)
print("Serparacion en oraciones del texto.")
print(frase2.sentences)
"""TextBlob permite realziar uan categorizacion de todas las palabras en sustancitos, adjetivos, etc etc"""
print("#----------")
for couple in frase2.tags:
    print(couple)

"""Se pueden obtner noun pgrases osea, sustantivos qeu son descritos"""
print("#----------")
print("busqueda de los noun_phrases")
print(frase2.noun_phrases)

"""PErmite realizar un analiss de sentimientos a partir del TextBlob"""
f3 =  TextBlob('I am a bad student. I will not be able to finish my studies')
print("#--------")
print("analisando la frase completa")
print(f3.sentiment)


"""Cuando la polaridad da un numero negativo estamos hablando de uns entimiento negativo como la tristeza mientras uno postivio
representa las emociones contratrios y la subjetividad recfiere a la seguridad del algoritmo en la clasificacion"""
print("#--------")
print("Analizando texto a partir de horaciones separadas:")
for sentence  in f3.sentences:
    print(f"Analizando la frase: {sentence} que obtiene como resultado:")
    print(sentence.sentiment)


"""Existe otro metodo de analisis llamado NavieBayesAnalizer que se desarrolloa partir de reseñas de peliculas el cual veremos a
continuacion"""

print("#---------")
print("Analisis de senitmientos del modelo NAvieBayesAnalizer")
texto2 = TextBlob('I am a bad student. I will not be able to finish my studies',analyzer = NaiveBayesAnalyzer())#en este caso particular funciona peor, es a criterio del programador decidir qeu motor de interpretacion utilizar
print(texto2.sentiment)

"""TextBlob teine una herramienta que permite hacerdeteccion del idioma del texto que se está ingresando al codigo  partir del
metodo .detect_language()"""
print("#----------")
print("Analisis del idioma del texto ingresado")
palabra = 'bonjour'
blob4 = TextBlob(palabra)
idio = (blob4.detect_language)#esta parte no me da el print averiguar por qeu carajos
print(idio)
"""Tambien es posible hacer traducciones utilizando un metodo de textblob"""
print("#-------")
textblob = TextBlob('I have good discipline to study. In the future I will be a great engineer')
traducida = textblob.translate(to='es')
print(f"La frase original es:\n{textblob}\ny traducida resulta en:\n{traducida}")

"""Otro de lso metodos que permite TextBlob es la pluralizacion y singularizacion de las palabras a travez del  modulo word"""
print("#------------")
veg = Word("Tomatoe")
vegplural = veg.pluralize()
print(f"La palabra original es:{veg} y pluralizada tenemos:{vegplural}")
veg = Word("Carrots")
vegsingular = veg.singularize()
print(f"La palabra original es:{veg} y singularizada tenemos:{vegsingular}")
"""Ademas se cuenta con un corretor de ortografia y tambien proviene de la biblioteca word"""
palabra = Word("whife")#puede ser while o wife
print("#------------")
"""El metodo .spellcheck retorna la psoible corerccion con una probabildiad de que la palabra sea la que se quizo escribir 
en guncion de como esta escrita y da multiples posibildiades con sus respectivas probabildiades en un foramto de tupla 
(palabra,posibilidad)"""
print("escribiste: ",palabra)
for correcta, posibilidad in palabra.spellcheck():
    print(f"quizas quieres decir:{correcta} con una posibilidad del:{posibilidad*100}%")
print("#-----")
prueba = Word("worker")
print(f"Definicion para la palabra:{prueba}")
print(prueba.definitions)
print("#---------")
print(f"La palabra{prueba} tiene como sinonimos:")
print(prueba.synsets)

