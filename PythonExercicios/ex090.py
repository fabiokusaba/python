#Desafio 090 Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['média'] = float(input(f'A média do {alunos["nome"]} é: '))
if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['média'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
for c, v in alunos.items():
    print(f'{c} é igual a {v}')