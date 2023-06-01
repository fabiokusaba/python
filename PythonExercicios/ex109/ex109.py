import moeda
preco = float(input('Digite o preço: R$'))
print(f'{moeda.moeda(preco)} com 10% de aumento é {moeda.aumentar(preco, 10, True)}')
print(f'{moeda.moeda(preco)} com 13% de desconto é {moeda.diminuir(preco, 13, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')