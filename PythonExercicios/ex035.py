#Desafio 035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas informadas FORMAM um triângulo.')
else:
    print('As retas informadas NÃO FORMAM um triângulo.')
