#Desafio 007 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua outra nota: '))
media = (nota1 + nota2) / 2
print(f'A média desse aluno foi {media}')
if media < 7:
    print('Reprovado')
else:
    print('Aprovado')