class Personal:
    def __init__(self,nombre,profesion,cargo):
        self.nombre = nombre
        self.profesion = profesion
        self.cargo = cargo
    def detalle(self):
        return "{} es un {} que tiene el cargo de {}".format(self.nombre,self.profesion,self.cargo)
class pers_nuevo(Personal):
    def contratacion(self,contrato):
        return "{} tiene contrato {}".format(self.nombre,contrato)

class pers_advo(Personal):
    def contratacion(self,contrato):
        return '{} tiene contrato: {}'.format(self.nombre,contrato)

Ingeniero = pers_nuevo("Paco","Ingeniero de sistemas","Supervición")
print(Ingeniero.detalle())

print(Ingeniero.contratacion("Temporal"))

class Cuenta:
    def __init__(self,nombre,capital):
        if capital<0:
            raise ValueError("El capital debe ser mayor a 0")
        self.nombre = nombre
        self.capital =capital
    def informacion(self):
        return "{} tiene un capital de {}".format(self.nombre,self.capital)

class Ahorro(Cuenta):
    def cantidad(self,deposito):
        if deposito<0:
            raise ValueError("La cantidad debe ser mayor a 0")
        self.capital+=deposito
        return "{} tiene ahora en su cuenta: {}".format(self.nombre,self.capital)

class gasto(Cuenta):
    def cantidad(self,retiro):
        if retiro < 0:
            raise ValueError("LA cantidad debe ser mayor a 0")
        if retiro>self.capital:
            raise ValueError("No tienes suficiente dinero")
        self.capital-=retiro
        return "{} ahora cuenta con un capital de: {}".format(self.nombre,self.capital)



cuenta1 = Ahorro("juan",2000)
print(cuenta1.informacion())
cuenta1.cantidad(1500)
print(cuenta1.informacion())
cuenta2 = gasto("Pedro",50000)
print(cuenta2.informacion())
cuenta2.cantidad(300)
print(cuenta2.informacion())