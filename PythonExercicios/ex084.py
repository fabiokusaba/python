#Desafio 084 Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista. No final, mostre:
#A)Quantas pessoas foram cadastradas.
#B)Uma listagem com as pessoas mais pesadas.
#C)Uma listagem com as pessoas mais leves.
#Para resolver esse desafio vou criar uma lista temporária onde os dados irão antes de ir para a lista principal.
#Vamos fazer um loop infinito utilizando while True para ler os dados temporários nome e peso.
#Para eu saber qual é a pessoa mais pesada e qual é a pessoa mais leve eu tenho que saber qual é o maior e menor peso.
#Para isso vamos criar duas variáveis maior e menor que vão receber 0.
#Agora vou fazer que se o len(pessoas) que é a minha lista principal for igual a 0 significa que eu não cadastrei ninguém ainda e se eu não coloquei nada significa que o meu maior é a mesma coisa que o meu menor que é a mesma coisa que dados[1] na posição 1 que é o meu peso.
#Para fazermos uma listagem de pessoas mais pesadas e uma listagem de pessoas mais leves vamos utilizar o for each para varrer cada pessoa da nossa lista.
#Agora eu faço uma verificação que se pessoa[1] que é o meu peso for igual ao maior (refere-se ao maior peso) eu faço um print com o nome deles. O mesmo se repete para o menor.
pessoas = list() #Lista principal
dados = list() #Lista temporária
menor = maior = 0
while True: #Loop infinito
    dados.append(str(input('Nome: '))) #Dado nome temporário
    dados.append(float(input('Peso kg: '))) #Dado peso temporário
    #Verificando o maior e menor peso.
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:]) #Criando uma cópia da nossa lista temporária na nossa lista principal.
    dados.clear() #Depois que eu der o .append() na minha lista principal eu preciso limpar a minha lista temporária.
    #Perguntando ao usuário se ele deseja continuar ou não.
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
#Listagem da pessoa com maior peso utilizando for.
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'{[pessoa[0]]} ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
#Listagem da pessoa com menor peso utilizando for.
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'{[pessoa[0]]} ', end='')