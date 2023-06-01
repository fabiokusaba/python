#Desafio 019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
aluno1 = input('Primeiro aluno:')
aluno2 = input('Segundo aluno:')
aluno3 = input('Terceiro aluno:')
aluno4 = input('Quarto aluno:')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_escolhido = choice(lista_alunos)
print(f'O aluno escolhido foi {aluno_escolhido}.')
