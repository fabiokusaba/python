#Desafio 055 Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
#Vamos iniciar o problema com as variáveis maior e menor recebendo 0 e pra isso fazemos o seguinte questionamento: se é o primeiro peso a ser lido esse valor tanto vai representar o maior como também vai representar o menor peso porque eu não li mais nenhum peso além desse. Então, quando estamos diante de duas extremidades maior e menor vou primeiro analisar se é a primeira ocorrência.
#Então partindo dessa lógica podemos pensar o seguinte: dentro do nosso laço ao iniciarmos com a primeira pessoa logo o seu peso vai corresponder tanto ao maior quanto ao menor peso.
#E continuando as iterações do nosso laço, não sendo mais o primeiro laço vou fazer a verificação se o peso que eu acabei de ler é maior do que o maior peso que eu tenho, ou seja, maior do que o peso da minha primeira pessoa, e se caso for maior esse peso que eu estou lendo passa a ser o maior e a mesma lógica é empregada quando vamos analisar o menor peso.
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa (Kg)? '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg.'.format(maior))
print('E o menor peso lido foi de {}Kg.'.format(menor))
    