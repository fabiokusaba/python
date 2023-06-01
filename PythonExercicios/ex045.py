#Desafio 045 Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
#Índices    0        1         2
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
#Fazendo interação JO KEN PÔ
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
#Fazendo uma linha como forma de separação
print('-=' * 15)
#Passando o número inteiro que o jogador escolheu como índice dos itens -> itens[jogador]
print('O jogador jogou {}.'.format(itens[jogador]))
#Passando o número inteiro que o computador escolheu como índice dos itens -> itens[computador]
print('O computador jogou {}.'.format(itens[computador]))
print('-=' * 15) #Linha de separação
#Jogadas do computador
if computador == 0: #Pedra
    #Jogadas do jogador
    if jogador == 0: #Pedra
        print('EMPATE!')
    elif jogador == 1: #Papel
        print('JOGADOR VENCEU!')
    elif jogador == 2: #Tesoura
        print('COMPUTADOR VENCEU!')
    else: #Não preencheu nenhuma das condições acima
        print('Jogada inválida!')
elif computador == 1: #Papel
        #Jogadas do jogador
    if jogador == 0: #Pedra
        print('COMPUTADOR VENCEU!')
    elif jogador == 1: #Papel
        print('EMPATE!')
    elif jogador == 2: #Tesoura
        print('JOGADOR VENCEU!')
    else: #Não preencheu nenhuma das condições acima
        print('Jogada inválida!')
elif computador == 2: #Tesoura
        #Jogadas do jogador
    if jogador == 0: #Pedra
        print('JOGADOR VENCEU!')
    elif jogador == 1: #Papel
        print('COMPUTADOR VENCEU!')
    elif jogador == 2: #Tesoura
        print('EMPATE!')
    else: #Não preencheu nenhuma das condições acima
        print('Jogada inválida!')

