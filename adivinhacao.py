print('***********************')
print('* Jogo da adivinhação *')
print('***********************')

numero_secreto = 42
numero_de_tentativas = 3
nao_acertou = True

while(numero_de_tentativas > 0 and nao_acertou):
    chute = int(input('Digite um número inteiro: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Você acertou, PARABENS!')
        nao_acertou = False
    elif (maior):
        print('numero errado, vc informou um numero MAIOR que o numero secreto.')
    elif (menor):
        print('numero errado, vc informou um numero MENOR que o numero secreto.')
    
    numero_de_tentativas -= 1

print('Fim de jogo.')
