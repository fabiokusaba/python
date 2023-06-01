from utilidadesCeV import moeda
from utilidadesCeV import dado

preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 20, 12)