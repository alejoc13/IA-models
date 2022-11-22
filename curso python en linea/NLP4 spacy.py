import spacy
nlp = spacy.load("en_core_web_sm") #-PAra trabajar ingles
documento = nlp("airbnb is an American company that operates an online marketplace for lodging, primarily homestays for vacation rentals, and tourism activities. Based in San Francisco, California, the platform is accessible via website and mobile app. Airbnb does not own any of the listed properties; instead, it profits by receiving commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com")
for entity in documento.ents: #identidica nombtre entidades y fechas
    print(f"{entity.text},{entity.label_}")