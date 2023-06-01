#Desafio 036 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa que você deseja comprar? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = float(input('Em quantos anos pretende pagar a casa? '))
prestacao = casa / (anos * 12)
minimo = salario * (30 / 100)
if prestacao <= minimo:
    status = 'APROVADO'
else:
    status = 'NEGADO'
print('Com base nas suas informações o seu empréstimo foi {}.'.format(status))
