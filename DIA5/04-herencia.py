class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def acelerar(self):
        print("El 🚗 esta acelerando")

    def estado(self):
        return f"Marca:{self.marca} \nModelo:{self.modelo} \nNumero de ruedas:{self.numero_ruedas}"


autoFord = Vehiculo("ford", "2004", 4)

print(autoFord.estado())


class Auto(Vehiculo):
    def __init__(self, sunroofe, marca, modelo):
        self.sunroofe = sunroofe
        super().__init__(marca, modelo, 4)

    def estado(self):
        return "Yo soy el estado del auto"


class Camion(Vehiculo):
    def __init__(self, numero_cambios, marca, modelo):
        self.numero_cambios = numero_cambios
        super().__init__(marca, modelo, 8)

    # def saludar(self):
        # print("Hola")

    # def saludar(self, nombre):
    #     print("Hola {nombre}")


objetoAuto = Auto(True, "Bugatti", "2020")
print(objetoAuto.estado())
print(objetoAuto.estado())
