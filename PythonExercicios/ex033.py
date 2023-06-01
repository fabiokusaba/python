#Desafio 033 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite seu primeiro número: '))
b = int(input('Digite seu segundo número: '))
c = int(input('Digite seu terceiro número: '))
#Para resolver esse desafio eu posso pensar em um número como sendo o menor e fazendo as condições com os demais, assim:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Para mostrarmos o maior vamos utilizar da mesma lógica feita com o menor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}.'.format(maior))
print('O menor valor digitado foi {}.'.format(menor))