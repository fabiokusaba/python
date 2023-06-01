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
