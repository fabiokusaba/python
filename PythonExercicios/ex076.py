#Desafio 076 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
#No final, mostre uma listagem de preços organizando os dados em forma tabular.
#Exemplo: listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90)
#Para conseguirmos organizar os nossos dados de forma tabular vamos precisar utilizar o for in range() onde vamos começar da posição 0 e vamos até o tamanho da lista com o uso do len().
#Agora eu consigo trabalhar se essa minha position é par ou ímpar, perceba que os nomes dos nossos produtos estão todos em uma posição par e os seus respectivos valores em uma posição ímpar.
listagem = ('Pão', 4, 'Leite', 6, 'Manteiga', 10, 'Barra de Chocolate', 9.90, 'Bolacha', 2.50)
print('-=' * 30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-=' * 30)
for position in range(0, len(listagem)):
    if position % 2 == 0:
        print(f'{listagem[position]:.<30}', end='')
    else:
        print(f'R${listagem[position]:> 4.2f}')
print('-=' * 30)