#Desafio 060 Faça um programa que leia um número qualquer e mostre seu fatorial.
#Ex: 5!= 5 x 4 x 3 x 2 x 1 = 120
#Resolvendo o desafio utilizando o módulo factorial.
'''from math import factorial
num = int(input('Digite um número para calcular o seu Fatorial: '))
fatorial = factorial(num)
print('O fatorial de !{} é {}.'.format(num, fatorial))'''

#Resolvendo o desafio utilizando while.
#Primeiro vamos criar a nossa variável c (contador) que vai receber o nosso número lido.
#Enquanto o contador for maior que 0 porque ele vai até o 1.
#Vou escrever meu contador como c -= 1
#Vou criar uma variável f para simbolizar o meu fatorial e ela vai começar com 1 já que o meu fator nulo de multiplicação é 1.
#O fator nulo de soma e subtração é 0. Por exemplo: se eu somo qualquer coisa e eu quero que a minha soma seja limpa eu tenho que começar com 0.
#Se eu for começar uma multiplicação limpa eu não posso começar com 0 porque qualquer coisa multiplicado por 0 dá 0.
#Então sempre que eu for trabalhar com fatorial ou com qualquer multiplicação e eu quero que ela fique limpa, ou seja, eu multiplico um número por qualquer outro e ele se mantém é 1.
#Para calcular o meu fatorial basta eu escrever antes do meu c -= 1 o meu f *= c
'''numero = int(input('Digite um número para calcular o seu Fatorial: '))
c = numero
f = 1
print('Calculando {}!'.format(numero))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

#Resolvendo o desafio utilizando o for
f = 1
numero = int(input('Digite o número para calcular o seu Fatorial: '))
for c in range(numero, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))
