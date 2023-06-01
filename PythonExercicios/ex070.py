#Desafio 070 Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#A)Qual é o total gasto na compra.
#B)Quantos produtos custam mais de R$1000.
#C)Qual é o nome do produto mais barato.
#Para descobrirmos o produto mais barato precisamos criar duas variáveis: um contador (cont) e o menor que vai receber o valor do produto mais barato. Então podemos falar o seguinte se o cont == 1 estamos analisando o nosso primeiro produto, logo o preço deste produto passará a ser o mais barato, se não partimos para o outro raciocínio de que se o preco for menor que o menor, ou seja, que o menor preço que temos até o momento, este preço passará a ser o menor, resolvemos a questão do produto mais bararto.
#Só que agora queremos saber o nome desse produto e para isso precisamos criar uma outra variável chamada barato e partimos da mesma lógica que utilizamos acima.
#Como eu tenho dois blocos iguais eu posso simplificar o nosso código da seguinte maneira:
#E eu posso fazer isso porque utilizando o or (ou) ele vai fazer com que se execute caso satisfaça uma ou outra condição, ou seja, sendo uma verdadeira o bloco será executado.
'''Código:
if cont == 1 or preco < menor:
    menor = preco
    barato = nomeproduto
'''
cont = total = produtos = menor = 0
barato = ' '
while True:
    nomeproduto = str(input('Digite o nome do produto: '))
    preco = float(input('Qual o preço do produto? '))
    cont += 1
    total += preco
    if preco > 1000:
        produtos += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nomeproduto
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'O valor total da compra é R$ {total:.2f}')
print(f'Da sua lista {produtos} produtos custam mais de R$1000.')
print(f'O produto mais barato da sua lista é {barato} e custa R${menor:.2f}.')

