class Persona:
    # un constructor es un metodo propio de las clases que se llamará cuando se cree una instancia
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def saludar(self):
        print(f"Hola {self.nombre}")

    def __str__(self):
        """
        Método que sirve para que cuando vayamos a llamar a imprimir el objeto, se modifique por algo más entendible
        """
        return self.nombre + " Instancia del objeto"

persona1 = Persona("Dany", "17-09-2001")
persona2 = Persona("Paul", "14-11-1999")

print(persona1.fecha_nacimiento)
print(persona1)
