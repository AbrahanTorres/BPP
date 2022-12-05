def suma(x, y):

    '''
Funcion que toma 2 argumentos y devuelve la suma de los mismos
Args:
    x (int/float): Primer valor a sumar
    y (int/float): Segundo valor a sumar
return: x+y
    '''
    return x + y

def resta(x, y):

    return x-y

def multiplicacion(x, y):

    return x*y

def division(x, y):

    return round(x / y, 2)

def escribir(fpath, data_in):
    '''
    Funcion que escribe en un archivo
    Args:
        fpath: path del archivo
        data_in: información a escribir
    '''

    with open(fpath, "w") as file_in:
        file_in.write(data_in)
