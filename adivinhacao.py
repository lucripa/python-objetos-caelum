print('***********************')
print('* Jogo da adivinhação *')
print('***********************')

numero_secreto = 42
total_de_tentativas = 3
#rodada = 1

#while( rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite um número inteiro: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Você acertou, PARABENS!')
        break
    elif (maior):
        print('numero errado, vc informou um numero MAIOR que o numero secreto.')
    elif (menor):
        print('numero errado, vc informou um numero MENOR que o numero secreto.')

    #rodada += 1

print('Fim de jogo.')
