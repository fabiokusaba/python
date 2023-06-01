#Desafio 046 Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo do 10 até o 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fogos de Artifício!')