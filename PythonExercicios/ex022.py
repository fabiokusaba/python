#Desafio 022 Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas,
#O nome com todas minúsculas,
#Quantas letras ao todo(sem considerar espaços),
#Quantas letras tem o primeiro nome.

nome_completo = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'O seu nome em letras maiúsculas é {nome_completo.upper()}.')
print(f'O seu nome em letras minúsculas é {nome_completo.lower()}.')
print('O seu nome tem {} caracteres.'.format(len(nome_completo) - nome_completo.count(' '))) #tirando o espaço entre o nome e o sobrenome
primeiro_nome = nome_completo.split()
print(f'O seu primeiro nome tem {len(primeiro_nome[0])} caracteres.')

#Resolução professor
#Outra opção para saber a quantidade de letras do primeiro nome
print('O seu primeiro nome tem {}.'.format(nome_completo.find(' ')))