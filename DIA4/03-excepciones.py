from typing import final

try:
    numero = 5/1
    print(f"el numero es {numero}")
    numero= 6000/0
    print(f"el numero es {numero}")
except ZeroDivisionError:
    print("Hubo un error al hacer la division")
except TypeError:
    print("No se puede sumar entre strings y numeros")
except:
    print("Error desconocido")
else:
    print("todo bien")
finally:
    print("Igual me ejecuto")


# ? Finally => no importa si la operación salió bien o hubo errores, igual se ejecutará
# ? else => para usar el else tenemos que obligatoriamente declarar un except, y este se ejecutará cuando no ingresa a ningun except(cuando la operacion no tuvo errores)


print("Soy un ejemplo que no tiene nada que ver")

# Ingresar 4 numeros, si uno de ellos no es un numero entonces no tomarlo en cuenta y volver a pedir hasta que tengamos los 4 numeros
# ingresa un numero: 1
# ingresa un numero: 2
# ingresa un numero: a
# ingresa un numero: 4
# ingresa un numero: f
# ingresa un numero: 10
# los numeros son: [1,2,4,10]

numeros = []
while len(numeros) != 4:
    try:
        numero = int(input("Ingresa un numero: "))
        numeros.append(numero)
    except:
        pass

print("Los numeros son {}".format(numeros))