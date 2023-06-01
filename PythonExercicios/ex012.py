#Desafio 012 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
produto = float(input('Digite o preço do produto: R$'))
desconto = produto - (produto * (5/100))
print(f'O preço do produto R${produto:.2f} com 5% de desconto é R$ {desconto:.2f}')