#Importando a biblioteca math
from math import sqrt, floor
#Lendo um número
num = int(input('Digite um número: '))
#Calculando a raiz quadrada de um número
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz)}.')

#Importando a biblioteca random para gerar números aleatórios
import random
num = random.randint(1, 10)
print(num)