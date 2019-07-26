import random

def jogar():

    print('*****************')
    print('* Jogo da Froca *')
    print('*****************')

    print('\nVocê tem 7 tentativas para sair da forca!\n')
    
    arquivo = open('palavra.txt', 'r')

    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    letra_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 1

    while(not enforcou and not acertou):

        chute = input('Qual a letra: ')
        chute = chute.strip().upper()

        if(chute.upper() in palavra_secreta.upper()):
            posicao = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letra_acertadas[posicao] = letra.upper()
                
            
                posicao += 1

        else:
            erros += 1
            print('\nTentativa {}'.format(tentativas))
            tentativas += 1

        print(letra_acertadas, end='\n\n')

        acertou = '_' not in letra_acertadas
        enforcou = erros == 7

        if(acertou ):
            print('PARABENS! Você ganhou!')
            break
        elif(enforcou):
            break
    print('Fim do jogo.')

    #for posicao in range(0, len(texto))
