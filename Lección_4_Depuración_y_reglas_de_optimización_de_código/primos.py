def es_primo(n):
    primo  = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo


lista = [3, 4, 8, 5, 5, 22, 13]

resultado = list(filter(es_primo, lista)) 
print(resultado)