import moeda
preco = float(input('Digite o preço: R$'))
print(f'{preco} com 10% de aumento é {moeda.aumentar(preco, 10)}')
print(f'{preco} com 13% de desconto é {moeda.diminuir(preco, 13)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'A metade de {preco} é {moeda.metade(preco)}')