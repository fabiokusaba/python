#Desafio 064 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = 0
num_digitados = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        num_digitados += 1
print('Você digitou {} números.'.format(num_digitados))
print('A soma de todos os números digitados desconsiderando 999 é {}.'.format(soma))

#Resolução do professor
#Uma outra forma de solucionar esse desafio seria da seguinte forma:
#Perceba que aqui passamos duas vezes o comando num, uma dentro de while no final e outra fora.
'''Código abaixo:
num = contador = soma = 0
num = int(input('Digite um número [999 para parar] '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(contador, soma))
'''