import nltk
from nltk.corpus import stopwords
from textblob import TextBlob #esta funciona despues de hacer la linea 3 por primera vez
#nltk.download("stopwords") #Esta lina se ejecuta una unica vez
# nltk.download('omw-1.4') #esta parte intala lo necesario para poder usar definiciones en NLP1
stops = stopwords.words("english")
print(stops)
"""PAra un texto una stopword es uan palabra que no aporta nada al analisis del texto, por tanto debe ser eliminada
para simplificar el texto y gastar menos memoria y recuersos en el analisis"""
blob = TextBlob("I have a beautiful day")
print([word for word in blob.words if word not in stops])#No elimina mayusculas, es un porbelam qeu uno mismo tiene que solucionar 


