#Desafio 104 Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Primeiro vou criar uma variável ok que vai começar com False, e também vou criar a variável valor que vai receber 0.
#Vou utilizar um loop infinito e vou ler o num por uma string.
#Se o meu num for numérico o valor vai receber o int(num) e o ok passa a ser True.
#Se ele não for um número ou estiver vazio eu vou printar na tela uma mensagem de erro.
#E no final eu vou verificar se está tudo ok aí eu dou um break e fora do while eu dou return valor.

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor
    
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')