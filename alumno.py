class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        return self.nota

    def aprobo(self):
        if self.nota >= 7:
            return "Aprobó"
        else:
            return "No aprobó"


x1 = Alumno("Angela", 4)
x2 = Alumno("José", 8)
x3 = Alumno("Tomás", 6.5)
