import tkinter
def saludar():
    texto['text'] = "Hola amigo"
def despedir():
    texto['text'] = "nospi"     

principal = tkinter.Tk()
principal.wm_title('programa')
texto = tkinter.Label(principal,text="saluda")

#botones
botonSaluda =  tkinter.Button(principal,text="hola",command = saludar)
botonDespide = tkinter.Button(principal,text="Adios",command = despedir)
texto.pack()
botonSaluda.pack()
botonDespide.pack()

principal.mainloop()
    
