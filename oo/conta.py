import abc

class Conta(abc.ABC):

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self):
        return self._saldo

    @property
    def titular(self):
        return self._titular

    @property
    def numero(self):
        return self._numero

    @property
    def limite(self):
        return self._limite

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def saca(self, valor):
        if (self._saldo < 0):
            print('Saldo insuficiente')
        elif valor > self._saldo + self._limite:
            print('Saldo insuficiente')
        else:
            self._saldo -= valor


    def deposita(self, valor):
        self._saldo += valor

    def transfere(self, conta, valor):
        self.saca(valor)
        conta.deposita(valor)
    @abc.abstractclassmethod
    def atualiza(self, taxa):
        pass
        
    def extrato(self):
        print('Numero: {}\nTitular: {}\nSaldo: {}\nLimite: {}'.format(self._numero, self._titular, self._saldo, self._limite))

    def __str__(self):
        pass

class Tributavel(abc.ABC):
    """Classe que contém operações de um objeto autenticável

    As subclass concretas devem sobrescrever o método get_valor_imposto.
    """

    @abc.abstractmethod
    def get_valor_imposto(self):
        pass

class ContaCorrente(Conta, Tributavel):
    def atualiza(self, taxa):
        self._saldo += self._saldo * (2*taxa)

    def get_valor_imposto(self):
        return self._saldo * 0.01

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * (3*taxa)

class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def selic(self):
        return self._selic

    @property
    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta):
        print(conta.saldo)
        conta.atualiza(self._selic)
        print(conta.saldo)

        self._saldo_total += conta.saldo

class ContaInvestimento(Conta):
    pass


class SeguroDeVida():
    def __init__(self, valor, tiutlar, numero_apolice):
        self._valor = valor
        self._titular = tiutlar
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor *0.05


if __name__ == '__main__':
    # conta1 = Conta('123-4', 'Luiz', 1000.0, 1000.0)
    # conta2 = Conta('123-5', 'Thais', 1000.0, 1000.0)
    # print(conta1.saldo)
    #
    # conta1.deposita(100.0)
    #
    # conta1.saca(50.0)
    #
    # conta1.extrato()
    #
    # conta1.transfere(conta2, 200)

    conta = ContaCorrente('123-4', 'Luiz', 1000.0, 1000.0)

    conta.atualiza(0.1)
    print(conta.saldo)

    #c = Conta('123-4', 'Joao', 1000.0)
    cc = ContaCorrente('123-5', 'Jose', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    adc = AtualizadorDeContas(0.01)

    #adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print(cc.saldo)
    print(cp.saldo)
    print(adc.saldo_total)

ci = ContaInvestimento('123-6', 'Maria', 1000.0)