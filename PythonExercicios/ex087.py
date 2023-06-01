#Desafio 087 Aprimore o desafio anterior, mostrando no final:
#A)A soma de todos os valores pares digitados.
#B)A soma dos valores da terceira coluna.
#C)O maior valor da segunda linha.
#Primeiro vamos declarar as nossas variáveis para a soma dos valores pares, a soma dos valores da terceira coluna e o maior valor.
#Primeiro vamos fazer a soma dos valores pares e pra isso quando eu estiver mostrando o valor da matriz[linha][coluna] eu vou verificar antes de terminar se ele é par. E se for par, eu vou fazer a somapar receber ele mesmo mais a matriz[linha][coluna] e com isso eu consigo mostrar a soma dos valores pares.
#Para eu calcular a soma da terceira coluna eu preciso fazer um for somente da linha porque a coluna não muda. Então a somacol vai ser ela mesma mais a matriz[linha][2] na coluna 2 porque eu já fixei a coluna e o que vai variar aqui vai ser a linha que vai ser 0, 1 e 2.
#Para eu descobrir o maior valor da segunda linha eu vou utilizar a mesma linha de raciocínio do caso anterior onde somamos os valores da terceira coluna só que neste caso o que vai mudar vai ser a coluna já que a linha vai ser fixa então vou precisar fazer um for para a coluna.
somapar = somacol = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}')
for linha in range(0, 3):
    somacol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somacol}')
for coluna in range(0, 3):
    if coluna == 0: #Sinal de que estamos trabalhando com a primeira coluna
        maior = matriz[1][coluna]
    else:
        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')
