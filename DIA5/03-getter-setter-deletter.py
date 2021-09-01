class Electrodomestico:
    def __init__(self):
        self.__nombre = ""
        self.__color = ""
        self.__precio = 0.0

    def __setNombre(self, nombre):
        """El setter sirve para definir el contenido del atributo de una manera más formal"""
        self.__nombre= nombre

    def __getNombre(self):
        """El getter sirve para devolver el valor del atributo privado"""
        return self.__nombre

    def __deleteNombre(self):
        """El deletter sirve para eliminar el contenido del atributo privado"""
        del self.__nombre

    #Property ==> sirve para definir el comportamiento que tendrá un atributo de la clase
    nombre= property(__getNombre, __setNombre,__deleteNombre)


objEllectrodomestico = Electrodomestico()
objEllectrodomestico.nombre = "lavadora" #setter
print(objEllectrodomestico.nombre)  #getter
#objEllectrodomestico.nombre  #deletter



