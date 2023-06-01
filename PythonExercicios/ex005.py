#Desafio 005 Faça um programa que leia um número e mostre na tela o seu sucessor e seu antecessor
num = int(input('Digite um número: '))
antecessor = num - 1
sucessor = num + 1
print(f'O número digitado é {num}, seu antecessor é {antecessor} e o seu sucessor é {sucessor}')
print(f'Analisando o valor {num}, seu antecessor é {num - 1}, e o sucessor é {num + 1}.')