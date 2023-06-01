#Desafio 028 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
numero_aleatorio = randint(0, 5)
numero_escolhido = int(input('Você consegue adivinhar um número aleatório entre 0 e 5? Digite seu palpite: '))
if numero_aleatorio == numero_escolhido:
    print('PARABÉNS! Você venceu!')
else:
    print('O número aleatório era {}, tente novamente.'.format(numero_aleatorio))

#Resolução professor
#Importando de time o método sleep para fazer com que o programa espere um tempo para depois continuar executando.