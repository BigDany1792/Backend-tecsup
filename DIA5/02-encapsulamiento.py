class Vehiculo:
    def __init__(self, largo, ancho, cilindrada, enMarcha=False):
        self.largo = largo
        self.ancho = ancho
        self.cilindrada = cilindrada
        self.enMarcha = enMarcha

        # cuando queremos indicar que un atributo va a ser privado (no puede ser accedido desde fuera de la clase) se le pone antes del nombre __

        self.__alarma = True

    def interruptor(self):
        resultado = self.__verificar_alarmas()
        if(resultado == True):
            self.__alarma = False
        else:
            self.alarma = True

    def encender(self, estado=True):
        resultado = self.__verificar_alarmas()
        if resultado:
            self.enMarcha = estado
        else:
            print("El vehiculo intenta ser robado 🚨🚨🚨")

    def verificar_alarmas(self):
        if(self.__alarma == True):
            return False
        else:
            return True
        print(self.__alarma)

   


objVehiculo = Vehiculo(2.20, 1.65, 1500)
objVehiculo.largo()


class Persona:
    def __init__(self, nombre, apellido, correo, password):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = self.__encriptar_password(password)

    def __encriptar_password(self, password):
        return "asdasdasdasd"+password+"asdadasdsa"


objPersona = Persona(nombre="Raul", apellido="Perez", correo="rperez@empresa.com", password="12345")

print(objPersona.password)

