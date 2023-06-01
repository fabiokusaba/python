#Desafio 010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1.00 = R$3.27
dinheiro = float(input('Digite quantos reais você tem em carteira: R$'))
dolar = dinheiro / 3.27
print(f'O valor informado corresponde a US$ {dolar:.2f} dólares, considerando US$1.00 = R$3.27')