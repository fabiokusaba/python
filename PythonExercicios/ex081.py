#Desafio 081 Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A)Quantos números foram digitados.
#B)A lista de valores, ordenada de forma decrescente.
#C)Se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'Foram digitados {len(valores)} números.')
valores.sort(reverse=True)
print(f'A lista de valores ordenada de forma decrescente é {valores}')
if 5 in valores:
    print('O número 5 está na lista.')
else:
    print('Não existe o número 5 na lista.')
    