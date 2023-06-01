def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * (taxa/100))
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * (taxa/100))
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


#Função para formatar a moeda, se eu não informar o preco o padrão vai ser o real, se eu não informar o preço o padrão vai ser o zero.
def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, tx_aumento=10, tx_reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{tx_aumento}% de aumento: \t{aumentar(preco, tx_aumento, True)}')
    print(f'{tx_reducao}% de redução: \t{diminuir(preco, tx_reducao, True)}')
    print('-' * 30)