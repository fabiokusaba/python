#Desafio 008 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = float(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'{metros} metros em centímetros valem {centimetros:.0f}cm e em milímetros {milimetros:.0f}mm.')