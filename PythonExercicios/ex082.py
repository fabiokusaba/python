#Desafio 082 Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os valores digitados foram {valores}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores ímpares digitados foram {impares}')