#Desafio 071 Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
#Para solucionar esse desafio primeiro precisamos criar uma variável total que vai ser responsável por pegar esse montante que é o valor que eu quero sacar.
#Vamos partir da lógica de que desse montante eu vou tirar R$50 o máximo que der, por exemplo: se eu quero sacar R$110 eu te dou duas notas de R$50 já eliminei R$100 e falta R$10, então preciso fazer com que o programa pense assim.
#Vou criar uma variável cédula atual que vai começar com a cédula de maior valor que no nosso caso é R$50. E outra variável que eu vou precisar aqui vai ser o total de cédulas para eu saber quantas cédulas vão ser necessárias.
#Vou criar aqui aquele enquanto infinito que já aprendemos e que vai ser quebrado quanto acabar o valor.
#Agora eu vou fazer assim se o total atual for maior ou igual ao valor da cédula, ou seja, se eu puder tirar, eu vou fazer com que o total seja o total - o valor da cédula, e a cada vez que eu tirar 50 eu vou acrescentar no meu totalcedula. Neste caso, eu estou verificando quantas vezes eu posso tirar 50 do meu total.
#Se não der mais para tirar 50 do meu total eu preciso verificar qual é a cédula atual, no caso a cédula atual é de 50, então eu vou verificar se a cédula atual for de 50 é sinal de que eu não posso mais tirar 50 então a minha cédula passa a ser 20 e vou seguindo essa mesma lógica até chegar na minha cédula de R$1.
#E isso daqui vai parar quando o meu total for igual a 0.
#E um detalhe muito importante é que a cada vez que eu mudo a nota eu preciso fazer com que o meu totalcedula volte a 0.
#Ainda podemos acrescentar fazendo com que ele só escreve se a cédula for maior que 0.
print('=' * 30)
print('BANCO MONEY')
print('=' * 30)
valor = int(input('Qual valor deseja sacar? R$'))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'Total de {totalcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
            