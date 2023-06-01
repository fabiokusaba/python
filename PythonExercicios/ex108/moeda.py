def aumentar(preco=0, taxa=0):
    res = preco + (preco * (taxa/100))
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * (taxa/100))
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res


#Função para formatar a moeda, se eu não informar o preco o padrão vai ser o real, se eu não informar o preço o padrão vai ser o zero.
def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
