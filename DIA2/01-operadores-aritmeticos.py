# OPERADORES ARITMETICOS
numero1 = 10
numero2 = 80

persona1 = "eduardo"
persona2 = "Ricardo"


# SUMA
# Nota: si las dos o más variables son núemricas se realizará la suma, si por el contrario las variables son string(carácteres) se CONCATENARAN(se juntarán)
print(numero1+numero2)
print(persona1+persona2)
# print(numero1+persona1)esto devuelve un error


# RESTA
print(numero1-numero2)
# print(persona1-persona2) esto devuelve un error cuando restmaos variables tipo string


# MULTIPLICACIÓN
print(numero1*numero2)
# print(persona1*persona2)esto devulve un error
# print(str(persona1)*persona2)
# se puede multiplicar un string y un numerico
print(f"la multiplicacion de 10 y 80 es:n{numero1*numero2}")


# DIVISÓN
# Toda división obtendrá como resultante un flotante(parte entero y parte decimal)
print(numero2/numero1)
print(numero1/numero2)


# MÓDULO
# El modulo es el resultado de la división
print(numero2 % numero1)
print(numero1 % numero2)


# COCIENTE
print(numero2 // numero1)
print(numero1 // numero2)
