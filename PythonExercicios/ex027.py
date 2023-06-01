#Desafio 027 Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza.
#primeiro = Ana
#último = Souza
digite_nome = str(input('Digite seu nome completo: ')).strip()
nome = digite_nome.split()
print('O seu primeiro nome é {}.'. format(nome[0]))
print('O seu último nome é {}.'.format(nome[len(nome) - 1]))