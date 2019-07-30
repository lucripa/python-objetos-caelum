from conta import *
from cliente import *

cliente = Cliente('Maria', 'Santos', '123-4')

conta = Conta('1234', Cliente, 12000.0)

print('Teste chamando atributo por atributo')
print(conta.numero)
print(conta.titular)
print(conta.saldo)
print(conta.limite)

print('\nTeste chamando por atributo extrato')
conta.extrato()