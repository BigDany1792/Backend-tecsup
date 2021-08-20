# segun la libreria camelcase que convierte cada inicio de palabra en mayuscula hacer lo mismo pero sin la libreria usando el codigo ascii

# si el texto de ingreso es:
texto = "hola alumnos buenas noches ya se viene el break"
# entonces el texto resultado debera ser:
resultado_final = ["Hola", "Alumnos", "Buenas", "Noches", "Ya", "Se"]


print(texto[1])
for letra in texto:
    print(letra, end="*")

# asi se saca la ubicacion del caracter usando Codigo ASCII
print(ord("x"))
print(chr(95+15))

