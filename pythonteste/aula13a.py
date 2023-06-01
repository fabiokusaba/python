#Caso eu queira que a contagem seja feita em ordem decrescente, ou seja, do maior para o menor, eu preciso passar ao final o -1 que corresponde a nossa iteração.
#Da mesma forma se eu passar no local correspondente a nossa iteração por exemplo: 2, ele vai fazer a contagem de 2 em 2.
''' Código abaixo:
for c in range(0, 7, 2):
    print(c)
print('FIM')
'''
#No exemplo abaixo estamos fazendo um range que vai contar até a quantidade que o nosso usuário informar.
#No caso o 'n' foi utilizado como parte de passagem do nosso for.
'''Código abaixo:
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM!')
'''

#Neste outro exemplo vamos ler o início, o fim e o passo.
'''Código abaixo:
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim + 1, passo):
    print(c)
print('FIM!')
'''

#Um outro exemplo: vamos supor que eu queira perguntar ao usuário 4 números e fazer ao final um somatório com os números que o usuário digitou.
'''Código abaixo:'''
soma = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    soma += n
print('A soma de todos os números escolhidos foi de {}.'.format(soma))
print('FIM!')
