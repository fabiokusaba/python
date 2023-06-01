#Desafio 059 Crie um programa que leia dois números e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] saber o maior valor
#[4] adicionar novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
menu = 0
while menu != 5:
    print('''Menu de Opções:
        [1] Somar
        [2] Multiplicar
        [3] Maior valor
        [4] Novos números
        [5] Sair do programa''')
    menu = int(input('Digite a sua opção: '))
    if menu == 1:
        print('O valor de {} + {} é {}.'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('O valor de {} x {} é {}.'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}.'.format(n1, n2, maior))
    elif menu == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif menu == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Volte sempre!')