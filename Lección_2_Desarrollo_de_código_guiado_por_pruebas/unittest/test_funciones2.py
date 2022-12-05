#el nombre de la clase siempre debe ser Test<loquequedamos>
import unittest
from funciones import calcularMedia

'''
.assertEqual(a, b): Verifica la igualdad de ambos valores.
.assertTrue(x): verifica que el valor es True.
.assertFalse(x): verifica que el valor es False.
.assertIs(a,b): verifica que ambas variables son la misma (ver operador is).
.assertIsNone(x): verifica que el valor es None.
.assertIn(a,b): verifica que a pertenece al iterable b (ver operador in).
.assertIsInstance(a,b): verifica que a es una instancia de b
.assertRaises(x): verifica que se lanza una excepción.

'''
class TestMedia(unittest.TestCase):

    def setUp(self):  #al principio test, siempre por cada test se abrirá, por cada función de test. por ejemplo podemos abrir un fichero en el setUp.
        print("Entrando en setUp")
    
    def tearDown(self):  # al final del test, siempre por cada test se cerrará, por cada función de test.  Por ejemplo podemos cerrar un fichero en el tearDown.
        print("Entrando en tearDown")

    #El nombre del método debe de ser test_<loquesea>
    def test_1(self):
        print("Dentro de test1")
        resultado = calcularMedia([20,20,20])
        self.assertEqual(resultado,20)

    def test_2(self):
        resultado = calcularMedia([20,30,20]) # en este buscamos que falle para ver como muestra el error
        self.assertEqual(resultado,20)

    def test_in(self):
        self.assertIn(1,[1,3,4]) #aquí decimos que 1 está contenido en la lista de [1,3,4]

    def test_excepcion(self):
        with self.assertRaises(ZeroDivisionError):
            x = 0/0