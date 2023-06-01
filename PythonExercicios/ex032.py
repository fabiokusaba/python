#Desafio 032 Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Digite um ano ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} ano BISSEXTO.'.format(ano))
else:
    print('{} esse ano NÃO É BISSEXTO.'.format(ano))

#Resolução professor
#Para fazer com que o Python analise o ano atual que está configurado na nossa máquina precisamos importar um módulo para isso:
''' from datetime import date
if ano == 0:
    ano = date.today().year #Pegando o ano atual '''
