'''for c in range(1, 10):
    print(c)
print('FIM!')'''
'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM!')'''

#Mesmo exemplo acima só que com while.
'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM!')'''

#Vamos supor agora que eu vou ficar lendo números enquanto o número for diferente de 0.
#Neste caso vou utilizar a estrutura while.
#No código abaixo a expressão 'n != 0' é o que chamamos de flag ou ponto de parada.
'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM!')'''

#Um outro exemplo que podemos fazer é: enquanto a resposta for 'sim' o nosso programa vai continuar lendo os números, a partir do momento que a resposta for 'não' nosso programa vai acabar.
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM!')'''

#
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))