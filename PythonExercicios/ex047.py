#Desafio 047 Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
#Utilizando o end=' ' para ignorar a quebra de linha e deixar tudo numa única linha.
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou!')

#Resolução do professor
#Pela lógica descrita acima o programa faz repetições em que ele não mostra um valor e por conta disso eu posso reduzir o meu programa para:
'''Código abaixo:
for c in range(2, 51, 2)
    print(c, end=' ')
'''
#E podemos fazer dessa forma porque sabemos que uma das vezes que ele faz o laço não é importante, por isso podemos fazer de 2 a 51 pulando de 2 em 2.
#Neste exemplo do professor é como se fossem gastos menos recursos do processador do seu computador porque o número de iterações é menor para realizar a mesma atividade, é uma forma de potencializar o seu programa consumindo menos e sendo da mesma forma eficaz.
        