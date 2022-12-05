# installar en el enviroment pytest: python -m pip install pytest   o  pip install pytest  
# para correr desde la terminal:  python -m pytest test_capitalize.py

#el nombre del script que contiene los test debe de empezar con test_<loquesea>.py
def capital(x):
    return x.capitalize()

#definir nuestro test
#el nombre de la funcion debe de comenzar con text_<loquesea>

def test_capital():
    assert capital("Hola") == "Hola"

def test_capital2():
    assert capital("Hola") == "hola"







