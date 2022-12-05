# para ejecutar el test desde la terminal: python -m unittest -v test_actividad_unittest.py
import unittest
import tempfile
from actividad_unittest import *

class Test(unittest.TestCase):

    def setup(self):
        print("Entrando en setUp")

    def tearDown(self):  
        print("Entrando en tearDown")

    def test_media(self):
        print("Dentro de test1")
        resultado = calcularMedia([20,20,20])
        self.assertEqual(resultado,20)
    
    def test_suma(self):
        resultado = suma(20, 25)
        self.assertEqual(resultado, 45)

    def test_resta(self):
        resultado = resta(20, 25)
        self.assertEqual(resultado, -5)

    def test_multiplicacion(self):
        resultado = mul(3, 3)
        self.assertEqual(resultado, 9)

    def test_power(self):
        resultado = power(3, 3)
        self.assertEqual(resultado, 27)

    def test_temporary_folder(self):
        tmpdir = tempfile.gettempdir()  #tmpdir para crear un directorio temporal, para el test.
        data_in = "CodingAbrahan"
        fpath = f"{tmpdir}/test.txt"
        escribir(fpath, data_in)

        with open(fpath) as file_out:
            data_out = file_out.read()

        self.assertEqual(data_in, data_out)
