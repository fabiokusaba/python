#Desafio 094 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A)Quantas pessoas foram cadastradas
#B)A média de idade do grupo
#C)Uma lista com todas as mulheres
#D)Uma lista com todas as pessoas com idade acima da média
dados = dict()
pessoas = list()
soma = média = 0 #Variáveis para o cálculo da soma de idade e média.
#Leitura dos dados.
while True: 
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while dados['sexo'] not in 'MmFf':
        dados['sexo'] = str(input('ERROR! Digite o sexo [M/F] novamente: ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade'] #Calculando a soma das idades
    pessoas.append(dados.copy())
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('ERROR! Digite [S/N] para continuar: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
#Análise dos dados lidos.
print(f'Foram cadastradas {len(pessoas)} pessoas.')
média = soma / len(pessoas) #Calculando a média de idade.
print(f'A média de idade é de {média:.2f} anos.')
print(f'O total de mulheres cadastradas foram ', end='')
for p in pessoas: #Verificando o total de mulheres cadastradas.
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão com a idade acima da média: ', end='')
for p in pessoas: #Verificando as pessoas com idade acima da média.
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items(): #Listagem das pessoas com idade acima da média.
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO!')