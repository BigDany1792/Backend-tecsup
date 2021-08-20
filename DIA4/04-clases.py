class Mueble:
    precio = 00.00
    color = "Blanco"
    especificaciones = []
    tipo = "ELegante"

    def indicar_tipo(self):
        # "self" se usa para indicar que el metodo pertenece a la clase en la que estamos trabajando, en este caso ==> "Mueble"
        return f"El tipo es: {self.tipo}"


mueble1 = Mueble()
mueble1.tipo= "Sofa-cama"
print(mueble1.indicar_tipo())

mueble2 = Mueble()
mueble2.tipo= "Silla"
print(mueble2.indicar_tipo())