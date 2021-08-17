# concatenando
mes = "agosto"
dia = 16
print("hoy es", dia, "de", mes)


# concatenando(2da forma)
alumnos =25

print("Los alumnos son {} y son del grupo {} y todos estan atentos".format(alumnos, 10))
print("Los alumnos son {1} y son del grupo {1} y todos estan atentos".format(
    alumnos, 10))  # en este caso los que esta dentro de format , representa una tupla
# Aqui se indica con la "f" que lo que está entre corchetes tiene que ser codigo python
print(f"Los alumnos son {1+1}")
print(f"Los alumnos son {alumnos}")
