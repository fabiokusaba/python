#Desafio 029 Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade que você trafegava? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade! Você foi multado em R${:.2f}.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')