#is => es
#is not => no es 

frutas = ['carambola', 'guayaba', 'higo', 'melocoton']
fruta = 'carambola'

#El 'is' e 'is not' se usa mas que todo para validar si las vatiables a comparar estan apuntadno a la misma dirección de memoria o no

print(fruta is frutas)


#para saber la posición en la que se almacena una variable en la memoria usamos el método id()

print(id(fruta))
print(id(frutas))
print("gola")