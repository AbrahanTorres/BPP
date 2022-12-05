def calcularMedia(*args):
    '''
    Funcion que puede recibir varios argumentos para calcular el promedio.
    
    Args: 
        args (int): números enteros.

    Returns: 
        media: retorna el promedio. 
    '''
    return(sum(*args)/len(*args))


def escribir(fpath, data_in):
    '''
    Funcion que escribe en un archivo.

    Args:
        fpath (str): path del archivo.
        data_in (str): información a escribir.
    '''

    with open(fpath, "w") as file_in:
        file_in.write(data_in)

print(calcularMedia.__doc__)
print(escribir.__doc__)