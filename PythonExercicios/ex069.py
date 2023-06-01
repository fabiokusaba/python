#Desafio 069 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A)Quantas pessoas tem mais de 18 anos.
#B)Quantos homens foram cadastrados.
#C)Quantas mulheres tem menos de 20 anos.
maior18 = sexomasc = mulheres20 = 0

while True:
    print('CADASTRO PESSOA')
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        sexomasc += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'Total de pessoas com 18 anos ou mais: {maior18}.')
print(f'Total de homens cadastrados: {sexomasc}.')
print(f'Total de mulheres com menos de 20 anos: {mulheres20}.')
