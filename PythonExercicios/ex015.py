#Desafio 015 Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
km = float(input('Digite a quantidade de km percorridos: '))
aluguel_dia = dias * 60
aluguel_km = km * 0.15
total = aluguel_dia + aluguel_km
print(f'O carro foi alugado por {dias} dias e percorreu {km} km, o valor a se pagar é R${total}')