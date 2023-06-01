#Desafio 052 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um número: '))
total = 0 #Variável criada para saber o número de divisíveis
for c in range(1, numero + 1):
    #Códigos dentro do Laço:
    #Criando uma condição para saber se o número é divisível pelo contador:
    if numero % c == 0:
        print('\033[33m', end=' ') #Adiciona uma cor amarela para números divisíveis
        total += 1 #Contar a quantidade de números divisíveis
    else:
        print('\033[31m', end=' ') #Adiciona uma cor vermelha para números não divisíveis
    print('{}'.format(c), end=' ')
#Códigos FORA do Laço
print('\n\033[mO número {} foi divisível {} vezes.'.format(numero, total)) #Acrescentamos códigos no início para quebrar a linha e zerar o estilo
#Criando as condições para saber se o número é primo ou não, no caso o meu contador tem que ser igual a 2 para que a minha condição de número primo seja satisfeita, caso contrário ele não será um número primo.
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')