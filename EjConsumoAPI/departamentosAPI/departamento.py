class Departamento:
    numero = 0
    nombre = ""
    localidad = ""

    def __str__(self):
        return (str(self.numero) + " - " + self.nombre + " - " + self.localidad)