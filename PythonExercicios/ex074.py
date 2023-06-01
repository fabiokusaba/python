#Desafio 074 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
#Para randomizar 5 números e colocar dentro de uma tupla basta que eu utilize os parêntesis e copie o meu código 5 vezes.
#Para saber qual é o maior valor eu posso utilizar o método específico das tuplas que é o max(), de forma similar para eu descobrir o menor valor eu posso utilizar min().
#Utilizando \n para pular para a próxima linha.
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')