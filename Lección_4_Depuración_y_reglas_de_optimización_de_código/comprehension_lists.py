#Los list comprenhensions permiten crear una lista de elementos en una sola línea de código.

cuadros = []

#la manera normal de hacer un for:
for i in range(10):
    cuadros.append(i**2)

#la manera usando list comprenhensions
cuadros1 = [i**2 for i in range(10)]


print(cuadros)
print(cuadros1)

#sysntaxis del list comprehensions:
# lista = [ expresión for elemento in iterable]

#también podemos llamar a funciones dentro del list comprehensinos:
def elevar2(i):
    return i**2

cuadros1 = [elevar2(i) for i in range(10)]

#podemos agregarle condiiones
# lista = [ expresión for elemento in iterable if condición]

frase = "Hola Mundo"

letras_o = [i for i in frase if i == "o"] # if

letras_o = [i if i == "o" else "-" for i in frase]  # if - else

print(letras_o)

# comprenhension set

letras_o = {i for i in frase }
print(letras_o)

#comprehension diccionarios
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]

mi_dict1 = {i:j for i, j in zip(l1, l2)}
print(mi_dict1)

#lambda, tipo de funciones anonimas, que se definen en una línea
def suma(a, b):
    return a+b

suma1 = lambda a,b : a+b

print(suma(2,3))
print(suma1(2,3))

#función  map, filter, y reduce
#vienen de un paradigma llamado programación funcional
#Se basa en el uso de funciones principalmente.

#map
#
#map (funcion_a_aplicar, iterable)

lista = [1, 2, 3, 4, 5]

def suma_mas2(x):
    return x+2

resultado = map(suma_mas2, lista) #map nos sirve para que para cada uno de los elementos de la lista se le aplica la función suma_mas2

resultado = map(lambda x: x+2, lista) #también se podría haber hecho de esta manera para no usar una función.

#filer
#filter (funcion_a_aplicar, iterable)
#El filter filtra una lista y nos dice si el elemento es true o false.
# por ejemeplo, en este caso verifica si el modulo 2 de cada uno de los elementos de la lista es igual a cero o no, entonces dará true o false.
def espar(x):
    return x%2 == 0

resultado = filter(espar, lista)

resultado = filter(lambda x : x%2 ==0, lista)#también podemos hacerlo de la siguiente forma con un lambda

#reduce
# nos permite hacer la sumatoria de un elemento
from functools import reduce

suma = reduce(lambda a,b: a+b, lista)

#Ya no es necesario hacerlo de esta manera porque la sumatoria viene en el core de python

suma = sum(lista)




























