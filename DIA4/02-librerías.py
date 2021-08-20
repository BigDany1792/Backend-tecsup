from camelcase import CamelCase

instancia = CamelCase()
texto = "Hola alumnos buenas noches ya se viene el break"

resultado = instancia.hump(texto)

print(resultado)

print(texto.capitalize)