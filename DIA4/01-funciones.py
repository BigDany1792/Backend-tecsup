# FUNCIOÓN
# una función es un bloque de codigo que se va a ejecutar cuantas veces sea llamada la función("Es un maquina a la que le das algo y te devuelve otra cosa")
# una función se crea con la palabra reservada "def"

def saludar():
    print("Hola buenas tardes")

# funciones con parametros
# los parametros que usan las funciones o las variables creadas dentro de las mismas solamente podran ser accedidas dentro de ellas!¡¡


def saludarPersona(nombre):
    print(f"Hola {nombre}, Como estas?")


saludarPersona("Dany")


def sin_nombre():
    '''Aqui va la descripcion de la función y va entre triple comilla simple'''
    print("Yo soy una funcion sin nombre")

# las funciones pueden recibir parametros y estos pueden ser opcionales

# las variables a las que le asignemos un valor no serán obligatorias a la hora de escribir los parametros


def registro(nombre, correo=None):
    print("Registro exitoso")


registro("dany")
registro("dany", "dany1792dota@gmail.com")
# registro()

# Crear una función llamada identificación en la cual se reciba el nombre, apellido y la nacionalidad del cliente, si en el caso no se pasa la nacionalidad entonces será peruano, imprimir el resultado en forma de un diccionario

def identification(nombre, apellido, nacionalidad="peruano"):
    resultado = {
        "nombre": nombre,
        "apellido": apellido,
        "nacionalidad": nacionalidad,
    }
    print(identification)

identification("dany", "chavez")

# todos los parametros que tengan un valor predeterminado siempre VAN AL FINAL
def sumatoria(num1, num2, num3=10):
    print(num1+num2+num3)

sumatoria(10,20)

# el parametro que tiene el simbolo asterisco al comienzo es un parametro especial de python que sirve para almacenar "n" valores
# todos los valores que pasemos a ese parametro se alamacenaran en una tupla en el mismo orden con el cual hemos pasado los parametros 
def alumnos(*args):
    print(args)


alumnos(
     "eduardo",
        "siannet"
            "pablo"
                "fernando"
                    "Jose")   

#!def tareas(nombre, *args, apellido):
 #!   print("ok")
        
#!tareas("eduardo","1","2",True, apellido="martinez")

def cachorros():
    # TODO: implementar logica
    pass #con el pass podemos dejar una función sin incluir logica por ahora

x=5

# en la función alumnos_notas se recibirá una cantidad N de alumnos en la cual se debe indicar cuantos aprobaron y cuantos desaprobaron siendo la nota minima 11

def alumnos_notas(*args):
    aprobados=[]
    desaprobados=[]
    for alumno in args:
        if(alumno["promedio"]>11):
            aprobados.append(alumno["promedio"])
        elif(alumno["promedio"]<11):
            desaprobados.append(alumno["promedio"])
    print(f"{aprobados}")
    print(f"{desaprobados}")    

alumnos_notas(
    {"nombre":"Raul", "promedio": 17},
    {"nombre": "Roxana", "promedio": 20},
    {"nombre": "Alfonso", "promedio": 10},
    {"nombre": "Pedro", "promedio": 8},
    {"nombre": "Katherine", "promedio": 16}
)


# keyword arguments ===> es muy similar a los *args solo con la diferencia que lo kwargs usan el nombre del parametro (nombre="eduardo")

def indeterminada(**kwargs):
    print(kwargs)

indeterminada(nombre="dany",apellido="chavez",nacionalidad="peruana")

def variada(*args,**kwargs):
    print(args)
    print(kwargs)


variada(10, "eduardo",{"est_civil" :"viudo"}, mascota="firulais", raza="bulldogs")


def sumatoria(num1,num2):
    return(num1+num2)
    print("no me ejecuto")


rpta = sumatoria(10,5)