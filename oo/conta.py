from cliente import *

class Conta:

    _total_conta = 0

    __slots__ = ('_saldo', '_titular', '_limite', '_numero')

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        Conta._total_conta += 1

    def deposita (self, valor):
        self._saldo += valor
    
    def saca(self, valor):
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True

    def extrato(self):
        print('Numero: {}\nTitular: {}\nSaldo: {}\nLimite: {}'.format(self._numero, self._titular, self._saldo, self._limite))
    

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @classmethod
    def get_total_contas(cls):
        return cls._total_conta