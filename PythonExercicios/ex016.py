#Desafio 016 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.
from math import floor
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {floor(num)}.')

#Resolução do professor
from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua parte inteira é {}.'.format(num, trunc(num)))

num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua parte inteira é {}.'.format(num, int(num)))