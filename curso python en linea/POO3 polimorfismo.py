class Matematicas:
    numcreditos = 8
    def mostrar_creditos(self):
        return "matimaticas tiene 8 creditos"

class Ingles:
    numcreditos = 5
    def mostrar_creditos(self):
        return "ingles tiene 5 creditos"

asignatura = Matematicas
print(asignatura.mostrar_creditos())
asignatura2 = Ingles
print(asignatura2.mostrar_creditos())