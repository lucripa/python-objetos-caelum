'''#exercicios 4.5
#1

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print(lista)

#a
print(max(lista))

#b
print(min(lista))

#c
for elemento in lista:
    if((elemento % 2) == 0):
        print('Numero par: {}'.format(elemento))

#d
print('ocorrencia: {}'.format(lista.count(12)))

#teste
print('len: ', len(lista))

#e
soma = 0
for elemento in lista:
    soma += elemento
media = soma / len(lista)
print('media: ', media)

#f
soma_negativa = 0
for elemento in lista:
    if(elemento < 0):
        soma_negativa += elemento
print('soma negativo: ', soma_negativa)

#2
nome = str(input('Informe seu primeiro nome: '))
sobrenome = str(input('Informe seu sobrenome: '))
idade = int(input('Informe sua idade: '))

usuario = [nome, sobrenome, idade]

print(usuario)

#3
nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))
nota3 = int(input('Informe a terceira nota: '))
nota4 = int(input('Informe a quarta nota: '))

lista_notas = [nota1, nota2, nota3, nota4]
media = (nota1 + nota2 + nota3 + nota4) / 4
print('As notas são: {} e a media é: {}'.format(lista_notas, media))

#teste soma nehativa em uma unica linha + impressao
somas_negativas = sum(negativo for negativo in lista if negativo < 0)
print('soma negativa 2: ', somas_negativas)

soma_lista = sum(positivo for positivo in lista)
#media = soma_lista / len(lista)
print('soma da lista {}'.format(soma_lista))
print('Media: {}'.format(soma_lista / len(lista)))

#4
nome_usuario = str(input('Informe seu nome: '))
idade_usuario = int(input('Informe sua idade: '))
cidade_usuario = str(input('Informe sua cidade: '))

dict_usuario = {'nome': nome_usuario, 'idade': idade_usuario, 'cidade': [cidade_usuario]}

for chave, valor in dict_usuario.items():
    print('{}: {}'.format(chave, valor))'''

def velocidade_media(distancia, tempo):
    pass
    velocidade = distancia/tempo
    print('Velocidade media: {}'.format(velocidade))

velocidade_media(100, 20)
velocidade_media(150, 22)
velocidade_media(200, 30)
velocidade_media(50, 3)
