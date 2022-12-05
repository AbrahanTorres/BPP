from wallet import Wallet, InsuficienteSaldo
import pytest

#para usar el tester es importante para cada función iniciar con la palabra test_

def test_cantidad_inicial():
    mi_wall = Wallet()
    assert mi_wall.saldo == 0

def test_inicializar_con_valor():
    mi_wall = Wallet(100)
    assert mi_wall.saldo == 100

def test_gastar():
    mi_wall = Wallet(100)
    mi_wall.gastar_dinero(50)
    assert mi_wall.saldo == 50

def test_anadir():
    mi_wall = Wallet(100)
    mi_wall.anadir_saldo(50)
    assert mi_wall.saldo == 150

def test_exception():
    mi_wall = Wallet(100) #si en la wallet tenemos 100, y queremos gastar  150, saldrá el error InsuficienteSaldo
    with pytest.raises(InsuficienteSaldo):
        mi_wall.gastar_dinero(150)
    

