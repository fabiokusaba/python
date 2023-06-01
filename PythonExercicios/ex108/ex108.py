import moeda
preco = float(input('Digite o preço: R$'))
print(f'{moeda.moeda(preco)} com 10% de aumento é {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'{moeda.moeda(preco)} com 13% de desconto é {moeda.moeda(moeda.diminuir(preco, 13))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')