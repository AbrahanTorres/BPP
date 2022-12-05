class InsuficienteSaldo(Exception):
    pass

class Wallet():

    def __ini__(self, cantidad=0):
        self.saldo = cantidad

    def gastar_dinero(self, cantidad):
        if self.saldo < cantidad:
            raise InsuficienteSaldo("No hay suficiente saldo en tu cuenta")
        else:
            self.saldo -= cantidad
    
    def anadir_saldo(self, cantidad):
        self.saldo += cantidad

    