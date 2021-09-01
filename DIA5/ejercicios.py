# ejemplo
# para evitar que en cada impresion se ejecute una nueva linea, se puede agregar el parametro "end" y este indicará como queremos que actue al finalizar la linea

# for numero in range(5):
#   print(numero, end="")


#! ejercicio 1
def dibujar_rectangulo(altura, ancho):
    
    for i in range(altura):
        print("*"*ancho)

# dibujar_rectangulo(4,5)



#! ejercicio 2
def dibujar_octogono(grosor):
    
    for i in range((grosor*2)-1):
        if(i < grosor):
            espacios = grosor-i-1
            print(' '*(espacios)+'*'*(grosor+(i*2)))
        else:
            print('*'*((grosor*3)-2))
    for i in range(grosor-1):
        print(' '*(i+1)+'*'*((grosor*3)-4-(i*2)))

#dibujar_octogono(5)



#! ejercicio 3
def triangulo_invertido(altura):

    for i in range(altura):
        print('*'*altura)
        altura -= 1

# triangulo_invertido(9)



#! ejercicio 4
def serie_collatz(numero):

    while numero != 1:
        if(numero % 2 == 0):
            numero /= 2
            print(int(numero))
        else:
            numero = (numero*3)+1
            print(int(numero))

# serie_collatz(19)
