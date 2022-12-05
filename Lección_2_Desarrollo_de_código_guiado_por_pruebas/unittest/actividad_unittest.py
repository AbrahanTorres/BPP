def calcularMedia(*args):
    return(sum(*args)/len(*args))

def suma(x, y):
    
    return x + y

def resta(x, y):

    return x - y

def mul(x, y):

    return x * y

def power(x, y):

    return pow(x, y)


def escribir(fpath, data_in):
    '''
    Funcion que escribe en un archivo
    Args:
        fpath: path del archivo
        data_in: información a escribir
    '''

    with open(fpath, "w") as file_in:
        file_in.write(data_in)