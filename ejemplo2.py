import tkinter as tk
from tkinter import messagebox
def obtenerNotas():
    corte1 = nota1.get()
    corte2 = nota2.get()
    necesita = (3.0-0.3*(corte1+corte2))/0.4
    return  notaNecesaria.set(necesita)
principal = tk.Tk()
principal.wm_title('calculadora de notas de la rata')
#Botones
BotonCalcular = tk.Button(principal,text="calcular",command = obtenerNotas)

#Variables para trabajo
nota1=tk.DoubleVar()
nota2=tk.DoubleVar()
notaNecesaria = tk.DoubleVar()
Comparation = tk.DoubleVar()


#cajas de texto y obtencion de datos
nota_entry = tk.Entry(principal,textvariable = nota1, font=('calibre',10,'normal'))
CajaCorte1 = tk.Label(principal, text = 'Nota corte 1', font=('calibre',10, 'bold'))

nota_entry2 = tk.Entry(principal,textvariable = nota2, font=('calibre',10,'normal'))
CajaCorte2 = tk.Label(principal, text = 'Nota corte 2', font=('calibre',10, 'bold'))

CajaFinal = tk.Label(principal, text = 'Para el corte final requiere:', font=('calibre',10, 'bold'))
nota_necesaria = tk.Entry(principal,textvariable = notaNecesaria, font=('calibre',10,'normal'))







CajaCorte1.pack()
nota_entry.pack()

CajaCorte2.pack()
nota_entry2.pack()

BotonCalcular.pack()
CajaFinal.pack()
nota_necesaria.pack()

principal.mainloop()

