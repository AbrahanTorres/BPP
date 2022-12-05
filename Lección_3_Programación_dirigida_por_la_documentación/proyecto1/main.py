# Librería para crear documentación: pip install pip install sphinx   
#Una vez instalada nos situamos en la carpeta docs, y lanzamos un asistente que nos
#va a permitir inicializar el proyecto con el siguiente comando: sphinx-quickstart 
#se siguen los pasos, luego, de la carpeta doc que estaba vacía, ahora se tendrán ficheros.
#Añadimos extensiones al archivo  doc/source/conf.py: https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365
# pegando lo siguiente: extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon']
#El siguiente paso es usar el comando en la terminal en doc: make html 
#Luego de correr el anterior comando, en doc/bulid se habrá creado más archivos que no estaban.

# Luego volvemos al website y copiamos lo siguiente y lo pegamos en index.rst debajo de conf.py
#.. automodule:: my_project.main
#    :members:
#Lo anterior es para agregar de manera manual los ficheros.
#Si queremos que la librearía los vaya añadiendo o creando automáticamente usamos el comando: sphinx-apidoc -o source ../proyecto1/ 
#Este comando nos creará un archivo nuevo por cada uno de los ficheros que teníamos en la otra carpeta, en proyect1. Si vemos nos ha creado
#main.rst y modules.rst, ese nombre de modules que se ha autogenerado, es el que usaremos en index.rst para que los vaya agregando de manera automática al index.


#Luego si queremos cambiar el tema: https://betterprogramming.pub/auto-documenting-a-python-project-using-sphinx-8878f9ddc6e9
# Instalamos el paquete: pip install sphinx-rtd-theme
# y en conf.py vamos a html_theme y cambiamos el alabaster por sphinx_rtd_theme


#Para visualización en index.rst el lenguaje especialziado: https://pythonhosted.org/an_example_pypi_project/sphinx.html

# más información: https://www.datacamp.com/tutorial/docstrings-python


def some_function(argument1):
    """Sumamary or Description of the Function
    
    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int: Returning value
   
    """

    return argument1

print(some_function.__doc__)