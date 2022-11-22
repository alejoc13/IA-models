from pathlib import Path
from textblob import TextBlob
from textblob import Word
texto = open("dracula.txt",encoding="utf-8")
dracula = TextBlob(texto.read()) #Metodo de conteo de TexBlob
print(dracula.words.count("crucifix"))
print(dracula.words.count("ladyCapulette"))