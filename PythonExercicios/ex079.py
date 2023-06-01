#Desafio 079 Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os e uma lista. Caso o número já exista lá dentro, ele não será cadastrado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
#Primeiro vamos criar uma lista numeros vazia. Uma outra forma de criar lista é utilizando list().
#Vamos criar a nossa variável n que vai ler esses números que vão ser digitados. Perceba que aqui nós não estamos lendo dentro de numeros.
#Agora precisamos perguntar ao usuário se ele deseja digitar outros valores ou se ele deseja parar e para isso vamos criar uma variável r (resposta).
#Eu só vou inserir o número se ele não estiver na minha lista e para isso posso fazer uma outra verificação. Se n não estiver em números eu adiciono n, se não não vou adicionar.
#E pra finalizar, para eu colocar os meus valores em ordem basta eu utilizar o sort().
numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')
    