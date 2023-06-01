#Desafio 088 Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar qantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
#Como eu quero sortear números para um jogo da MEGA SENA eu não posso sortear números repetidos, por exemplo sortear 5 e depois sortear o 5 de novo e para que isso não ocorra eu preciso fazer uma verificação.
#Então vou criar uma variável sortear para sortear números de 1 a 60 e vou criar uma variável cont que vai receber de início 0, sendo que essa minha variável que irá sortear os números vai estar dentro de um loop infinito while True.
#Agora eu vou verificar se esse número que eu acabei de sortear não está dentro da minha lista e se ele não estiver eu vou adicionar ele. E se ele for adicionado eu faço cont += 1.
#Logo abaixo eu vou verificar se o meu cont (contador) for maior ou igual a 6 e isso quer dizer que ele já sorteou 6 números e dou um break.
#Agora eu preciso perguntar a quantidade de jogos que o usuário deseja e pra isso vou criar uma variável qnt onde vai receber um input com essa pergunta.
#Vou ter uma variável total que vai ser o total de vezes que ele vai sortear e de início ela vai começar com 0.
#Daí vou criar um equanto dizendo o seguinte: enquanto o total for menor ou igual a quantidade vou continuar sorteando os números e fazendo mais jogos.
#A cada vez que eu sortear eu vou criar uma outra lista chamada jogos que vai fazer uma cópia da minha lista e depois que eu fizer uma cópia eu apago a minha lista.
#Agora eu vou fazer um for para cada elemento da minha lista de jogos
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 30)
print('                    JOGOS DA MEGA SENA                    ')
print('-=' * 30)
qnt = int(input('Quantos jogos deseja fazer? '))
total = 1
while total <= qnt:
    cont = 0
    while True:
        sortear = randint(1, 60)
        if sortear not in lista:
            lista.append(sortear)
            cont += 1
        if cont >= 6:
            break
    lista.sort() #Colocando os números sorteados em ordem.
    jogos.append(lista[:]) #Fazendo uma cópia de lista.
    lista.clear() #Apagando a lista após ter feito uma cópia.
    total += 1
print('-=' * 3, f'SORTEANDO {qnt} JOGOS', '-=' * 3)
#Fazendo um for para cada elemento da lista jogos
for index, lista in enumerate(jogos):
    print(f'Jogo {index+1}: {lista}')
    sleep(2)
print('-=' * 5, 'BOA SORTE!', '-=' * 5)


