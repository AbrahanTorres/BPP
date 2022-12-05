
num = int(input("Introduce un valor: "))

assert type(num) == int,"debe ingresar un número entero"

class Miexcepcion(Exception):
    def __init__(self, param):
        self.param = param

try:
    if num > 10:
        raise Miexcepcion("Por favor ingrese un número menor o igual a 10")    

except Miexcepcion as e:

    print(e.param)


