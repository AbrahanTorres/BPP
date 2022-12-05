from actividad_pytest import *
import pytest

#Función suma
def test_suma():
    assert suma(2, 2) == 4

#pytest nos permite usar decoradores, en este ejemplo para asignar multiples parametros en el test.
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (3,2,5),
        (2,3,5),
        (suma(3, 2), 5, 10),
        (3, suma(2, 5), 10)
    ]
)
def test_suma_multiple(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected


#Función resta
def test_resta():
    assert resta(5, 5) == 0
    
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (3,2,1),
        (4,3,1),
        (resta(3, 2), 5, -4),
        (3, resta(5, 2), 0)
    ]
)
def test_resta_multiple(input_a, input_b, expected):
    assert resta(input_a, input_b) == expected

#Función multiplicacion

def test_multiplicacion():
    assert multiplicacion(5, 5) == 25
    
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (3,2,6),
        (4,3,12),
        (multiplicacion(3, 2), 5, 30),
        (3, multiplicacion(5, 2), 30)
    ]
)
def test_multiplicacion_multiple(input_a, input_b, expected):
    assert multiplicacion(input_a, input_b) == expected

#Función division
def test_division():
    assert division(5, 5) == 1
    
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (3,2,1.5),
        (4,3,1.33),
    ]
)
def test_division_multiple(input_a, input_b, expected):
    assert division(input_a, input_b) == expected

#Función escribir

def test_temporary_folder(tmpdir):  #tmpdir para crear un directorio temporal, para el test.
    data_in = "CodingAbrahan"
    fpath = f"{tmpdir}/test.txt"
    escribir(fpath, data_in)

    with open(fpath) as file_out:
        data_out = file_out.read()

    assert data_in == data_out
