def espar(x):
    return x%2 == 0

lista = [3, 4, 8, 5, 5, 22, 13]

resultado = list(filter(espar, lista))
print(resultado)