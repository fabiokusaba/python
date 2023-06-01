#Desafio 067 Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    numero_tabuada = int(input('Digite um número que você queira saber a tabuada: '))
    if numero_tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{numero_tabuada} x {c} = {numero_tabuada * c}')
print('TABUABA FINALIZADA!')