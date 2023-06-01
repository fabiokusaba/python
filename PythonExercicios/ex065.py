#Desafio 065 Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média de todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer continuar ou não a digitar valores.
resposta = 'S'
soma = 0
contador = 0
maior = 0
menor = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if contador == 1: #Como meu contador está no primeiro número estou partindo da lógica de que ele será o meu maior e menor número.
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / contador
print('Você digitou {} números e a média foi {}.'.format(contador, media))
print('A soma de todos os números que você digitou é {}.'.format(soma))
print('O maior número é {} e o menor número é {}.'.format(maior, menor))