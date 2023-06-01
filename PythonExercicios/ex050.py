#Desafio 050 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contador = 0
for c in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Você informou {} números pares e a soma deles foi {}.'.format(contador, soma))