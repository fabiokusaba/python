#Desafio 014 Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
celsius = float(input('Digite uma temperatura em ºC: '))
fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura em Celsius convertida para Fahrenheit é {fahrenheit}ºF')