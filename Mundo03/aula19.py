#Variáveis Compostas (Dicionários)
#Dicionários são estruturas de dados semelhantes as tuplas e as listas só que dessa vez eu consigo ter índices literais, consigo personalizar os índices.
#Tuplas são identificadas por parênteses (), listas por colchetes [] e dicionários em Python por chaves {}.
#Posso declarar o meu dicionário utilizando também dict().
#No código abaixo eu acabei de dizer que 'Pedro' é o valor e 'nome' é o identificador do elemento.

'''Código abaixo:
dados = {'nome': 'Pedro', 'idade': 25}
dados['sexo'] = 'M' #Adicionando um elemento.
del dados['idade'] #Removendo um elemento.
print(dados['nome'])
print(dados['idade'])

filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme.values()) #Método interno que vai me retornar todos os valores do meu dicionário.
print(filme.keys()) #Método que vai me retornar todas as chaves do meu dicionário.
print(filme.items()) #Método que vai me retornar tanto as chaves quanto os valores.
'''

#Posso utilizar esses conceitos de values, keys e items para utilizar nos laços, por exemplo o for:
'''Código abaixo:
for key, value in filme.items():
    print(f'O {key} é {value}')
'''

#Assim como você viu na aula passada você pode juntar todos eles: listas, tuplas e dicionários, então você pode ter uma estrutura mais ou menos assim:
'''Código abaixo:
locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}, {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}, {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]
print(locadora[0]['ano'])
print(locadora[2]['titulo'])
'''