#Desafio 072 Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
#Para garantir que o nosso usuário vai digitar um número entre 0 e 20 podemos utilizar o while True (laço infinito) e passando como flag de que se o número digitado pelo usuário for maior ou igual a 0 e menor ou igual a 20 eu vou dar um break.
#Para fazermos com que o nosso programa leia o número que o usuário digitou por extenso basta passarmos como índice da nossa tupla o valor que o usuário digitou visto que o número digitado corresponde ao índice do seu valor por extenso.
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
                print(f'O número digitado foi {num} e por extenso {cont[num]}.')
                resp = ' '
                while resp not in 'SsNn':
                        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
                if resp in 'Nn':
                        break
        else:
                print('Tente novamente.', end=' ')
print('Obrigado! Volte sempre.')

