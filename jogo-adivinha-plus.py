print('***********************')
print('* Jogo da adivinhação *')
print('***********************')

numero_secreto = 42
chute = input('Digite um numero de 0 a 100: ')
if chute.isnumeric(): 
    chute = int(chute)     
    if (chute == numero_secreto):
        print('Você acertou, PARABENS!')
    elif:
        print('Você errou! O numero secreto é maior...')
else:
    print('Informe somente numeros inteiros')