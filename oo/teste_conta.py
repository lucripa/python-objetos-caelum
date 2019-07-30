def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    if conta['saldo'] >= valor:
        conta['saldo'] -= valor
        return True
    else:
        return False    
    
def extrato(conta):
    print('nuemero: {}\nvalor: {}'.format(conta['numero'], conta['saldo']))