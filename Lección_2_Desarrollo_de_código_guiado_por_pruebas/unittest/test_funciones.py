#instalamos la librería de test unittest con: python -m pip install unittest2
# para ejecutar el test desde la consola: python -m unittest -v test_funciones.py
import unittest
from funciones import calcularMedia

#Usando unittest será necesario crear una clase de la siguiente manera:

class TestMedia(unittest.TestCase):

    def test1(self):
        resultado = calcularMedia([20, 20, 20])
        self.assertEqual(resultado, 20)  #unittest tiene assert predefinidos