from decimal import Decimal 

class Cuenta:
    def __init__(self,nombre,ahorro):  #__int__ indica qeu asi se inicializa todo nuevo objeto del tipo cuenta
        if ahorro<Decimal("0.00"):
            raise ValueError("El capital inicial debe ser mayor a 0")
        self.nombre = nombre
        self.ahorro = ahorro
    def deposito(self,cantidad):
        if cantidad<Decimal("0.00"):
            raise ValueError("La cantidad debe ser positiva")
        self.ahorro+=cantidad


cuenta1 = Cuenta("Juan",2000)   
print(cuenta1.nombre)
print(cuenta1.ahorro)

cuenta1.deposito(2000)
print(f"la cuenta de {cuenta1.nombre} ahora cuenta con: {cuenta1.ahorro}")

