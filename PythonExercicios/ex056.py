#Desafio 056 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres tem menos de 21 anos.
#Como sabemos que são 4 pessoas vamos iniciar a resolução do problema fazendo: for pessoa in range(1, 5)
#Para solucionarmos a média de idade do grupo vamos criar uma variável soma_idade que vai receber 0 e passar dentro do nosso laço: soma_idade += idade veja que aqui eu estou somando todas as idades das pessoas que fazem parte do nosso grupo. Após, vamos criar outra variável media_idade onde ela vai receber a soma_idade dividido por 4 que é a quantidade de integrantes do nosso grupo.
#Para descobrirmos o homem mais velho vamos criar duas variáveis: maior_idade_homem que vai receber 0 e nome_homem_velho que não vai receber nada por enquanto. Feito isso vamos criar uma condição partindo da lógica de que sendo a primeira iteração do nosso laço uma pessoa do sexo masculino essa pessoa vai ser a de maior idade e seguindo as iterações do nosso laço estando ainda no sexo masculino vamos criar uma nova condição para testar se a idade atual que estamos verificando é maior que a idade que já temos, sendo verdadeira esse homem passará a ser o de maior idade.
#Uma observação muito importante aqui utilizamos sexo in 'Mm' para indicar que vamos aceitar tanto se o usuário digitar o sexo com 'M' maiúsculo ou com 'm' minúsculo.
#Para solucionarmos o último problema em descobrir quantas mulheres tem menos de 21 anos vamos criar uma nova variável total_mulher que vai receber 0 e vamos criar uma condição falando que se o sexo for feminino e a idade for menor que 21 vamos adicionar +1 ao nosso contador de mulheres com menos de 21 anos que demos o nome de total_mulher.
soma_idade = 0
maior_idade_homem = 0
nome_homem_velho = ''
total_mulher = 0
for pessoa in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = str(input('Nome: ')).strip() #Uso do strip() para tirar os espaços inúteis
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Ff' and idade < 21:
        total_mulher += 1     
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_homem_velho))
print('Nosso grupo tem {} mulheres menores de 21 anos.'.format(total_mulher))
