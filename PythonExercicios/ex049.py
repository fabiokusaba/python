#Desafio 049 Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input('Digite um número que você queira saber a tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(numero, c, numero * c))