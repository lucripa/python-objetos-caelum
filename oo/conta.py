from cliente import *

class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def deposita (self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True

    def extrato(self):
        print('Numero: {}\nTitular: {}\nSaldo: {}\nLimite: {}'.format(self.numero, self.titular, self.saldo, self.limite))