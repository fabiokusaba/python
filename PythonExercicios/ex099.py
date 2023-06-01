#Desafio 099 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* num):
    cont = maior = 0 #Variáveis para descobrir o maior valor.
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num: #Usando for para varrer os valores de num.
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0: #Verificando o maior valor.
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()