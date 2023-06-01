#Desafio 037 Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal
numero = int(input('Digite um número inteiro: '))
print('''Qual será a base de conversão: 
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('Sua opção é: '))
if opcao == 1:
    print('{} convertido para binário é {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}.'.format(numero, oct(numero)[2:]))
    status = 'Octal'
elif opcao == 3:
    print('{} convertido para hexadecimal é {}.'.format(numero, hex(numero)[2:]))
else:
    print('Digite uma opção de conversão válida, tente novamente!')
    
#[2:] Utilizando do fatiamento de strings para remover os caracteres que não desejamos, no caso estamos removendo os índices 0 e 1 e começando a partir do 2