#Desafio 098 Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
#Seu programa tem que realizar três contagens através da função criada:
#A)De 1 até 10, de 1 em 1
#B)De 10 até 0, de 2 em 2
#C)Uma contagem personalizada
from time import sleep
def contador(inicio, fim, passo):
    #Teste lógico para validar o passo zerado e passo negativo.
    if passo < 0:
        passo *= -1 #Estou transformando o passo menor de 0, que seria negativo, em positivo.
    if passo == 0:
        passo = 1 #Se o passo for 0 eu vou fazer com que ele assuma um valor padrão de 1.
    
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}.')
    sleep(2)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True) #Desativa o buffer de tela
            sleep(0.5)
            cont += passo
    if inicio > fim:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True) #Desativa o buffer de tela
            sleep(0.5)
            cont -= passo
    print('FIM!')
    print('-=' * 20)


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)