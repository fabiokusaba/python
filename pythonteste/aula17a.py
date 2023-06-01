'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
'''
valores = []
'''valores.append(5)
valores.append(9)
valores.append(4)'''
'''for v in valores:
    print(f'{v}...', end=' ')'''
#Se além do valor se eu querer o índice eu posso fazer da seguinte forma:
'''for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da Lista.')'''
#Outra coisa que você pode fazer é ler valores pelo teclado e colocar dentro da Lista.
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da Lista.')
