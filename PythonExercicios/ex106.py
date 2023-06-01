#Desafio 106 Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
#OBS: use cores.
#Vamos começar com o nosso programa principal vou criar uma variável chamada comando e esse comando vai começar vazio e será uma string.
#E vou fazer um loop infinito e ler esse comando.
#Vou verificar se o meu comando for igual a FIM eu vou dar break, se não vou a minha função ajuda() e vou passar meu comando.
#Vou criar a minha função ajuda() que vai receber como parâmetro um com (comando) e esse com vai receber o help().
#Vou criar outra função chamada título que vai receber uma msg e uma cor.
#Vou fazer que o meu tam (tamanho) seja o comprimento da minha msg e vou utilizar isso no meu print.
#Para eu trabalhar com cores e ter um certo auxílio eu vou criar uma tupla chamada c (cores) onde eu vou passar alguns valores.
from time import sleep
c = ('\033[m', # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m', # 6 - branco
     )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\' ', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)
    

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)
    

#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)