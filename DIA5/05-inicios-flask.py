from logging import debug
from flask import Flask

#__name__ => muestra si el archivo en el cual se esta llamando a la clase Flask es el archivo principal del proyecto, esto se hace para evitar que la instancia de la clase Flask se pueda crear en otros lados(patron de diseño SINGLETON)
app = Flask(__name__)

#si estamos en el archivo pirncipal del proyecto nos imprimirá __main__ caso contrario imprimirá la ubicación del archivos
#print(__name__)

#decorador ==> es un patrón de software que se utilizarpara modificar el funcionamiento de una clase o una función enparticular sin la necesidad de emplear otros metodos como la herencia( cosas que no se puede en una funcion comun y corriente)


@app.route('/')
def inicio():
    print("Me llamaron!")
    return {
        "message": "Hello World!"
    }


#Nota: Todo el codigo a implementar siempre debe ir antes del run()
app.run(debug=True)