#Desafio 054 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#Considere a maioridade com 21 anos.
from datetime import date
ano = date.today().year
maioridade = 0
menoridade = 0
for pessoa in range(1, 8):
    nascimento = int(input('Ano de nascimento da {}ª pessoa? '.format(pessoa)))
    idade = ano - nascimento
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print('Existem {} pessoas maiores de 21 anos e que atingiram a maioridade.'.format(maioridade))
print('Existem {} pessoas com menos de 21 anos e que ainda não atingiram a maioridade.'.format(menoridade))