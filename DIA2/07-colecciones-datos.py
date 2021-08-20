# List ==> Listas
# Ordenadas y modificables
#se definen con corchetes []
colores = ["azul", "rojo", "morado", "amarillo", "verde"]
mezclada = ["otoño", 14 , False , 15.2 , [1,2,3]]
#las listas empiezan en la posición cero

#imprimir la primera posición
#En python si la posición no existe, lanzara un error, a diferencia de JS, que indicará undefined(no definido)
print(colores[1])
#al usar valores negativos en las posiciones de la lista "se invertirá" y podremos recorrer la lista 
print(colores[-1])
# con el operador ":" definimos el rango en las posiciones de una lista que deseemos imprimir
print(colores[1:2])
# si no definimos el segundo valor retornará desde el valor inicial hasta el final
print(colores[1:])
#si no definimos el primer valor retornará desde el inicio hasta el 2do valor
print(colores[:4])

#sirve para copiar EL CONTENIDO DE LA LISTA mas no su ubicación de memoria
colores_2=colores[:]

print(id(colores_2))   
print(id(colores))

#metodo para agregar un elemento a una lista
colores.append('esmeralda')
print(colores)

#metodo para eliminar un valor
#1. solamente si existe lo eliminará, sino lanzará un error
colores.remove("azul")
print(colores)
#2. si queremos elimanrlo y ADEMAS guardar el valor eliminado en una variable
color_eliminado= colores.pop(0)
print(colores)
print(color_eliminado)
#3. metodo para eliminar el valor 
#este metodo tambien sirve para eliminar variables
nombre="eduardo"
#del nombre
#print(nombre)
#otras formas de usar el del
#del colores[0]
#del colores[:3]

#longitud de la lista
print(len(colores))


#|||||||||


# TUPLAS
# La tupla a diferencia de la lista es una colección de datos ordenada PERO que una vez creada no se puede editar 
# se definen con parentesis ()

days_week = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print(days_week[1])
print(len(days_week))

#para contar cuantas veces se repite un valor en usamos el metodo count
print(days_week.count("Lunes"))


# DICCIONARIOS
persona = {
    "nombre": "Dany",
    "apellido": "Chavez",
    "correo": "dany1792dota@gmail.com",
    "edad": 20,
    "donacion_organos": True,
    "hobbies": [
        {
            'nombre': 'Volar drones',
            'conocimiento': 'avanzado'
        },
        {
            'nombre': 'Volar cohetes',
            'conocimiento': 'basico'
        }
    ]
}

print(persona["edad"])
print(persona["hobbies"][0]['nombre'])

#imprimir el primer hobby de la persona 
# Volar drones
print(persona['hobbies'][0])

#forma de extraer solamente las llaves
print(persona.keys())

#forma de extraer solamente los valores
print(persona.values())

persona.clear()
print(persona)


#CONJUNTOS
#Colección de datos desordanada , que una vez que la creamos no pdoremos acceder a sus posiciones ya que estará ordenada aleatoriamente
#Se puede editar mas no se puede ingresar a sus elemenetos por sus posiciones
alumnos = {"kevin", "Dany", "Paul", "Sebastian", "Sandra"}
print(alumnos)
alumnos.add("Diego")
print(alumnos)
alumnos.remove("Diego")
print(alumnos)