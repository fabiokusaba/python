#Desafio 096 Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.
def área(larg, comp):
    a = larg * comp
    print(f'Um terreno de dimensões {larg}x{comp} tem {a}m²')


#Programa Principal
print('Controle de Terrenos')
print('-=' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

área(largura, comprimento)
