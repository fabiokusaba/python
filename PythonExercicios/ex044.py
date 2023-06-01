#Desafio 044 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
#O comando abaixo centraliza o 'LOJAS PREÇO BAIXO' em 40 espaços adicionando '='
print('{:=^40}'.format(' LOJAS PREÇO BAIXO '))
produto = float(input('Digite o valor da compra: R$'))
print('''Qual a opção de pagamento:
[1] à vista dinheiro/cheque: desconto de 10%
[2] à vista no cartão: desconto de 5%
[3] em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: juros de 20%''')
pagamento = int(input('Informe a opção desejada: '))
if pagamento == 1:
    valor = produto - (produto * 10 / 100)
elif pagamento == 2:
    valor = produto - (produto * 5 / 100)
elif pagamento == 3:
    valor = produto
    valor_parcela = valor / 2
    print('Sua compra foi parcelada em 2x de R${:.2f}.'.format(valor_parcela))
elif pagamento == 4:
    valor = produto + (produto * 20 / 100)
    parcelas = int(input('Digite a quantidade de parcelas: '))
    valor_parcela = valor / parcelas
    print('Parcelas de R${:.2f}.'.format(valor_parcela))
else:
    valor = produto
    print('Opção inválida de pagamento, tente novamente.')
print('De R${:.2f} passou para R$ {:.2f}'.format(produto, valor))

