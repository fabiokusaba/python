#Desafio 058 Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
palpite = 1
print('Olá, sou o seu computador. Será que você consegue adivinhar o número que eu pensei entre 0 e 10?')
jogador = int(input('Escolha um número: '))
while computador != jogador:
    palpite += 1
    if computador > jogador:
        jogador = int(input('Escolha um número maior: '))
    if computador < jogador:
        jogador = int(input('Escolha um número menor: '))
print('Parabéns você venceu! Foram necessários {} tentativas.'.format(palpite))

#Resolução professor
#Criou uma variável acertou que recebeu False.
#Criou uma variável palpite que vai ser o nosso contador de palpites que inicia no 0.
#Usou while com a seguinte lógica enquanto não acertar o programa continua perguntando o palpite do usuário.
#Uma vez que o usuário acerte a variável acertou recebe True e com isso nosso jogo é finalizado.
'''palpite = 0
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Errou, tente um número menor.')
        elif jogador < computador:
            print('Errou, tente um número maior.')
print('Parabéns! Você acertou depois de {} tentativas.'.format(palpite))'''