#Desafio 092 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#Para se aposentar considere 35 anos de contribuição, ou seja, a partir do momento em que sua carteira está assinada.
from datetime import date
ano = date.today().year
trabalhador = dict()
trabalhador['nome'] = str(input('nome: '))
nascimento = int(input('ano de nascimento: '))
trabalhador['idade'] = ano - nascimento
trabalhador['ctps'] = int(input('ctps (digite 0 se não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['ano_contratação'] = int(input('ano de contratação: '))
    trabalhador['salário'] = float(input('salário: R$'))
    trabalhador['aposentadoria'] = (trabalhador['ano_contratação'] + 35 - ano) + trabalhador['idade']
else:
    trabalhador['ctps'] = 0
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')