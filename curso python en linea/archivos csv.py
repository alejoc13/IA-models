import pandas as pd
import matplotlib
import csv
with open("seguidores.csv",mode = 'w',newline='') as seguidores:
    writer = csv.writer(seguidores)
    writer.writerow(["@charlidamelio","D’Amelio",108.1])
    writer.writerow(["@zachking","Zach",56.6])
    writer.writerow(["@bellapoarch","Bella",56.3])
with open("seguidores.csv",mode ='r',newline='') as seguidores:
    lectura = csv.reader(seguidores)
    print(f'{"Handle":<20}{"Nombre":<10}{"num-seg":>10}')
    for record in lectura:
        handle,nombre,cant = record
        print(f'{handle:<20}{nombre:<10}{cant:>10}')
    
"""CAbe resaltar que tambien es posible abrir un archivo csv desde pandas como se hizo en clases anteriores."""
dfgym = pd.read_csv("datos_gimnasio.csv")
print(dfgym.head(5))