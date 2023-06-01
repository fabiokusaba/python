#Cálculo do fatorial de um número, retornar para o meu programa principal para mostrar o valor na tela.
def fatorial(num=1): #Passando o meu parâmetro numero como opcional, portanto se ele não for informado o valor utilizado será 1.
    f = 1 #Variável local f (fatorial) valendo 1.
    for c in range(num, 0, -1): #Para fazer o fatorial preciso fazer um for onde ele vai começar do num vai até 0 voltando de 1 em 1.
        f *= c
    return f
    

print(fatorial(5))
'''n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''
'''f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''

'''def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')'''