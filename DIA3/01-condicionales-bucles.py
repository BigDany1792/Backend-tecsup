# CONDICIONALES
# si eres mayor de edad
# edad = int(input("Ingrese sus edad: "))
# if(18 < edad and edad < 65):
#     print("Puedes vacunarte")
# elif(edad > 65):
#     print("Usted necesita una tercera dosis")
# else:
#     print("Aun no puede vacunarse")


# # OPERADOR TERNARIO
# # es una forma de hacer una validación pero en una sola linea de codigo

# texto = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
# print(texto)

# variable1, variable2 = ["eduardo", "martin"]
# print(variable1)
# print(variable2)


# numero = int(input("Ingrese un numero: "))

# if(numero % 2 == 0 and numero > 0):
#     print("Es par")
# elif(numero % 2 != 0):
#     print("Es impar")
# else:
#     print("El número es cero")

# # BUCLES
# # FOR => repite desde hasta
# # si nosotros queremos iterar una coleccion de datos la mejor forma es mediante un FOR
# meses = ["agosto", "septiembre", "octubre", "diciembre"]
# for mes in meses:
#     print(mes)
# #a diferencia del manejo de scopes(alcance) de la veriable en JS, en python, la variable sigue existiendo fuera del FOR
# print(mes)

# for numero in range(10):
#     print(numero)

# #el range puede recibir hasta 3 parametros

# #range(n) => n : el limite de las iteraciones
# for numero in range(10):
#     print(numero)
# #range(n,m) => n : numero inicial || m: numero final
# for numero in range(1,10):
#     print(numero)
# #range(n,m,o) => n: numero inicial || m: numero final || o: el incremento o decremento en cada ciclo
# for numero in range(1,10,2):
#     print(numero)

# numeros = [-4,7,-10,8,25,-7]
# positivos = []
# negativos = []
# for num in numeros:
#     if(num>0):
#         positivos.append(num)
#     else:
#         negativos.append(num)

# print(f"Hay {len(positivos)} números positivos y {len(negativos)} números negativos")
# print(f"Hay {len(positivos)} positivos y son {positivos}")
# print(f"Hay {len(negativos)} negativos y son {negativos}")


# BREAK
# hace que el bucle finalice de manera inesperada
# for seg in range(60):
#     print(seg)
#     if (seg == 10):
#         break

# # NOTA : en python el switch - case no existe!.

# print("======")
# # continue
# # salta la iteración actual
# for numero in range(15):
#     if (numero == 10):
#         continue
#     print(numero)


numeros = [1,2,5,9,12,15,17,19,21,39]
multiplos_3 = []
multiplos_5 = []

for num in numeros:
    if(num % 15 == 0):
        continue
    elif(num % 3 == 0):
        multiplos_3.append(num)
    elif(num % 5 == 0):
        multiplos_5.append(num)

print(f"Multiplos de 3 {multiplos_3}, multiplos de 5 {multiplos_5}")