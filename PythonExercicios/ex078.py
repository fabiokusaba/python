#Desafio 078 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
listanum = []
for cont in range(0, 5):
    listanum.append(int(input('Digite um número: ')))
print(f'O maior valor digitado foi {max(listanum)} na posição {listanum.index(max(listanum))}')
print(f'O menor valor digitado foi {min(listanum)} na posição {listanum.index(min(listanum))}')

#Resolução Professor:
#Para descobrirmos o maior e menor valor digitados vamos criar uma variável maior e uma variável menor.
#Agora para fazer a verificação eu posso verificar da seguinte maneira: se for o primeiro valor lido, logo este será o meu maior e menor valor. E para eu me referir ao primeiro valor eu posso falar que se o meu c for igual a 0.
#Agora se não for eu preciso verificar novamente, se o valor que eu acabei de ler for maior que o maior valor, logo ele passará a ser o maior valor e para o menor valor eu parto do mesmo raciocínio.
#Para sabermos a posição que se encontra o nosso maior e menor valor vamos precisar varrer a nossa lista inteira e podemos fazer isso utilizando for com enumerate().
#Vou verificar que se o valor for igual ao maior eu quero que ele me printe o índice dele.
listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()