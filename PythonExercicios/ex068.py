#Desafio 068 Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
#Criamos um validador para a nossa escolha de par ou ímpar, ou seja, enquanto o usuário não escolher par ou ímpar ele vai continuar perguntando.
#Agora temos a informação se o usuário escolheu par ou ímpar então podemos pensar da seguinte forma se o usuário escolheu par e o resto da divisão do nosso resultado por 2 for igual a 0 quer dizer que o nosso usuário ganhou e daí adicionamos 1 vitória para ele, do contrário quer dizer que ele perdeu e usamos break para desviar o fluxo do nosso jogo e encerrar o programa.
#Na mesma linha de raciocínio iremos fazer com o ímpar.
#Para incrementar ainda no nosso jogo podemos fazer um print de deu PAR se o resto da divisão do resultado por 2 for igual a zero, se não deu ÍMPAR.
from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 5)
    resultado = jogador + computador
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado}.', end=' ')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if resultado % 2 == 0:
            print('Você ganhou!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if resultado % 2 == 1:
            print('VOcê ganhou!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {vitoria} vezes.')
