#Desafio 006 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
#Outra forma de calcular a raiz quadrada é utilizando pow(num, (1/2))
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print(f'O número digitado é {num}, o dobro é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz:.2f}')