#Desafio 017 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

cateto_oposto = float(input('Digite o comprimento do cateto oposto de um triângulo retângulo: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente de um triângulo retângulo: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f'O cateto oposto vale {cateto_oposto}, o cateto adjacente vale {cateto_adjacente} e o valor da sua hipotenusa é {hipotenusa:.2f}.')

#Resolução professor
from math import hypot
hipotenusa = hypot(cateto_oposto, cateto_adjacente)