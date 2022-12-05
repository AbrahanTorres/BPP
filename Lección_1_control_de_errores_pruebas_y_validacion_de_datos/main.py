# errores de syntaxis, cuando no escribimos correctamente nuestro código, o no se identa correctamente, o no colocamos las palabras de forma correcta

if (5>2) print("Es mayor")  #no estamos trabajando como python nos dice que trabajemos

# errores lógicos suelen ser porque nosotros no llegamos a programar algo de manera correcta

resultado = 2 + 8/2  #está mal escrito para la operación matemática.
print(f"La media es {resultado}")

#Excepciones

try:
    numero = 10
    divisor = int(input("Introduce un valor"))
    resultado = numero / divisor

except ZeroDivisionError: #except nos permite usar diferentes excepciones
    print("Error división entre 0")

except ValueError:
    print("Error por el valor pasado")

except Exception as e:  #preferible y recomendada, dado que es más general
    print("Ha ocurrido un error:", e)

else: 
    print("Se ejecta siempre que no se ejecute el except")

finally:
    print("Se ejecuta siempre, independientemente de como haya ido el try")

#Raise, nos permite lanzar una excepción

raise ZeroDivisionError #Nos permite a nosotros decidir cuando lanzar un error en particular
raise NameError ("Información de la excepción")


#assert, nos permite realizar comprobaciones
#si la expresión es falsa, se lanza una excepción de tipo AssertionError

assert(4==5)  # dado que  4 no es igual a  5, se lanza un AssertionError

''' por debajo es una especie de if.
if condicion:
    raise AssertionError()
'''

assert False, "El mensaje personalizado"

#Testing con assert

def suma(a, b):
    return  a + b

assert(suma(2,3) == 5) #con el assert le indicamos cual debería ser el resultado,  en este caso como el correcto no salta, es decir no da error
assert(suma(4,3) == 5) # en este caso, como 4 + 3 es igual a 7  y no igual  5, el assert nos dará el error.


def suma(a,b):
    assert(type(a) == int)
    assert(type(b) == int)

    return a + b

assert(suma(2, s) == 5)  #en este caso como el assert especifica que el tipo sea int, y le pasamos un string, nos eleva el error

class Clase1:
    pass

class Clase2:
    pass

m1 = Clase1()
m2 = Clase2()

assert(isinstance(m1, Clase2)) #con is instance preguntamos si m1 pertenece a Clase2, como no es así al correrlo lo indicará
assert(isinstance(m1, Clase1)) # en este caso is instance al preguntarle si m1 pertenece a Clase1 no habrá problema dado que sí pertenece.


#Creando nuestras propias excepciones

class Miexcepcion(Exception):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

try:
    raise Miexcepcion("Mensaje 1", "Mensaje2")     #de esta manera lo que hacemos es que cuando lancemos la excepción, le estamos pasando la información al manejador de excepciones
                        
except Miexcepcion as e:

    #aux = e.args[0]
    print(e.param1)
    print(e.param2)


class Miexcepcion2(Exception):
    pass #en este caso como no hemos declarao atributos, pasamos en forma de diccionarios los mensajes que queremos:

try:
    raise Miexcepcion2({"m1":"Mensaje 1", "m2":"Mensaje2"})     #de esta manera lo que hacemos es que cuando lancemos la excepción, le estamos pasando la información al manejador de excepciones
                        
except Miexcepcion2 as e:

    aux = args[0]
    print(aux["m1"])
    print(aux["m2"])










