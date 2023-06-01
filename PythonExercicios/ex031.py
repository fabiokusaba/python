#Desafio 031 Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
distancia = float(input('Qual a distância em Km da sua viagem? '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Sua viagem vai custar R${:.2f}.'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Sua viagem vai custar R${:.2f}.'.format(passagem))

#Resolução professor utilizando o if simplificado
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45