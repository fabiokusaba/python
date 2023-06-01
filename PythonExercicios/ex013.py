#Desafio 013 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input('Digite o seu salário: '))
aumento = salario + (salario * (15/100))
print(f'O seu salário com 15% de aumento corresponde a R$ {aumento:.2f}')